import json, csv, random, os

QUESTIONS_FILE = "questions.json"
RESULTS_FILE = "results.csv"
NUM_QUESTIONS = 20

def load_questions():
    with open(QUESTIONS_FILE, encoding='utf-8') as f:
        questions = json.load(f)
    random.shuffle(questions)
    return questions[:NUM_QUESTIONS]

def ask_user_info():
    first_name = input("Введіть ваше ім'я: ").strip()
    last_name = input("Введіть ваше прізвище: ").strip()
    group = input("Введіть вашу групу: ").strip()
    return first_name, last_name, group

def run_quiz(questions):
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nПитання {i}: {q['question']}")
        for idx, option in enumerate(q['options'], 1):
            print(f"{idx}. {option}")
        while True:
            try:
                answer = int(input("Ваш вибір (1-4): "))
                if 1 <= answer <= 4:
                    break
                else:
                    print("Введіть число від 1 до 4.")
            except ValueError:
                print("Введіть коректне число.")
        if q['options'][answer - 1] == q['answer']:
            score += 1
    return int((score / len(questions)) * 100)

def save_result(first_name, last_name, group, score):
    file_exists = os.path.exists(RESULTS_FILE)
    with open(RESULTS_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Ім'я", "Прізвище", "Група", "Оцінка"])
        writer.writerow([first_name, last_name, group, score])

def view_stats_by_name_or_group():
    search = input("Введіть ім’я і прізвище або групу для пошуку: ").strip().lower()
    found = False
    with open(RESULTS_FILE, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        print("\nРезультати пошуку:")
        for row in reader:
            if (row["Ім'я"].lower() + " " + row["Прізвище"].lower() == search) or (row["Група"].lower() == search):
                print(f"{row['Ім\'я']} {row['Прізвище']} ({row['Група']}): {row['Оцінка']} балів")
                found = True
    if not found:
        print("Нічого не знайдено.")

def view_top_n():
    try:
        n = int(input("Введіть кількість топ учасників для відображення: "))
    except ValueError:
        print("Некоректне число.")
        return
    with open(RESULTS_FILE, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        results = list(reader)
    sorted_results = sorted(results, key=lambda x: int(x['Оцінка']), reverse=True)
    print(f"\nТОП-{n} результатів:")
    for i, row in enumerate(sorted_results[:n], 1):
        print(f"{i}. {row['Ім\'я']} {row['Прізвище']} ({row['Група']}): {row['Оцінка']} балів")

def main():
    while True:
        print("\n=== МЕНЮ ===")
        print("1. Пройти тест")
        print("2. Переглянути статистику")
        print("3. Переглянути ТОП-N результатів")
        print("4. Вийти")

        choice = int(input("Ваш вибір: ").strip())
        match choice:
            case 1:
                first_name, last_name, group = ask_user_info()
                questions = load_questions()
                score = run_quiz(questions)
                print(f"\nВаш результат: {score} балів.")
                save_result(first_name, last_name, group, score)
            case 2:
                view_stats_by_name_or_group()
            case 3:
                view_top_n()
            case 4:
                break
            case _:
                print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()