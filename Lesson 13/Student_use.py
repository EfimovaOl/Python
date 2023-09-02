from Student import Student

student = Student("Иван Петров", "subjects.csv")
student.add_score("Math", 4)
student.add_test_result("Math", 80)
print(student.average_test_score("Math"))
print(student.average_score())