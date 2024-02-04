import pygame, sys, random
from renderer import project

pygame.init()

WIDTH = 1900
HEIGHT = 1000
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('3D')

point = [0,10,10]

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	win.fill((0,0,0))

	projected = project(1, point, (WIDTH, HEIGHT))
	print(projected)
	pygame.draw.circle(win, (255,255,255), projected, 1)


	pygame.display.update()
	clock.tick(60)