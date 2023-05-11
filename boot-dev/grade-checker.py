'''A local college is having trouble with its student administration program. 
They have asked you to help them print a student's grade from their English_1010 class.

Here's the structure of a student dictionary:

{
    "type": {
        "student": {
            "name": "Allan",
            "courses": {
                "math_1050": {
                    "current_grade": "B",
                },
                "English_1010": {
                    "current_grade": "A-",
                },
            },
        }
    }
}

Complete the get_english_grade function. It accepts a student dictionary and returns the student's grade in English 1010.
'''

def get_english_grade(student):
    return student["type"]["student"]["courses"]["English_1010"]["current_grade"]


def test(student):
    grade = get_english_grade(student)
    name = student["type"]["student"]["name"]
    print(f"{name}'s grade in English is {grade}")


test(
    {
        "type": {
            "student": {
                "name": "Allan",
                "courses": {
                    "math_1050": {
                        "current_grade": "C",
                    },
                    "English_1010": {
                        "current_grade": "D-",
                    },
                },
            }
        }
    }
)

test(
    {
        "type": {
            "student": {
                "name": "Lane",
                "courses": {
                    "math_1050": {
                        "current_grade": "D",
                    },
                    "English_1010": {
                        "current_grade": "F",
                    },
                },
            }
        }
    }
)


test(
    {
        "type": {
            "student": {
                "name": "Breanna",
                "courses": {
                    "math_1050": {
                        "current_grade": "A",
                    },
                    "English_1010": {
                        "current_grade": "A",
                    },
                },
            }
        }
    }
)

test(
    {
        "type": {
            "student": {
                "name": "Tiff",
                "courses": {
                    "math_1050": {
                        "current_grade": "A",
                    },
                    "English_1010": {
                        "current_grade": "A",
                    },
                },
            }
        }
    }
)