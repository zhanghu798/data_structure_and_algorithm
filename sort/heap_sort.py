#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import numpy as np


def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def max_heapify(A, i, lenA):
    '''
    维护大顶堆性质: 假设下标元素为i的元素中的左子树和右子树均满足大顶堆性质, 调整i元素为顶点的树正体大顶堆性质
	'''
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
    '''
    建大顶堆: 从含有叶子节点的下标最大的节点建大顶堆(由二叉树含有叶子节点的那一层为开始层,从底层上层开始建堆)
    '''
    for i in range((len(A)-1)/2, -1, -1):
        max_heapify(A, i, len(A))

def headsort(A):
    '''
    将大顶堆的从按小标增大,数据由小到大排序
    '''
    build_max_heap(A)
    lenA = len(A)
    for i in xrange(lenA - 1,0, -1):
        A[0], A[i] = A[i], A[0]
        lenA -= 1
        max_heapify(A, 0, lenA)

def verify(A):
    a = A[0]
    for b in A[1:]:
        if a > b:
            print "error"
            return
        a = b
    print "success"

if __name__ == '__main__':

    count = 1000
    A = np.random.randint(1, 5*count, count)
    A = list(A)
    print len(A)
    #print A
    headsort(A)
    verify(A)
    print len(A)
    #print A
 
