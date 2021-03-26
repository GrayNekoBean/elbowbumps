from elbowbumps import db

class UserData(db.Model):
    __tablename__ = 'user_data'

    ud_id = db.Column(db.Integer, primary_key=True)
    ud_avatar = db.Column(db.String(50))
    ud_forename = db.Column(db.String(50))
    ud_surname = db.Column(db.String(50))
    ud_birthyear = db.Column(db.Integer)
    ud_email = db.Column(db.String(50), unique=True)
    ud_phone = db.Column(db.String(13), unique=True)
    ud_password = db.Column(db.String(100))
    ud_gender = db.Column(db.Enum('M', 'F', 'NB', name='gender'))
    ud_twitter = db.Column(db.String(50), unique=False)
    ud_id_twitter = db.Column(db.String(50), unique=False)

    def __init__(self, forename, surname, birthyear, email, phone, password, gender, twitter='', id_twitter='', avatar = ''):
        self.ud_forename = forename
        self.ud_surname = surname
        self.ud_birthyear = birthyear
        self.ud_email = email
        self.ud_phone = phone
        self.ud_password = password
        self.ud_gender = gender
        self.ud_twitter = twitter
        self.ud_id_twitter = id_twitter
        self.ud_avatar = avatar
    
    def serialise(self):
        return {
            'id': self.ud_id,
            'forename': self.ud_forename,
            'surname': self.ud_surname,
            'birthyear': self.ud_birthyear,
            'email': self.ud_email,
            'phone': self.ud_phone,
            'gender': self.ud_gender,
            'twitter': self.ud_twitter,
            'id_twitter': self.ud_id_twitter,
            'avatar': self.ud_avatar
        }

class UserInterestData(db.Model):
    __tablename__ = 'user_interest_data'

    uid_id = db.Column(db.Integer, primary_key=True)
    uid_ud_id = db.Column(db.Integer)
    uid_interest_type = db.Column(db.String(50))
    uid_twitter_score = db.Column(db.Float(10))
    uid_questionnaire_score =  db.Column(db.Float(10))
    uid_interest_weight = db.Column(db.Float(10))
    uid_squared_weight = db.Column(db.Float(10))

    def __init__(self, ud_id, interest_type, twitter_score, questionnaire_score):
        self.uid_ud_id = ud_id
        self.uid_twitter_score = twitter_score
        self.uid_questionnaire_score = questionnaire_score
        self.uid_interest_type = interest_type
        self.updateScores()
    
    def updateScores(self):
        if self.uid_questionnaire_score == 0:
            self.uid_interest_weight = self.uid_twitter_score
        elif self.uid_twitter_score == 0:
            self.uid_interest_weight = self.uid_questionnaire_score
        else:
            self.uid_interest_weight = (self.uid_twitter_score + self.uid_questionnaire_score)/2

        self.uid_squared_weight = float(self.uid_interest_weight) * float(self.uid_interest_weight)

        sw = SquaredWeights.query.filter_by(uid_ud_id=self.uid_ud_id).first()

        if sw:
            with db.engine.connect() as con:
                new_weight = con.execute(f'select sum(uid_interest_weight * uid_interest_weight) from user_interest_data uid where uid_ud_id = {self.uid_ud_id};')
                sw.sum = new_weight.first().sum
                db.session.commit()

        else:
            with db.engine.connect() as con:
                weight = con.execute(f'select sum(uid_interest_weight * uid_interest_weight) from user_interest_data uid where uid_ud_id = {self.uid_ud_id};').first().sum
                sw = SquaredWeights(self.uid_ud_id, weight)
                db.session.add(sw)
                db.session.commit()

class UserMatch(db.Model):
    __tablename__ = 'user_match'
    
    um_id = db.Column(db.Integer, primary_key=True)
    um_ud_id_1 = db.Column(db.Integer)
    um_ud_id_2 = db.Column(db.Integer)
    um_1_matched = db.Column(db.Boolean)
    um_2_matched = db.Column(db.Boolean)
    
    def __init__(self, id_1, id_2):
        self.um_ud_id_1 = id_1
        self.um_ud_id_2 = id_2
        self.um_1_matched = False
        self.um_2_matched = False
    

class SquaredWeights(db.Model):
    __tablename__ = 'squared_weights'

    uid_ud_id = db.Column(db.Integer, primary_key=True)
    sum = db.Column(db.Integer)

    def __init__(self, ud_id, weight):
        self.uid_ud_id = ud_id
        self.sum = weight
