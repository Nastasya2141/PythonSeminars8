import random
import statistics
def zadacha1():
# Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу.
#  Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.

    amount_groups = int(input("Введите количество групп: "))
    list_of_ratings = []
    mean_ratings = []

    for i in range(amount_groups):
        list_of_ratings.append([random.randint(1, 5) for i in range(random.randint(20, 30))])
        mean_ratings.append(statistics.mean(list_of_ratings[i]))

    print(f' Оценки : {list_of_ratings}',end = ' ')
    print(f'Группа с наилучшим средним баллом - {mean_ratings.index(max(mean_ratings)) + 1}')


def zadacha2():
# Задача 2. Дана квадратная матрица, заполненная случайными числами. 
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.
    rows = 5
    columns = 5
    numbers = [None] * rows

    for index in range(len(numbers)):
        numbers[index] = [random.randint(1, 50) for _ in range(columns)]

    for el in numbers:
        print (el)

    sum_diagonal = 0
    for i in range(rows):
        for j in range(columns):
                if i == j:
                    sum_diagonal += numbers[i][j]

    print(f'Сумма главной диагонали матрицы: {sum_diagonal}')

    sum_rows = list(sum(row) for row in numbers)
    print(f'Суммы строк: {sum_rows}')

    for i in range(rows):
        if sum_rows[i] > sum_diagonal:
            print(f'{i+1} строка')
            


def zadacha3():   
# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год. 
# Каждому месяцу соответствует своя строка.
# Определите самый жаркий и самый холодный 7-дневный промежуток каждого месяца. Выведите их даты.
    def period_month(temperatures, period, month ):
        max_temp = 0
        min_temp = 40
        day_maxtemp = 1
        day_mintamp = 1
        
        for i in range(len(temperatures)- period + 1):
            temp_in_period = temperatures [i:i + period]
            print(f'{i + 1} - {i + period}. {temp_in_period}')
            sum_temp = sum(temp_in_period)
            if sum_temp > max_temp:
                max_temp =  sum_temp
                day_maxtemp = i
            elif sum_temp < min_temp:
                min_temp =  sum_temp
                day_mintamp = i
        print(f'максимальная температура с {day_maxtemp + 1} по {day_maxtemp + period} {month}')
        print(f'минимальная температура с {day_mintamp + 1} по {day_mintamp + period} {month}')  


    rows = 5
    temperatures = [None] * rows
    for index in range(len(temperatures)):
        temperatures[index] = [random.randint(10, 35) for _ in range(31)]

        
    n = int(input('Введите номер соответствующий  номеру месяца с мая по сентябрь:'))

    for i in range(len(temperatures)): 
        if n == 1:  
            period_month(temperatures[0], 7, 'мая')
        elif  n == 2:  
            period_month(temperatures[1], 7, 'июня') 
        elif  n == 3:  
            period_month(temperatures[2], 7, 'июля') 
        elif  n == 4:  
            period_month(temperatures[3], 7, 'августа') 
        elif  n == 5:  
            period_month(temperatures[4], 7, 'сентября')            
            
    
            
            
    print(f'все температуры {temperatures}') 

    
        

    
# zadacha1()
# zadacha2()
# zadacha3()