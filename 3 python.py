# import statistics;
# print(statistics.median([2,3,4,5,6,7]))


num_list = [10,12,15,16,17,18]
n = len(num_list)
num_list.sort()

if n%2 == 0:
    median1 = num_list[n//2]
    median2 = num_list[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = num_list[n//2]
print(str(median))