import random


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]
nested_list2 = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


class MyIterator:

	def __init__(self, some_list):
		self.main_list = some_list

	def __iter__(self):
		self.main_list_cursor = 0  # курсор основного списка
		self.nested_list_cursor = 0  # курсор списка вложенного в основной список
		return self

	def __next__(self):
		self.nested_list_cursor += 1

		if len(self.main_list) == 0:
			self.main_list_cursor += 1
			self.nested_list_cursor = 0

		if len(self.main_list) == 0:
			raise StopIteration

		return self.main_list.pop()


for item in MyIterator(nested_list):
	print(item)


print('*******************')


def random_list(list1):
	for i in list1:
		yield i


random_element = tuple(random_list(nested_list2))
print(random_element)



