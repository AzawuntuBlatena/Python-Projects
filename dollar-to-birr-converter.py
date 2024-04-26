def main():
  print('this code converts us dolar in to ethiopian birr')
  print()
  dollar=eval(input('enter the amount of dolar: '))
  pound=convert_to_pound(dollar)

  print('that is', pound , 'Et. Birr.')
convert_to_pound = lambda dollar: dollar*57.36
main()