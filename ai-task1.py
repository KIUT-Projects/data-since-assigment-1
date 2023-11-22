import numpy as np
from colorama import Fore

print(
    "A = np.arange(100).reshape(10, 10) ni qo‘llab 10x10 massiv yarating. A massivning har bir qatorining maksimum qiymatini toping.")

# 10x10 massivni yaratish
A = np.arange(100).reshape(10, 10)

print(Fore.BLUE + "\nBizning massiv: ")
print(A)

# Har bir qatorning maksimum qiymatini topish
max_values = np.max(A, axis=1)

# Natijalarni chop etish
print(Fore.GREEN + "\nHar bir QATORning maksimum qiymati:", max_values)

max_values_column = np.max(A, axis=0)
print(Fore.GREEN + "Har bir USTUNning maksimum qiymati:", max_values_column)

