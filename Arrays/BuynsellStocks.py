#Time Complexity ---> O(n)
#Space Complexity ----> O(1)



arr = [310,315,275,295,260,270,290,230,255,250]

minimum = arr[0]
prevprofit = 0
for i in range(1, len(arr)):
    if arr[i] < minimum:
        minimum = arr[i]
    else:
        profit = arr[i] - minimum
        # if profit > prevprofit:
        #     prevprofit = profit
        prevprofit = max(profit, prevprofit)
print(minimum, prevprofit)