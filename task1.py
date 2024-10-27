money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
months = 0
while money_capital >= 0:
    budget = money_capital + salary
    if spend <= budget:
        money_capital -= (spend - salary)
        months += 1
        spend *= (1 + increase)
    else:
        break
print("Количество месяцев, которое можно протянуть без долгов:", months)
