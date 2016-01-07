import time

from modern_paste import db


class Paste(db.Model):
    __tablename__ = 'paste'

    paste_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_active = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, default=None, index=True)
    post_time = db.Column(db.Integer)
    expiry_time = db.Column(db.Integer, default=None)
    title = db.Column(db.Text, default=None)
    language = db.Column(db.Text)
    password_hash = db.Column(db.Text, default=None)
    contents = db.Column(db.Text)

    def __init__(
        self,
        user_id,
        password_hash,
        contents,
        expiry_time,
        title,
        language,
    ):
        self.is_active = True
        self.user_id = user_id
        self.post_time = int(time.time())
        self.expiry_time = expiry_time
        self.title = title
        self.language = language
        self.password_hash = password_hash
        self.contents = contents

    def as_dict(self):
        """
        Represent this paste as an easily JSON-serializable dictionary

        :return: Dictionary of paste properties
        """
        return {
            'is_active': self.is_active,
            'user_id': self.user_id,
            'post_time': self.post_time,
            'expiry_time': self.expiry_time,
            'contents': self.contents,
            'title': self.title,
            'language': self.language,
        }