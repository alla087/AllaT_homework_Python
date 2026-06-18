from sqlalchemy import create_engine
from sqlalchemy.sql import text


class StudentTable:

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)
        self.scripts = {
		"select": text("select * from student"),

		"delete_by_id": text("DELETE student WHERE user_id = :id_to_delete"),
		"insert_new": text("INSERT INTO student(user_id, level, education_form, subject_id)"
                           " values (:new_user_id, :new_level, :new_education_form, :new_subject_id)"),
		"get_max_id": text("SELECT MAX(user_id) FROM student "),
		"select by id": text("SELECT * FROM student "
                         "WHERE user_id =:select_id AND")
      }
    def get_students(self):
        return self.db.execute(self.scripts["select"]).fetchall()
# вернет студента по ID (проверка удаления)
    def get_student_by_id(self, new_id):
        return self.db.execute(self.scripts["select by id"], select_id=new_id).fetchall()

# добавление студента
    def add_student_by_id(self,new_user_id, new_level, new_education_form, new_subject_id):
        self.db.execute(self.scripts["insert_new"],
                               new_user_id=new_user_id,
                               new_level=new_level,
                               new_education_form=new_education_form,
                               new_subject_id=new_subject_id
                               )

    def delete(self, id):
        self.db.execute(self.scripts["delete by id"], id_to_delete=id)