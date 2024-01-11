from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment

from .schema import AssignmentSchema, AssignmentSubmitSchema
principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)


@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns list of assignments"""
    principals_assignments = Assignment.get_assignments_by_principal(p.principal_id)
    principals_assignments_dump = AssignmentSchema().dump(principals_assignments, many=True)
    return APIResponse.respond(data=principals_assignments_dump)