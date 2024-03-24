from myproject import app,db
from myproject.firstmeal import generatemeal, gender, cuisine, onClickGenerateMeal, feedbacklst
from flask import render_template, redirect, request, url_for, flash, abort, session

from flask_login import login_user,login_required,logout_user
from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm, FeedbackForm
from werkzeug.security import generate_password_hash, check_password_hash

meals = []
breakfastlstarg = []
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/exercise')
def exercise():
    return render_template('exercise.html')

@app.route('/menu')
def menu():
      
    uid = session['userid']
    user = User.query.filter_by(id=uid).first()
    age = int(user.age)
    height = int(user.height)
    weight = int(user.weight)
    exercise = float(user.exercise)
    usergender = gender()
    usercuisine = cuisine()
    hasCancer = 'N'
    hasDiabetes = 'N'
    if user.disease == 'diabetes':
        hasDiabetes = 'Y'
    if user.disease == 'cancer':
        hasCancer = 'Y'

    meals, breakfastlst = onClickGenerateMeal(uid,age,height,weight,usergender,exercise,hasCancer,hasDiabetes,usercuisine, breakfastlstarg)
    session['meals'] = meals
    session['breakfastlst'] = breakfastlst
    return render_template('menu.html', meals=meals)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'GET':
        form = FeedbackForm()
        meals = session['meals']
        return render_template('feedback.html', meals=meals, form=form)
    
    uid = session['userid']
    user = User.query.filter_by(id=uid).first()
    age = int(user.age)
    height = int(user.height)
    weight = int(user.weight)
    exercise = float(user.exercise)
    usergender = gender()
    usercuisine = cuisine()
    hasCancer = 'N'
    hasDiabetes = 'N'
    if user.disease == 'diabetes':
        hasDiabetes = 'Y'
    if user.disease == 'cancer':
        hasCancer = 'Y'
    # meals, breakfastlst = generatemeal(21,176,69,1.2,'M','Y','Y','gujarat')
    # session['meals'] = meals
    # session['breakfastlst'] = breakfastlst
    # return render_template('menu.html', meals=meals)
    breakfastlstargs = session['breakfastlst']
    meals, breakfastlst = feedbacklst(uid,age,height,weight,usergender,exercise,hasCancer,hasDiabetes,usercuisine, breakfastlstargs)
    session['meals'] = meals
    session['breakfastlst'] = breakfastlst
    return redirect(url_for('menu'))


@app.route('/logout')
@login_required
def logout():
    session.pop('breakfastlst',None)
    session.pop('meals',None)

    logout_user()
    flash('You logged out!')
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        # Grab the user from our User Models table
        user = User.query.filter_by(email=form.email.data).first()
        
        # Check that the user was supplied and the password is right
        # The verify_password method comes from the User object
        # https://stackoverflow.com/questions/2209755/python-operation-vs-is-not

        if  user is not None and user.check_password(form.password.data):
            #Log in the user
            session['userid'] = user.id
            login_user(user)
            flash('Logged in successfully.')

            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            next = request.args.get('next')

            # So let's now check if that next exists, otherwise we'll go to
            # the welcome page.
            if next == None or not next[0]=='/':
                next = url_for('home')

            return redirect(next)
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    disease=form.disease.data,
                    height=form.height.data,
                    age=form.age.data,
                    weight=form.weight.data,
                    blood=form.blood.data,
                    exercise=form.exercise.data,
                    plan_period=form.plan_period.data,
                    food_type=form.food_type.data,
                    diet_pref=form.diet_pref.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! Now you can login!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)