'''
We need to be able to report to our players how many enemies are in their immediate vicinity - but they want the count of each enemy by its kind. 
Complete the count_enemies function. It takes a list of enemy names as input. It should return a dictionary where the keys are all the enemy names 
from the list, and the values are the counts of how many times each enemy appeared in the list.'''

def count_enemies(enemy_names):
    enemies = {}

    for enemy in enemy_names:
        if enemy in enemies:
            enemies[enemy] += 1
        else:
            enemies[enemy] = 1
        
    return enemies        


# Don't edit below this line


def main():
    print(
        count_enemies(
            [
                "jackal",
                "kobold",
                "jackal",
                "kobold",
                "soldier",
                "kobold",
                "soldier",
                "soldier",
                "jackal",
                "jackal",
                "gremlin",
                "jackal",
                "jackal",
            ]
        )
    )


main()