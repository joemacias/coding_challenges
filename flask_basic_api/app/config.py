class Config:
    """
    This class define constants values in the app
    """
    DEBUG = True # Flag to active debug mode
    TOKEN_RATE = 1  # Number of tokens add per second
    BUCKET_CAPACITY = 2 # Maximum number of tokens in the bucket
    SECRET_KEY = 'your_secret_key_here'
    RATE_LIMIT_ENDPOINT = 'api.limited'