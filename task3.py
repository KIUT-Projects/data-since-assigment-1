### Data Since - Task 3 - Umarov Kamoliddin

print(f"3ta raqamdan o'rta qiymatni topish")

from colorama import Fore

# Foydalanuvchidan uchta raqam kiritish
raqam1 = int(input(Fore.GREEN + "Birinchi raqamni kiriting: "))
raqam2 = int(input(Fore.GREEN + "Ikkinchi raqamni kiriting: "))
raqam3 = int(input(Fore.GREEN + "Uchinchi raqamni kiriting: "))

# If shart operatori orqali o'rtadagi raqamni topish
if raqam1 <= raqam2 <= raqam3 or raqam3 <= raqam2 <= raqam1:
    orta_raqam = raqam2
elif raqam2 <= raqam1 <= raqam3 or raqam3 <= raqam1 <= raqam2:
    orta_raqam = raqam1
else:
    orta_raqam = raqam3

# Natija
print(Fore.YELLOW + f"Uch raqamning orasidagi o'rtadagi raqam: {orta_raqam}")