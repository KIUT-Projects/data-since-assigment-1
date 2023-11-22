### Data Since - Task 2 - Umarov Kamoliddin

print(f"Ko'p xonali son kiritib, teskarisini chiqarish")

from colorama import Fore

# Son qabul qilish
son = int(input(Fore.GREEN + "Ko'p xonali son kiriting: "))
javob = 0

while son != 0:
    digit = son % 10
    javob = javob * 10 + digit
    son //= 10

# Natija
print(Fore.YELLOW + f"Kiritilgan son: {son}")
print(Fore.YELLOW + f"Teskari son: {javob}")
