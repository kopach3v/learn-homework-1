"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""




def occupation(age):
    
    if age < 6 :
        return "Вы в садике"
    elif 6<= age < 18:
        return 'Школа'
    elif 18<= age <= 24:
        return 'Вуз'
    
    return 'Работа'

def main():
    input_age = int(input('Введите возраст: '))
    print(occupation(input_age))



if __name__ == "__main__":
    main()

