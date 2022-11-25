# Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
# Ввод: 4
#[-4, -3, -2, -1, 0, 1, 2, 3,4]


from random import randint
numbers = []
for i in range(int(input('Enter element: '))):
    numbers.append(randint (-100,100))
print(numbers)

def get_numbers(numbers):
    count =0 
    for element in numbers:
        count +=1
    return count
print('Number of elements: ', get_numbers(numbers))

x = int(input('Enter position of  element: '))
y = int(input('Enter position of  element: '))
a = int(input('Enter position of  element: '))
b = int(input('Enter position of  element: '))
c = int(input('Enter position of  element: '))

for i in range(len(numbers)):
    mult = numbers[x -1]*numbers[y - 1]*numbers[a - 1]*numbers[b - 1]*numbers[c - 1]
print(f'Mult of elements: {numbers[x -1]} * {numbers[y -1]} * {numbers[a - 1]} * {numbers[b- 1]} * {numbers[c - 1]} =', mult)
