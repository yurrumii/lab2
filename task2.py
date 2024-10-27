salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

security_pillow = 0
for month in range(months):
    security_pillow += spend
    spend *= (1 + increase)
security_pillow -= (salary * months)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {int(security_pillow):}")