from geoapi import db

class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    unique_id = db.Column(
        db.String(8)
    )

    email = db.Column(
        db.String(150)
    )

    pw_hash = db.Column(
        db.String(255)
    )

    api_key = db.Column(
        db.String(500)
    )

    refresh_api_key = db.Column(
        db.String(500)
    )

    def commit_new_user(self):
        db.session.add(self)
        db.session.flush()
        db.session.commit()
