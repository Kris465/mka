print("1. Лара Крофт находит артефакт")
print("2. Лара Крофт сталкивается с врагами")
print("3. Лара Крофт изучает карту")
action = int(input("Введите событие:"))
if action == 1:
    print("Это может изменить всё!")
elif action == 2:
    print("Я не сдамся без боя!")
elif action == 3:
    print("Каждый шаг — это новое открытие!")
else:
    print("Лара Крофт исследует руины")
