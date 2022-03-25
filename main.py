import random


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


class MyIterator(list):

	def __iter__(self):
		return self

	def __next__(self):

		if len(self) == 0:
			raise StopIteration
		return self.pop()


for item in MyIterator(nested_list):
	for i in item:
		print(i)


print('*******************')


def random_list(list1):
	for i in list1:
		yield random.choice(list1)


random_element = tuple(random_list(nested_list))
print(random_element)



