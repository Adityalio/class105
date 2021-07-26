import math
import csv
import statistics
with open ("data.csv",newline='') as f :
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]
print(data)

def mean (data):
    total=0
    n=len(data)
    for x in data:
        total=total+x

    mean=total/n
    return mean

std=statistics.stdev(data)
print(std)

