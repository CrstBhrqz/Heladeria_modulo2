from config.db_ice_cream_saloon import db

class Ingrediente(db.Model):
    __tablename__ = 'INGREDIENTES'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255))
    cantidad = db.Column(db.Float, nullable=False)
    unidad_medida = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Ingrediente {self.nombre}>'

class Producto(db.Model):
    __tablename__ = 'PRODUCTOS'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255))
    precio = db.Column(db.Float, nullable=False)
    ingredientes = db.relationship('Ingrediente', secondary='producto_ingrediente', backref='productos')

    def __repr__(self):
        return f'<Producto {self.nombre}>'
