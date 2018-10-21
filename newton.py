#!/bin/python

import os
from PIL import Image

width = 720
height = 720

xStart = -5
xEnd = 5
yStart = -5
yEnd = 5

xIncrement = (xEnd - xStart) / width
yIncrement = (yEnd - yStart) / height

def calculateRoot(number, rootDegree = 4, numberOfIterations = 10):
	xn = number

	if number == 0:
		return (0, 0)

	for i in range(numberOfIterations):
		xn = (1.0 / rootDegree) * ((rootDegree - 1) * xn + 1.0/pow(xn, rootDegree - 1))

		test = abs(pow(xn, 4))

		if abs(test - 1) < 1e-4:
			return (xn, i)


	return (xn, numberOfIterations)

def generateImage(rootDegree = 4, numberOfIterations = 10):
	img = Image.new('RGBA', (width, height))
	pixels = img.load()

	for xOffset in range(width):
		for yOffset in range(height):
			(xn, speed) = calculateRoot(xStart + xOffset * xIncrement + (yStart + yOffset * yIncrement)*1.0j, rootDegree, numberOfIterations)

			r = int((1 + xn.real) * 127)
			g = int((1 + xn.imag) * 127)
			b = 150
			a = 0cd#int(150 * (1 - speed / numberOfIterations))

			test = abs(pow(xn, 4))

			if r > 255 or g > 255 or r < 0 or g < 0 or abs(test - 1) > 1e-4:
				r = g = b = 0

			pixels[xOffset, yOffset] = (r, g, b, a)

	return img
	#.save('rootDegree_{:d}_numberOfIterations_{:d}.png'.format(rootDegree, numberOfIterations))

#for rootDegree in range(4, 11):
imgs = []
rootDegree = 4

for numberOfIterations in range(10, 15):
	print('Calculating {:d}th root using {:d} iterations'.format(rootDegree, numberOfIterations))
	imgs.append(generateImage(rootDegree, numberOfIterations))


imgs[0].save('test.gif',
	         save_all=True,
	         append_images=imgs[1:],
	         duration=250,
	         loop=0)