def common_elements():
	multiple_of_3 = set(range(0,100,3))
	multiple_of_5 = set(range(0,100,5))
	res_set = multiple_of_3.intersection(multiple_of_5)
	return res_set


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
