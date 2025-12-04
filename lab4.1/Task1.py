class Display:
    def __init__(self, width, height, ppi, model):
        # Инициализация основных параметров монитора
        self.width = width
        self.height = height
        self.ppi = ppi
        self.model = model

    def compare_size(self, other):
        # Сравнение площади экранов
        my_size = self.width * self.height
        other_size = other.width * other.height

        if my_size > other_size:
            print(f"{self.model} is larger than {other.model}")
        elif my_size < other_size:
            print(f"{self.model} is smaller than {other.model}")
        else:
            print(f"{self.model} and {other.model} are the same size")

    def compare_sharpness(self, other):
        # Сравнение четкости по PPI
        if self.ppi > other.ppi:
            print(f"{self.model} (PPI: {self.ppi}) is sharper than {other.model} (PPI: {other.ppi})")
        elif self.ppi < other.ppi:
            print(f"{self.model} (PPI: {self.ppi}) is less sharp than {other.model} (PPI: {other.ppi})")
        else:
            print(f"{self.model} and {other.model} have the same sharpness")

    def compare_with_monitor(self, other):
        # Полное сравнение размеров и четкости
        print(f"\nFull comparison: {self.model} vs {other.model}")
        self.compare_size(other)
        self.compare_sharpness(other)


# создаем 3 монитора
display1 = Display(1920, 1080, 96, "Samsung S24")
display2 = Display(2560, 1440, 109, "Dell UltraSharp")
display3 = Display(1920, 1080, 92, "LG 24inch")

# сравниваем мониторы
print("Task 1: Monitor comparison\n")
display1.compare_size(display2)
display1.compare_sharpness(display3)
display2.compare_with_monitor(display3)

