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
	n = 1
	k = 1
	j = 1
	fc = []
	fib_njit = []
	f_person = []
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())
	print(f.fib())

	stepper = range(30,46)

	for i in stepper:
		# Clasic fib
		steg_tid = pc()
		start = pc()
		fib_classic(i)
		fc.append(pc()-start)
		# Njit fib
		start = pc()
		fib(i)
		fib_njit.append(pc()-start)
		# f.Person()
		f = Person(i)
		start = pc()
		f.fib()
		f_person.append(pc()-start)



	"""
	for i in range(15):
		f = Person(j)
		f_person.append(f.fib())
		j += 1



	#fig.savefig('full_figure1.png')
	print(f'For a pythonic fib value of {n} it is: {fc} and it took {end-start} seconds')
	print(' ')
	start = pc()
	#fig, ax1 = plt.subplots()
	for i in range(15):
		fib_njit.append(fib(k))
		k += 1
	end = pc()
	"""
	plt.plot(stepper, fc, 'b')
	plt.plot(stepper, f_person, 'r')
	plt.plot(stepper, fib_njit,'k')
	plt.xlabel(' " n " ')
	plt.ylabel('  time  ')
	plt.legend([f'Fibonacci_python','F_person','Fibonacci_Njit'])
	plt.savefig('Time_test_30_to_45.png')

	#print(f'For a njit function for fib with value {k} it is: {fib_njit} and it took {end - start} seconds')


if __name__ == '__main__':
	main()
