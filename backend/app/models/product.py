from app import db;

#the class inherits as a database model
class Product(db.Model):
    #defines the name in the database table
    __tablename__: 'products'

    #creation of product table columns
    id_product = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_product = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Float, nullable=True)
    description = db.Column(db.Text, nullable=True)
    stock = db.Column(db.Integer, nullable=False)
    #id_category = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def __repr__(self):
        return f"<Product {self.name_product}>"