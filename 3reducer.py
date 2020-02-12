s = open("challenge2.txt","r")
r = open("challenge3.txt", "w")

thisKey = ""
thisValue = 0.0
count = 0
old_value = None


for line in s:
  data = line.strip().split('\t')
  paymentType, amount = data

  if paymentType != thisKey:
    # if thisKey:
    #   # output the last key value pair result
    #   #r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = paymentType 
    thisValue = 0.0
  
  # apply the aggregation function
  #thisValue += float(amount)
  if old_value is None:
    old_value = paymentType

  if old_value == paymentType:
    count = count + 1
  else:
    r.write(old_value + '\t' + str(count)+'\n' )
    count = 1
    old_value = paymentType

# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()
