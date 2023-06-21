BALANCE = 0  #стартовый баланс
CURRENCY = 50 #размер одной кратности
DRAW_PERCENT = 1.5 #процент за снятие
MIN_PER_LIMIT = 30 #минимальная комиссия за снятие
MAX_PER_LIMIT = 600 #максимальная комиссия за снятие
PERCENT_FOR_THIRD = 3 #процент за каждую третью операцию
RICH_LIMIT = 5000000 #лимит богатства
RICH_PERCENT = 10 #процент на богатство
COUNTER = 0 #счётчик операций

def pay(balance1, currency1, counter1): #пополнение счёта
    counter1 = counter1 + 1
    if counter1 % 3 == 0:
        balance1 = balance1 * 1.03
    balance1 = rich_limit(balance1)
    print("БАЛАНС ВАШЕГО СЧЁТА: ", round(balance1, 2))
    print("1 ПОПОЛНЕНИЕ = 50уе")
    b = int(input("Введите количество пополнений: "))
    balance1 = balance1 + b * currency1
    print("БАЛАНС ВАШЕГО СЧЁТА: ", round(balance1, 2) , "уе")
    menu(balance1, currency1, counter1)
   
def draw(balance2, currency2, counter2): #снятие со счёта
    counter2 = counter2 + 1
    if counter2 % 3 == 0:
        balance2 = balance2 * 1.03
    balance2 = rich_limit(balance2)
    print("БАЛАНС ВАШЕГО СЧЁТА: ", round(balance2, 2))
    print("1 СНЯТИЕ = 50уе")
    b = int(input("Введите количество снятий: "))
    if (b * currency2 + comission(b * currency2)) < balance2:
        print("Размер снятия:", b * currency2, "уе")
        print("Размер комиссии: ", comission(b * currency2) , "уе")
        balance2 = balance2 - b * currency2 - comission(b * currency2)
        print("БАЛАНС ВАШЕГО СЧЁТА: ", round(balance2, 2) , "уе")
        menu(balance2, currency2, counter2)
    else:
        print("Превышение баланса, возвращаем в главное меню")
        menu(balance2, currency2, counter2)

def comission(com): #расчёт комиссии
    if com * 0.015 < 30:
        comission = 30
        return comission
    if com * 0.015 > 600:
        comission = 600
        return comission
    else:
        comission = com * 0.015
        return comission

def rich_limit(balance5): #расчёт налога на богатство
    if balance5 > 5000000:
        balance5 = balance5 * 0.9
        return balance5
    else:
        return balance5

def menu(balance3, currency3, counter3): #меню банковата
    print("1 ПОПОЛНИТЬ")
    print("2 СНЯТЬ")
    print("3 БАЛАНС")
    print("4 ВЫЙТИ")
    a = int(input("Введите пункт меню: "))
    if a == 1:
        balance3 = pay(balance3, currency3, counter3)
    if a == 2:
        balance3 = draw(balance3, currency3, counter3)
    if a == 3:
        print("БАЛАНС ВАШЕГО СЧЁТА: ", round(balance3, 2))
        menu(balance3, currency3, counter3)
    if a == 4:
        print("ХОРОШЕГО ДНЯ!")   
    else:
        print("ERROR!!! НЕВЕРНЫЙ ВВОД!!! ВОЗВРАТ В МЕНЮ!!!")
        menu(balance3, currency3, counter3)
    
menu(BALANCE, CURRENCY, COUNTER)