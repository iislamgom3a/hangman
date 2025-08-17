import tkinter as tk
from PIL import Image, ImageTk

hand_font = ("Virgil 3 YOFF", 50)


class LoseFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="white")

        self.message_label = tk.Label(
            self,
            text="Just a looser!",
            font=hand_font,
            bg="white",
            fg="#ff1111",
        ).pack(pady=5, padx=5, fill="x", expand=True)

        # image
        original = Image.open("assets/frame 5-2.jpg")
        resized = original.resize((500,500))
        self.image = ImageTk.PhotoImage(resized)
        tk.Label(self, image=self.image, bg="white").pack(
            padx="10", pady="10", side="left"
        )
        
        btn_style = {
            "font": ("Virgil 3 YOFF", 20),
            "bg": "#1B8130",
            "fg": "white",
            "width": 10,
        }
        tk.Button(
            self, text="Play Again", **btn_style, command= self.go_to_play
        ).place(x=630, y=330)


    def go_to_play(self): 
        self.master.show_frame("CategoryFrame")


