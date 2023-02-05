import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = tkinter.Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=1, column=2)

        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Question placeholder",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR,
        )
        self.canvas.grid(row=2, column=1, columnspan=2, pady=50)

        correct_image = tkinter.PhotoImage(file="images/true.png")
        self.correct_button = tkinter.Button(
            image=correct_image,
            bg=THEME_COLOR,
            highlightthickness=0
        )
        self.correct_button.grid(row=3, column=1)

        wrong_image = tkinter.PhotoImage(file="images/false.png")
        self.wrong_button = tkinter.Button(
            image=wrong_image,
            bg=THEME_COLOR,
            highlightthickness=0
        )
        self.wrong_button.grid(row=3, column=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
