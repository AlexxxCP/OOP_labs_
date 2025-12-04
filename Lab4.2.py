from datetime import datetime
from enum import Enum


class StudyField(Enum):
    # Направления обучения
    MECHANICAL_ENGINEERING = "MECHANICAL_ENGINEERING"
    SOFTWARE_ENGINEERING = "SOFTWARE_ENGINEERING"
    FOOD_TECHNOLOGY = "FOOD_TECHNOLOGY"
    URBANISM_ARCHITECTURE = "URBANISM_ARCHITECTURE"
    VETERINARY_MEDICINE = "VETERINARY_MEDICINE"


class Student:
    def __init__(self, firstName, lastName, email, enrollmentDate, dateOfBirth):
        # Информация о студенте
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.enrollmentDate = enrollmentDate
        self.dateOfBirth = dateOfBirth
        self.isGraduated = False

    def __str__(self):
        status = "Graduate" if self.isGraduated else "Student"  # Статус студента
        return f"{self.firstName} {self.lastName} ({self.email}) - {status}"


class Faculty:
    def __init__(self, name, abbreviation, studyField):
        # Информация о факультете
        self.name = name
        self.abbreviation = abbreviation
        self.students = []
        self.studyField = studyField

    def addStudent(self, student):
        # Добавление студента
        if student not in self.students:
            self.students.append(student)
            print(f"✓ Student {student.firstName} {student.lastName} added to {self.name}")
        else:
            print(f"✗ Student already enrolled in {self.name}")

    def graduateStudent(self, email):
        # Выпуск студента
        for student in self.students:
            if student.email == email:
                student.isGraduated = True
                print(f"✓ Student {student.firstName} {student.lastName} graduated from {self.name}")
                return
        print(f"✗ Student with email {email} not found")

    def displayEnrolledStudents(self):
        # Показать активных студентов
        enrolled = [s for s in self.students if not s.isGraduated]
        if enrolled:
            print(f"\n--- Active Students of {self.name} ({self.abbreviation}) ---")
            for s in enrolled:
                print(f"  • {s}")
        else:
            print(f"No active students in {self.name}")

    def displayGraduates(self):
        # Показать выпускников
        graduates = [s for s in self.students if s.isGraduated]
        if graduates:
            print(f"\n--- Graduates of {self.name} ({self.abbreviation}) ---")
            for s in graduates:
                print(f"  • {s}")
        else:
            print(f"No graduates in {self.name}")

    def belongsToFaculty(self, email):
        # Проверка принадлежности по email
        return any(student.email == email for student in self.students)

    def __str__(self):
        return f"{self.name} ({self.abbreviation}) - {self.studyField.value}"


class University:
    def __init__(self, name):
        # Университет содержит несколько факультетов
        self.name = name
        self.faculties = []

    def createFaculty(self, name, abbreviation, studyField):
        faculty = Faculty(name, abbreviation, studyField)
        self.faculties.append(faculty)
        print(f"✓ Faculty {name} created")
        return faculty

    def searchStudentFaculty(self, email):
        # Поиск факультета студента
        for faculty in self.faculties:
            if faculty.belongsToFaculty(email):
                return faculty
        return None

    def displayFaculties(self):
        # Показать все факультеты
        if self.faculties:
            print(f"\n=== Faculties of {self.name} ===")
            for i, f in enumerate(self.faculties, 1):
                print(f"{i}. {f}")
        else:
            print("No faculties created")

    def displayFacultiesByField(self, studyField):
        # Показать факультеты по направлению
        filtered = [f for f in self.faculties if f.studyField == studyField]
        if filtered:
            print(f"\n--- Faculties of field {studyField.value} ---")
            for f in filtered:
                print(f"  • {f}")
        else:
            print(f"No faculties in the field {studyField.value}")


def showMenu():
    # Главное меню
    print("\n" + "=" * 60)
    print("   STUDENT MANAGEMENT SYSTEM — TUM")
    print("=" * 60)
    print("\n--- FACULTY OPERATIONS ---")
    print("1. Create and enroll a student into a faculty")
    print("2. Graduate a student")
    print("3. Show active students of a faculty")
    print("4. Show graduates of a faculty")
    print("5. Check student-faculty membership")
    print("\n--- GENERAL OPERATIONS ---")
    print("6. Create new faculty")
    print("7. Find student's faculty by email")
    print("8. Show all faculties")
    print("9. Show faculties by field")
    print("0. Exit")
    print("=" * 60)


def main():
    # Создаем университет
    tum = University("Technical University of Moldova")

    # Создаем стартовые факультеты
    faf = tum.createFaculty("Faculty of Computers, Informatics and Microelectronics",
                            "FCIM", StudyField.SOFTWARE_ENGINEERING)
    fmei = tum.createFaculty("Faculty of Mechanical Engineering",
                             "FMEI", StudyField.MECHANICAL_ENGINEERING)

    print("\n✓ System initialized with 2 faculties")

    while True:
        showMenu()
        choice = input("\nChoose an operation: ").strip()

        if choice == "1":
            tum.displayFaculties()
            try:
                fac_num = int(input("\nFaculty number: ")) - 1
                if 0 <= fac_num < len(tum.faculties):
                    firstName = input("First name: ")
                    lastName = input("Last name: ")
                    email = input("Email: ")
                    student = Student(firstName, lastName, email, datetime.now(), datetime(2000, 1, 1))
                    tum.faculties[fac_num].addStudent(student)
                else:
                    print("✗ Invalid faculty number")
            except:
                print("✗ Input error")

        elif choice == "2":
            tum.displayFaculties()
            try:
                fac_num = int(input("\nFaculty number: ")) - 1
                if 0 <= fac_num < len(tum.faculties):
                    email = input("Student email: ")
                    tum.faculties[fac_num].graduateStudent(email)
                else:
                    print("✗ Invalid faculty number")
            except:
                print("✗ Input error")

        elif choice == "3":
            tum.displayFaculties()
            try:
                fac_num = int(input("\nFaculty number: ")) - 1
                if 0 <= fac_num < len(tum.faculties):
                    tum.faculties[fac_num].displayEnrolledStudents()
                else:
                    print("✗ Invalid faculty number")
            except:
                print("✗ Input error")

        elif choice == "4":
            tum.displayFaculties()
            try:
                fac_num = int(input("\nFaculty number: ")) - 1
                if 0 <= fac_num < len(tum.faculties):
                    tum.faculties[fac_num].displayGraduates()
                else:
                    print("✗ Invalid faculty number")
            except:
                print("✗ Input error")

        elif choice == "5":
            tum.displayFaculties()
            try:
                fac_num = int(input("\nFaculty number: ")) - 1
                if 0 <= fac_num < len(tum.faculties):
                    email = input("Student email: ")
                    if tum.faculties[fac_num].belongsToFaculty(email):
                        print(f"✓ Student belongs to {tum.faculties[fac_num].name}")
                    else:
                        print(f"✗ Student does NOT belong to {tum.faculties[fac_num].name}")
                else:
                    print("✗ Invalid faculty number")
            except:
                print("✗ Input error")

        elif choice == "6":
            print("\nAvailable study fields:")
            for i, field in enumerate(StudyField, 1):
