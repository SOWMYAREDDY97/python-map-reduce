unsorted = open("challenge1.txt", "r")
sorted = open("challenge2.txt", "w")

dataList = unsorted.readlines()
dataList.sort()

for line in dataList:
    sorted.write(line)


unsorted.close()
sorted.close()