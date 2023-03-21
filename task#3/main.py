import os


def reads_text():
    """Функция парсит список файлов в словарь, где ключ это количество строк файла"""
    current = os.getcwd()
    folder = 'sorted'
    files = os.listdir(folder)
    text = {}

    for file in files:
        full_path = os.path.join(current, folder, file)
        with open(full_path, encoding='utf-8') as f:
            lines = f.readlines()
            count_lines = str(len(lines))
            text[count_lines] = [file] + ['\n'] + [count_lines] + ['\n'] + lines

    return text


def writes_text():
    """Функция записывает в файл 'final_text.txt' текст, отсортированный по количеству строк"""
    text = reads_text()
    sort_count_lines = sorted(list(text.keys()))

    f = open('final_text.txt', 'w')
    f.close()

    for count in sort_count_lines:
        with open('final_text.txt', 'a', encoding='utf-8') as f:
            f.writelines(text[count])


writes_text()