from datetime import datetime
import calendar

def annuity_payment(principal: float, daily_rate: float, months: int, start_date: str, pay_day: int):
    """
    Обчислює ануїтетний платіж та графік погашення з розбивкою на тіло і відсотки.

    :param principal: сума кредиту
    :param daily_rate: добова відсоткова ставка (наприклад 0.0005 для 0.05%)
    :param months: термін у місяцях
    :param start_date: початкова дата у форматі YYYY-MM-DD
    :param pay_day: число місяця для щомісячної оплати
    """

    # Переводимо добову ставку в місячну (середньо 30.4375 днів)
    monthly_rate = (1 + daily_rate) ** 30.4375 - 1

    # Ануїтетний платіж
    payment = principal * (monthly_rate / (1 - (1 + monthly_rate) ** -months))

    payments = []
    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    balance = principal

    for m in range(1, months + 1):
        # Наступна дата платежу
        year, month = current_date.year, current_date.month
        month += 1
        if month > 12:
            month = 1
            year += 1

        # День платежу
        last_day = calendar.monthrange(year, month)[1]
        pay_date = datetime(year, month, min(pay_day, last_day))

        # Відсотки за місяць
        interest = balance * monthly_rate
        # Тіло кредиту
        principal_part = payment - interest
        # Зменшуємо залишок
        balance -= principal_part

        # Корекція останнього платежу (щоб борг = 0)
        if m == months:
            principal_part += balance
            payment = principal_part + interest
            balance = 0

        payments.append({
            "№": m,
            "Дата": pay_date.strftime("%Y-%m-%d"),
            "Платіж": round(payment, 2),
            "Відсотки": round(interest, 2),
            "Тіло": round(principal_part, 2),
            "Залишок": round(balance, 2)
        })

        current_date = pay_date

    return round(payment, 2), payments


# 🔹 Тест
principal = 10000   # кредит
daily_rate = 0.001  # 0.05%/день
months = 12
start_date = "2025-08-20"
pay_day = 15

payment, schedule = annuity_payment(principal, daily_rate, months, start_date, pay_day)

print(f"Щомісячний платіж ≈ {payment} грн\n")
print("Графік:")
for row in schedule:
    print(row)
