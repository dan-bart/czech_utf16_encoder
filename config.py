# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://danbart:Encoder1337@encoder-flask-db.c8f7bpdlpyw1.us-east-1.rds.amazonaws.com:3306/encoder_flask_db'
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = '1234'
