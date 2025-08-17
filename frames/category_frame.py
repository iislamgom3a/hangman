import tkinter as tk


hand_font = ("Virgil 3 YOFF", 25)
normal_font = ("sf pro text", 20)


class CategoryFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="white")
        font = ("Virgil 3 YOFF", 20)

        # TODO
        # Label
        self.message_label = tk.Label(
            self,
            text="Choose the Cateogory",
            font=hand_font,
            bg="white",
            fg="#761111",
        ).pack(pady=5, padx=5, expand=True)

        # 2.confiugre grid
        buttons_frame = tk.Frame(self, bg="white")
        buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)

        btn_style = {
            "font": ("Virgil 3 YOFF", 18),
            "bg": "#2679c5",
            "fg": "white",
            "width": 29,
        }
        # buttons 
        categories = [
            ("Fruites", 0, 0),
            ("Jobs", 0, 1), 
            ("Sports", 1, 0),
            ("Animals", 1, 1),
            ("countries", 2, 0),
            ("Colors", 2, 1)
        ]

        for text, row, col in categories:
            btn = tk.Button(buttons_frame, text=text, **btn_style,
                        command=lambda t=text: self.go_to_win(t))
            btn.grid(row=row, column=col, padx=5, pady=5)


    
    def go_to_win(self, category): 
        print(f'pressed button {category}')

        self.master.selected_category = category
        self.master.show_frame("PlayFrame")



