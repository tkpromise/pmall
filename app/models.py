import uuid
from datetime import datetime
from flask_login import UserMixin
from . import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ ='users'
    id = db.Column(db.Integer, primary_key=True)
    mebid = db.Column(db.Integer)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64))
    storedValue = db.Column(db.Integer)
    points = db.Column(db.Integer)
    coupons = db.Column(db.Integer)
    memberType = db.Column(db.String(32))
    pub_date = db.Column(db.DateTime)
    
    def __init__(self, mebid, username, password, points, coupons):
        self.mebid = mebid
        self.username = username
        self.password = password
        self.points = points
        self.coupons = coupons
        self.memberType = '3B VIP'
        self.storedValue = 0
        self.pub_date = datetime.now()

    def __repr__(self):
        return '<username %r>' % (self.username)

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(128), unique=True)
    price = db.Column(db.Integer(), default=128)
    pointsRequired = db.Column(db.Integer(), default = 1024)
    img = db.Column(db.String(128), nullable=True)
    
    def __init__(self, name, price, pointsRequired, img):
        self.id = str(uuid.uuid4())
        self.name = name
        self.price = price
        self.pointsRequired = pointsRequired
        self.img = img

    def __repr__(self):
        return '<name> %r>' % (self.name)

class Exchange(db.Model):
    __tablename__ = 'exchanges'
    id = db.Column(db.Integer, primary_key=True)
    itemid = db.Column(db.String(128))
    item = db.Column(db.String(128))
    guest = db.Column(db.String(128))
    phone = db.Column(db.String(129))
    address = db.Column(db.String(128))
    username = db.Column(db.String(128))

    def __init__(self, itemid, item, guest, phone, address, username):
        self.itemid = itemid
        self.item = item
        self.guest = guest
        self.phone = phone
        self.address = address
        self.username = username

    def __repr__(self):
        return '<item> %r>' % (self.item)
