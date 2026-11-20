from shoppinglib.users import *


class App:

    def __init__(self):
        self.user = None

    def validate_login(self, login, password):
        self.user = user_exists(login)
        if self.user and get_user_password(login) == password:
            return True
        self.user = None
        return False

    def register(self):
        while True:
            login = input('Enter your username:\t')
            if user_exists(login):
                print(f'User {login} already exists')
                continue
            password = input('Enter your password:\t')
            self.user = create_user(login, password)
            break

    def get_login(self):
        while True:
            login = input('Digite o nome do Usuário:\t')
            password = input('Digite o password:\t')
            if self.validate_login(login, password):
                print(f'{self.user.username} logged in successfully!')
            print(f'Invalid username or password')

    def start(self):
        exit_app = False
        while not exit_app:
            if not self.user:
                response = input('Register: C\nLogin: L\nExit: S')
                if response.lower() == 'c':
                    self.register()
                elif response.lower() == 'l':
                    self.get_login()
                elif response.lower() == 's':
                    exit_app = True
                else:
                    print(f'You entered {response}; please choose an available option\n')
            else:
                response = input('Log out: D\nExit: S')
                if response.lower() == 'd':
                    self.user = None
                elif response.lower() == 's':
                    exit_app = True


app = App()
app.start()



