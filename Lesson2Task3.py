a1 = input("Введите 1 дробь в формате a/b: ")
b1 = input("Введите 2 дробь в формате a/b: ")
a_split = a1.split("/")
b_split = b1.split("/")
a_chis = int(a_split[0])
a_znam = int(a_split[1])
b_chis = int(b_split[0])
b_znam = int(b_split[1])

summ = float((a_chis * b_znam + b_chis * a_znam)/(a_znam * b_znam))
print("Сумма дробей = " , summ)

mult = float((a_chis * b_chis)/(a_znam * b_znam))
print("Произведение дробей = " , mult)