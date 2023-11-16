from main import User, get_data


def register():
    first_name = input('Enter your fist_name: ')
    last_name = input('Enter your last_name: ')
    brithday = input('Enter your brithday: ')
    email = input('Enter your email: ')
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    user = User(first_name, last_name, brithday, email, username, password)
    return user.append_to_json()


def login():
    username = input('Enter username: ')
    password = input('Enter password: ')

    users = get_data()

    for user in users:
        if user['username'] == username and user['password'] == password:
            return user['id']
        return 0