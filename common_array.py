from binarySearch import binarysearch as bs
def common(a,b,c):
    comm_sum=0
    for i in range(len(a)):
        if bs(b, a[i]):
            if bs(c, a[i]):
                comm_sum+=a[i]

    print(comm_sum)

common([1,2,2,3],[5,3,2,2],[7,3,2,2])
