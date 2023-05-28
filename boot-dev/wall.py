'''Creating a class called Wall with a property called armor
that is initialized to 10 and a height that starts at 5.
'''

class Wall:
	armor = 10
	height = 5
	
	def get_cost(self):
		return self.armor * self.height

	def fortify(self):
		self.armor *= 2

def main():
    wall = Wall()
    print(f"Cost of wall: {wall.get_cost()}")

    print("fortifying wall...")
    wall.fortify()
    print(f"Cost of wall: {wall.get_cost()}")

    print("fortifying wall...")
    wall.fortify()
    print(f"Cost of wall: {wall.get_cost()}")

    print("fortifying wall...")
    wall.fortify()
    print(f"Cost of wall: {wall.get_cost()}")
    
    wall_2 = Wall()
    print(wall_2.armor)
    wall_2.armor = 20
    print(wall_2.armor)
    Wall.armor = 5
    print(wall_2.armor)    


main()
