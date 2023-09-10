# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
# имена str, ставка int, премия str с указанием процентов вида «10.25%». 
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии


def gen_diict(names:list, salary:list, premium:list):
    return {names: salary*(1+float(premium[:-1]) / 100) for names, salary, premium in zip(names, salary, premium)}


names = ['Ivan', 'Michail', 'Petr']
salary = [50_000, 60_000, 65_000]
premium = ['10.25%', '11.05%', '12.30%']

print(gen_diict(names, salary, premium))