from app.config.db_ice_cream_saloon import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(50), nullable= True)
    description = db.Column(db.Text, nullable= True)
    done = db.Column(db.Boolean, default=False, nullable=True)