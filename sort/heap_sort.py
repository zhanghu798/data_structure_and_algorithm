#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import numpy as np

def parent(i):
    return i/2

def left(i):
    return 2*i

def right(i):
    return 2*i + 1

def max_heapify(A, i, lenA):

    l = left(i)
    r = right(i)
    if l < lenA and A[l] > A[i]:
        largest_index = l
    else:
        largest_index = i

    if r < lenA and A[r] > A[largest_index]:
        largest_index = r

    if largest_index != i:
        A[i], A[largest_index] = A[largest_index], A[i]
        max_heapify(A, largest_index, lenA)

def build_max_heap(A):
    for i in range(len(A)/2, -1, -1):
        max_heapify(A, i, len(A))

def headsort(A):
    build_max_heap(A)
    lenA = len(A)
    for i in xrange(lenA - 1,0, -1):
        A[0], A[i] = A[i], A[0]
        lenA -= 1
        max_heapify(A, 0, lenA)

def verify(A):
    a = A[1]
    for b in A[1:]:
        if a > b:
            print "error"
            return
        a = b
    print "success"

if __name__ == '__main__':

    count = 100000
    A = np.random.randint(1, 5*count, count)
    A = list(A)
    print A
    print len(A)
    headsort(A)
    print A
    print len(A)
