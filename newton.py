#!/bin/python

from PIL import Image
from math import sqrt

width = 720
height = 720

xStart = -5
xEnd = 5
yStart = -5
yEnd = 5

xIncrement = (xEnd - xStart) / width
yIncrement = (yEnd - yStart) / height

def calculateRoot(number, rootDegree = 4, numberOfIterations = 40):
	xn = number

	if number == 0:
		return 0

	for i in range(numberOfIterations):
		xn = (1.0 / rootDegree) * ((rootDegree - 1) * xn + 1.0/pow(xn, rootDegree - 1))

	return xn

img = Image.new('RGB', (width, height))
pixels = img.load()

for xOffset in range(width):
	for yOffset in range(height):
		xn = calculateRoot(xStart + xOffset * xIncrement + (yStart + yOffset * yIncrement)*1.0j, 10)

		r = int((1 + xn.real) * 127)
		g = int((1 + xn.imag) * 127)
		b = 150

		test = abs(pow(xn, 4))

		if r > 255 or g > 255 or r < 0 or g < 0 or abs(test - 1) > 1e-4:
			r = g = b = 0

		pixels[xOffset, yOffset] = (r, g, b)

img.save('image.png');
img.show()