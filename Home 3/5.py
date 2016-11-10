steps = input('Введите количество ступеней ')
try:
    steps = int(steps)
    if steps != 0:
        for i in range(1, steps + 1):
            print(str(i) * i)
    else:
        print('Вы ввели 0')
except:
    print('Повторите пожалуйста ввод, используйте только цыфры')