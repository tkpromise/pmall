from datetime import date
from flask import render_template, session, redirect, url_for, request, flash
from flask_login import login_required

from .import main
from .coupon import getcoupon 
from .getpersonmemberbymobile import getpersonmemberbymobile
from .getmemberpointsum import getmemberpointsum
from .. import db
from ..models import User, Item, Exchange

@main.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)

@main.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)


@main.route('/create-item', methods=['GET', 'POST'])
@login_required
def create_item():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        pointsRequired = request.form.get('pointsRequired')
        img = request.form.get('img') 

        item = Item(name=name, price=price, pointsRequired=pointsRequired, img=img)
        db.session.add(item)
        db.session.commit()
    return render_template('create_item.html')
        
@main.route('/exchange', methods=['GET', 'POST'])
@login_required
def exchange():
    itemid = request.args.get('id')
    item = Item.query.filter(Item.id == itemid).first()

    if request.method == 'POST':
        item = request.form.get('item')
        guest = request.form.get('guest')
        phone = int(request.form.get('phone'))
        address = request.form.get('address')
        username = request.form.get('username')
        user = User.query.filter_by(username=username).first()
        itemname = Item.query.filter_by(name=item).first()
        if user.points > itemname.pointsRequired:
            user.points = user.points - itemname.pointsRequired
            
            exchange = Exchange(itemid=itemid, item=item, guest=guest, phone=phone, address=address, username=username)
            db.session.add(exchange)
            db.session.commit()
            flash('兑换成功')
            return redirect(url_for('main.index'))
        else:
            flash('积分不足')
            return redirect(url_for('main.exchange'))
    return render_template('exchange.html', item=item)

@main.route('/service')
@login_required
def service():
    exchanges = Exchange.query.all()
    return render_template('service.html', exchanges=exchanges)

@main.route('/query', methods=['GET', 'POST'])
def query():
    if request.method == 'POST':
        mobile = request.form.get('mobile')
        mebid = getpersonmemberbymobile(mobile)
        if mebid != False:
            point = getmemberpointsum(mebid)
            coupon=getcoupon(mebid)
            if coupon != False:
                return render_template('coupon.html', coupon=coupon, mobile=mobile, point=point)
            else:
                flash('未查询到此用户的优惠信息')
                return redirect(url_for('main.query'))
        else:
            flash('未查询到此用户的优惠信息')
            return redirect(url_for('main.query'))
    return render_template('query.html')


        

@main.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'

@main.route('/sky')
def sky():
    return render_template('skylee91.html')
