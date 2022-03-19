sum=0
while True:
      print('enter the product price and press /q/ for exit. ')
      c_input=input('enter the product price: \n')
      if c_input!='q':
          sum=sum+int(c_input)
          print(f'counting total {sum} ')
      else:
          print(f"Your total bill is {sum}. ")
          print('thanks for visiting here')    
          break