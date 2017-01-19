import numpy

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4

test_results = []

for i in range(1000000):
	numpy.random.shuffle(cards)
	test_results.append(cards.index(1))

print numpy.mean(test_results)