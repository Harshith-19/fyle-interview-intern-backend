from core import db
from core.libs import helpers, assertions
from core.apis.authprincipal import AuthPrincipal


class Principal(db.Model):
    __tablename__ = 'principals'
    id = db.Column(db.Integer, db.Sequence('principals_id_seq'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False)
    updated_at = db.Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False, onupdate=helpers.get_utc_now)

    def __repr__(self):
        return '<Principal %r>' % self.id
    
    @classmethod
    def filter(cls, *criterion):
        db_query = db.session.query(cls)
        return db_query.filter(*criterion)

    @classmethod
    def get_by_id(cls, _id):
        return cls.filter(cls.id == _id).first()
    

    @classmethod
    def validate(cls, auth_principal : AuthPrincipal):
        principal = cls.get_by_id(auth_principal.principal_id)
        assertions.assert_found(principal, 'No principal with this id was found')
        return principal.user_id == auth_principal.user_id
