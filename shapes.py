import turtle
t = turtle.Turtle()

class circle():
	def __init__(self, r):
                self.r = r
                t.circle(r)

class polygon():
	def __init__(self, sides = 0, length = 0):
                self.sides = sides
                self.length = length

class square(polygon):
	def show(self):
		for i in range(4):	
		     	t.fd(self.length)
		     	t.rt(90)

class triangle(polygon):
        def show(self):
                for i in range(3):
                        t.fd(self.length)
                        t.rt(120)

class pentagon(polygon):
	def show(self):
		for i in range(5):
			t.fd(self.length)
			t.rt(72)

class hexagon(polygon):
        def show(self):
                for i in range(6):
                        t.fd(self.length)
                        t.rt(60)

class octagon(polygon):
        def show(self):
                for i in range(8):
                        t.fd(self.length)
                        t.rt(45)

cir = circle(400)
turtle.Screen().reset()
sq = square(4, 500)
sq.show()
turtle.Screen().reset()
tri = triangle(3, 300)
tri.show()
turtle.Screen().reset()
pen = pentagon(5, 400)
pen.show()
turtle.Screen().reset()
oct = octagon(8, 300)
oct.show()
turtle.done()