import tkinter as tk 
from frames.start_frame import StartFrame
from frames.category_frame import CategoryFrame
from frames.signup_frame import SignUpFrame
from frames.signin_frame import SignInFrame
from frames.play_frame import PlayFrame
from frames.lose_frame import LoseFrame
from frames.win_frame import WinFrame


class HangmanApp(tk.Tk): 
    def __init__(self):
        super().__init__()
        self.selected_category = None
        self.game_score = 0
        self.player_username = ""

        self.title("Hangman")
        # self.resizable(False, False) 
        self.geometry("900x700")

        icon = tk.PhotoImage(file='assets/hanged.png')
        self.iconphoto(True, icon)


        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frame_classes = {
                    'StartFrame': StartFrame,
                    'SignInFrame': SignInFrame,
                    'SignUpFrame': SignUpFrame,
                    'CategoryFrame': CategoryFrame,
                    'PlayFrame': PlayFrame,
                    'WinFrame': WinFrame,
                    'LoseFrame': LoseFrame
                }

        self.show_frame("StartFrame")

    def show_frame(self, name):
        FrameClass = self.frame_classes[name]
        frame = FrameClass(self)
        frame.grid(row=0, column=0, sticky=tk.NSEW, padx=10, pady=10)
        # Get and show the frame
        if hasattr(frame, 'on_show'):
            frame.on_show()
        frame.tkraise()        
