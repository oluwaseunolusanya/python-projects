'''We need to display on our player's screens what the most common enemy in a given area of the game map is. 
Complete the get_most_common_enemy function. It should iterate over all the enemies in the dictionary and 
return the name of the enemy with the highest count.

Note: enemies_dict is a dictionary of name -> count.'''

def get_most_common_enemy(enemies_dict):
	max_count = float("-inf")    #Starting the max_count with the lowest value possible using Python special function 'float()'.
	most_common =""
	
	for enemy in enemies_dict:
		if enemies_dict[enemy] > max_count:
			max_count = enemies_dict[enemy]
			most_common = enemy
	
	return most_common
		
		


def test(enemies_dict):
    most_common = get_most_common_enemy(enemies_dict)
    print(f"Using dict: {enemies_dict}")
    print(f"Most common: {most_common}")
    print("----")


def main():
    test({"jackal": 4, "kobold": 3, "soldier": 10, "gremlin": 5})
    test({"jackal": 1, "kobold": 3, "soldier": 2, "gremlin": 5})
    test({"jackal": 2, "gremlin": 7})


main()