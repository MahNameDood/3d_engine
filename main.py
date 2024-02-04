import pygame, sys, random, math
from renderer import project
from triangle import Triangle


pygame.init()

WIDTH = 1900
HEIGHT = 1000
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('3D')

cam_pos = [0,0,0]
cam_rot = [0.0,0.0,0.0]
focal_length = 1000

mouse_sens = 0.2
mouse_moved = [0.0,0.0]

draw_grid = True

t = 0
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	win.fill((0,0,0))
	keys = pygame.key.get_pressed()

	for x in range(50):
		for z in range(50):
			pos = [x*10, 10, z*10]
			#grid_tri = Triangle((pos, pos, pos))
			#grid_tri.render(win, focal_length, (WIDTH, HEIGHT), (255,0,0), cam_pos, cam_rot)
			pygame.draw.circle(win, (255,0,0), project(focal_length, (WIDTH, HEIGHT), pos, cam_pos, cam_rot), 2)
	
	
	

	test = Triangle(([10,0,1], [0,10,1], [0,0,1]))
	test.render(win, focal_length, (WIDTH, HEIGHT), (255,255,255), cam_pos, cam_rot)

	if keys[pygame.K_a]:
		cam_pos[0] -= 1
	if keys[pygame.K_d]:
		cam_pos[0] += 1
	if keys[pygame.K_w]:
		cam_pos[2] += 1
	if keys[pygame.K_s]:
		cam_pos[2] -= 1
	if keys[pygame.K_SPACE]:
		cam_pos[1] -= 1
	if keys[pygame.K_LSHIFT]:
		cam_pos[1] += 1
	if keys[pygame.K_e]:
		cam_rot[1] -= 1
	if keys[pygame.K_q]:
		cam_rot[1] += 1
	if keys[pygame.K_u]:
		cam_rot[0] -= 1
	if keys[pygame.K_j]:
		cam_rot[0] += 1



	mouse_moved = (pygame.mouse.get_pos()[0] - WIDTH/2, pygame.mouse.get_pos()[1] - HEIGHT/2)
	pygame.mouse.set_pos((WIDTH/2, HEIGHT/2))
	t += 1
	pygame.display.update()
	clock.tick(60)