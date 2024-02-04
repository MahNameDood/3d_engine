import math, pygame
from renderer import project

class Triangle:
	def __init__(self, points):
		self.points = points
	def render(self, win, focal_length, win_dim, col, cam_pos, cam_rot):
		projected_points = []
		for p in self.points:

			proj = project(focal_length, win_dim, p, cam_pos, cam_rot)

			projected_points.append(proj)

		pygame.draw.polygon(win, col, projected_points)