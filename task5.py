### Data Since - Task 5 - Umarov Kamoliddin

print(f"Son kvadratini hisoblash")

from colorama import Fore

def kvadratni_hisobla(son):
    natija = son ** 2
    return natija

# Foydalanuvchidan son olish
A = int(input(Fore.GREEN + "Istalgan sonni kiriting: "))

# Funktsiyani chaqirib, natijani hisoblash
B = kvadratni_hisobla(A)

# Natija
print(Fore.YELLOW + f"{A} ning kvadrati {B} ga teng.")