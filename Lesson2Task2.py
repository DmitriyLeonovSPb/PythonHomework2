def decTransHex(dec):
    hex = ''
    while(dec > 0):
        num1 = dec % 16
        hex = numbers[num1] + hex
        dec = dec // 16
    return hex

dec_num = int(input("Введите десятичное число: "))
numbers = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}

hex_trans = decTransHex(dec_num)
print(hex_trans)