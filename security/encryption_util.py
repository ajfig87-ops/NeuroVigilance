import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

class EncryptionUtil:
    def __init__(self):
        # Load key from .env file
        load_dotenv()
        key = os.getenv("FERNET_KEY")
        if key is None:
            raise ValueError("FERNET_KEY not found in environment variables.")
        self.fernet = Fernet(key.encode())
        self.key = key.encode()

    def encrypt(self, data: str) -> str:
        return self.fernet.encrypt(data.encode()).decode()

    def decrypt(self, token: str) -> str:
        return self.fernet.decrypt(token.encode()).decode()

    def get_key(self) -> str:
        return self.key.decode()
