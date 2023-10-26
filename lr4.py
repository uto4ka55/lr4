class Record:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.number_type = self.type_of_number()

    def type_of_number(self):
        if self.number.startswith("+38044"):
            return "міський"
        else:
            return "мобільний"

    def __str__(self):
        return f"Ім'я: {self.name}, Номер: {self.number}, Тип: {self.number_type}"

class Phonebook:
    def __init__(self):
        self.records = []
        print(self.records)

    def add_record(self, name, number):
        record = Record(name, number)
        self.records.append(record)

    def delete_record(self, name):
        matching_records = [record for record in self.records if name in record.name]
        if matching_records:
            for record in matching_records:
                self.records.remove(record)
            print(f"Видалено {len(matching_records)} запис(ів) з '{name}' в імені.")
        else:
            print(f"Не знайдено жодних записів з '{name}' в імені.")

    def search_records(self, name_part):
        matching_records = [record for record in self.records if name_part in record.name]
        if matching_records:
            print(f"Знайдено {len(matching_records)} запис(ів) з '{name_part}' в імені:")
            for record in matching_records:
                print(record)
        else:
            print(f"Не знайдено жодних записів з '{name_part}' в імені.")

    def display_records(self):
        if self.records:
            print("Записи в телефонній книзі:")
            for record in self.records:
                print(record)
        else:
            print("Телефонна книга порожня.")

phonebook = Phonebook()
while True:
    print("\nМеню Телефонної книги:")
    print("1. Додати запис")
    print("2. видалити запис")
    print("3. Шукити запис")
    print("4. Показати всі записи")
    print("5. Вийти з програми")

    choice = input("Введіть номер дії, яку ви бажаєте зробити: ")

    if choice == "1":
        name = input("Введіть ім'я: ")
        number = input("Введіть номер: ")
        phonebook.add_record(name, number)
    elif choice == "2":
        name = input("Введіть частину імені для видалення: ")
        phonebook.delete_record(name)
    elif choice == "3":
        name_part = input("Введіть частину імені для пошуку: ")
        phonebook.search_records(name_part)
    elif choice == "4":
        phonebook.display_records()
    elif choice == "5":
        print("До побачення!")
        break
    else:
        print("Некоректний вибір.")