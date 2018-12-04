#!/bin/python

import os
from PIL import Image, ImageDraw, ImageFont
from FrameGenerator import FrameGenerator

for rootDegree in range(4, 11):
	imgs = []
	width = 1000#4096
	height = 1000#2160
	fg = FrameGenerator(rootDegree, width, height, -width / 1000, width / 1000, -height / 1000, height / 1000)

	numberOfIterations = 0

	while len(fg.points_left) > 4000 or fg.is_first_iteration:
		imgs.append(fg.iterate(2))
		print('Calculated {:2d}th root using {:2d} iterations ({:d} points left to converge)'.format(rootDegree, numberOfIterations, len(fg.points_left)))
		numberOfIterations += 2

		draw = ImageDraw.Draw(imgs[len(imgs) - 1])
		font = ImageFont.truetype('DejaVuSans.ttf', int(height / 25.0))
		draw.text((int(width / 2.0), 0), str(numberOfIterations), (255, 255, 255), font=font)
		#imgs[len(imgs) - 1].save('test/test_{:d}.gif'.format(len(imgs)))


	imgs[0].save('test/{:d}th_root.gif'.format(rootDegree),
		         save_all=True,
		         append_images=imgs[1:],
		         duration=100,
		         loop=0,
		         optimize=True)