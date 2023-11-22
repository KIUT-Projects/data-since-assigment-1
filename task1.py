### Data Since - Task 1 - Umarov Kamoliddin

print(f"Doira maydonini kiritib, uzunligi va diametrini hisoblash")

from colorama import Fore
import math

pi = 3.14

# Doira maydonini kiritish
S = float(input(Fore.GREEN +"Doiraning maydonini kiriting: "))

# Doira radiusini hisoblash
radius = math.sqrt(S / pi)

# Diametr chiqarish
diameter = radius * 2

# Uzunligini hisoblash
length = 2 * math.pi * radius

# Natija
print(Fore.YELLOW + f"Doiraning Diametri (D):{diameter}")
print(Fore.YELLOW + f"Doiraning Uzunligi (L): {length}")
