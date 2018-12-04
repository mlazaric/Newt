from PIL import Image
from Point import Point

class FrameGenerator:
	def __init__(self, root_degree=4, width=720, height=720, x_start=-1, x_end=1, y_start=-1, y_end=1):
		self.root_degree = root_degree
		
		self.height = height
		self.width = width

		self.x_start = x_start
		self.x_end = x_end
		self.y_start = y_start
		self.y_end = y_end

		self.xIncrement = (x_end - x_start) / width
		self.yIncrement = (y_end - y_start) / height

		self.is_first_iteration = True
		self.points_left = []
		self.last_image = None

	def iterate(self, num_of_iterations=1):
		if self.is_first_iteration:
			img = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 255))
			pixels = img.load()

			self.is_first_iteration = False

			for xOffset in range(self.width):
				for yOffset in range(self.height):
					xn = Point(self.x_start + xOffset * self.xIncrement + (self.y_start + yOffset * self.yIncrement)*1.0j, self.root_degree)

					xn.iterate(num_of_iterations)

					if not xn.has_converged:
						self.points_left.append((xOffset, yOffset, xn))

					pixels[xOffset, yOffset] = xn.get_color()

			self.last_image = img.copy()

			return img
		else:
			img = self.last_image.copy()
			pixels = img.load()

			for (xOffset, yOffset, xn) in self.points_left:
				xn.iterate(num_of_iterations)

				pixels[xOffset, yOffset] = xn.get_color()

			self.points_left = [(xOffset, yOffset, xn) for (xOffset, yOffset, xn) in self.points_left if not xn.has_converged]
			self.last_image = img.copy()

			return img
