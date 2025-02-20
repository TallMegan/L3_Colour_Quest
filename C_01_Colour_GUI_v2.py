from tkinter import *
from functools import partial  # to prevent unwanted windows


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

        # strings for labels
        intro_string = "In each round you will be invited to choose a colour. " \
                       "Your goal is to beat the target score " \
                       "and win the round (and keep your points)"

        # choose_string = "Please choose a whole number more than zero"
        choose_string = "How many rounds do you want to play?"

        # List of labels to be made (text | font | fg)
        start_labels_list = [
            ["Colour Quest", ("Arial", "16", "bold"), None],
            [intro_string, ("Arial", "12"), None],
            [choose_string, ("Arial", "12", "bold"), "#009900"]
        ]

        # create labels and add them to the reference list
        start_labels_ref = []

        for count, item in enumerate(start_labels_list):
            make_label = Label(self.start_frame, text=item[0], font=item[1],
                               fg=item[2],
                               wraplength=350, justify="left", pady=10, padx=20)
            make_label.grid(row=count)

            start_labels_ref.append(make_label)

        # extract choice label so that it can be changed to an
        # error message if necessary
        self.choose_label = start_labels_ref[2]

        # frame so that entry box and button can be in teh same row
        self.entry_area_frame = Frame(self.start_frame)
        self.entry_area_frame.grid(row=3)

        self.num_rounds_entry = Entry(self.entry_area_frame, font=("Arial", "20", "bold"),
                                      width=10)
        self.num_rounds_entry.grid(row=0, column=0, padx=10, pady=10)

        # create play button
        self.play_button = Button(self.entry_area_frame, font=("Arial", "16", "bold"),
                                  fg="#FFFFFF", bg="#0057D8", text="Play", width=10,
                                  command=self.check_rounds)
        self.play_button.grid(row=0, column=1)

    def check_rounds(self):

        # retrieve temperature to be converted
        rounds_wanted = self.num_rounds_entry.get()

        # reset label and entry box (for when users come back to home screen)
        self.choose_label.config(fg="#009900", font=("Arial", "12", "bold"))
        self.num_rounds_entry.config(bg="#FFFFFF")

        error = "Please choose a number more than zero"
        has_errors = "no"

        # checks that amount to be converted is a number above zero
        try:
            rounds_wanted = int(rounds_wanted)
            if rounds_wanted > 0:
                # invoke play class (and take across number of rounds)
                Play(rounds_wanted)

                # hide root window (ie: hide rounds choice window)
                root.withdraw()

        except ValueError:
            has_errors = "yes"

        # display the error if necessary
        if has_errors == "yes":
            self.choose_label.config(text=error, fg="#990000",
                                     font=("Arial", "10", "bold"))

            self.num_rounds_entry.config(bg="#F4CCCC")
            self.num_rounds_entry.delete(0, END)


class Play:
    """
    Interface for playing the Colour Quest Game
    """

    def __init__(self, how_many):
        self.play_box = Toplevel()

        # game heading label
        self.game_frame = Frame(self.play_box)
        self.game_frame.grid(pady=10, padx=10)

        self.game_heading_label = Label(self.game_frame, text=f"Round 0 of {how_many}",
                                        font=("Arial", "16", "bold"))
        self.game_heading_label.grid(row=0, pady=15)

        # score to beat label
        self.score_to_beat_frame = Frame(self.game_frame)
        self.score_to_beat_frame.grid(pady=10, padx=10)

        self.score_to_beat_label = Label(self.score_to_beat_frame, text=f"Score to beat: #",
                                         font=("Arial", "14"), bg="#FFF2CC")
        self.score_to_beat_label.grid(row=1)

        # game instructions
        self.choose_a_colour_frame = Frame(self.game_frame)
        self.choose_a_colour_frame.grid(pady=10, padx=10)

        self.choose_a_colour_label = Label(self.choose_a_colour_frame,
                                           text=f"Choose a colour below. Good Luck. 🍀",
                                           font=("Arial", "14"), bg="#D5E8D4")
        self.choose_a_colour_label.grid(row=2)

        # next round button
        self.next_round_button = Button(self.game_frame, text="Next Round",
                                        font=("Arial", "16", "bold"), bg="#0057D8",
                                        fg="#FFFFFF", width=20)
        self.next_round_button.grid(row=5)

        # hints and stats buttons

        self.hint_stats_frame = Frame(self.game_frame)
        self.hint_stats_frame.grid(row=6, padx=10, pady=10)

        self.hints_button = Button(self.hint_stats_frame, text="Hints",
                                   font=("Arial", "16", "bold"), bg="#FF8000",
                                   fg="#FFFFFF", width=0)
        self.hints_button.grid(row=0, column=0)

        self.stats_button = Button(self.hints_button, text="Stats",
                                   font=("Arial", "16", "bold"), bg="#333333",
                                   fg="#FFFFFF", width=0)
        self.stats_button.grid(row=0, column=1)

        # end game button
        self.end_game_button = Button(self.game_frame, text="End Game",
                                      font=("Arial", "16", "bold"),
                                      fg="#FFFFFF", bg="#990000",
                                      command=self.close_play)
        self.end_game_button.grid(row=7)

    def close_play(self):
        # reshow root (ie: choose rounds) and end current
        # game / allow new game to start
        root.deiconify()
        self.play_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    StartGame()
    root.mainloop()
