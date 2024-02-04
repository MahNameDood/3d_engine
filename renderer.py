import math

def project(focal_length, win_dim, p, cam_pos, cam_rot):
	new_point = [0,0]
	point = p 

	point[0] -= cam_pos[0]
	point[1] -= cam_pos[1]
	point[2] -= cam_pos[2]

	if point[2] == 0:
		point[2] = 0.001
	new_point[0] = (point[0] * (focal_length / point[2])) + win_dim[0]/2
	new_point[1] = (point[1] * (focal_length / point[2])) + win_dim[1]/2



	return new_point

