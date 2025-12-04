import sys
import os

class FileReader:
    @staticmethod
    def read_file_into_string(path):
        # Чтение файла и возврат строки
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()

class TextData:
    def __init__(self, text, filename):
        # Сохраняем текст и имя файла
        self.fileName = filename
        self.text = text
        # Подсчитываем параметры текста
        self.numberOfVowels = self._count_vowels()  # Подсчет гласных
        self.numberOfConsonants = self._count_consonants()  # Подсчет согласных
        self.numberOfLetters = self._count_letters()  # Подсчет всех букв
        self.numberOfSentences = self._count_sentences()  # Подсчет предложений
        self.longestWord = self._find_longest_word()  # Поиск самого длинного слова

    def _count_vowels(self):
        vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
        return sum(1 for char in self.text if char in vowels)

    def _count_consonants(self):
        vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
        return sum(1 for char in self.text if char.isalpha() and char not in vowels)

    def _count_letters(self):
        return sum(1 for char in self.text if char.isalpha())

    def _count_sentences(self):
        sentence_endings = '.!?'
        return sum(1 for char in self.text if char in sentence_endings)

    def _find_longest_word(self):
        cleaned = ''.join(c if c.isalpha() or c.isspace() else ' ' for c in self.text)
        words = cleaned.split()
        return max(words, key=len) if words else ""

    def __str__(self):
        # Возврат форматированной информации о тексте
        return f"""
=== File Information: {self.fileName} ===
Number of vowels: {self.numberOfVowels}
Number of consonants: {self.numberOfConsonants}
Number of letters: {self.numberOfLetters}
Number of sentences: {self.numberOfSentences}
Longest word: {self.longestWord}
"""

# основная
if __name__ == "__main__":
    # передан ли путь к файлу
    if len(sys.argv) < 2:
        print("Usage: python task2.py <path_to_txt_file>")
        print("Creating test file...\n")

        # тестовый файл
        test_content = "Hello world! This is a simple test. Python programming is amazing!"
        with open("../test.txt", "w", encoding="utf-8") as f:
            f.write(test_content)

        file_path = "../test.txt"
    else:
        file_path = sys.argv[1]

    # Чтение файла и анализ текста
    text = FileReader.read_file_into_string(file_path)
    textData = TextData(text, os.path.basename(file_path))

    print(textData)