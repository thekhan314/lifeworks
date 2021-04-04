from app import db

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entry = db.Column(db.String(120), index=True, unique=True)
    project = db.Column(db.String(120))
    notes = db.Column(db.String(1000))

    def __repr__(self):
        return '<Entry {}>'.format(self.entry)    
