import json


# Класс для хранения данных об инопланетянине
class Alien:
    def __init__(self, id, isHumanoid, originPlanet, age, physicalTraits):
        self.id = id  # ID инопланетянина
        self.isHumanoid = isHumanoid  # Гуманоид или нет
        self.originPlanet = originPlanet  # Планета происхождения
        self.age = age  # Возраст
        self.physicalTraits = physicalTraits if physicalTraits else []  # Список характеристик


# Основной класс для классификации
class AlienClassifier:
    def __init__(self):
        self.aliens = []  # Список всех инопланетян
        # Словарь для хранения ID по вселенным
        self.universes = {
            "starWars": [],
            "marvel": [],
            "hitchhikers": [],
            "rings": []
        }

    # Чтение данных из файла
    def read_input(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Создаем объекты Alien из JSON
        for item in data:
            alien = Alien(
                item['id'],
                item['isHumanoid'],
                item['originPlanet'],
                item['age'],
                item['physicalTraits']
            )
            self.aliens.append(alien)

        print(f"Loaded {len(self.aliens)} aliens")

    # Проверка: есть ли у инопланетянина определенная характеристика
    def has_trait(self, alien, trait):
        return trait in alien.physicalTraits

    # Определение вселенной по правилам
    def determine_universe(self, alien):

        # STAR WARS - Wookiee
        if (alien.isHumanoid == False and
                alien.originPlanet == 'KASHYYYK' and
                (alien.age is None or alien.age <= 400)):
            # Если нет характеристик или есть HAIRY/TALL
            if (len(alien.physicalTraits) == 0 or
                    self.has_trait(alien, 'HAIRY') or
                    self.has_trait(alien, 'TALL')):
                return 'starWars'

        # STAR WARS - Ewok
        if (alien.isHumanoid == False and
                alien.originPlanet == 'ENDOR' and
                (alien.age is None or alien.age <= 60)):
            if (len(alien.physicalTraits) == 0 or
                    self.has_trait(alien, 'SHORT') or
                    self.has_trait(alien, 'HAIRY')):
                return 'starWars'

        # MARVEL - Asgardian
        if (alien.isHumanoid == True and
                alien.originPlanet == 'ASGARD' and
                (alien.age is None or alien.age <= 5000)):
            if (len(alien.physicalTraits) == 0 or
                    self.has_trait(alien, 'BLONDE') or
                    self.has_trait(alien, 'TALL')):
                return 'marvel'

        # HITCHHIKER'S GUIDE - Betelgeusian
        if (alien.isHumanoid == True and
                alien.originPlanet == 'BETELGEUSE' and
                (alien.age is None or alien.age <= 100)):
            # Должны быть EXTRA_ARMS или EXTRA_HEAD
            if len(alien.physicalTraits) == 0:
                return 'hitchhikers'
            for trait in ['EXTRA_ARMS', 'EXTRA_HEAD']:
                if self.has_trait(alien, trait):
                    return 'hitchhikers'

        # HITCHHIKER'S GUIDE - Vogon
        if (alien.isHumanoid == False and
                alien.originPlanet == 'VOGSPHERE' and
                (alien.age is None or alien.age <= 200)):
            if (len(alien.physicalTraits) == 0 or
                    self.has_trait(alien, 'GREEN') or
                    self.has_trait(alien, 'BULKY')):
                return 'hitchhikers'

        # LORD OF THE RINGS - Elf
        if (alien.isHumanoid == True and
                alien.originPlanet == 'EARTH' and
                self.has_trait(alien, 'POINTY_EARS')):
            return 'rings'

        # LORD OF THE RINGS - Dwarf
        if (alien.isHumanoid == True and
                alien.originPlanet == 'EARTH' and
                (alien.age is None or alien.age <= 200)):
            if (self.has_trait(alien, 'SHORT') or
                    self.has_trait(alien, 'BULKY')):
                return 'rings'

        # Если не подходит ни под одну категорию
        return None

    # Классификация всех инопланетян
    def classify(self):
        for alien in self.aliens:
            universe = self.determine_universe(alien)
            if universe:
                self.universes[universe].append(alien.id)

        # Вывод результатов
        print(f"\nClassification complete:")
        for universe, ids in self.universes.items():
            print(f"{universe}: {len(ids)} aliens")

    # Сохранение результатов в файл
    def write_output(self, filename):
        output = []

        # Формируем список для JSON
        for universe, ids in self.universes.items():
            if ids:  # Только если есть инопланетяне
                output.append({
                    "universe": universe,
                    "individuals": ids
                })

        # Записываем в файл
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2)

        print(f"\nOutput written to {filename}")


# Главная функция
def main():
    classifier = AlienClassifier()  # Создаем классификатор

    classifier.read_input('input.json')  # Читаем файл
    classifier.classify()  # Классифицируем
    classifier.write_output('output.json')  # Сохраняем результат

    print("\nClassification complete!")


# Запуск программы
if __name__ == "__main__":
    main()