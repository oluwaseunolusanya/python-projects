'''Creating a class called Wall with a property called armor
that is initialized to 10 and a height that starts at 5.
'''

class Wall:
	armor = 10
	height = 5
	
	def fortify(self):
		self.armor *= 2

def main():
	wall = Wall()
	print(wall.armor)
	print(wall.height)
	wall.fortify()
	print(wall.armor)
	wall.fortify()
	print(wall.armor)

main()
