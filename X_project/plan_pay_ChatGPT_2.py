from datetime import datetime
import calendar

def to_cents(x: float) -> int:
    """Перетворення у копійки (int)."""
    return int(round(x * 100))

def from_cents(x: int) -> float:
    """Назад у гривні."""
    return x / 100.0


def simulate_schedule_with_interest_debt(principal, daily_rate, months, start_date, pay_day, payment):
    """Повертає фінальний залишок (тіло + борг по відсотках) у копійках."""
    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    balance = to_cents(principal)
    interest_debt = 0

    for m in range(1, months + 1):
        # Дата наступного платежу
        year, month = current_date.year, current_date.month
        month += 1
        if month > 12:
            month = 1
            year += 1
        last_day = calendar.monthrange(year, month)[1]
        pay_date = datetime(year, month, min(pay_day, last_day))

        # Нараховані відсотки (проста ставка)
        days = (pay_date - current_date).days
        interest = to_cents(from_cents(balance) * daily_rate * days)

        pay_remaining = payment

        # 1. Погашення боргу по відсотках
        if pay_remaining >= interest_debt:
            pay_remaining -= interest_debt
            interest_debt = 0
        else:
            interest_debt -= pay_remaining
            pay_remaining = 0

        # 2. Погашення поточних відсотків
        if pay_remaining >= interest:
            pay_remaining -= interest
        else:
            interest_debt += (interest - pay_remaining)
            pay_remaining = 0

        # 3. Погашення тіла
        balance -= pay_remaining

        current_date = pay_date

    return balance + interest_debt


def annuity_payment_iterative_with_interest_debt(principal, daily_rate, months, start_date, pay_day, tol=1, max_iter=200):
    """
    Підбирає платіж так, щоб фінальний баланс був <= 0.
    Усі розрахунки у копійках (tol=1 → точність до 1 копійки).
    """
    low, high = 0, to_cents(principal) * 2
    payment = (low + high) // 2

    for _ in range(max_iter):
        final_total = simulate_schedule_with_interest_debt(principal, daily_rate, months, start_date, pay_day, payment)

        if -tol <= final_total <= tol:
            break
        if final_total > 0:  # залишок > 0 → платіж малий
            low = payment
        else:               # залишок < 0 → платіж завеликий
            high = payment

        payment = (low + high) // 2

    # 🔹 Гарантуємо, що борг погашений (залишок ≤ 0)
    final_total = simulate_schedule_with_interest_debt(principal, daily_rate, months, start_date, pay_day, payment)
    if final_total > 0:
        payment += 1  # додаємо 1 копійку

    # Будуємо фінальний графік
    schedule = []
    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    balance = to_cents(principal)
    interest_debt = 0

    for m in range(1, months + 1):
        year, month = current_date.year, current_date.month
        month += 1
        if month > 12:
            month = 1
            year += 1
        last_day = calendar.monthrange(year, month)[1]
        pay_date = datetime(year, month, min(pay_day, last_day))

        days = (pay_date - current_date).days
        interest = to_cents(from_cents(balance) * daily_rate * days)
        pay_remaining = payment

        # 1. Борг по відсотках
        if pay_remaining >= interest_debt:
            paid_interest_debt = interest_debt
            pay_remaining -= interest_debt
            interest_debt = 0
        else:
            paid_interest_debt = pay_remaining
            interest_debt -= pay_remaining
            pay_remaining = 0

        # 2. Поточні відсотки
        if pay_remaining >= interest:
            paid_interest = interest
            pay_remaining -= interest
        else:
            paid_interest = pay_remaining
            interest_debt += (interest - pay_remaining)
            pay_remaining = 0

        # 3. Тіло
        paid_principal = pay_remaining
        balance -= paid_principal

        schedule.append({
            "№": m,
            "Дата": pay_date.strftime("%Y-%m-%d"),
            "Днів": days,
            "Платіж": from_cents(payment),
            "Відсотки (поточні)": from_cents(interest),
            "Погашено боргу по %": from_cents(paid_interest_debt),
            "Погашено поточних %": from_cents(paid_interest),
            "Недоплата %": from_cents(interest_debt),
            "Тіло": from_cents(paid_principal),
            "Залишок тіла": from_cents(balance),
            "Загальний борг": from_cents(balance + interest_debt)
        })

        current_date = pay_date

    return from_cents(payment), schedule


# 🔹 Тест
principal = 10000
daily_rate = 0.0005  # 0.05% на день
months = 360
start_date = "2025-08-20"
pay_day = 25

payment, schedule = annuity_payment_iterative_with_interest_debt(principal, daily_rate, months, start_date, pay_day)

print(f"Підібраний щомісячний платіж ≈ {payment:.2f} грн\n")
print("Графік:")
for row in schedule:
    print(row)