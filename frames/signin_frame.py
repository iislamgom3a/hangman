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


class SignInFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="white")
        self.failed_attempts = 0
        self.max_attempts = 3

        # Fields grid
        fiedls_frame = tk.Frame(self, bg="white")
        fiedls_frame.pack(pady=20, padx=20, fill="x")
        fiedls_frame.grid_rowconfigure(0, weight=1)
        fiedls_frame.grid_rowconfigure(1, weight=1)
        fiedls_frame.grid_rowconfigure(2, weight=1)
        fiedls_frame.grid_columnconfigure(0, weight=1)

        # username & password fields
        tk.Label(fiedls_frame, text="Username", bg="white", font=hand_font).grid(
            row=0, column=0, padx=5, pady=5
        )
        self.username_entry = tk.Entry(fiedls_frame, font=normal_font, bg="white")
        self.username_entry.grid(row=0, column=1, padx=50, pady=1)

        tk.Label(fiedls_frame, text="Password", bg="white", font=hand_font).grid(
            row=1, column=0, padx=5, pady=5
        )
        self.password_entry = tk.Entry(
            fiedls_frame, show="*", font=normal_font, bg="white"
        )
        self.password_entry.grid(row=1, column=1, padx=70, pady=1)

        # Main Label
        self.message_label = tk.Label(
            self,
            text="happy to see you again",
            font=hand_font,
            bg="white",
            fg="#0e0f3c",
        ).pack(pady=5, padx=5, fill="x", expand=True)

        #image
        original = Image.open("assets/frame 2-1.jpg")
        resized = original.resize((350, 350))
        self.image = ImageTk.PhotoImage(resized)
        tk.Label(self, image=self.image, bg="white").pack(
            padx="10", pady="10", side="bottom"
        )

        #Buttons
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
            buttons_frame, text="Sign In", **btn_style, command=self.sign_in
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
            text="Go To Sign Up",
            **signup_btn_style,
            command=self.go_to_sign_up,
        ).grid(row=0, column=1, padx=10, pady=5, sticky=tk.EW)

    def sign_in(self):
        if self.failed_attempts >= self.max_attempts:
            self.show_error(
                "Access Denied",
                f"You have exceeded the maximum number of login attempts ({self.max_attempts}). Please restart the application.",
            )
            return

        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            self.show_error(
                "Input Error", "Please enter both username and password!"
            )
            return

        login_result = self.check_user_credentials(username, password)

        if login_result == "success":
            self.show_success("Login Successful", f"Welcome back, {username}!")
            self.failed_attempts = 0
            self.master.player_username = username

            self.master.show_frame("CategoryFrame")

        elif login_result == "user_not_exists":
            response = messagebox.askyesno(
                "User not found",
                f"The Username {username} doesn't exist.\nWould your like to make an acount",
            )
            if response:
                self.go_to_sign_up()

        elif login_result == "wrong_password":
            self.failed_attempts += 1
            remaining_attempts = self.max_attempts - self.failed_attempts

            if remaining_attempts > 0:
                self.show_error_with_retry(
                    f"Incorrect password for user '{username}'.\n\nAttempts remaining: {remaining_attempts}"
                )
            else:
                self.show_error(
                    "Access Denied",
                    f"Maximum login attempts ({self.max_attempts}) exceeded. Please restart the application.",
                )

            return

            

    def check_user_credentials(self, username, password):
        user_exits = False
        with open(users_file, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if not row:
                    continue
                if row[0].strip() == username:
                    user_exits = True
                    if row[1].strip() == password:
                        return "success"
                    else:
                        return "wrong_password"
            if not user_exits:
                return "user_not_exists"

    def show_error(self, title, message):
        """Show error message dialog"""
        messagebox.showerror(title, message)
        self.clear_fields()  # Clear password field for security

    def show_success(self, title, message):
        """Show success message dialog"""
        messagebox.showinfo(title, message)
        self.clear_fields()

    def show_error_with_retry(self, message):
        """Show error with retry option"""
        result = messagebox.askretrycancel("Error", message)
        self.clear_password()

    def clear_fields(self):
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def go_to_sign_up(self):
        self.clear_fields()
        self.failed_attempts = 0
        self.master.show_frame("SignUpFrame")

    def clear_password(self): 
        self.password_entry.delete(0, tk.END)