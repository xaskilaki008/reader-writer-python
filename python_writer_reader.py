import os

def read_text_files(directory, output_file):
    counter = 1
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    # Проверяем, является ли файл текстовым
                    if file.endswith(('.txt', '.csv', '.json', '.xml', '.html', 
                                    '.log', '.py', '.js', '.php', '.c', '.cpp', '.java', 
                                    '.go', '.rb', '.sh', '.ts', '.kt', '.swift')):
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            content = infile.read()
                        
                            # Получаем расширение файла для подсветки синтаксиса
                            extension = os.path.splitext(file)[1][1:].lower()
                            lang = {
                                'py': 'python',
                                'js': 'javascript',
                                'ts': 'typescript',
                                'php': 'php',
                                'c': 'c',
                                'cpp': 'cpp',
                                'java': 'java',
                                'go': 'go',
                                'kt': 'kotlin',
                                'swift': 'swift',
                                'rb': 'ruby',
                                'sh': 'bash',
                                'md': 'markdown'
                            }.get(extension, extension)
                            
                            # Получаем относительный путь
                            rel_path = os.path.relpath(file_path, directory)
                            
                            # Форматируем вывод
                            outfile.write(f"### Листинг – {counter}. {file} \\{rel_path}\n\n")
                            outfile.write(f"```{lang}\n{content}\n```\n\n")
                            counter += 1
                            
                except UnicodeDecodeError:
                    continue
                except Exception as e:
                    print(f"Ошибка при обработке файла {file_path}: {e}")

input_directory = input("Введите путь к папке: ")
output_file = input("Введите имя выходного файла (например, output.md): ")

read_text_files(input_directory, output_file)
print(f"Готово! Результат сохранён в {output_file}")