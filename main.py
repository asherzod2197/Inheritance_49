# 49. Do‘kon zaxiralari

class Stock:
    def __init__(self, item_type, quantity):
        self.item_type = item_type      # "Meva", "Telefon", "Kiyim" va h.k.
        self.quantity = quantity        # zaxira miqdori (dona / kg / litr)

    def check_quantity(self):
        """Joriy zaxira miqdori"""
        return self.quantity

    def __str__(self):
        return f"{self.item_type:14} | {self.quantity:6} dona"


# -----------------------------------------------
# Voris sinflar (emoji va chiroyli chiqish)
# -----------------------------------------------

class FoodStock(Stock):
    def __str__(self):
        qty = self.check_quantity()
        status = "✅ yetarli" if qty >= 50 else "⚠️ kam qoldi" if qty > 0 else "❌ tugagan"
        return f"🍎 {self.item_type:12} → {qty:5} dona  ({status})"


class ElectronicsStock(Stock):
    def __str__(self):
        qty = self.check_quantity()
        status = "✅ yetarli" if qty >= 10 else "⚠️ kam qoldi" if qty > 0 else "❌ tugagan"
        return f"📱 {self.item_type:12} → {qty:5} dona  ({status})"


# --------------------------------------------------
# Do‘kon zaxira holatini chiqarish
# --------------------------------------------------

def show_store_stock(items):
    print("\n" + "═" * 70)
    print("       DO‘KON ZAXIRA HOLATI — QOLDIQ KUZATUV       ".center(70))
    print("═" * 70)
    print("Mahsulot turi               Qoldiq (dona)     Holat")
    print("─" * 70)

    total_items = 0
    low_stock = []

    for item in items:
        print(item)
        qty = item.check_quantity()
        total_items += qty
        
        if qty < 20 and qty > 0:
            low_stock.append(item.item_type)

    print("─" * 70)
    print(f"Jami zaxira miqdori (barcha mahsulotlar):     {total_items:6} dona")

    if low_stock:
        print("\n⚠️ Tez orada to‘ldirish kerak bo‘lgan mahsulotlar:")
        for name in low_stock:
            print(f"  • {name}")

    print("═" * 70 + "\n")


# Test ma'lumotlari
zaxiralar = [
    FoodStock("Meva (olma + banan)", 180),
    ElectronicsStock("Telefon (smartfon)", 42),
    FoodStock("Non va non mahsulotlari", 28),      # kam qolgan
    ElectronicsStock("Quloqchinlar", 8),           # juda kam
    FoodStock("Sut va sut mahsulotlari", 0),       # tugagan
    ElectronicsStock("Planshet", 15),
]

show_store_stock(zaxiralar)


# Sizning misol qiymatlaringiz bilan:
print("\nSizning misol zaxirangiz:\n")
misol_zaxiralar = [
    FoodStock("Meva", 200),
    ElectronicsStock("Telefon", 50),
]

show_store_stock(misol_zaxiralar)
