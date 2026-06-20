from sqlalchemy import create_engine, inspect, text


class SubjectTable:
    __scripts = {
        'select':text("SELECT * FROM subject"),

        'insert_new': text(
            "INSERT INTO subject (subject_id, subject_title)"
            " VALUES(:new_id, :new_subject)"
        ),
        'update_subject': text(
            "UPDATE subject SET subject_id=:new_sub_id"
            " WHERE subject_title=:new_subject_title"
        ),
        'delete_by_subject_title': text(
            "DELETE FROM subject "
            "WHERE subject_title=:subject_to_delete")
        }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_subjects(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts['select'])
        subjects = result.fetchall()  # Получаем все строки
        conn.close()
        return subjects

    def create_subject(self, new_id, subject_name):
        conn = self.__db.connect()
        conn.execute(self.__scripts['insert_new'],{'new_id':new_id, 'new_subject':subject_name})
        conn.commit()
        conn.close()

    def update_subject(self, new_id, title):
        conn = self.__db.connect()
        conn.execute(self.__scripts['update_subject'], {'new_sub_id': new_id, 'new_subject_title': title})

        conn.commit()
        conn.close()

    def delete_subject(self, subject_name):
        conn = self.__db.connect()
        conn.execute(self.__scripts['delete_by_subject_title'],
                     {'subject_to_delete':subject_name})
        conn.commit()
        conn.close()
#