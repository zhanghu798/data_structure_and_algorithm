#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import numpy as np

def partition(A, p, r):
    boundary_value = A[r]   #比较对象,临界值
    boundary_index = p - 1 #临界值索引,A[p,r)中,下标值 <= boundary_index 的部分的 value < critical_value; 标值 > boundary_index 的部分的 value > critical_value
    for j in xrange(p, r):
        y = A[j]
        if A[j] <= boundary_value: #小于比较比较值时,需要将当前值放在临界值索引+1的位置,并修改当前临界索引值为+1
            boundary_index += 1
            A[boundary_index], A[j] = A[j], A[boundary_index]

    #将比较对象放到临界点
    boundary_index += 1
    A[boundary_index], A[r] = A[r], A[boundary_index]
    return boundary_index


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q+1, r)

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
    quicksort(A, 0, len(A)-1)
    print A
    print len(A)

    #yanzhen(A)