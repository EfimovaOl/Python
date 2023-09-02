class StudentNameError(Exception):
    def __init__(self, massage="Имя студента введено неверно. Должно содержать только буквы и начинаться с заглавной буквы"):
        self.massage = massage
        super().__init__(self.massage)

class InvalidSubjectError(Exception):
    def __init__(self, subject_name):
        self.massage = f"Предмет '{subject_name}' не найден в файле csv."
        super().__init__(self.massage)

class InvalidScoreError(Exception):
    def __init__(self, score, score_type="Оценка"):
        self.massage = f"{score_type} '{score}' недействительна. Оценки должны быть от 2 до 5, а результаты от 0 до 100."
        super().__init__(self.massage)