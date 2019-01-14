class Cat:

	type = "cat"

	def __init__(self, name, breed):
		self.name = name
		self.colors = []
		self.breed = breed

	def add_color(self, color):
		self.colors.append(color)


one = Cat("Tomo", "Russian")
two = Cat("Dachi", "Alpine")

one.add_color("white")
two.add_color("black")

print(one.colors)
print(two.colors)

two.add_color("brown")

print(one.colors)
print(one.breed)
print(two.colors)
print(two.breed)

print(Cat.type)
print(one.type)
print(two.type)
