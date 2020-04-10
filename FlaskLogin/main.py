from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from simpleCalculator import simpleCalculator as calculatorfun
from . import db
from .models import History, User

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/calculator')
@login_required
def calculator():
    all_data = History.query.filter(History.email == current_user.email)
    return render_template('calculator.html', name=current_user.name, ALLhistory=all_data)


@main.route('/calculator', methods=['POST'])
def calc_post():
    calc = request.form.get('res')
    print(calc)
    first = calc.split('z')
    if (first[1] == '+'):
        res = calculatorfun.add(float(first[0]), float(first[2]))
        history = History(num1=float(first[0]), num2=float(first[2]), op=first[1], res=float(round(res, 5)),
                          email=current_user.email)


    elif (first[1] == '-'):
        res = calculatorfun.subtraction(float(first[0]), float(first[2]))
        history = History(num1=float(first[0]), num2=float(first[2]), op=first[1], res=float(round(res, 5)),
                          email=current_user.email)


    elif (first[1] == '/'):
        res = calculatorfun.divide(float(first[0]), float(first[2]))
        history = History(num1=float(first[0]), num2=float(first[2]), op=first[1], res=float(round(res, 5)),
                          email=current_user.email)


    elif (first[1] == '*'):
        res = calculatorfun.multiply(float(first[0]), float(first[2]))
        history = History(num1=float(first[0]), num2=float(first[2]), op=first[1], res=float(round(res, 5)),
                          email=current_user.email)


    elif (first[1] == '%'):
        res = float(float(first[0]) / 100)
        history = History(num1=float(first[0]), op=first[1], res=float(round(res, 5)), email=current_user.email)


    elif (first[1] == 'invSq'):
        res = float(1 / calculatorfun.square(float(first[0])))
        history = History(num1=float(first[0]), op=first[1], res=float(round(res, 5)), email=current_user.email)


    elif (first[1] == 'invSqrt'):
        res = float(1 / calculatorfun.squareRoot(float(first[0])))
        history = History(num1=float(first[0]), op=first[1], res=float(round(res, 5)), email=current_user.email)


    elif (first[1] == 'sq'):
        res = calculatorfun.square(float(first[0]))
        history = History(num1=float(first[0]), op=first[1], res=float(round(res, 5)), email=current_user.email)


    elif (first[1] == 'sqrt'):
        res = calculatorfun.squareRoot(float(first[0]))
        history = History(num1=float(first[0]), op=first[1], res=float(round(res, 5)), email=current_user.email)

    db.session.add(history)
    db.session.commit()

    all_data = History.query.filter(History.email == current_user.email)

    return render_template('calculator.html', result=res, result2=res, ALLhistory=all_data)


@main.route('/delete/<int:id>')
def delete(id):
    all_data = History.query.get(id)
    db.session.delete(all_data)
    db.session.commit()

    all_data = History.query.filter(History.email == current_user.email)

    return render_template('calculator.html', ALLhistory=all_data)

@main.route('/edit/<int:id>')
def edit(id):
    all_data = History.query.get(id)

    res = all_data.res
    all_data1 = History.query.filter(History.email == current_user.email)
    return render_template('calculator.html', result=res, result2=res, ALLhistory=all_data1)

@main.route('/clear')
def clearHistory():
    all_data = History.query.filter(History.email == current_user.email).delete()
    db.session.commit()

    all_data1 = History.query.filter(History.email == current_user.email)
    return render_template('calculator.html', ALLhistory=all_data1)


@main.route('/clearEntry/<res>')
def clearEntry(res):
    s1 = ''
    s2 = 'z'
    res1 = res.split('z')[:-1]
    res2=res.split('z')[:-1]
    s1 = s1.join(res1)
    s2 = s2.join(res2)+"z"
    all_data = History.query.filter(History.email == current_user.email)
    return render_template('calculator.html', result=s1, result2=s2, ALLhistory=all_data)
