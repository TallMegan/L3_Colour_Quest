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
        self.rounds_won = IntVar

        # lists for stats component

        # highest score test data
        # self.all_scores_list = [20,20, 20, 16, 19]
        # self.all_high_scores_list = [20, 20, 20, 16, 19]
        # self.rounds_won.set(5)

        # lowest score test data
        # self.all_scores_list = [0, 0, 0, 0, 0]
        # self.all_high_scores_list = [20, 20, 20, 16, 19]
        # self.rounds_won.set(0)

        # random score test data
        self.all_scores_list = [0, 15, 16, 0, 16]
        self.all_high_scores_list = [20, 19, 18, 20, 20]
        self.rounds_won.set(0)

        self.play_box = Toplevel()

        self.game_frame = Frame(self.play_box)
        self.game_frame.grid(padx=10, pady=10)

        self.heading_label = Label(self.game_frame, text="Colour Quest", font=("Arial", "16", "bold"))
        self.heading_label.grid(row=0)

        self.stats_button = Button(self.game_frame, font=("Arial", "14", "bold"))
        self.stats_button.grid(row=1)

    def to_stats(self):
        """
        Retrieves everything we need to display the game / round statistics """

        # IMPORTANT: retrieve number of rounds
        # won as a number (rather than the 'self' container)
        rounds_won = self.rounds_won.get()
        stats_bundle = [rounds_won, self.all_scores_list,
                        self.all_high_scores_list]

        Stats(self, stats_bundle)


class Stats:
    """
    Display hints for Colour Quest game
    """

    def __init__(self, partner, all_stats_info):

        # extract information from master list
        rounds_won = all_stats_info[0]
        user_scores = all_stats_info[1]
        high_scores = all_stats_info[2]

        # sort users scores to find high score
        user_scores.sort()

        # Top level() makes a new dialogue box
        self.stats_box = Toplevel()

        # disable help button
        partner.stats_button.config(state=DISABLED)

        # if users press cross at top, closes help and
        # 'releases' help button
        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats, partner))

        self.stats_frame = Frame(self.stats_box, width=300,
                                 height=200)
        self.stats_frame.grid()

        self.stats_heading_label = Label(self.stats_frame,
                                         text="Stats",
                                         font=("Arial", "14", "bold"))
        self.stats_heading_label.grid(row=0)

        hint_text = "To use the program, simply enter the temperature you wish " \
                    "to convert and then choose to convert " \
                    "to either degree celsius or Fahrenheit.. \n\n Note that " \
                    "-273 degrees C (-459 F) is absolute zero (the " \
                    "coldest possible temperature). If you try to convert a temperature " \
                    "that is less than -273 " \
                    "degrees C you will get an error message. To see your calculation " \
                    "history and export it to a text " \
                    "file, please click the History / Export button"

        self.stat_text_label = Label(self.stats_frame,
                                     text=hint_text, wraplength=350,
                                     justify="left")
        self.stat_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.stats_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_stats, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        # list and loop to set background colour on
        # everything except the buttons
        recolour_list = [self.stats_frame, self.stats_heading_label,
                         self.stat_text_label]
        for item in recolour_list:
            item.config(bg=background)

    def close_stats(self, partner):
        """
        Closes help dialogue box (and enables help button)
        """
        # Put help button back to normal...
        partner.to_stats_button.config(state=NORMAL)
        self.stats_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    StartGame()
    root.mainloop()
