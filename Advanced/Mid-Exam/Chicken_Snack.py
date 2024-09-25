from collections import deque

money = [int(x) for x in input().split()]
price_food = deque([int(i) for i in input().split()])
pocket = []

count_food = 0

while money and price_food:
    current_money = money.pop()
    current_price_food = price_food.popleft()

    if current_money == current_price_food:
        count_food += 1

    elif current_money > current_price_food:
        count_food += 1
        if not money:
            break
        else:
            pocket.append((current_money - current_price_food) + money[-1])
            money[-1] = money[-1] + (current_money - current_price_food)
    else:
        continue

if count_food >= 4:
    print(f'Gluttony of the day! Henry ate {count_food} foods.')

if count_food == 1:
    print(f'Henry ate: {count_food} food.')
elif count_food == 2 or count_food == 3:
    print(f'Henry ate: {count_food} foods.')

if count_food == 0:
    print(f'Henry remained hungry. He will try next weekend again.')





