"""
User Story - Credit: BOOT.DEV
=============================
A school principal seeks a program to securely store student information
and automatically calculate letter grades based on score.
1. The program shall simplify grading and course management for teachers.
2. The program should maintain student privacy for enrolled courses.
"""

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.__courses = {}

    def calculate_letter_grade(self, score):
        if score >= 90:
            return "A"
        elif score in range(80, 90):
            return "B"
        elif score in range(70, 80):
            return "C"
        elif score in range(60, 70):
            return "D"
        else:
            return "F"

    def add_course(self, course_name, score):
        course_grade = self.calculate_letter_grade(score)
        self.__courses[course_name] = course_grade

    def get_courses(self):
        return self.__courses
          


def test(student_name, courses, scores):
    student = Student(student_name, scores)
    print(f"Student created: {student_name}")

    for i, course in enumerate(courses):
        student.add_course(course, scores[i])
        print(f"Added course: {course} with score: {scores[i]}")
    courses = student.get_courses()
    for course in courses:
        print(f"{student_name}'s grade in {course} is a {courses[course]}")
    test_encapsulation(student)
    print("=====================================")


def test_encapsulation(student):
    try:
        print(student.__courses)
    except:
        print("Private data member is encapsulated properly")


def main():
    test("John Thorton", ["Math", "English", "History"], [85, 92, 76])
    test("Jasper Allen", ["Science", "Social Studies"], [90, 88])
    test(
        "Bobby Christensen",
        ["Physics", "Chemistry", "Biology", "Geology"],
        [80, 78, 85, 90],
    )


main()
