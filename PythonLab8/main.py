#Функція що виводить контент словнику в консоль
def d_print(d):
    print("\nПовний список студентів:")
    for n, v in d.items():
        print(n, v)
    print("")

#Функція, що додає нову особу, або змінює дані уже існуючої
def d_add(d):
    name = input("Введіть ім'я у форматі 'ім'я прізвище по батькові': ")

    if name in d:
        print("Ця особа вже є в списку: ")
        if input("Змінити дані? Так / Ні : ").lower() == "ні":
            return None

    #Заповнення групи та курсу для нової особи у вхідному словнику
    d[name] = {
        "група": input("Введіть групу студента: "),
        "курс": input("Введіть курс студента: "),
    }

    #Створення словнику оцінок з предметів
    grades = {}
    while True:
        #На кожній ітерації алгоритм запитує користувача чи бажає він ввести ще один предмет
        c = input("Додати предмет? Так / Ні : ").lower()
        if c == "так":
            subject = input("Введіть назву предмета: ")
            grades[subject] = float(input("Введіть оцінку: "))
        elif c == "ні":
            break
        else:
            print("Невідома команда.")

    #Додоання оцінок особи до словнику
    d[name]["оцінки"] = grades


#Початковий список студентів
students = {
    "Чекмарьов Андрій Михайлович": {
        "група": "КН31",
        "курс": 2,
        "оцінки": {
            "Пайтон": 5.0,
            "Чисельні методи": 4.0,
            "ММДО": 4.5,
            "АТСД": 5.0,
            "Організація IT-бізнесу": 4.4
        }
    },
    "Ліцман Данііл Володимирович": {
        "група": "КН31",
        "курс": 2,
        "оцінки": {
            "Пайтон": 4.0,
            "Чисельні методи": 4.7,
            "ММДО": 4.8,
            "АТСД": 5.0,
            "Організація IT-бізнесу": 4.5
        }
    },
    "Майборода Єгор Андрійович": {
        "група": "КН31",
        "курс": 2,
        "оцінки": {
            "Пайтон": 4.8,
            "Чисельні методи": 5,
            "ММДО": 4.2,
            "АТСД": 4.7,
            "Організація IT-бізнесу": 4.8
        }
    }
}

#Цикл у якому відбувається діалог з користувачем
while True:
    #Запит команди в користувача
    print("\n'команди' - вивести список команд.")
    c = input("Введіть команду: ").lower()

    #Обробка команди
    match c:
        case "команди": #Вивід списку всіх команд
            print("'вивід' - вивести інформації.",
                  "\n'додати' - додати нового студента, або змінити дані всже існуючого",
                  "\n'вихід' - закінчити роботу.")
        case "вихід":
            break
        case "вивід":
            d_print(students)
        case "додати":
            d_add(students)
        case _:
            print("Невідома команда.")

