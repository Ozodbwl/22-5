import json


def get_data():
    try:
        with open('user.json', 'r') as f:
            users: list = json.load(f)
            return users
    except (FileNotFoundError, json.JSONDecodeError):
        with open('user.json', 'w') as f:
            json.dump([], f, indent=4)
            return []


class User:
    def __init__(self, first_name, last_name, brithday, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.brithday = brithday
        self.email = email
        self.username = username
        self.password = password

    def append_to_json(self):
        users = get_data()
        if not self.user_exists():
            user = {
                'id': users[-1]['id'] + 1 if len(users) != 0 else 1,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'brithday': self.brithday,
                'email': self.email,
                'username': self.username,
                'password': self.password
            }
            users.append(user)
            with open('user.json', 'w') as f:
                json.dump(users, f, indent=4)
            print('Successfully registered')
        else:
            print('Username or email already exists!')

    def user_exists(self):
        users: list = get_data()
        for user in users:
            if user['username'] == self.username or user['email'] == self.email:
                return True
        return False