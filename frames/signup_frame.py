import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import csv

# users db file path (csv)
curr_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(curr_dir)
users_file = os.path.join(project_root, "users.csv")

hand_font = ("Virgil 3 YOFF", 25)
normal_font = ("sf pro text", 20)


class SignUpFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="white")
        # Label
        self.message_label = tk.Label(
            self,
            text="Yes we're collecting your data!",
            font=hand_font,
            bg="white",
            fg="#0e0f3c",
        ).pack(pady=5, padx=5, fill="x", expand=True)

        # add image
        original = Image.open("assets/frame 2-2.jpg")
        resized = original.resize((300, 300))
        self.image = ImageTk.PhotoImage(resized)
        tk.Label(self, image=self.image, bg="white").pack(
            padx="10", pady="10", side="left"
        )

        # Fields grid
        fiedls_frame = tk.Frame(self, bg="white")
        fiedls_frame.pack(pady=20, padx=20, fill="x")
        fiedls_frame.grid_rowconfigure(0, weight=1)
        fiedls_frame.grid_rowconfigure(1, weight=1)
        fiedls_frame.grid_rowconfigure(2, weight=1)
        fiedls_frame.grid_rowconfigure(3, weight=1)
        fiedls_frame.grid_columnconfigure(0, weight=1)
        fiedls_frame.grid_columnconfigure(1, weight=1)

        self.username_entry = tk.Entry(fiedls_frame, font=normal_font, bg="white")
        self.username_entry.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry.insert(0, "username")

        self.password_entry = tk.Entry(fiedls_frame, font=normal_font, bg="white")
        self.password_entry.grid(row=0, column=1, padx=10, pady=10)
        self.password_entry.insert(0, "password")

        self.age_entry = tk.Entry(fiedls_frame, font=normal_font, bg="white")
        self.age_entry.grid(row=1, column=0, padx=10, pady=10)
        self.age_entry.insert(0, "Your Age")

        self.job_entry = tk.Entry(fiedls_frame, font=normal_font, bg="white")
        self.job_entry.grid(row=1, column=1, padx=10, pady=10)
        self.job_entry.insert(0, "Your Job")

        self.address_entry = tk.Entry(fiedls_frame, font=normal_font, bg="white")
        self.address_entry.grid(row=2, column=0, padx=10, pady=10)
        self.address_entry.insert(0, "Your Address")

        self.gender_entry = tk.Entry(fiedls_frame, font=normal_font, bg="white")
        self.gender_entry.grid(row=2, column=1, padx=10, pady=10)
        self.gender_entry.insert(0, "Gender")

        self.conf_password_entry = tk.Entry(fiedls_frame, font=normal_font, bg="white")
        self.conf_password_entry.grid(row=3, column=0, padx=10, pady=10)
        self.conf_password_entry.insert(0, "confirm password")

        # Buttons
        buttons_frame = tk.Frame(self, bg="white")
        buttons_frame.pack(side="bottom", padx="20", pady="20")
        buttons_frame.grid_columnconfigure(0, weight=1)
        btn_style = {
            "font": ("Virgil 3 YOFF", 18),
            "bg": "#2679c5",
            "fg": "white",
            "width": 8,
        }
        tk.Button(
            buttons_frame, text="Sign Up", **btn_style, command=self.sign_up
        ).grid(row=0, column=0, padx=20, pady=5, sticky=tk.EW)

        # go to signup
        signup_btn_style = {
            "font": ("Virgil 3 YOFF", 18),
            "bg": "#28a745",
            "fg": "white",
            "width": 16,
        }
        tk.Button(
            buttons_frame,
            text="Go To Login",
            **signup_btn_style,
            command=self.go_to_sign_in,
        ).grid(row=0, column=1, padx=10, pady=5, sticky=tk.EW)

    def sign_up(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        conf_password = self.conf_password_entry.get().strip()

        # check if the info are incomplete
        if (
            self.username_entry.get() == "username"
            or self.password_entry.get() == "password"
            or self.age_entry.get() == "Your Age"
            or self.job_entry.get() == "Your Job"
            or self.address_entry.get() == "Your Address"
            or self.conf_password_entry.get() == "confirm password"
            or self.gender_entry.get() == "Gender"
        ):

            self.show_error_with_retry("Please enter all your info!")
            return

        signup_result = self.check_user_credentials(username, password, conf_password)

        if signup_result == "success":
            with open(users_file, "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file, lineterminator="\n")
                writer.writerow(
                    [
                        self.username_entry.get().strip(),
                        self.password_entry.get().strip(),
                        self.age_entry.get().strip(),
                        self.gender_entry.get().strip(),
                        self.address_entry.get().strip(),
                        self.job_entry.get().strip(),
                    ]
                )
            self.show_success("succes", "Signed Up Successful, Please Login!")

        elif signup_result == "user_exists":
            response = messagebox.askyesno(
                "User exists",
                f"The Username {username} already exist.\nWould your like to Login",
            )
            if response:
                self.go_to_sign_in()

        elif signup_result == "wrong_conf_password":
            self.show_error_with_retry("Passwords doesn't match!")

    def check_user_credentials(self, username, password, conf_password):
        user_exits = False
        with open(users_file, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if not row:
                    continue
                if row[0].strip() == username:
                    user_exits = True
                    return "user_exists"
            if not user_exits:
                if password == conf_password:
                    return "success"
                elif password != conf_password:
                    return "wrong_conf_password"

    def show_error(self, title, message):
        """Show error message dialog"""
        messagebox.showerror(title, message)
        self.clear_fields()  # Clear password field for security

    def show_success(self, title, message):
        """Show success message dialog"""
        messagebox.showinfo(title, message)
        self.clear_fields()

    def show_error_with_retry(self, message, retry_function=None):
        """Show error with retry option"""
        result = messagebox.askretrycancel("Error", message)
        if result and retry_function:
            retry_function()

    def go_to_sign_in(self):
        self.clear_fields()
        self.master.show_frame("SignInFrame")

    def clear_fields(self):
        self.username_entry.delete(0, tk.END)
        self.username_entry.insert(0, "username")
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, "password")
        self.job_entry.delete(0, tk.END)
        self.job_entry.insert(0, "Your Job")
        self.age_entry.delete(0, tk.END)
        self.age_entry.insert(0, "Your Age")
        self.address_entry.delete(0, tk.END)
        self.address_entry.insert(0, "Your Address")
        self.gender_entry.delete(0, tk.END)
        self.gender_entry.insert(0, "Gender")
        self.conf_password_entry.delete(0, tk.END)
        self.conf_password_entry.insert(0, "confirm password")

    def clear_password(self):
        self.password_entry.delete(0, tk.END)
