def collatz(number):
	if number%2==0:
		result = number//2
		return result
	
	elif number%2==1:
		result = 3*number+1
		return result
	else:
		print('Invalid Integer.')

print('Enter Integer:')
num=int(input())

while True:
    if collatz(num) !=1:
        new_num = collatz(num)
        print(new_num)
        num=new_num

    if collatz(num) == 1:
        print(collatz(num))
        break
