class Point:
	def __init__(self, number, rootDegree):
		self.number = number
		self.rootDegree = rootDegree
		self.currNumberOfIterations = 0
		self.has_converged = False

	def iterate(self):
		if self.number == 0:
			return

		self.number = (1.0 / self.rootDegree) * ((self.rootDegree - 1) * self.number + 1.0/pow(self.number, self.rootDegree - 1))
		self.currNumberOfIterations += 1
		self.has_converged = self.__has_converged()

	def __has_converged(self):
		test = abs(pow(self.number, 4))

		return abs(test - 1) < 1e-4

	def get_color(self):
		r = int((1 + self.number.real) * 127)
		g = int((1 + self.number.imag) * 127)
		b = 150
		a = 255

		if r > 255 or g > 255 or r < 0 or g < 0 or not self.has_converged:
			r = g = b = 0

		return (r, g, b, a)