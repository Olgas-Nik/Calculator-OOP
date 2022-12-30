

class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum_n(self):
        return self.num1 + self.num2

    def minus_n(self):
        return self.num1 - self.num2

    def mult_n(self):
        return self.num1 * self.num2

    def devide_n(self):
        try:
           r = self.num1 / self.num2
        except ZeroDivisionError:
           return 'error'
        else:
            return r

    while True:

        print('+, -, /, *')
        zn = input()
        if zn == "0":
            break

        num1 = float(input('Введите число:  '))
        num2 = float(input('Введите число:  '))
        cal_obj = Calculator(num1, num2)

        if zn == '+':
            print(cal_obj.sum_n())
        elif zn == '-':
            print(cal_obj.minus_n())
        elif zn == '*':
            print(cal_obj.mult_n())
        elif zn == '/':
            print(cal_obj.devide_n())

