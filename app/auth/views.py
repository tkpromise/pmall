from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required

from . import auth
from . forms import LoginForm
from . memberloginjson import memberloginjson
from . getpersonmemberbymobile import getpersonmemberbymobile
from . getmemberpointsum import getmemberpointsum
from . querycouponslistbymebid import querycouponslistbymebid
from ..models import User
from .. import db

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login = memberloginjson(form.username.data, form.password.data)
        user  = User.query.filter_by(username=form.username.data).first()
        #if login and user == None:
        if login:
            if user == None:
                mebid = getpersonmemberbymobile(form.username.data)
                points = getmemberpointsum(mebid)
                coupons = querycouponslistbymebid(mebid)
                user = User(mebid=mebid, username=form.username.data, password=form.password.data, points=points, coupons=coupons)
                db.session.add(user)
                db.session.commit()
                login_user(user, form.remember_me.data)
                next = request.args.get('next')
                if next is None or not next.startswith('/'):
                    next = url_for('main.index')
                return redirect(next)
            else:
                mebid = getpersonmemberbymobile(form.username.data)
                user.points = getmemberpointsum(mebid)
                db.session.commit()
                login_user(user, form.remember_me.data)
                next = request.args.get('next')
                if next is None or not next.startswith('/'):
                    next = url_for('main.index')
                return redirect(next)

        flash('Invalid username or password')
    return render_template('auth/login.html', form=form) 

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
