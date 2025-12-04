from enum import Enum
from datetime import datetime


class StudyField(Enum):
    MECHANICAL_ENGINEERING = "Mechanical Engineering"
    SOFTWARE_ENGINEERING = "Software Engineering"
    FOOD_TECHNOLOGY = "Food Technology"


class Student:
    def __init__(self, firstName, lastName, email):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.graduated = False

    def __str__(self):
        status = "Graduate" if self.graduated else "Enrolled"
        return f"{self.firstName} {self.lastName} ({self.email}) - {status}"


class Faculty:
    def __init__(self, name, abbreviation, field):
        self.name = name
        self.abbreviation = abbreviation
        self.field = field
        self.students = []

    def addStudent(self, student):
        self.students.append(student)
        print(f"✓ Added {student.firstName} to {self.name}")

    def graduateStudent(self, email):
        for student in self.students:
            if student.email == email:
                student.graduated = True
                print(f"✓ {student.firstName} graduated!")
                return
        print("✗ Student not found")

    def showEnrolled(self):
        print(f"\n--- Enrolled in {self.name} ---")
        for student in self.students:
            if not student.graduated:
                print(f"  {student}")

    def showGraduates(self):
        print(f"\n--- Graduates of {self.name} ---")
        for student in self.students:
            if student.graduated:
                print(f"  {student}")

    def hasStudent(self, email):
        for student in self.students:
            if student.email == email:
                return True
        return False


class University:
    def __init__(self, name):
        self.name = name
        self.faculties = []

    def createFaculty(self, name, abbr, field):
        faculty = Faculty(name, abbr, field)
        self.faculties.append(faculty)
        print(f"✓ Faculty {name} created")
        return faculty

    def findStudentFaculty(self, email):
        for faculty in self.faculties:
            if faculty.hasStudent(email):
                return faculty
        return None

    def showAllFaculties(self):
        print(f"\n=== All Faculties ===")
        for i, f in enumerate(self.faculties, 1):
            print(f"{i}. {f.name} ({f.abbreviation}) - {f.field.value}")

    def showFacultiesByField(self, field):
        print(f"\n--- Faculties in {field.value} ---")
        for faculty in self.faculties:
            if faculty.field == field:
                print(f"  {faculty.name}")

    def exportToFile(self, filename=None):
        """Экспортирует все данные в текстовый файл"""
        if filename is None:
            filename = f"TUM_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

        with open(filename, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write(f"TUM UNIVERSITY REPORT\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 60 + "\n\n")

            for faculty in self.faculties:
                f.write(f"\n{'=' * 60}\n")
                f.write(f"FACULTY: {faculty.name} ({faculty.abbreviation})\n")
                f.write(f"Field: {faculty.field.value}\n")
                f.write(f"{'=' * 60}\n")

                # Enrolled students
                enrolled = [s for s in faculty.students if not s.graduated]
                f.write(f"\nEnrolled Students ({len(enrolled)}):\n")
                f.write("-" * 60 + "\n")
                if enrolled:
                    for student in enrolled:
                        f.write(f"  • {student.firstName} {student.lastName}\n")
                        f.write(f"    Email: {student.email}\n")
                else:
                    f.write("  No enrolled students\n")

                # Graduates
                graduates = [s for s in faculty.students if s.graduated]
                f.write(f"\nGraduates ({len(graduates)}):\n")
                f.write("-" * 60 + "\n")
                if graduates:
                    for student in graduates:
                        f.write(f"  • {student.firstName} {student.lastName}\n")
                        f.write(f"    Email: {student.email}\n")
                else:
                    f.write("  No graduates yet\n")

                f.write("\n")

            # Summary
            f.write("\n" + "=" * 60 + "\n")
            f.write("SUMMARY\n")
            f.write("=" * 60 + "\n")
            f.write(f"Total Faculties: {len(self.faculties)}\n")

            total_students = sum(len(f.students) for f in self.faculties)
            total_enrolled = sum(len([s for s in f.students if not s.graduated]) for f in self.faculties)
            total_graduates = sum(len([s for s in f.students if s.graduated]) for f in self.faculties)

            f.write(f"Total Students: {total_students}\n")
            f.write(f"  - Enrolled: {total_enrolled}\n")
            f.write(f"  - Graduates: {total_graduates}\n")

        import os
        full_path = os.path.abspath(filename)
        print(f"\n✓ Report saved to: {full_path}")


def main():
    print("\n=== TUM STUDENT SYSTEM ===\n")

    tum = University("TUM")

    fcim = tum.createFaculty("FCIM", "FCIM", StudyField.SOFTWARE_ENGINEERING)
    fmei = tum.createFaculty("ME", "ME", StudyField.MECHANICAL_ENGINEERING)

    while True:
        print("\n" + "-" * 40)
        print("1. Add student")
        print("2. Graduate student")
        print("3. Show enrolled students")
        print("4. Show graduates")
        print("5. Check if student in faculty")
        print("6. Create faculty")
        print("7. Find student's faculty")
        print("8. Show all faculties")
        print("9. Show faculties by field")
        print("10. Export report to file")
        print("0. Exit")
        print("-" * 40)

        choice = input("Choice: ").strip()

        if choice == "1":
            tum.showAllFaculties()
            fac_num = int(input("Faculty number: ")) - 1
            firstName = input("First name: ")
            lastName = input("Last name: ")
            email = input("Email: ")

            student = Student(firstName, lastName, email)
            tum.faculties[fac_num].addStudent(student)

        elif choice == "2":
            tum.showAllFaculties()
            fac_num = int(input("Faculty number: ")) - 1
            email = input("Student email: ")
            tum.faculties[fac_num].graduateStudent(email)

        elif choice == "3":
            tum.showAllFaculties()
            fac_num = int(input("Faculty number: ")) - 1
            tum.faculties[fac_num].showEnrolled()

        elif choice == "4":
            tum.showAllFaculties()
            fac_num = int(input("Faculty number: ")) - 1
            tum.faculties[fac_num].showGraduates()

        elif choice == "5":
            tum.showAllFaculties()
            fac_num = int(input("Faculty number: ")) - 1
            email = input("Student email: ")
            if tum.faculties[fac_num].hasStudent(email):
                print("✓ YES, student is here")
            else:
                print("✗ NO, student not here")

        elif choice == "6":
            print("\nFields:")
            print("1. Mechanical Engineering")
            print("2. Software Engineering")
            print("3. Food Technology")

            name = input("Faculty name: ")
            abbr = input("Abbreviation: ")
            field_num = int(input("Field (1-3): "))

            fields = [StudyField.MECHANICAL_ENGINEERING,
                      StudyField.SOFTWARE_ENGINEERING,
                      StudyField.FOOD_TECHNOLOGY]
            tum.createFaculty(name, abbr, fields[field_num - 1])

        elif choice == "7":
            email = input("Student email: ")
            faculty = tum.findStudentFaculty(email)
            if faculty:
                print(f"✓ Student is in: {faculty.name}")
            else:
                print("✗ Student not found")

        elif choice == "8":
            tum.showAllFaculties()

        elif choice == "9":
            print("\n1. Mechanical Engineering")
            print("2. Software Engineering")
            print("3. Food Technology")
            field_num = int(input("Field (1-3): "))

            fields = [StudyField.MECHANICAL_ENGINEERING,
                      StudyField.SOFTWARE_ENGINEERING,
                      StudyField.FOOD_TECHNOLOGY]
            tum.showFacultiesByField(fields[field_num - 1])

        elif choice == "10":
            # Экспорт в файл
            custom = input("Enter filename (or press Enter for auto): ").strip()
            if custom:
                if not custom.endswith('.txt'):
                    custom += '.txt'
                tum.exportToFile(custom)
            else:
                tum.exportToFile()

        elif choice == "0":
            print("\nBye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()