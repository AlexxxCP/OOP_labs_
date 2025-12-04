class Display:
    def __init__(self, width, height, ppi, model):
        # Инициализация параметров монитора
        self.width = width
        self.height = height
        self.ppi = ppi
        self.model = model

    def compare_size(self, other):
        # Сравнение площади экранов
        my_size = self.width * self.height
        other_size = other.width * other.height

        if my_size > other_size:
            return f"{self.model} is larger than {other.model}"
        elif my_size < other_size:
            return f"{self.model} is smaller than {other.model}"
        else:
            return f"{self.model} and {other.model} are the same size"

    def compare_sharpness(self, other):
        # Сравнение четкости по PPI
        if self.ppi > other.ppi:
            return f"{self.model} is sharper than {other.model}"
        elif self.ppi < other.ppi:
            return f"{self.model} is less sharp than {other.model}"
        else:
            return f"{self.model} and {other.model} have equal sharpness"

    def compare_with_monitor(self, other):
        # Полное сравнение
        result = f"\n=== Comparison of {self.model} and {other.model} ===\n"
        result += self.compare_size(other) + "\n"
        result += self.compare_sharpness(other)
        return result


class Assistant:
    def __init__(self, assistant_name):
        # Имя ассистента и список мониторов
        self.assistant_name = assistant_name
        self.assigned_displays = []

    def assign_display(self, display):
        # Добавление монитора
        self.assigned_displays.append(display)
        print(f"Display {display.model} added to {self.assistant_name}'s list")

    def assist(self):
        # Проверка и сравнение мониторов
        if len(self.assigned_displays) < 2:
            print(f"{self.assistant_name}: Not enough monitors to compare")
            return

        print(f"\n{self.assistant_name} helps you choose a monitor:\n")

        for i in range(len(self.assigned_displays) - 1):
            current = self.assigned_displays[i]
            next_display = self.assigned_displays[i + 1]
            print(current.compare_with_monitor(next_display))

    def buy_display(self, display):
        # Покупка монитора (удаление из списка)
        if display in self.assigned_displays:
            self.assigned_displays.remove(display)
            print(f"\n{self.assistant_name}: You purchased {display.model}!")
            return display
        else:
            print(f"\n{self.assistant_name}: Display {display.model} not found in the list")
            return None


# Testing (тестирование)
if __name__ == "__main__":
    print("=== Task 3: Assistant Class ===\n")

    # Creating displays
    display1 = Display(1920, 1080, 96, "Samsung S24")
    display2 = Display(2560, 1440, 109, "Dell UltraSharp")
    display3 = Display(1920, 1080, 92, "LG 24inch")
    display4 = Display(3840, 2160, 163, "Apple Studio Display")

    # Creating assistant
    assistant = Assistant("Tech Assistant")

    # Adding displays
    assistant.assign_display(display1)
    assistant.assign_display(display2)
    assistant.assign_display(display3)
    assistant.assign_display(display4)

    # Getting assistance
    assistant.assist()

    # Buying a display
    bought = assistant.buy_display(display2)

    print(f"\nRemaining displays: {[d.model for d in assistant.assigned_displays]}")
