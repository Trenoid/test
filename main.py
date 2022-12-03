class student:
    plata_obuchenie = 80000 # Стоимость обучения
    balance = 0             # Баланс на карте
    grades = []             # Оценки студента
    grant = 30000           # Степендия, выдается 1 раз
    grant_status = 0        # 0 - Степендия не получена, 1 - Степендия получена

    def __init__ (self,name,group):
        self.name = name        # Имя студента
        self.group = group      # номер группы

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

    def oplata(self):                               # <экземпляр>.oplata() снимает с баланса plata_obuchenie и меняет статус на "Оплачено"
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
        for counter in self.grades:
            if counter != 5:
                return "Возможно вас переведут на контрактное обучение"
        return "Ваши оценки позволяют остаться вам на бюджете"

    def grantt(self):                                   # Функция выдает студенту ступендию
        if self.grant_status == 1:                      # Проверет не была ли выдана степендия
            return "Степендия уже получена"
        self.balance = self.balance + self.grant        #Степендия поступает на баланс карты
        self.grant_status = 1
        return self.balance





acc2= budget("Albina","450") #Здесь можешь потестить как работает программа
acc2.grantt()
print(acc2.balance)
print(acc2.grantt())
print(acc2.balance)



acc1 = contract("Ramis","11_210")
acc1.deposit(100000)
acc1.withdraw(300)
acc1.oplata()
print(acc1.balance)

acc1.perfomance(5)
acc1.perfomance(5)
print(acc1.grades)
print(acc1.trancition())

