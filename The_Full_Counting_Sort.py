def countSort(arr):
    #creating 2-D list 
    result = [[] for i in range(100)]
    
    # first half of iteration
    for i in range(n//2):
        result[int(arr[i][0])].append('-')
        
    # second half of iteration
    for i in range(n//2,n):
        result[int(arr[i][0])].append(arr[i][1])
        
    # print the results
    for string in result:
        if string:
            print(*string, end=' ')
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
