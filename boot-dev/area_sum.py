'''Complete the area_sum() function. It accepts an array of rectangles, where each rectangle is a dictionary that has the following structure:
{
  "height": 5,
  "width": 6
}

The function will calculate the area of each rectangle, then sum them all up and return the result.
'''

def area_sum(rectangles):
    total_area = 0

    for rectangle in rectangles:
        area = rectangle["height"] * rectangle["width"]
        total_area += area

    return total_area


def test(rects):
    sum = area_sum(rects)
    print(f"sum is {sum}")


test([{"height": 4, "width": 5}])
test([{"height": 4, "width": 5}, {"height": 4, "width": 9}, {"height": 18, "width": 5}])
test(
    [
        {"height": 4, "width": 5},
        {"height": 8, "width": 5},
        {"height": 19, "width": 5},
        {"height": 21, "width": 5},
    ]
)
