from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(background=THEME_COLOR)

        # Question Board
        canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        text_question = canvas.create_text(150, 125, text='Question goes here', fill=THEME_COLOR, font=('Arial', 20, 'italic'))
        canvas.grid(row=1, column=0, padx=20, pady=20, columnspan=2)

        # Score Label
        label_score = Label(text=f'Score: 0', fg='white', bg=THEME_COLOR, font=('Arial', 12, 'normal'))
        label_score.grid(row=0, column=1, pady=20, padx=20)

        # Buttons
        image_true = PhotoImage(file='images/true.png')
        button_true = Button(image=image_true, highlightthickness=0)
        button_true.grid(row=2, column=0)
        image_false = PhotoImage(file='images/false.png')
        button_false = Button(image=image_false, highlightthickness=0)
        button_false.grid(row=2, column=1, pady=20)

        self.window.mainloop()
