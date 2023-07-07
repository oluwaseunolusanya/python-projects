"""Write a function to find the median of a given list of numbers.
"""
def median_followers(nums):
    sorted_nums = sorted(nums) 
    if len(nums) > 1:
        quotient = len(sorted_nums) // 2
        #print(quotient)
        remainder = len(sorted_nums) % 2
       # print(remainder)
        if remainder  == 0:
            return (sorted_nums[quotient] + sorted_nums[quotient - 1]) / 2
        else:
            return sorted_nums[quotient]
    elif len(sorted_nums) == 0:
        raise Exception("List cannot be empty.")
    else:
        return sorted_nums[0]
        
    


def test(nums):
    res = round(median_followers(nums))
    print(f"Follower counts: {nums}")
    print(f"Median follower count: {res}")
    print("----")


def main():
    test([7, 4, 3, 100, 2343243, 343434, 1, 2, 32])
    test([12, 12, 12])
    test([10, 200, 3000, 5000, 4])
    test([10, 200, 3000, 5000, 4, 6])


main()
