#Данное задание 
#Вычислите сумму цифр данного натурального числа. 
def func():
  number=input('Введите натуральное число:')
  return number
def sum_natural(number):
  count=list(number) # преобразуем вводимое число( в виде строки) в список 
  summa=0 # обнуляем сумму, для накопления суммы 
  for el in count : # пробегаемся по всему списку, берем один элемент из списка и выполняем следующее действие 
    summa=summa+ int(el) # складываем данное с последующим числом, при этом преобразуем каждый элемент списка в int
  return summa
def print_screen(s):
  print('Сумма данного натурального числа: {}'.format(s))
  
if __name__ == "__main__":

print_screen(sum_natural(func()))
