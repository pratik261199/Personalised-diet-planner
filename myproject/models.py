from myproject import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
# By inheriting the UserMixin we get access to a lot of built-in attributes
# which we will be able to call in our views!
# is_authenticated()
# is_active()
# is_anonymous()
# get_id()


# The user_loader decorator allows flask-login to load the current user
# and grab their id.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    # Create a table in the db
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), index=True)
    disease = db.Column(db.String(64), index=True)
    age = db.Column(db.String(64), index=True)
    height = db.Column(db.String(64), index=True)
    weight = db.Column(db.String(64), index=True)
    blood = db.Column(db.String(64), index=True)
    exercise= db.Column(db.String(64), index=True)
    diet_pref = db.Column(db.String(64), index=True)
    plan_period = db.Column(db.String(64), index=True)
    food_type = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, disease, age, height, weight, blood, exercise, diet_pref, plan_period, food_type, password):
        self.email = email
        self.username = username
        self.disease = disease
        self.age=age
        self.height = height
        self.weight=weight
        self.blood=blood
        self.exercise=exercise
        self.diet_pref=diet_pref
        self.plan_period=plan_period
        self.food_type=food_type
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        # https://stackoverflow.com/questions/23432478/flask-generate-password-hash-not-constant-output
        return check_password_hash(self.password_hash,password)

class Breakfast(db.Model):
    
    __tablename__ = 'Breakfast'
    
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.Text)
    Calories = db.Column(db.Float(10))
    Proteins = db.Column(db.Float(10))
    Carbohydrates = db.Column(db.Float(10))
    Fiber = db.Column(db.Float(10))
    Fats = db.Column(db.Float(10))
    Cholesterol = db.Column(db.Float(10))
    Sodium = db.Column(db.Float(10))
    Ingredients = db.Column(db.Text)
    Steps = db.Column(db.Integer)
    Time = db.Column(db.Integer)
    Servings = db.Column(db.Integer)
    AggregatedRating = db.Column(db.Integer) 
    ReviewCount = db.Column(db.Integer)
    soup = db.Column(db.Text)
  
class LunchDinner(db.Model):
    
    __tablename__ = 'LunchDinner'

    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.Text)
    Calories = db.Column(db.Float(10))
    Proteins = db.Column(db.Float(10))
    Carbohydrates = db.Column(db.Float(10))
    Fiber = db.Column(db.Float(10))
    Fats = db.Column(db.Float(10))
    Cholesterol = db.Column(db.Float(10))
    Sodium = db.Column(db.Float(10))
    Ingredients = db.Column(db.Text)
    Steps = db.Column(db.Integer)
    Time = db.Column(db.Integer)
    Servings = db.Column(db.Integer)
    AggregatedRating = db.Column(db.Integer) 
    ReviewCount = db.Column(db.Integer)
    soup = db.Column(db.Text)
