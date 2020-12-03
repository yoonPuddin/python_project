num = int(input("시작 숫자: "))
m = int(input("빠지는 수 : "))
zegop = int(input("제곱승 수 : "))
iter_ = int(input("반복횟수 : "))

for i in range(iter_,0,-1):
	for j in range(iter_,i,-1):
		print(" ", end= " ")
	for j in range(num, num-i*m,-m):
		print(j**zegop-1,end = " ")
	for j in range(j+m, num+1, m):
		print(j**zegop-1, end= " ")
	print()
for i in range(1, iter_,1):
	for j in range(iter_, i+1,-1):
		print(" ", end=" ")
	for j in range(num,num-i*m,-m):
		print(j**zegop-1,end=" ")
	for j in range(num-i, num+1,m):
		print(j**zegop-1, end= " ")
	print()

