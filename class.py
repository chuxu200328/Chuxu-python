# a = [5,2,6,7,9,1,0,3]

# def find_min(list):
# 	b = list[0]
# 	for i in list:
# 		if b > i:
# 			b = i
# 	print(b)

# find_min(a)





a = [5,2,6,7,9,1,0,3]
def find_min(list):
	if len(list) > 0:
		return min(list)
	else:
		return "Invalid"
def find_index(list,item):
	if len(list) > 0:
		for i in range(len(list)):
			if list[i] == item:
				return i
	else:
		return"Invalid"

def selection_sort(list):
	new_list = []
	while len(list) > 0:
		x = find_min(list)
		y = find_index(list,x)
		list.pop(y)
		new_list.append(x)
	return new_list


def swap(x,y):
	return y, x


def _bubble_sort(list):
	for i in range(1,len(list)):
		index_b = i
		index_a = i - 1

		if list[index_b] < list[index_a]:
			list[index_b],list[index_a] = swap(list[index_b],list[index_a])

def bubble_sort(list):
	if len(list) <= 1:
		return list	
	
	for i in range(len(list)):
		_bubble_sort(list)

	print(list)
	
bubble_sort(a)


