from enum import Enum

class Intensity(Enum):
    LIGHT = "LIGHT"
    NORMAL = "NORMAL"
    STRONG = "STRONG"

class SyrupType(Enum):
    VANILLA = "VANILLA"
    CARAMEL = "CARAMEL"
    CHOCOLATE = "CHOCOLATE"

# TASK 1
# Родитель всех кофе
class Coffee:
    def __init__(self, intensity):
        self._intensity = intensity
        self._name = "Coffee"

    # Метод для печати кофе
    def printCoffeeDetails(self):
        print(f"Coffee: {self._name}")
        print(f"Intensity: {self._intensity.value}")

    # Метод приготовления кофе
    def makeCoffee(self):
        print(f"Making {self._name}...")
        print("Step 1: Brewing coffee")
        return self


# Добавляет молоко
class Cappuccino(Coffee):
    def __init__(self, intensity, mlOfMilk):
        super().__init__(intensity)
        self._mlOfMilk = mlOfMilk
        self._name = "Cappuccino"

    def printCoffeeDetails(self):
        super().printCoffeeDetails()
        print(f"Milk: {self._mlOfMilk} ml")

    def makeCappuccino(self):
        print(f"Making {self._name}...")
        super().makeCoffee()
        print(f"Step 2: Adding {self._mlOfMilk} ml of milk")
        return self


# Добавляет воду
class Americano(Coffee):
    def __init__(self, intensity, mlOfWater):
        super().__init__(intensity)
        self._mlOfWater = mlOfWater
        self._name = "Americano"

    def printCoffeeDetails(self):
        super().printCoffeeDetails()
        print(f"Water: {self._mlOfWater} ml")

    def makeAmericano(self):
        print(f"Making {self._name}...")
        super().makeCoffee()
        print(f"Step 2: Adding {self._mlOfWater} ml of water")
        return self


# Добавляет сироп
class SyrupCappuccino(Cappuccino):
    def __init__(self, intensity, mlOfMilk, syrup):
        super().__init__(intensity, mlOfMilk)
        self._syrup = syrup
        self._name = "SyrupCappuccino"

    def printCoffeeDetails(self):
        super().printCoffeeDetails()
        print(f"Syrup: {self._syrup.value}")

    def makeSyrupCappuccino(self):
        print(f"Making {self._name}...")
        super().makeCappuccino()
        print(f"Step 3: Adding {self._syrup.value} syrup")
        return self


# Добавляет тыквенную специю
class PumpkinSpiceLatte(Cappuccino):
    def __init__(self, intensity, mlOfMilk, mgOfPumpkinSpice):
        super().__init__(intensity, mlOfMilk)
        self._mgOfPumpkinSpice = mgOfPumpkinSpice
        self._name = "PumpkinSpiceLatte"

    def printCoffeeDetails(self):
        super().printCoffeeDetails()
        print(f"Pumpkin Spice: {self._mgOfPumpkinSpice} mg")

    def makePumpkinSpiceLatte(self):
        print(f"Making {self._name}...")
        super().makeCappuccino()
        print(f"Step 3: Adding {self._mgOfPumpkinSpice} mg of pumpkin spice")
        return self


# TASK 4: BARISTA

class Barista:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def takeOrder(self, coffee):
        self.orders.append(coffee)
        print(f"\nBarista {self.name}: Order accepted!")

    def showOrderDetails(self, coffee):
        print("\n" + "=" * 40)
        coffee.printCoffeeDetails()
        print("=" * 40)

    def prepareCoffee(self, coffee):
        print("\n" + "-" * 40)

        if isinstance(coffee, PumpkinSpiceLatte):
            coffee.makePumpkinSpiceLatte()
        elif isinstance(coffee, SyrupCappuccino):
            coffee.makeSyrupCappuccino()
        elif isinstance(coffee, Cappuccino):
            coffee.makeCappuccino()
        elif isinstance(coffee, Americano):
            coffee.makeAmericano()
        else:
            coffee.makeCoffee()

        print(f"Ready: {coffee._name}")
        print("-" * 40)

    def processAllOrders(self):
        if not self.orders:
            print(f"\nBarista {self.name}: No orders!")
            return

        print(f"\nBarista {self.name} is making {len(self.orders)} coffee(s)...")

        for i, coffee in enumerate(self.orders, 1):
            print(f"\n>>> ORDER #{i} <<<")
            self.showOrderDetails(coffee)
            self.prepareCoffee(coffee)

        print(f"\nAll orders done!")
        self.orders.clear()


def main():
    print("    COFFEE SHOP")

    barista = Barista("John")

    while True:
        print("\n MENU")
        print("1. Order Coffee")
        print("2. Order Americano")
        print("3. Order Cappuccino")
        print("4. Order Syrup Cappuccino")
        print("5. Order Pumpkin Spice Latte")
        print("6. Process orders")
        print("0. Exit")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            coffee = Coffee(Intensity.NORMAL)
            barista.takeOrder(coffee)

        elif choice == "2":
            coffee = Americano(Intensity.NORMAL, 150)
            barista.takeOrder(coffee)

        elif choice == "3":
            coffee = Cappuccino(Intensity.NORMAL, 100)
            barista.takeOrder(coffee)

        elif choice == "4":
            coffee = SyrupCappuccino(Intensity.NORMAL, 100, SyrupType.VANILLA)
            barista.takeOrder(coffee)

        elif choice == "5":
            coffee = PumpkinSpiceLatte(Intensity.STRONG, 120, 30)
            barista.takeOrder(coffee)

        elif choice == "6":
            barista.processAllOrders()

        elif choice == "0":
            print("\nThank you! Goodbye!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
