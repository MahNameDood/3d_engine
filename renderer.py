import math

def project(focal_length, point, win_dim):
	new_point = [0,0]

	new_point[0] = (point[0] * (focal_length / point[2])) + win_dim[0]/2
	new_point[1] = (point[1] * (focal_length / point[2])) + win_dim[1]/2



	return new_point