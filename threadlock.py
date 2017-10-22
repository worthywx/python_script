#!/usr/bin/env python

from atexit import register
from random import randrange
from threading import Thread, Lock, currentThread
from time import ctime, sleep

class CleanOutputSet(set):
	def __str__(self):
		return ', '.join(x for x in self)

lock = Lock()
loops = (randrange(2, 5) for x in xrange(randrange(3, 7)))
remaining = CleanOutputSet()

def loop(nsec):
	myname = currentThread().name
	lock.acquire()
	remaining.add(myname)
	print '[%s] started %s' % (ctime(), myname)
	lock.release()
	sleep(nsec)
	lock.acquire()
	remaining.remove(myname)
	print '[%s] ended %s (%d secs)' % (ctime(), myname, nsec)
	print '   (remaining: %s)' % (remaining or None)
	lock.release()

def main():
	for pause in loops:
		Thread(target=loop, args=(pause, )).start()

@register
def _atexit():
	print 'all done at:', ctime()

if __name__ == "__main__":
	main()
