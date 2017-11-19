# Uncomment and implement the function stubs 
# each function must run properly for both lists and tuples
# run on command line as follows:
# python si_practice1.py

def my_length(arg1):
	# count number of elements in arg1 
	#	without using len() function
	counter = 0
	for elem in arg1:
		# iterates through all elements in arg1
		# elem contains the value, NOT the index of each element
		counter = counter + 1

	return counter

def my_concat(arg1, arg2):
	# append all of arg2 to arg1 
	#	without using arg1 + arg2
	# returned container must be of same type as arg1
	out_container = arg1
	for elem in arg2:
		out_container.append(elem)

	return out_container

def my_min(arg1):
	# find and return the element with the minimum value in arg1
	#	without using min(arg1)
	# for arg1 that contains char elements, refer to an ASCII table 
	# 	to find its equivalent numerical value
	min_value = arg1[0]
	for elem in arg1[1:]: # start at index 1 rather than index 0 and iterate to the end
		if elem < min_value:
			min_value = elem

	return min_value	

def my_max(arg1):
	# find and return the element with the maximum value in arg1
	#	without using max(arg1)
	# for arg1 that contains char elements, refer to an ASCII table 
	# 	to find its equivalent numerical value
	max_value = arg1[0]	
	for elem in arg1[1:]: 
		if elem > max_value:
			max_value = elem

	return max_value	

def my_sum(arg1):
	# sum all of the elements in arg1 
	#	without using sum(arg1)
	sum_val = 0
	for elem in arg1:
		sum_val += elem

	return sum_val

def my_index(arg1, val):
	# find and return the index of the first element in arg1 with value val 
	#	without using arg1.index(val)
	# Throw an exception if val is not found. (Or just print a string)
	index = 0
	for elem in arg1:
		if elem == val:
			return index
		else:
			index += 1
	print("{0} value not found.".format(val)) # {0} will be replaced by first argument in format() function

def my_count(arg1, val):
	# find and return the number of elements in arg1 whose value matches val	
	#	without using arg1.count(val)	
	count = 0
	for elem in arg1:
		if elem == val:
			count += 1

	return count
	
def main():
	example_list = [1,2,3,4,5,6,7,8,9,10]
	example_tuple = ('a','b','c','d','e','f','g')
	print(my_length(example_list))
	print(my_length(example_tuple)) 
	print(my_concat(example_list))
	# print out outputs for the rest of the functions...

if __name__ == "__main__":
	main()
