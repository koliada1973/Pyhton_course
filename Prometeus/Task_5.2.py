# Напишіть програму, яка просить користувача вводити цілі числа допоки користувач не зазначить «готово» (“done”).
# Після введення «готово» (“done”), виведіть найбільше та найменше з введених чисел.
# Якщо користувач вводить некоректне число, обробіть його за допомогою try / except, виведіть на екран відповідне повідомлення, та проігноруйте це число.
# Виведіть 7, 2, bob, 10, і 4, та порівняйте з наведеними нижче результатами.

largest = None
smallest = None
while True:
    user = input("Enter number: ")
    if user == "done":
        break
    try:
        user = int(user)
    except:
        print("Invalid input")
        continue
    if smallest is None or user < smallest:
        smallest = user

    if largest is None or user > largest:
        largest = user
print('Maximum is ', largest)
print('Minimum is ', smallest)
