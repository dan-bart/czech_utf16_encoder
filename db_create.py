from czech_utf16_encoder import db
from czech_utf16_encoder.models import Data

try:   
    db.create_all()
    print("DB created.")
except Exception as e:
    print(e)