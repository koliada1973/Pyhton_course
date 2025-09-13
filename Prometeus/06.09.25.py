# a = float(input("Enter Hours:"))
# r = float(input("Enter rate: "))
#
# res = 0
#
# if a > 40:
#     delta_hours = a - 40
#     res = delta_hours * r * 1.5 + 40 * r
# elif a <= 40:
#     res = a * r
# print(res)



score = input("Enter Score: ")
try:
    score = float(score)
except:
    print("Error")

if score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
elif score >= 0.5:
    print("F")