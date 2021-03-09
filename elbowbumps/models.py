from __main__ import db

class UserData(db.Model):
    __tablename__ = 'user_data'

    ud_id = db.Column(db.Integer, primary_key=True)
    ud_forename = db.Column(db.String(50))
    ud_surname = db.Column(db.String(50))
    ud_birthyear = db.Column(db.Integer)
    ud_email = db.Column(db.String(50), unique=True)
    ud_phone = db.Column(db.String(13), unique=True)
    ud_password = db.Column(db.String(100))
    ud_gender = db.Column(db.Enum('M', 'F', 'NB', name='gender'))
    ud_twitter = db.Column(db.String(50), unique=False)

    def __init__(self, forename, surname, birthyear, email, phone, password, gender, twitter=''):
        self.ud_forename = forename
        self.ud_surname = surname
        self.ud_birthyear = birthyear
        self.ud_email = email
        self.ud_phone = phone
        self.ud_password = password
        self.ud_gender = gender
        self.ud_twitter = twitter
    
    def serialise(self):
        return {
            'id': self.user_id,
            'forename': self.ud_forename,
            'surname': self.ud_surname,
            'birthyear': self.ud_birthyear,
            'email': self.ud_email,
            'phone': self.ud_phone,
            'gender': self.ud_gender,
            'twitter': self.ud_twitter
        }

class UserInterestData(db.Model):
    __tablename__ = 'user_interest_data'

    uid_id = db.Column(db.Integer, primary_key=True)
    uid_ud_id = db.Column(db.Integer)
    uid_interest_type = db.Column(db.String(50))
    uid_interest_weight = db.Column(db.Float(10))
    uid_squared_weight = db.Column(db.Float(10))

    def __init__(self, ud_id, interest_type, interest_weight):
        self.uid_ud_id = ud_id
        self.uid_interest_type = interest_type
        self.uid_interest_weight = interest_weight
        self.uid_squared_weight = interest_weight * interest_weight


class TwitterData(db.Model):
    __tablename__ = 'twitter_data'

    #columns: user_id, twitter_username, category, category score
    td_id = db.Column(db.Integer, primary_key=True)
    td_ud_id = db.Column(db.Integer)
    td_twitter_name = db.Column(db.String(15))
    td_category = db.Column(db.String(20))
    td_category_score = db.Column(db.Float(10))

    def __init__(self, ud_id, twitter_name, category, category_score):
        self.td_ud_id = ud_id
        self.td_twitter_name = twitter_name
        self.td_category = category
        self.td_category_score = category_score



