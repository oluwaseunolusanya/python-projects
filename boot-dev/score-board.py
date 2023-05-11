'''Total Score
A website that tracks basketball scores and stats is having trouble with its data. The first-half score and second-half score are stored in separate dictionaries, making it difficult for them to parse the overall score. They have asked you to help them write a program that merges the two dictionaries and another function that calculates the total score.
Challenge

Complete the merge and total_score functions.

The merge function accepts two score dictionaries as input and returns a single merged dictionary that contains all of the keys and values from the input dictionaries.

The total_score function should take a single score dictionary as input and return the total score calculated from the values of that dictionary.
'''

def merge(dict1, dict2):
    return (dict1|dict2)


def total_score(score_dict):
    total_score = 0

    for k,v in score_dict.items():
        total_score += v

    return total_score


# Don't touch below this line


def test(first_half, second_half):
    merged = merge(first_half, second_half)
    total = total_score(merged)
    print(f"The team scored {total} points")


test(
    {"first_quarter": 24, "second_quarter": 31},
    {"third_quarter": 29, "fourth_quarter": 40},
)

test(
    {"first_quarter": 25, "second_quarter": 2},
    {"third_quarter": 31, "fourth_quarter": 0},
)


test(
    {"first_quarter": 12, "second_quarter": 2},
    {"third_quarter": 32, "fourth_quarter": 87},
)