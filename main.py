# Calculator v1.0 ! 
def solve():
  print(totalAnswer)
print('First number')
firstInput = float(input())
print('Act (+, -, *, /)')
actInput = input()
print('Second number')
secondInput = float(input())
if actInput == '+':
  totalAnswer = firstInput + secondInput
if actInput == '-':
  totalAnswer = firstInput - secondInput
if actInput == '*':
  totalAnswer = firstInput * secondInput
if actInput == '/':
  if secondInput == '0':
    print('You cannot devide by zero!')
  else:
    totalAnswer = firstInput / secondInput
solve()
