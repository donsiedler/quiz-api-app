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
            width=280,
            text="Question placeholder",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR,
        )
        self.canvas.grid(row=2, column=1, columnspan=2, pady=50)

        correct_image = tkinter.PhotoImage(file="images/true.png")
        self.correct_button = tkinter.Button(
            image=correct_image,
            bg=THEME_COLOR,
            highlightthickness=0,
            command=self.correct_pressed,
        )
        self.correct_button.grid(row=3, column=1)

        wrong_image = tkinter.PhotoImage(file="images/false.png")
        self.wrong_button = tkinter.Button(
            image=wrong_image,
            bg=THEME_COLOR,
            highlightthickness=0,
            command=self.wrong_pressed,
        )
        self.wrong_button.grid(row=3, column=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def correct_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)



