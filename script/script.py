import os
import http.server
import socketserver
import importlib
import sys

# Добавляем путь к проекту в системный путь (чтобы Python мог найти модули)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Порт, на котором будет работать сервер
PORT = 8080

# Путь к директории, где хранится HTML файл
DIRECTORY = "script"

# Создаем обработчик для сервера
Handler = http.server.SimpleHTTPRequestHandler
Handler.directory = DIRECTORY

# Импортируем файлы движка и игры
def load_and_run_modules():
    """Загружаем и запускаем другие Python модули для управления игрой."""
    try:
        # Подключаем движок Cube2D
        engine = importlib.import_module("engine")  # Импортируем движок из файла engine.py
        print("Движок Cube2D загружен.")

        # Подключаем другие файлы, если они нужны
        # Например, game.py — для логики игры
        game = importlib.import_module("game")  # Импортируем игру из файла game.py
        print("Игра загружена.")

        # Если нужно, можно запустить дополнительные компоненты
        # engine.run() или game.start() — зависит от логики вашего проекта
        engine.run()  # Пример запуска движка, если у него есть функция run()

    except Exception as e:
        print(f"Ошибка при загрузке модулей: {e}")

def run(server_class=http.server.HTTPServer, handler_class=http.server.SimpleHTTPRequestHandler):
    """Запускаем сервер."""
    server_address = ("", PORT)
    httpd = server_class(server_address, handler_class)
    print(f"Запуск сервера на порту {PORT}...")
    httpd.serve_forever()

if __name__ == "__main__":
    # Загружаем и запускаем все модули перед запуском сервера
    load_and_run_modules()
    
    # Запускаем сервер для обслуживания HTML страницы
    run()
