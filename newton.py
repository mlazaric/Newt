#!/bin/python

import os
from PIL import Image
from FrameGenerator import FrameGenerator

for rootDegree in range(4, 11):
	imgs = []
	fg = FrameGenerator(rootDegree, 1920, 1080, -1.920, 1.920, -1.080, 1.080)

	numberOfIterations = 1

	while len(fg.pointsLeft) > 2000 or fg.isFirstIteration:
		print('Calculating {:2d}th root using {:2d} iterations ({:d} points left to converge)'.format(rootDegree, numberOfIterations, len(fg.pointsLeft)))
		imgs.append(fg.iterate())
		numberOfIterations += 1


	imgs[0].save('{:d}th_root.gif'.format(rootDegree),
		         save_all=True,
		         append_images=imgs[1:],
		         duration=250,
		         loop=0,
		         optimize=True)