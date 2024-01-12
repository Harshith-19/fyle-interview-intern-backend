import json
from flask import request
from core.libs import assertions
from core.apis.authprincipal import AuthPrincipal
from core.models.teachers import Teacher
from core.models.principals import Principal
from core.models.students import Student
from functools import wraps


def accept_payload(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        incoming_payload = request.json
        return func(incoming_payload, *args, **kwargs)
    return wrapper


def authenticate_principal(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        p_str = request.headers.get('X-Principal')
        assertions.assert_auth(p_str is not None, 'principal not found')
        p_dict = json.loads(p_str)
        p = AuthPrincipal(
            user_id=p_dict['user_id'],
            student_id=p_dict.get('student_id'),
            teacher_id=p_dict.get('teacher_id'),
            principal_id=p_dict.get('principal_id')
        )

        if request.path.startswith('/student'):
            validation = Student.validate(p)
            assertions.assert_true(validation, 'Validation failed')
            assertions.assert_true(p.student_id is not None, 'requester should be a student')
        elif request.path.startswith('/teacher'):
            validation = Teacher.validate(p)
            assertions.assert_true(validation, 'Validation failed')
            assertions.assert_true(p.teacher_id is not None, 'requester should be a teacher')
        elif request.path.startswith('/principal'):
            validation = Principal.validate(p)
            assertions.assert_true(validation, 'Validation failed')
            assertions.assert_true(p.principal_id is not None, 'requester should be a principal')
        else:
            assertions.assert_found(None, 'No such api')

        return func(p, *args, **kwargs)
    return wrapper
