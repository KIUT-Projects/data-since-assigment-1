### Data Since - Task 4 - Umarov Kamoliddin

print(f"Kg narxini bilib, 10kg gacha narxini chiqarish")

from colorama import Fore

#1 kg olma narxi
narx_1kg = float(input(Fore.GREEN + "1 kg olma narxini kiriting: "))

# For orqali 1 dan 10 gacha bo'lgan olmalar uchun narxni hisoblash
for kg in range(1, 11):
    total_narx = kg * narx_1kg
    print(Fore.YELLOW + f"{kg} kg olma narxi: {total_narx} so'm")
