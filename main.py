from tkinter import Tk, Button, Label, Entry, mainloop
import random as rd
from tkinter.constants import RIGHT,  BOTTOM, END


class Game :
    def __init__(self):
        self.lifes = 3
        self.score = 0

        self.number_range = list(range(1, 3))
        self.info_text1 = f"Guess the correct number, you have {self.lifes} lifes left."
        self.info_text2 = f"Congratulations! You gain 1 life"
        self.text_font = ("Times", 13)

        self.draw()
        self.locate()
        self.loop()

    def draw(self):
        self.root = Tk()
        self.score_lbl = Label(
            self.root,
            font = self.text_font,
            text = f"Your score : {self.score}"
        )

        self.prediction_ent = Entry(
            self.root,
            font = self.text_font,
            width = 50,
        )    

        self.info_lbl = Label(
            self.root,
            text = self.info_text1,
            font = self.text_font
        )

        self.take_answer_btn = Button(
            self.root,
            text = "Guess",
            width = 10,
            font = self.text_font,
            command = self.compare
        )

    def locate(self):
        self.score_lbl.pack()
        self.prediction_ent.pack()
        self.take_answer_btn.pack()
        self.info_lbl.pack(side = BOTTOM)

    def loop(self):
        self.root.mainloop()

    def compare(self):
        if 1 < self.lifes : 
            try :
                self.selected_number = rd.choice(self.number_range)
                self.answer = int(self.prediction_ent.get())
            except:
                self.answer = 0

            if self.selected_number == self.answer:
                self.info_lbl.config(text = self.info_text2)
                self.score += 10
                self.score_lbl["text"] = f"{self.score}"
                self.lifes += 1
            else:
                self.lifes -= 1
                self.info_text1 = f"Guess the correct number, you have {self.lifes} lifes left."
                self.info_lbl.config(text = self.info_text1)

        else:
            self.info_lbl.config(text = "You have no lifes :( Wanna play a new game ?")
            self.take_answer_btn["state"] = "disable"
            self.create_restart_btn()

    def reset_game(self):
        self.score = 0
        self.lifes = 3
        self.res_btn.destroy()
        self.take_answer_btn["state"] = "active"
        self.info_text1 = f"Guess the correct number, you have {self.lifes} lifes left."
        self.score_lbl["text"] = self.score
        self.info_lbl["text"] = self.info_text1
        self.prediction_ent.delete(0, END)

    def create_restart_btn(self):
        self.res_btn = Button(
        self.root,
        text = "Restart",
        width = 10,
        font = self.text_font,
        command = self.reset_game
        )
        self.res_btn.pack()

game = Game()