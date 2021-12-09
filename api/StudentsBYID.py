from flask_restful import Resource
import logging as logger

class StudentsById(Resource):


    def get(self,studentId,student_name,email):
        logger.debug("Inside get method of student by Student-ID ={} Student-Name ={} Student-Email ={} ".format(studentId,student_name,email))
        return {"message":"inside get method of student by id. Student-ID ={} Student-Name ={} Student-Email ={} ".format(studentId,student_name,email)},200

    def post(self,studentId,student_name,email):
        logger.debug("Inside post method of student by Student-ID ={} Student-Name ={} Student-Email ={} ".format(studentId,student_name,email))
        return {"message":"inside post method of student by id. Student-ID ={} Student-Name ={} Student-Email ={} ".format(studentId,student_name,email)},200
    

    def put(self,studentId,student_name,email):
        logger.debug("Inside put method of student by Student-ID ={} Student-Name ={} Student-Email ={} ".format(studentId,student_name,email))
        return {"message":"inside put method of student by id. Student-ID ={} Student-Name ={} Student-Email ={} ".format(studentId,student_name,email)},200
        

    def delete(self,studentId,student_name,email):
        logger.debug("Inside delete method of student by Student-ID ={} Student-Name ={} Student-Email ={} ".format(studentId,student_name,email))
        return {"message":"inside delete method of student by id. Student-ID ={} Student-Name ={} Student-Email ={} ".format(studentId,student_name,email)},200
        