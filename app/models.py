from . import db

#class to store the dataset values

class Dataset(db.Model):
    __tablename__ = 'dataset'
    id = db.Column(db.Integer,primary_key = True)
    amount = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=db.func.now())
    

    def __repr__(self):
        return f'Dataset {self.id}'





    