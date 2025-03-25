from engine import Engine
from scenes import MenuScene
from objects import GameObject

def main():
    print("Запуск игры...")

    # Создаем движок и загружаем настройки из файла
    game = Engine()

    # Создаем сцену меню
    menu_scene = MenuScene(game)
    game.set_scene(menu_scene)

    # Добавляем несколько объектов на сцену
    player = GameObject(100, 100, 50, 50, (255, 0, 0))  # Красный квадрат
    game.objects.add(player)

    # Запускаем игровой цикл
    game.game_loop()

    game.quit()

if __name__ == "__main__":
    main()
