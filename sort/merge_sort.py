#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import numpy as np
import copy
def merge(left_A, right_A):
    result_A = []
    left_index = 0
    right_index = 0
    while left_index < len(left_A) and right_index < len(right_A):
        if left_A[left_index] <= right_A[right_index]:
            result_A.append(left_A[left_index])
            left_index += 1
        else:
            result_A.append(right_A[right_index])
            right_index += 1

    if left_index < len(left_A):
        result_A += left_A[left_index:]
    if right_index < len(right_A):
        result_A += right_A[right_index:]

    return result_A
        
        

def merge_sort(A):
    if len(A) == 1:
        return A
    mid_index = len(A)/2
    left_A = merge_sort(A[:mid_index])
    right_A = merge_sort(A[mid_index:])
    return merge(left_A, right_A)

def merge_sort_no_recursion(A):
    """原址排序"""
    step = 1
    lenA = len(A)
    while step < len(A):
        for start_index in xrange(0, lenA, step*2):
            left_A = A[start_index:start_index+step]
            right_A = A[start_index+step:start_index+2*step]
            A[start_index:start_index+step*2] = merge(left_A, right_A)
        step *= 2
    return A


def verify(A):
    a = A[1]
    for b in A[1:]:
        if a > b:
            print "error"
            return
        a = b

    print "success"


if __name__ == '__main__':
    import time
    count = 100000000
    A = np.random.randint(1, 5*count, count)
    A = list(A)
    #print A
    print len(A)

    A_copy = copy.deepcopy(A)
    start = time.clock()
    result_A = merge_sort_no_recursion(A_copy)

    end = time.clock()
    print "read: %f s" % (end - start)

    A_copy = copy.deepcopy(A)
    start = time.clock()
    result_A = merge_sort(A_copy)
    end = time.clock()
    print "read: %f s" % (end - start)
    #verify(A)
    #print A
    #print len(A)
