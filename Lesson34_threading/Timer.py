import threading, time

def countdown(n):
    while n > 0:
        print(f"Залишилось: {n} сек")
        time.sleep(1)
        n -= 1
    print("🚀 Час вийшов!")

t = threading.Thread(target=countdown, args=(5,), daemon=True)
t.start()

# print("Головна програма може закінчитись раніше...")
time.sleep(6)   # після 3 сек main закінчить роботу