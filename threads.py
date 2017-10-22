#!/usr/bin/env python
import threading
from time import sleep, ctime
from MyThread import MyThread

loops = [4, 2]

def loop(nloop, nsec):
	sleep(nsec)

def main():
	print "starting at:", ctime()
	threads = []
	nloops = range(len(loops))
	
	for i in nloops:
		t = MyThread(loop, (i, loops[i]), loop.__name__)
		threads.append(t)

	for i in nloops: 
		threads[i].start()

	for i in nloops:
		threads[i].join()

	print "all done at:", ctime()

if __name__ == "__main__":
	main()
