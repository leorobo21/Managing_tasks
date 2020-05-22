def div(am, x, y):
	if ((amount-am) % y == 0):
		time1 = am//x
		time2 = (amount-am)//y
		for i in range(time1):
			li.append(x)
				
		for j in range(time2):
			li.append(y)
	else:
		am -= 1
		recur(am)
	return li


def  recur(am):
	if(am%5 == 0):div(am, 5, 7)
	elif(am%7 == 0):div(am, 7, 5)
	else:
		am -= 1
		recur(am)
	return li


def change(amount):
	global  li
	li = []
	return recur(amount)

if __name__ == '__main__':
	amount = int(input())
	if(amount <= 23 or amount >= 1000):
		exit()
	print(change(amount))