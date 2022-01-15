# 9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

spam = input('Input: ')
if (spam == '1'):
  print('Hello')
elif (spam == '2'):
  print('Howdy')
else:
  print('Greetings!')




# 13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

for i in range(1, 11):
  print(i)

i = 1
while (i <= 10):
  print(i)
  i += 1