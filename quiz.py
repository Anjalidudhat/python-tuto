class User:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password  # In a real application, passwords should be hashed.
        self.scores = {}  # {quiz_id: score}

    def __str__(self):
        return f"User ID: {self.user_id}, Username: {self.username}, Scores: {self.scores}"
class Question:
    def __init__(self, question_id, text, options, correct_option):
        self.question_id = question_id
        self.text = text
        self.options = options  # List of options
        self.correct_option = correct_option

    def check_answer(self, answer):
        return answer == self.correct_option

    def __str__(self):
        return f"Question ID: {self.question_id}, Text: {self.text}, Options: {self.options}"
class Quiz:
    def __init__(self, quiz_id, title):
        self.quiz_id = quiz_id
        self.title = title
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def __str__(self):
        return f"Quiz ID: {self.quiz_id}, Title: {self.title}, Questions: {[q.question_id for q in self.questions]}"
class QuizManagementSystem:
    def __init__(self):
        self.users = {}
        self.quizzes = {}
        self.questions = {}

    # User Management
    def add_user(self, user_id, username, password):
        if user_id in self.users:
            print(f"User with ID {user_id} already exists.")
        else:
            self.users[user_id] = User(user_id, username, password)
            print(f"User {username} added successfully.")

    def authenticate_user(self, username, password):
        for user in self.users.values():
            if user.username == username and user.password == password:
                return user
        return None

    # Quiz Management
    def create_quiz(self, quiz_id, title):
        if quiz_id in self.quizzes:
            print(f"Quiz with ID {quiz_id} already exists.")
        else:
            self.quizzes[quiz_id] = Quiz(quiz_id, title)
            print(f"Quiz {title} created successfully.")

    def add_question_to_quiz(self, quiz_id, question):
        if quiz_id in self.quizzes:
            self.quizzes[quiz_id].add_question(question)
            print(f"Question added to quiz {quiz_id} successfully.")
        else:
            print(f"No quiz found with ID {quiz_id}.")

    # Question Management
    def create_question(self, question_id, text, options, correct_option):
        if question_id in self.questions:
            print(f"Question with ID {question_id} already exists.")
        else:
            self.questions[question_id] = Question(question_id, text, options, correct_option)
            print(f"Question created successfully.")

    # Taking Quizzes
    def take_quiz(self, user, quiz_id):
        if quiz_id in self.quizzes:
            quiz = self.quizzes[quiz_id]
            score = 0
            for question in quiz.questions:
                print(question.text)
                for idx, option in enumerate(question.options, 1):
                    print(f"{idx}. {option}")
                answer = int(input("Choose the correct option: ")) - 1
                if question.check_answer(question.options[answer]):
                    score += 1
            user.scores[quiz_id] = score
            print(f"Your score for quiz {quiz_id} is {score}/{len(quiz.questions)}")
        else:
            print(f"No quiz found with ID {quiz_id}.")

    # Progress Tracking
    def view_progress(self, user):
        print(user)
qms = QuizManagementSystem()

# Adding users
qms.add_user(1, "Alice", "password123")
qms.add_user(2, "Bob", "password456")

# Creating questions
qms.create_question(1, "What is the capital of France?", ["Paris", "London", "Berlin", "Rome"], "Paris")
qms.create_question(2, "What is 2 + 2?", ["3", "4", "5", "6"], "4")

# Creating a quiz and adding questions
qms.create_quiz(1, "General Knowledge")
qms.add_question_to_quiz(1, qms.questions[1])
qms.add_question_to_quiz(1, qms.questions[2])

# User takes the quiz
user = qms.authenticate_user("Alice", "password123")
if user:
    qms.take_quiz(user, 1)

# View progress
qms.view_progress(user)




