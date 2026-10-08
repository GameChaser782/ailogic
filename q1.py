def solve(a):
    n = len(a)
    i, j = 0, n-1
    while(i!=j):
        if a[j]>a[i]:
            j=j-1
        else:
            i=i+1

    return a[i]
    
def main():
    a = [3, 4, 5, 1, 2]
    print(solve(a))
    return solve(a)