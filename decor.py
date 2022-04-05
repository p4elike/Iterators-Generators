import random


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

len_list = int(len(nested_list))

nested_list2 = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


class MyIterator:

	def __init__(self, some_list):
		self.main_list = some_list

	def __iter__(self):
		return self

	def __next__(self):
		for element in self.main_list:

			if len(element) != 0:
				return element.pop()

		raise StopIteration


for item in MyIterator(nested_list):
	print(item)


print('*******************')


def random_list(list1):
	for i in list1:
		yield i


random_element = tuple(random_list(nested_list2))
print(random_element)

