import os
import importlib.util

class Engine:
    def __init__(self):
        self.mods = []
        self.load_mods()

    def load_mods(self):
        mods_dir = "mods"
        if not os.path.exists(mods_dir):
            os.makedirs(mods_dir)
        
        for mod_name in os.listdir(mods_dir):
            if mod_name.endswith(".py"):
                mod_path = os.path.join(mods_dir, mod_name)
                mod_name = mod_name[:-3]  # Убираем расширение .py
                spec = importlib.util.spec_from_file_location(mod_name, mod_path)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                self.mods.append(mod)
                print(f"Загружен мод: {mod_name}")
    
    def game_loop(self):
        # Игровой цикл...
        pass
