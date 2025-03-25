import os
import hashlib

class AccountManager:
    def __init__(self):
        self.users_file = "account/users.txt"
        self.load_users()

    def load_users(self):
        """Загружаем пользователей из файла users.txt."""
        if not os.path.exists(self.users_file):
            os.makedirs(os.path.dirname(self.users_file), exist_ok=True)
            open(self.users_file, 'w').close()  # Создаем пустой файл если его нет
        self.users = {}
        with open(self.users_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                username, password_hash = line.strip().split(',')
                self.users[username] = password_hash

    def register(self, username, password):
        """Регистрируем нового пользователя с паролем."""
        if username in self.users:
            print("Пользователь уже существует!")
            return False
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        self.users[username] = password_hash
        with open(self.users_file, 'a') as file:
            file.write(f"{username},{password_hash}\n")
        print("Регистрация успешна!")
        return True

    def authenticate(self, username, password):
        """Проверяем, соответствует ли введенный пароль."""
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        return self.users.get(username) == password_hash
