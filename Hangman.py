from tkinter import *
import random

hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def guess_func(event=None):
    global ATTEMPTS, pic  # Declare ATTEMPTS as global so we can modify it
    found = False
    l = userinput.get().lower()  # Get the input from the Entry widget and make it lowercase
    userinput.delete(0, END)  # Clear the input box after taking input

    if len(l) == 1 and l.isalpha():  # Ensure it's a single valid letter
        for i in range(len(WORD)):
            if l == WORD[i]:
                start[i] = l
                found = True
        if not found:
            ATTEMPTS -= 1
            result_label.config(text=f"Wrong Answer! {ATTEMPTS} attempts left.")
            if l in let_lbl:
                let_lbl[l].config(fg='red')
            pic += 1
            thehangman.config(text=hangman_pics[pic])
        else:
            result_label.config(text="Good job! Keep guessing.")
            if l in let_lbl:
                let_lbl[l].config(fg='green')

        word_display.set(' '.join(start))  # Update the word display

        if ''.join(start) == WORD:
            result_label.config(text="Congratulations! You guessed the word!")
            disable_guessing()
        elif ATTEMPTS == 0:
            result_label.config(text=f"You lost! The word was: {WORD}")
            disable_guessing()
    else:
        result_label.config(text="Please enter a valid single letter.")


def disable_guessing():
    guessbutton.config(state=DISABLED)  # Disable the guess button after the game ends
    userinput.unbind('<Return>', enterbutton)
    userinput.config(state=DISABLED)


# GUI setup
hang = Tk()
hang.geometry('650x420')
hang.title("Hangman Game")
# hang.anchor('center')

welcome = Label(hang, text="Welcome to Hangman", font=("Arial", 20), padx=10, pady=20, anchor='center',
                justify='center')
welcome.grid(column=0, row=0, sticky="ew")

gamespace = Frame(hang)
gamespace.grid(column=0, row=1)

column1 = Frame(gamespace, padx=10)
column1.grid(column=0, row=0)

column2 = Frame(gamespace)
column2.grid(column=1, row=0)

guess = Label(column1, text="Guess a letter", font=("Arial", 14), pady=20)
guess.grid(column=0, row=0)

guessingframe = Frame(column1)
guessingframe.grid(column=0, row=1)

userinput = Entry(guessingframe, font=("Arial", 14))
userinput.grid(column=0, row=0)
enterbutton = userinput.bind('<Return>', guess_func)

white1 = Label(guessingframe, width=5)
white1.grid(column=1, row=0)

guessbutton = Button(guessingframe, text="Guess", command=guess_func, height=1)
guessbutton.grid(column=2, row=0)

result_label = Label(column1, text="", font=("Arial", 14))
result_label.grid(column=0, row=2)

# Initial game setup
WORDS = open(r"C:\Users\lenovo\source\repos\pythontest\pythontest\words.txt").read().splitlines()
ATTEMPTS = 6
pic = 0

WORD = random.choice(WORDS)

start = ['_'] * len(WORD)
word_display = StringVar()
word_display.set(' '.join(start))

word_label = Label(column1, textvariable=word_display, font=("Arial", 18), padx=10, pady=20)
word_label.grid(column=0, row=3)

letterbox = Frame(column1)
letterbox.grid(column=0, row=4)

# take the data
letters = [('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'),
           ('n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')]
let_lbl = {}

for i in range(2):
    for j in range(13):
        let = letters[i][j]
        e = Label(letterbox, text=letters[i][j], width=2, height=1,
                  font=('Arial', 16, 'bold'),
                  relief='solid',
                  borderwidth=1,
                  anchor='center')
        let_lbl[let] = e  # Store the label in the dictionary
        e.grid(row=i, column=j)

man = Frame(column2, padx=40)
man.grid(column=8, row=1)

thehangman = Label(man, text=hangman_pics[pic], font=('Arial', 20, 'bold'), anchor='center')
thehangman.grid()

# Start the GUI event loop
hang.mainloop()