# Початковий словник із 10 країн
# Ключ: назва країни, Значення: внутрішній словник із характеристиками
countries_db = {
    "Україна": {"частина_світу": "Європа", "площа": 603628, "населення": 41.1},
    "Єгипет": {"частина_світу": "Африка", "площа": 1002450, "населення": 109.3},
    "Японія": {"частина_світу": "Азія", "площа": 377975, "населення": 125.1},
    "Канада": {"частина_світу": "Північна Америка", "площа": 9984670, "населення": 38.9},
    "Бразилія": {"частина_світу": "Південна Америка", "площа": 8515767, "населення": 214.3},
    "Нігерія": {"частина_світу": "Африка", "площа": 923768, "населення": 218.5},
    "Франція": {"частина_світу": "Європа", "площа": 551695, "населення": 67.8},
    "Індія": {"частина_світу": "Азія", "площа": 3287263, "населення": 1408.0},
    "Австралія": {"частина_світу": "Австралія та Океанія", "площа": 7692024, "населення": 25.7},
    "Кенія": {"частина_світу": "Африка", "площа": 580367, "населення": 54.0}
}


def print_country_info(name, info):
    """Допоміжна функція для гарного виведення одного запису."""
    print(f"Країна: {name:<12} | Частина світу: {info['частина_світу']:<20} | "
          f"Площа: {info['площа']:>10} км² | Населення: {info['населення']:>6.1f} млн")


def display_all(data):
    """1. Виведення на екран усіх значень словника."""
    if not data:
        print("\nСловник наразі порожній.")
        return

    print("\n" + "=" * 70)
    print("СПИСОК УСІХ КРАЇН У БАЗІ ДАНИХ:")
    print("=" * 70)
    for country, details in data.items():
        print_country_info(country, details)
    print("=" * 70)


def add_record(data):
    """2. Додавання нового запису з валідацією числових полів."""
    print("\n--- Додавання нової країни ---")
    name = input("Введіть назву країни: ").strip().capitalize()

    if not name:
        print("Помилка: назва країни не може бути порожньою!")
        return

    if name in data:
        print(f"Запис про країну '{name}' вже існує. Оновлення даних скасовано.")
        return

    region = input("Введіть частину світу (Європа, Азія, Африка тощо): ").strip().capitalize()

    # Обробка винятків при введенні площі
    try:
        area = int(input("Введіть площу (ціле число, км²): "))
        if area <= 0:
            raise ValueError("Площа повинна бути додатною.")
    except ValueError as e:
        print(f"Помилка введення площі: {e}. Запис не додано.")
        return

    # Обробка винятків при введенні населення
    try:
        population = float(input("Введіть населення (дійсне число, млн чол.): "))
        if population <= 0:
            raise ValueError("Населення повинно бути додатним.")
    except ValueError as e:
        print(f"Помилка введення населення: {e}. Запис не додано.")
        return

    data[name] = {
        "частина_світу": region,
        "площа": area,
        "населення": population
    }
    print(f"Країну '{name}' успішно додано до словника!")


def delete_record(data):
    """3. Видалення запису за ключем з перехопленням KeyError."""
    print("\n--- Видалення країни ---")
    name = input("Введіть назву країни для видалення: ").strip().capitalize()

    try:
        del data[name]
        print(f"Країну '{name}' успішно видалено.")
    except KeyError:
        print(f"Помилка: Країну з назвою '{name}' не знайдено в словнику.")


def display_sorted(data):
    """4. Перегляд вмісту словника за відсортованими ключами."""
    if not data:
        print("\nСловник порожній.")
        return

    # Створюємо список відсортованих ключів за допомогою sorted()
    sorted_keys = sorted(data.keys())

    print("\n" + "=" * 70)
    print("КРАЇНИ В АЛФАВІТНОМУ ПОРЯДКУ:")
    print("=" * 70)
    for country in sorted_keys:
        print_country_info(country, data[country])
    print("=" * 70)


def find_africa_and_asia_countries(data):
    """5. Завдання: пошук країн, розташованих в Африці або Азії."""
    target_regions = {"африка", "азія"}
    matched_countries = []

    for country, details in data.items():
        if details.get("частина_світу", "").lower() in target_regions:
            matched_countries.append((country, details["частина_світу"]))

    print("\n" + "=" * 70)
    print("РЕЗУЛЬТАТ ПОШУКУ (Країни Африки та Азії):")
    print("=" * 70)
    if matched_countries:
        print(f"Знайдено країн: {len(matched_countries)}\n")
        for country, region in matched_countries:
            print(f" - {country} ({region})")
    else:
        print("Країн, що розміщені в Африці або Азії, не знайдено.")
    print("=" * 70)


def main():
    """Головне меню програми (діалог з користувачем)."""
    while True:
        print("\n" + "#" * 40)
        print("          ГОЛОВНЕ МЕНЮ")
        print("#" * 40)
        print("1. Показати всі країни")
        print("2. Додати нову країну")
        print("3. Видалити країну")
        print("4. Показати країни за алфавітом (сортування ключів)")
        print("5. Знайти країни в Африці або Азії")
        print("0. Вийти з програми")
        print("#" * 40)

        choice = input("Оберіть пункт меню (0-5): ").strip()

        if choice == "1":
            display_all(countries_db)
        elif choice == "2":
            add_record(countries_db)
        elif choice == "3":
            delete_record(countries_db)
        elif choice == "4":
            display_sorted(countries_db)
        elif choice == "5":
            find_africa_and_asia_countries(countries_db)
        elif choice == "0":
            print("\nРоботу програми завершено. До побачення!")
            break
        else:
            print("\nНевірний вибір! Введіть цифру від 0 до 5.")


if __name__ == "__main__":
    main()