listInput = input("Give me some numbers (0-9) separated by a comma, no spaces")
arr = listInput.split(",")
print(arr)



i=0
swapcount = True
final_swap_pos = len(arr)-1
while (swapcount):
    swapcount = False
    for x in range(final_swap_pos):
        if arr[i]>arr[i+1]:
            arr[i], arr[i+1]=arr[i+1], arr[i]
            swapcount = True
        i=i+1
    

    if i==final_swap_pos:
        i=0

print(arr)
