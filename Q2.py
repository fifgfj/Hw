import random
menu = {
        "咖哩飯" : 79
        ,"麻醬麵" : 50
        ,"滷肉飯" : 30
        ,"招牌炒飯" : 65
        ,"古早味乾麵" : 55
        }
print(f"以下是菜單\n{menu}")
bot = random.randint(1, 3)
man = input("現在可以進行活動\n請輸入剪刀、石頭、布:)")
if man == "剪刀":
    man_value = 1
elif man =="石頭":
    man_value = 2
elif man ==  "布":
    man_value = 3
if bot == 1:
    bot_decision = "剪刀"
elif bot == 2:
    bot_decision = "石頭"
elif bot == 3:
    bot_decision = "布"

if bot == man_value:
    discount = 9
    print(f"店員出: {bot_decision}")
    print("平手")
elif bot == man_value +1 or man_value - 2:
    discount = 10
    print(f"店員出: {bot_decision}")
    print("你輸了")
elif man_value == bot +1 or bot - 2:
    discount = 5
    print(f"店員出: {bot_decision}")
    print("你贏了")

print("以下是你的消費明細")
print("----------------------------------")
order = {}
order_amount1 = random.randint(1, 10)
order["咖哩飯"] = order_amount1
order_amount2 = random.randint(1, 10)
order["麻醬麵"] = order_amount2
order_amount3 = random.randint(1, 10)
order["滷肉飯"] = order_amount3
order_amount4 = random.randint(1, 10)
order["招牌炒飯"] = order_amount4
order_amount5 = random.randint(1, 10)
order["古早味乾麵"] = order_amount5
total = menu["古早味乾麵"] * order_amount5 + menu["咖哩飯"] * order_amount1 + menu["麻醬麵"] * order_amount2 + menu["滷肉飯"] * order_amount3 + menu["招牌炒飯"] * order_amount4
discount_total = int(total *(discount/10))
print(order)
print(f"打{discount}折後，總金額為:{discount_total}元")