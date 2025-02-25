from pymongo import MongoClient

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def find_by_username(username):
        # Connect to MongoDB server
        client = MongoClient('mongodb://localhost:27017/')
        
        # Select database
        db = client['itmowadhw2']
        
        # Select collection
        users_collection = db['users']
        
        # Find user by username in the "users" collection
        user_data = users_collection.find_one({'username': username})
        
        # If user is found, create User object and return it
        if user_data:
            return User(user_data['username'], user_data['password'])
        else:
            return None