from core import db
from core.libs import helpers
from core.models.principals import Principal
from core.libs import assertions
from core.apis.authprincipal import AuthPrincipal


class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, db.Sequence('teachers_id_seq'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False)
    updated_at = db.Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False, onupdate=helpers.get_utc_now)

    def __repr__(self):
        return '<Teacher %r>' % self.id
    

    @classmethod
    def filter(cls, *criterion):
        db_query = db.session.query(cls)
        return db_query.filter(*criterion)
    

    @classmethod
    def get_by_id(cls, _id):
        return cls.filter(cls.id == _id).first()
    

    @classmethod
    def validate(cls, auth_principal : AuthPrincipal):
        teacher = cls.get_by_id(auth_principal.teacher_id)
        assertions.assert_found(teacher, 'No teacher with this id was found')
        return teacher.user_id == auth_principal.user_id
    

    @classmethod
    def get_teachers_by_principal(cls):
        return cls.filter().all()