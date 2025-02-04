
class User:
    def __init__(self, id: int, name: str, username: str, phone_number: str):
        self.id = id
        self.name = name
        self.username = username
        self.phone_number = phone_number

    
    def __str__(self):
        return f'User {self.username} (ID: {self.id})'
    
    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, username={self.username}, phone_number={self.phone_number})"
