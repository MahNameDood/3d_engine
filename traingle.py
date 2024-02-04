import math, pygame
from renderer import project

class Triangle:
	def __init__(self, points):
		self.points = points
	def render(self, win, focal_length, win_dim, col):
		projected_points = []
		for p in self.points:
			projected_points.append(project(focal_length, win_dim, p))

		pygame.draw.polygon(win, col, projected_points)
