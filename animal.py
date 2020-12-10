class Animals:
	def __init__(self, legs = 4, eyes = 2, ears = 2):
		self.legs = legs
		self.eyes = eyes
		self.ears = ears
	#abstract class
	def place(self):
		pass
	#virtual class
	def eat(self):
		print("eats food")
			
class Domestic(Animals):
	def place(self):
		print("Pets of humans")
		
class Wild(Animals):
	def place(self):
		print("Lives in Jungle")
		
#inheriting animal class in herbivores, carnivores and omnivores
class Herbivores(Animals):
	def eat(self):
		print("Eats plants")
		
class Carnivores(Animals):
	def eat(self):
		print("Eats other animals")
		
class Omnivores(Animals):
	def eat(self):
		print("Eats plants and animals")
		
		
class cow(Domestic, Herbivores):
	def speak(self):
		print("moo")
	def colour(self):
		print("black, white, brown")
	def lifespan(self):
		print("18-22 years")

class goat(Domestic, Herbivores):
	def speak(self):
		print("bleat")
	def colour(self):
		print("black, white, brown")
	def lifespan(self):
		print("15-18 years")
		
class deer(Wild, Herbivores):
	def speak(self):
		print("bellow")
	def colour(self):
		print("brown")
	def lifespan(self):
		print("15-25 years")
		
class giraffe(Wild, Herbivores):
	def speak(self):
		print("hum")
	def colour(self):
		print("brown or orange with patches")
	def lifespan(self):
		print("26 years")
		
class zebra(Wild, Herbivores):
	def speak(self):
		print("bray")
	def colour(self):
		print("black and white")
	def lifespan(self):
		print("25 years")
		
class dog(Domestic, Omnivores):
	def speak(self):
		print("bark")
	def colour(self):
		print("black, white, brown, golden, yellow")
	def lifespan(self):
		print("10-13 years")
		
class bear(Wild, Omnivores):
	def speak(self):
		print("growl")
	def colour(self):
		print("white, brown")
	def lifespan(self):
		print("20 years")

class cat(Domestic, Carnivores):
	def speak(self):
		print("meow")
	def colour(self):
		print("black, white, brown, grey, orange")
	def lifespan(self):
		print("2-16 years")
		
class tiger(Wild, Carnivores):
	def speak(self):
		print("roar")
	def colour(self):
		print("orange with black strips")
	def lifespan(self):
		print("10-15 years")
		
class lion(Wild, Carnivores):
	def speak(self):
		print("roar")
	def colour(self):
		print("yellow")
	def lifespan(self):
		print("10-14 years")
		

#k = Animals(4,2,2)
a = deer()
a.eat()
a.speak()
a.colour()
a.lifespan()
print(a.eyes)
print(a.legs)
		

		
		
	
