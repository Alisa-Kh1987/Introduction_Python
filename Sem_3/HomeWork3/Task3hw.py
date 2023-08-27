# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

# # Сначала короткий вариант решения - с использованием функции most_common.
# import re
# from collections import Counter

# long_str = ("Главный герой, от лица которого ведётся изложение, Джеймс Терн — потомственный врач, выросший на Мадейре."
#             " Его отец был вынужден покинуть Англию, ибо был поражён оспой, выжил, но так и не смог оправиться от последствий заболевания."
#             " Получив от дяди небольшое наследство, в двадцать четыре года Джеймс сумел окончить медицинский факультет"
#             " с золотой медалью, но у него нет денег, связей и репутации, чтобы открыть частную практику. После смерти матери он без жалованья"
#             " поступил врачом на пароход, чтобы посмотреть на экзотические страны. В Мексике по дороге в Сан-Хосе он встретил молодую американку"
#             " Эмму Беккер; вместе им пришлось пережить нападение разбойников, а прибыв в город, они оказались в эпицентре оспенной эпидемии."
#             " Женитьба принесла Терну пять тысяч долларов приданого, которые жена посоветовала пустить на открытие практики."
#             " На малой родине Терна (Денчестере) царём и богом стал сэр Джон Белл, бывший ассистент отца Терна, который сразу невзлюбил молодого конкурента."
#             " Лишь чудом Терн обрёл репутацию: майор Селби страдал от тромбоза, тогда как Белл поставил ему неверный диагноз."
#             " После смерти Селби от закупорки лёгочной артерии вскрытие расставило всё на свои места."
#             " Белл разработал изощрённый план мести: навязался принимать роды Эммы Терн, а сам направил Джеймса наблюдать за родами леди Бланш Колфорд."
#             " Эмма умерла от родильной горячки; не перенесла рождения ребёнка и леди Бланш, после чего Джон Белл объявил,"
#             "что родильная горячка заразна и Терн погубил леди Колфорд."
#             " Лишь благодаря поддержке влиятельного политика Стивена Стронга суд присяжных оправдал молодого врача, а далее и лорд Колфорд отказался от моральных претензий,"
#             " которые оценил в 10 000 фунтов стерлингов. Терн к этому времени уже собирался выпить яд."
#             " Стронг предложил Джеймсу Терну вступить в его партию, которая одновременно боролась за повышение подоходного налога и против принудительной вакцинации."
#             " На выборах Терн неожиданно обходит сэра Томаса Колфорда.")

# # удаляем все знаки препинания и сразу приводим всё к одному (нижнему) регистру
# long_str = re.sub(r'[.,"\'-?:!;]', '', long_str).lower()

# words_list = long_str.split()
# print(f'words = {words_list}')

# result = Counter(words_list)
# print()
# print(f'10 наиболее встречающихся слов: {result.most_common(10)}')

# # Ну и длинный вариант - с прохождением по всему списку, подсчетом вхождений, сортировкой и т.п.
import re

long_str = ("Главный герой, от лица которого ведётся изложение, Джеймс Терн — потомственный врач, выросший на Мадейре."
            " Его отец был вынужден покинуть Англию, ибо был поражён оспой, выжил, но так и не смог оправиться от последствий заболевания."
            " Получив от дяди небольшое наследство, в двадцать четыре года Джеймс сумел окончить медицинский факультет"
            " с золотой медалью, но у него нет денег, связей и репутации, чтобы открыть частную практику. После смерти матери он без жалованья"
            " поступил врачом на пароход, чтобы посмотреть на экзотические страны. В Мексике по дороге в Сан-Хосе он встретил молодую американку"
            " Эмму Беккер; вместе им пришлось пережить нападение разбойников, а прибыв в город, они оказались в эпицентре оспенной эпидемии."
            " Женитьба принесла Терну пять тысяч долларов приданого, которые жена посоветовала пустить на открытие практики."
            " На малой родине Терна (Денчестере) царём и богом стал сэр Джон Белл, бывший ассистент отца Терна, который сразу невзлюбил молодого конкурента."
            " Лишь чудом Терн обрёл репутацию: майор Селби страдал от тромбоза, тогда как Белл поставил ему неверный диагноз."
            " После смерти Селби от закупорки лёгочной артерии вскрытие расставило всё на свои места."
            " Белл разработал изощрённый план мести: навязался принимать роды Эммы Терн, а сам направил Джеймса наблюдать за родами леди Бланш Колфорд."
            " Эмма умерла от родильной горячки; не перенесла рождения ребёнка и леди Бланш, после чего Джон Белл объявил,"
            "что родильная горячка заразна и Терн погубил леди Колфорд."
            " Лишь благодаря поддержке влиятельного политика Стивена Стронга суд присяжных оправдал молодого врача, а далее и лорд Колфорд отказался от моральных претензий,"
            " которые оценил в 10 000 фунтов стерлингов. Терн к этому времени уже собирался выпить яд."
            " Стронг предложил Джеймсу Терну вступить в его партию, которая одновременно боролась за повышение подоходного налога и против принудительной вакцинации."
            " На выборах Терн неожиданно обходит сэра Томаса Колфорда.")

long_str = re.sub(r'[.,"\'-?:!;]', '', long_str).lower()

words_list = long_str.split()
unique_words = list(set(long_str.split()))
print(f'unique_words = {unique_words}')

res_list = []

for word in unique_words:
    count = 0
    for word1 in words_list:
        if word1 == word:
            count += 1
    res_list.append((count, word))
    rev_list = sorted(res_list, reverse=True)
    
print()
print(f'res_list = {res_list}')

print()
print(f'rev_list = {rev_list}')

print()
print(f'10 наиболее часто встречающихся слов = {rev_list[:10:]}')


