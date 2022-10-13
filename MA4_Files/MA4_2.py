#!/usr/bin/env python3

from person import Person
from numba import njit
from time import perf_counter as pc
from matplotlib import pyplot as plt


def fib_classic(n):

	if (n <= 1):
		return n
	else:
		return fib_classic(n - 1) + fib_classic(n - 2)



@njit
def fib(n):

	if (n <= 1):
		return n
	else:
		return fib(n - 1) + fib(n - 2)


def main():
	n = 30
	k = 30
	fc = []
	fib_njit = []
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())
	print(f.fib())
	fig, ax = plt.subplots()

	start = pc()
	for i in range(15):
		fc.append(fib_classic(n))
		n += 1
	end = pc()
	ax.plt(n,fc)
	ax.set_xlabel(' " n " ')
	ax.set_ylabel(' " time " ')
	fig.savefig('full_figure1.png')
	print(f'For a pythonic fib value of {n} it is: {fc} and it took {end-start} seconds')
	print(' ')
	start = pc()
	fig, ax1 = plt.subplots()
	for i in range(15):
		fib_njit.append(fib(k))
		k += 1
	end = pc()
	ax1.plt(n, fib_njit)
	ax1.set_xlabel(' " n " ')
	ax1.set_ylabel(' " time " ')
	fig.savefig('full_figure2.png')
	print(f'For a njit function for fib with value {k} it is: {fib_njit} and it took {end - start} seconds')


if __name__ == '__main__':
	main()
