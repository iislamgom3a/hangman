from PIL import Image, ImageTk
import tkinter as tk

hand_font = ('Virgil 3 YOFF', 25)

class StartFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg='white')

        global hand_font
        # Title
        tk.Label(self, text="Welcome to Hangman", font=hand_font, bg='white', fg="#0e0f3c").pack(
            pady='10', padx=10, fill='x', expand=True
        )
        # Image
        original = Image.open('assets/welcome.png')
        resized = original.resize((350, 350))  
        self.image = ImageTk.PhotoImage(resized)
        tk.Label(self, image=self.image, bg='white').pack(padx='50', pady='50', side='left')

        # Buttons Frame
        buttons_frame = tk.Frame(self, bg='white')
        buttons_frame.pack(side='right', expand=True, fill='both', padx='20', pady='20')
        
        # Configure grid weights for centering
        buttons_frame.grid_rowconfigure(0, weight=1)  # Top spacing
        buttons_frame.grid_rowconfigure(1, weight=0)  # Sign In button
        buttons_frame.grid_rowconfigure(2, weight=0)  # Sign Up button
        buttons_frame.grid_rowconfigure(3, weight=1)  # Bottom spacing
        buttons_frame.grid_columnconfigure(0, weight=1)  # Center horizontally
        
        btn_style = {"font": ('Virgil 3 YOFF', 18), "bg": "#2679c5", "fg": "white", "width": 12}
        
        signin_btn = tk.Button(
            buttons_frame, 
            text="Sign In", 
            command=lambda: master.show_frame("SignInFrame"),
            **btn_style
        )
        signin_btn.grid(row=1, column=0, padx=20, pady=5, sticky=tk.EW)
        
        signup_btn = tk.Button(
            buttons_frame, 
            text="Sign Up",
            command=lambda: master.show_frame("SignUpFrame"), 
            **btn_style
        )
        signup_btn.grid(row=2, column=0, padx=20, pady=5, sticky=tk.EW)
        



