import tkinter as tk
from gui_quiz_app.quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain : QuizBrain): # shows the data type of quiz_brain
        self.quiz = quiz_brain
        # window
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(width=500, height=800, bg= THEME_COLOR, padx=20, pady=50)

        # canvas
        self.canvas = tk.Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="", width= 280, font= ("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=60)

        # label
        self.score_label = tk.Label(text= "Score: 0", bg=THEME_COLOR, fg= "white", font= ("Arial", 15, "bold"))
        self.score_label.grid(row=0, column=1, sticky= "e")

        # button
        check_image = tk.PhotoImage(file="images/true.png")
        cross_image = tk.PhotoImage(file="images/false.png")

        self.check_button = tk.Button(image= check_image,
                                      highlightthickness= 0,
                                      command=lambda : self.check_correct_answer("true"))

        self.cross_button = tk.Button(image= cross_image,
                                      highlightthickness= 0,
                                      command=lambda : self.check_correct_answer("false"))

        self.check_button.grid(row=2, column=0)
        self.cross_button.grid(row=2, column=1)

        # calling the method
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """gets the next question from the question list"""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            next_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=next_question)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.score_label.config(text=f"Score: {self.quiz.score}/{len(self.quiz.question_list)}")
            self.check_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def check_correct_answer(self, user_answer):
        self.give_user_feedback(self.quiz.check_answer(user_answer))

    def give_user_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


