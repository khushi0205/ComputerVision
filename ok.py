arr = [10
, 1, 2, 0, 2]
def sort_desc(arr):
    n=len(arr)
    print("n: ", n)
    for i in range(n):
        print("")
        for j in range(0, n-i-1):
            print("jello: ", arr[j], arr[j+1])
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print("jjello: ", arr[j], arr[j+1], "\n")
                print("desc arr: ", arr)

def sort_asc(arr):
    
    print("asc arr: ", arr)

print(sort_desc(arr))
print (arr)