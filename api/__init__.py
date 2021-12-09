from flask_restful import Api

from app import flaskAppInstance
from .Students import Students
from .StudentsBYID import StudentsById


restServer = Api(flaskAppInstance)


restServer.add_resource(Students,"/api/v1.0/students")

restServer.add_resource(StudentsById,"/api/v1.0/students/id/<string:studentId>/<string:student_name>/<string:email>")