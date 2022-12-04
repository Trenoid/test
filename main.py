class student:
    plata_obuchenie = 80000 # Стоимость обучения
    balance = 0             # Баланс на карте
    grades = []             # Оценки студента
    grant = 30000           # Степендия, выдается 1 раз
    grant_status = 0        # 0 - Степендия не получена, 1 - Степендия получена
    hostel_plata = 3000     # Месячная стоимость проживания в общежитие
    hostel_counter = 9      # Кол-во месяцев за которые нужно заплатить


    def __init__ (self,name,group,hostel_status = 0):
        self.name = name                    # Имя студента
        self.group = group                  # номер группы
        self.hostel_status = hostel_status  # 0 - не нуждается в общежитие, 1 - нуждается в общежитие

    def deposit (self,amount):      #  <экземпляр>.deposit(x) пополнит баланс карты на x
        self.balance = self.balance + amount
        return self.balance

    def withdraw (self,amount):                 #  <экземпляр>.withdraw(x) снимет с  баланса карты  x
        if amount > self.balance:               # Проверяет достаточно ли средств на карте
            return "Недостаточно средств"       # Выводит ошибку если на карте недостаточно средств
        self.balance = self.balance - amount
        return self.balance

    def perfomance(self,grade):                 # успеваемость студента: <экз>.perfomance(x) добовляет в список оценку x, x == [1,5]
        self.grade = grade
        self.grades.append(self.grade)          # Добовляет оценку от 1 до 5 в список оценок
        return self.grades



class contract(student):        # Новый подкласс, с наследованием от student. Предназначен для студентов контрактников
    plata_obuchenie = 80000     # Фиксированная плата за обучение
    status = "Не оплачено"

    def oplata_obuchenie(self):                               # <экземпляр>.oplata() снимает с баланса, plata_obuchenie и меняет статус на "Оплачено"
        if self.balance < self.plata_obuchenie:     # Проверяет достаточно ли средств на балансе карты
            return "Недостаточно средств"
        self.balance = self.balance - self.plata_obuchenie
        self.status = "Оплачено"
        return self.balance

    def trancition(self):               # Заявка на переход с контрактного на бюджетное обучение
        for counter in self.grades:     # Начинает проверку успеваемости
            if counter != 5:            # Если студент не отличник отклоняет заявку на бюджетное обучение
                return "Вы не можете перейти на бюджет из-за недостаточной успеваемости"
        return "Мы расcмотрим ваш переход на бюджет"

class budget(student):           # Новый подкласс, с наследованием от student. Предназначен для студентоd бюджетников

    def trancition(self):        # Функция проверяет останется ли студент на бюджете
        for counter in range (len(self.grades)):
            if self.grades[counter] != 5:
                return "Возможно вас переведут на контрактное обучение"
        return "Ваши оценки позволяют остаться вам на бюджете"

    def grantt(self):                                   # Функция выдает студенту ступендию
        if self.grant_status == 1:                      # Проверет не была ли выдана степендия
            return "Степендия уже получена"
        self.balance = self.balance + self.grant        #Степендия поступает на баланс карты
        self.grant_status = 1
        return self.balance

class dormitory_student(contract):
    hostel_plata = 3000  # Месячная стоимость проживания в общежитие
    hostel_counter = 9  # Кол-во месяцев за которые нужно заплатить

    def oplata_dormitory(self):
        if self.hostel_counter == 0:
            return "Вы уже полностью оплатили за общежитие"
        if self.balance < self.hostel_plata:
            return "Недостаточно средств"
        self.balance = self.balance - self.hostel_plata
        self.hostel_counter = self.hostel_counter - 1
        return self.balance

    def see_hostel_counter(self):
        return print(f'Вам осталось заплатить за {self.hostel_counter} месяцев')










students = {"acc1","acc2","acc3"}

kolvo_student = 0
while 1 == 1:

    comanda = input("Введите одну из команд ")

    if comanda == "new":
        new_object = input("Хотите завести новый обьект, 0-нет, 1 - да, 2- да, 3 - да (вводить по очереди)")
        if new_object == "1":
            type_student = input(
                "Введите тип студента: 1 - бюджетник, 2 - контрактник, 3 - контрактник и нуждается в общежитие")
            if type_student == "1":
                acc1 = budget(input("Введите имя студента "), input("Введите номер группы студента "))
                kolvo_student += 1
            if type_student == "2":
                acc1 = contract(input("Введите имя студента "), input("Введите номер группы студента "))
                kolvo_student += 1
            if type_student == "3":
                acc1 = dormitory_student(input("Введите имя студента "), input("Введите номер группы студента "))
                kolvo_student += 1
            print(f'Введен новый студент, его идентификатор acc1 ')

        if new_object == "2":
            type_student = input(
                "Введите тип студента: 0 - бюджетник, 1 - контрактник, 2 - контрактник и нуждается в общежитие")
            if type_student == "0":
                acc2 = budget(input("Введите имя студента "), input("Введите номер группы студента "))
                kolvo_student += 1
            if type_student == "1":
                acc2 = contract(input("Введите имя студента "), input("Введите номер группы студента "))
                kolvo_student += 1
            if type_student == "2":
                acc2 = dormitory_student(input("Введите имя студента "), input("Введите номер группы студента "))
                kolvo_student += 1
            print(f'Введен новый студент, его идентификатор acc2 ')

        if new_object == "3":
            type_student = input(
                "Введите тип студента: 0 - бюджетник, 1 - контрактник, 2 - контрактник и нуждается в общежитие")
            if type_student == "0":
                acc3 = budget(input("Введите имя студента "), input("Введите номер группы студента "))
                kolvo_student += 1
            if type_student == "1":
                acc3 = contract(input("Введите имя студента "), input("Введите номер группы студента "))
                kolvo_student += 1
            if type_student == "2":
                acc3 = dormitory_student(input("Введите имя студента "), input("Введите номер группы студента "))
                kolvo_student += 1
            print(f'Введен новый студент, его идентификатор acc1 ')

    if comanda == "deposit":
        kolvo = int(input("На сколько рублей хотите пополнить баланс "))
        to_whom = input("Введите идентификатор студента, которому хотите пополнить счет ")
        if to_whom == "acc1":
            acc1.deposit(kolvo)
            print(f'Текущий баланс студента {acc1.name} : {acc1.balance}')
        if to_whom == "acc2":
            acc2.deposit(kolvo)
            print(f'Текущий баланс студента {acc2.name} : {acc2.balance}')
        if to_whom == "acc3":
            acc3.deposit(kolvo)
            print(f'Текущий баланс студента {acc3.name} : {acc3.balance}')


    if comanda == "withdraw":
        kolvo = int(input("Сколько рублей хотите снять "))
        to_whom = input("Введите идентификатор студента, со счета которого нужно снять деньги ")
        if to_whom == "acc1":
            acc1.withdraw(kolvo)
            print(f'Текущий баланс студента {acc1.name} : {acc1.balance}')
        if to_whom == "acc2":
            acc2.withdraw(kolvo)
            print(f'Текущий баланс студента {acc2.name} : {acc2.balance}')
        if to_whom == "acc3":
            acc3.withdraw(kolvo)
            print(f'Текущий баланс студента {acc3.name} : {acc3.balance}')


    if comanda == "perfomance":
        assessment = input("Введите оценку которую получил студент ")
        to_whom = input("Введите идентификатор студента ")
        if to_whom == "acc1":
            acc1.perfomance(assessment)
            print(f'Список оценок студента {acc1.name} {acc1.grades}')
        if to_whom == "acc2":
            acc2.perfomance(assessment)
            print(f'Список оценок студента {acc2.name} {acc2.grades}')
        if to_whom == "acc3":
            acc3.perfomance(assessment)
            print(f'Список оценок студента {acc3.name} {acc3.grades}')

    if comanda == "oplata_obuchenie":
        to_whom = input("Введите идентификатор студента")
        if to_whom == "acc1":
            acc1.oplata_obuchenie()
            print("Оплачено")
        if to_whom == "acc2":
            acc2.oplata_obuchenie()
            print("Оплачено")
        if to_whom == "acc3":
            acc3.oplata_obuchenie()
            print("Оплачено")

    if comanda == "grantt":
        to_whom = input("Введите идентификатор студента")
        if to_whom == "acc1":
            acc1.grantt()
            print("Получено")
        if to_whom == "acc2":
            acc2.grantt()
            print("Получено")
        if to_whom == "acc3":
            acc3.grantt()
            print("Получено")

    if comanda == "trancition":
        to_whom = input("Введите идентификатор студента")
        if to_whom == "acc1":
            acc1.trancition()
            print(acc1.trancition())
        if to_whom == "acc2":
            acc2.trancition()
            print(acc2.trancition())
        if to_whom == "acc3":
            acc3.trancition()
            print(acc3.trancition())

    if comanda == "balance":
        to_whom == "Введите идентификатор студента"
        if to_whom == "acc1":
            print(acc1.balance)
        if to_whom == "acc2":
            print(acc2.balance)
        if to_whom == "acc3":
            print(acc3.balance)

    if comanda == "oplata_obuchenie":
        to_whom = input("Введите идентификатор студента")
        if to_whom == "acc1":
            acc1.oplata_dormitory()
            print("Оплачено")
        if to_whom == "acc2":
            acc2.oplata_dormitory()
            print("Оплачено")
        if to_whom == "acc3":
            acc3.oplata_dormitory()
            print("Оплачено")

