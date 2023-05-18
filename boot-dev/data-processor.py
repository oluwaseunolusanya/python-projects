'''John is a data analyst, but he's bad with code. He has asked you for a script that can remove duplicates from some of his data sets.

Complete the remove_duplicates function. It accepts a list of strings and removes any duplicate values.

Bonus points if you can write the body of the function in a single line of code.
'''

def remove_duplicates(lst):
    return set(lst)

def test(lst):
    removed = sorted(remove_duplicates(lst))
    print(f"Variable 'removed' is of type: {type(removed)}")
    print("List after duplicates removed:")
    for item in removed:
        print(f"- {item}")
    print("---")


test(["basketball", "football", "soccer", "baseball", "basketball"])
test(
    [
        "Age of Empires",
        "World of Warcraft",
        "Halo",
        "Call of Duty",
        "Age of Empires",
        "Magic the Gathering",
        "Halo",
    ]
)
test(
    [
        "Lane",
        "Allan",
        "James",
        "Tiffany",
        "John",
        "Cameron",
        "Lane",
        "Allan",
        "James",
        "Tiffany",
        "John",
        "Cameron",
        "Chad",
        "Tj",
        "Tim",
        "Gertrude",
        "Stephanie",
    ]
)