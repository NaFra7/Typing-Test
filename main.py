from tkinter import *
import tkinter as tk
from tkinter import ttk
import time
import random



# ------ Test sentence dictionary ---- #

test_sentences = {
    1: "The arsonist had oddly shaped feet.",
    2: "Squalid squatters swing swift sabers salaciously.",
    3: "Insidious insects instigate irrefutable irritation in important imports.",
    4: "Telephones used to interrupt internet connections back in the 1990s.",
    5: "Peter piper picked a peck of pickled peppers, but he never sang a song.",
    6: "Somewhere out there is a seagull waiting to steal a sandwich.",
    7: "The local zoo keeps 454 varieties of fish, but only 4 of them are edible.",
    8: "Nine masked men danced merrily in the streets of New York.",
    9: "Panicked picnickers pushed past pilgrims perusing panoplies of persimmons.",
    10: "There was once a man named Samwell Gamgee, who is the only reason the One Ring was destroyed.",
    11: "Cats know precisely when to pester you, and precisely when to offer comfort.",
    12: "Tyrannosaurus Rex were dinosaurs that were angry simply because they couldn't hug anything.",
    13: "If Star Wars would branch outside of the Skywalker saga, it would do much better than it is now.",
    14: "Janice in accounting always brings brownies for everyone on the third friday of each month.",
    15: "Celebrating a birthday is usually a joyous occasion.",
    16: "Popcorn is terrible for you nutritionally, but it tastes so good that it doesn't matter."
}


# -------- Functions ----- #

def begin():
    """Fetches a test sentence, focuses the entry field, and starts the timer.
    When enter is pressed, triggers the check_results function."""
    global test_sentence
    test_sentence = test_sentences[random.randint(1, 16)]
    test_text.config(text=f"Test Sentence: {test_sentence}")
    text_entry.focus()
    global start_time
    start_time = time.time()
    text_entry.bind("<Return>", check_result)


def check_result(event):
    """Compares entered text against test sentence and resets the entry field. If entered text matches, it calculates
    WPM and shows it to the user. If entered text does not match, asks user to try again."""
    entered_text = text_entry.get()
    text_entry.delete(0, tk.END)
    if entered_text == test_sentence:
        end_time = time.time()
        time_taken = end_time - start_time
        wpm = (len(test_sentence) / 5) / (time_taken / 60)
        results.config(text=f"Your typing speed: {wpm:.2f} WPM")
    else:
        results.config(text="Oops. Too many typos. Try again.")
    test_text.config(text="")


# ----- UI SETUP ------ #
window = Tk()
window.title("Typing Test")
mainframe = ttk.Frame(window)
mainframe.grid(column=0, row=0)
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
logo = PhotoImage(file='logo.png')

# ---- UI styling ---- #

style = ttk.Style()
style.configure('Test.TButton', padding=(7, 7, 10, 10), background="green")
style.configure('ilabel.TLabel', padding=(5, 5, 5, 5))

# ------ Buttons ------- #
start_test = ttk.Button(mainframe, text="Start Test", command=begin, style="Test.TButton")
start_test.grid(column=0, row=2)

# ----- Labels ------- #
instructions = ttk.Label(mainframe, text="Click 'Start Test' and then hit the 'enter' key once you are done typing.",
                         wraplength=200)
instructions.grid(column=0, row=1)

test_text = ttk.Label(mainframe, text="", font=16)
test_text.grid(column=1, row=0)

results = ttk.Label(mainframe, text='')
results.grid(column=2, row=1)

logo_label = ttk.Label(mainframe, image=logo, style="Logo.TLabel")
logo_label.grid(column=0, row=0)

# ------ Entry ------ #
text_entry = ttk.Entry(mainframe, width=100)
text_entry.grid(column=1, row=2)

# ----- mainloop ----- #

window.mainloop()
