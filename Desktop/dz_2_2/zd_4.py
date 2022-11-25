# Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.


n = int(input('Enter the number: '))   
      
sum_numbers = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum_numbers += i
print(sum_numbers)