from tkinter import *
from functools import partial


class StartGame:
    """
    Colour quest main menu
    """

    def __init__(self):
        """
        Gets number of rounds from user
        """

        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # create play button
        self.play_button = Button(self.start_frame, font=("Arial", "16", "bold"),
                                  fg="#FFFFFF", bg="#0057D8", text="Play", width=10,
                                  command=self.check_rounds)

        self.play_button.grid(row=0, column=1, padx=20, pady=20)

    def check_rounds(self):
        """
        Check users have entered 1 or more rounds
        """
        rounds_wanted = 5
        self.to_play(rounds_wanted)

    def to_play(self, num_rounds):
        """
        Invokes game GUI and takes across a number of rounds to be played
        """

        Play(num_rounds)
        # hide root window
        root.withdraw()


class Play:
    """
    Interface for playing the Colour Quest Game
    """

    def __init__(self, how_many):
        self.play_box = Toplevel()

        self.game_frame = Frame(self.play_box)
        self.game_frame.grid(padx=10, pady=10)

        self.heading_label = Label(self.game_frame, text="Colour Quest",
                                   font=("Arial", "16", "bold"))
        self.heading_label.grid(row=-0)

        self.to_hint_button = Button(self.game_frame, font=("Arial", "14", "bold"),
                                     text="Hints", width=15, fg="#FFFFFF",
                                     bg="#FF8000", padx=10, pady=10, command=self.to_hints)
        self.to_hint_button.grid(row=1)

    def to_hints(self):
        """
        Displays hints for playing game
        :return:
        """

        DisplayHints(self)


class DisplayHints:
    """
    Display hints for Colour Quest game
    """

    def __init__(self, partner):
        # setup dialogue box and background colour
        background = "#ffe6cc"

        # Toplevel() makes a new dialogue box
        self.hint_box = Toplevel()

        # disable help button
        partner.to_hint_button.config(state=DISABLED)

        # if users press cross at top, closes help and
        # 'releases' help button
        self.hint_box.protocol('WM_DELETE_WINDOW', partial(self.close_hints, partner))

        self.hint_frame = Frame(self.hint_box, width=300,
                                height=200)
        self.hint_frame.grid()

        self.hint_heading_label = Label(self.hint_frame,
                                        text="Help / Info",
                                        font=("Arial", "14", "bold"))
        self.hint_heading_label.grid(row=0)

        hint_text = "To use the program, simply enter the temperature you wish " \
                    "to convert and then choose to convert " \
                    "to either degree celsius or Fahrenheit.. \n\n Note that " \
                    "-273 degrees C (-459 F) is absolute zero (the " \
                    "coldest possible temperature). If you try to convert a temperature " \
                    "that is less than -273 " \
                    "degrees C you will get an error message. To see your calculation " \
                    "history and export it to a text " \
                    "file, please click the History / Export button"

        self.hint_text_label = Label(self.hint_frame,
                                     text=hint_text, wraplength=350,
                                     justify="left")
        self.hint_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.hint_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_hints, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        # list and loop to set background colour on
        # everything except the buttons
        recolour_list = [self.hint_frame, self.hint_heading_label,
                         self.hint_text_label]
        for item in recolour_list:
            item.config(bg=background)

    def close_hints(self, partner):
        """
        Closes help dialogue box (and enables help button)
        """
        # Put help button back to normal...
        partner.to_hint_button.config(state=NORMAL)
        self.hint_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    StartGame()
    root.mainloop()
