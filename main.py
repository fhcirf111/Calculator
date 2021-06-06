# Calculator v1.1 ! 
print('First number')
firstInput = float(input())
print('Act (+, -, *, /)')
actInput = input()
print('Second number')
secondInput = float(input())
if actInput == '+':
  totalAnswer = firstInput + secondInput
  print(totalAnswer)
if actInput == '-':
  totalAnswer = firstInput - secondInput
  print(totalAnswer)
if actInput == '*':
  totalAnswer = firstInput * secondInput
  print(totalAnswer)
if actInput == '/':
  if secondInput == 0:
    print('You cannot devide by zero!')
  else:
    totalAnswer = firstInput / secondInput
    print(totalAnswer)
