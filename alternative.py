x=raw_input("enter the name ")
for i in range(0,len(x),2):
	if (i+1)%10 == 1:
		text = 'st'
	elif (i+1)%10 == 2:
		text = 'nd'
	elif (i+1)%10 == 3:
		text = 'rd'
	else:
		text = 'th'
	print str(i+1)+(text) , " value is ", x[i]