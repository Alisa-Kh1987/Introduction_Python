# Задание №6
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

# first_balance = 0
class Bankomat:

    def __init__(self, current_balance: float, first_balance: float):
        self.current_balance = current_balance
        self.first_balance = first_balance
    def current_balance(current_balance, first_balance=0.0):
        current_balance = first_balance

    def add_money_to_card(current_balance):
        # Введем счетчик количеств пополнения карты
        count = 0
        add_summ = float(input("Укажите сумму пополнения карты: "))
        if add_summ % 50 == 0:
            if count <= 3:
                print(f"Вы внесли сумму: {add_summ}")
            else:
                add_summ = add_summ*0.97
            count += 1
            current_balance = add_summ + current_balance
            print(f"Текущий баланс карты составляет: {current_balance}")
        else:
            print("Необходимо внести сумму, кратную 50!")

    def output_money(current_balance):
        output_summ = float(input("Какую сумму Вы хотите снять с карты?"))
        if output_summ % 50 == 0:
            print("Предупреждение:комиссия за снятие составляет 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.")
