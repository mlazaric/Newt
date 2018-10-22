from PIL import Image
from Point import Point

class FrameGenerator:
	def __init__(self, rootDegree=4, width=720, height=720, xStart=-1, xEnd=1, yStart=-1, yEnd=1):
		self.rootDegree = rootDegree
		
		self.height = height
		self.width = width

		self.xStart = xStart
		self.xEnd = xEnd
		self.yStart = yStart
		self.yEnd = yEnd

		self.xIncrement = (xEnd - xStart) / width
		self.yIncrement = (yEnd - yStart) / height

		self.isFirstIteration = True
		self.pointsLeft = []
		self.lastImage = None

	def iterate(self):
		if self.isFirstIteration:
			img = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 255))
			pixels = img.load()

			self.isFirstIteration = False

			for xOffset in range(self.width):
				for yOffset in range(self.height):
					xn = Point(self.xStart + xOffset * self.xIncrement + (self.yStart + yOffset * self.yIncrement)*1.0j, self.rootDegree)

					xn.iterate()

					if not xn.has_converged:
						self.pointsLeft.append((xOffset, yOffset, xn))

					pixels[xOffset, yOffset] = xn.get_color()

			self.lastImage = img

			return img
		else:
			img = self.lastImage.copy()
			pixels = img.load()

			for (xOffset, yOffset, xn) in self.pointsLeft:
				xn.iterate()

				pixels[xOffset, yOffset] = xn.get_color()

			self.pointsLeft = [(xOffset, yOffset, xn) for (xOffset, yOffset, xn) in self.pointsLeft if not xn.has_converged]
			self.lastImage = img

			return img
