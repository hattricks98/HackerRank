# Complete the compareTriplets function below.
def compareTriplets(a, b):

    A = (a[0]>b[0]) + (a[1]>b[1]) + (a[2]>b[2])
    B = (a[0]<b[0]) + (a[1]<b[1]) + (a[2]<b[2])
    return A, B


a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

result = compareTriplets(a, b)
print(result)