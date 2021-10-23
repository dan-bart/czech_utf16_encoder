from czech_utf16_encoder import db

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entry = db.Column(db.String(256), index=True, unique=False)
    output = db.Column(db.String(256), index=True, unique=False)
    
    def __init__(self, entry, output):
        self.entry = entry
        self.output = output

    def __repr__(self):
        return '<Data %r %s>' % self.entry, self.output