import random
answer_1 = random.randint(1, 9)
answer_2 = random.randint(1, 9)
answer_3 = random.randint(1, 9)
answer_4 = random.randint(1, 9)
bot_number = []
bot_number.append(answer_1)
bot_number.append(answer_2)
bot_number.append(answer_3)
bot_number.append(answer_4)
key = answer_1 *1000 + answer_2 * 100 + answer_3 * 10+ answer_4*1
a = 0
b = 0
print(key)
while True:
    guess = int(input("請輸入4位數字"))
    man_guess_1 = int(guess / 1000)
    man_guess_2 = int(guess / 100) - man_guess_1*10
    man_guess_3 = int(guess / 10) - man_guess_1*100 - man_guess_2*10
    man_guess_4 = int(guess / 1) - man_guess_1*1000 -man_guess_2*100 -man_guess_3*10
    man_number = []
    man_number.append(man_guess_1)
    man_number.append(man_guess_2)
    man_number.append(man_guess_3)
    man_number.append(man_guess_4)
    my_list = bot_number + man_number
    for i in range(4):
        if my_list[i] == my_list[i + 4]:
            a += 1
            b -= 1
    for j in bot_number:
        if j in man_number:
            b += 1
    print(a,"a" ,b,"b")
    a = 0
    b = 0
            
        

