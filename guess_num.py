import random
r = random.randint(1,100)
#print(r)
left = 1
right = 100
count = 1
while True:
	num = int(input('請從1~100猜一個數字'))
#	num = int(num)
	count += 1
	if num == r:
		print('恭喜你猜對了!!共猜了', str(count), '次！')
		break
	elif num > r and num <= right:
		print('猜錯了，答案在', str(left),'~',str(num),'之間，再猜一次！')
		right = num
	elif num < r and num >= left:
		print('猜錯了，答案在', str(num),'~',str(right),'之間，再猜一次！')
		left = num
	elif (num > right and num <=100) or (num < left and num >=1):
		print('猜錯了，答案在', str(left),'~',str(right),'之間，再猜一次！')
	elif num > 100 or num < 1:
		print('只能輸入1~100')