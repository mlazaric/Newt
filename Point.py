import math

class Point:
	def __init__(self, number, root_degree):
		self.number = number
		self.root_degree = root_degree
		self.curr_number_of_iterations = 0
		self.has_converged = False

	def iterate(self, num_of_iterations=1):
		if self.number == 0:
			return
		if self.has_converged:
			return

		for i in range(num_of_iterations):
			self.number = (1.0 / self.root_degree) * ((self.root_degree - 1) * self.number + 1.0/pow(self.number, self.root_degree - 1))
			self.curr_number_of_iterations += 1
			self.has_converged = self.__has_converged()

			if self.has_converged:
				break

	def __has_converged(self):
		test = abs(pow(self.number, self.root_degree))

		return abs(test - 1) < 1e-4

	def get_color(self):
		shade = 1 - math.atan(self.curr_number_of_iterations / (self.root_degree * 20)) / (math.pi / 2)
		#shade = (1 - self.curr_number_of_iterations/100.0) ** 2

		r = int((1 + self.number.real) * 127 * shade)
		g = int((1 + self.number.imag) * 127 * shade)
		b = int(150 * shade)
		a = 255

		if r > 255 or g > 255 or r < 0 or g < 0 or not self.has_converged:
			r = g = b = 0

		return (r, g, b, a)