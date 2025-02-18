from tkinter import *


class TempName:
    """
    Colour quest main menu
    """

    def __init__(self):

        self.main_screen = Frame(padx=10, pady=10)
        self.main_screen.grid()

        # sets up the heading
        self.temp_heading = Label(self.main_screen, text="Colour Quest",
                                  font=("Arial", "16", "bold"))
        self.temp_heading.grid(row=0)

        # sets up instructions label
        instructions = "In each round you will be invited to choose a colour. " \
                       "Your goal is to beat the target score " \
                       "and win the round (and keep your points)"
        self.instructions = Label(text=instructions, font=("Arial", "12"),
                                  wraplength=350)
        self.instructions.grid(row=1, pady=10, padx=10)

        self.question = Label(text="How many rounds do you want to play?",
                              font=("Arial", "12", "bold"), fg="#008000")

        self.question.grid(row=2)

        self.round_entry = Entry(self.main_screen)





# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    TempName()
    root.mainloop()
