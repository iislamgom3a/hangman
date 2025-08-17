import tkinter as tk
from PIL import Image, ImageTk
import random

hand_font = ("Virgil 3 YOFF", 40)


class PlayFrame(tk.Frame): 
    def __init__(self, master):
        super().__init__(master, bg="white")
        self.selected_category = self.master.selected_category.lower() 
        self.username = self.master.player_username
        self.selected_word = str() 
        self.chances = int()
        self.selecet_word(self.selected_category)
        self.WordesFrame = None
        print(f"cateogry from play_fram is {self.selected_category}")
        self.info_frame()
        self.words_frame()
        self.bind('<KeyPress>', self.on_key_press)
        self.correct_guesses = ['_'] * len(self.selected_word) 
        self.focus_set()
        
    
    def info_frame(self):
        self.InfoFrame = tk.Frame(self)
        self.InfoFrame.pack(side='top', fill="x")
        category_label = tk.Label(self.InfoFrame, text=f"Left Chances: {self.chances}", 
                                font=("Arial", 16))
        category_label.pack(pady=20, padx=10, side='right')
        
        category_label = tk.Label(self.InfoFrame, text=f"Player: {self.username}", 
                                font=("Arial", 16))
        category_label.pack(pady=20, padx=10, side='left')

    def words_frame (self): 
        if self.WordesFrame != None: 
            self.WordesFrame.destroy()
        self.WordesFrame = tk.Frame(self, background='white')
        self.WordesFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.WordesFrame.grid_rowconfigure(0, weight=1)
        for i in range(len(self.selected_word)): 
            self.WordesFrame.grid_columnconfigure(i, weight=1)

        for i, ch in enumerate(self.correct_guesses) :
            word_label = tk.Label(self.WordesFrame, text=ch, font=hand_font , borderwidth=1, relief="solid", padx=10, pady=10,)
            word_label.grid(row=0, column=i, padx=10, pady=10)
        
    def on_key_press(self, event)-> str:
        print(f"Key pressed: {event.char}")
        gussesed_char =  event.char.lower()

        if gussesed_char in self.selected_word and gussesed_char not in self.correct_guesses:  
            postions = []
            for i, ch in enumerate(self.selected_word):
                if ch == gussesed_char:
                    postions.append(i)
                for i in postions: 
                    self.correct_guesses[i] = gussesed_char
                self.words_frame()
                print(self.correct_guesses)
        else: 
            self.chances -=1 
            self.InfoFrame.destroy()
            self.info_frame()
            print(f"Wrong guess. Remaining chances: {self.chances}")

        if not '_' in self.correct_guesses: 
            print("you won")
            self.go_to_win()

        elif self.chances <= 0: 
            print('Your lose')
            self.go_to_lose()


    def selecet_word(self, cat)-> str: 
        categories = {
            "fruites": [
                "apple", "banana", "mango", "orange", "strawberry",
                "grapes", "pineapple", "watermelon", "peach", "kiwi"
            ],
            "jobs": [
                "doctor", "engineer", "teacher", "artist", "chef",
                "pilot", "nurse", "lawyer", "farmer"
            ],
            "sports": [
                "football", "basketball", "tennis", "cricket", "baseball",
                "swimming", "boxing", "volleyball", "rugby", "golf"
            ],
            "animals": [
                "dog", "cat", "elephant", "tiger", "lion",
                "horse", "zebra", "giraffe", "kangaroo", "monkey"
            ],
            "countries": [
                "egypt", "france", "japan", "brazil", "canada",
                "india", "germany", "mexico", "australia", "italy"
            ],
            "colors": [
                "red", "blue", "green", "yellow", "purple",
                "orange", "black", "white", "pink", "brown"
            ]
        }
        try: 
            li = categories[cat]
            word = self.selected_word = random.choice(li)
            self.chances = len(word) + 2
            self.correct_guesses = ['_'] * len(word)

            print(f"current word: {self.selected_word}")
        except KeyError: 
            print(KeyError)

    def go_to_win(self): 
        self.master.show_frame("WinFrame")
    
    def go_to_lose(self): 
        self.master.show_frame("LoseFrame")








