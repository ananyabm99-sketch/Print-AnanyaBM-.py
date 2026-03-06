def average(array):
    sum =0
    s = set(array)
    p = list(s)
    for i in range(len(p)):
        sum += p[i]
    avg = sum/len(p)
    return avg    
        
        

    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)