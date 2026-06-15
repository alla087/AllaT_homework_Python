from StudentTable import StudentTable

db = StudentTable("postgresql://postgres:123@localhost:5432/QA")

# напишем автотест на добавление
def test_add_new():
   list=db.get_students()
   assert len(list)>=1

# изменение
#создаем студента с исходными данными
def test_update_student_data():
    student_id = db.add_student(name="Иван")
#изменяем данные студента
    new_name = "Игорь"
    db.update_student(student_id, name=new_name)
#получаем данные из БД и проверяем, что они изменились
    updated_student = db.get_student_by_id(student_id)
    assert updated_student["name"] == new_name

#удаление
def def test_delete_student():
#создаем студента с исходными данными
    student_id = db.add_student(name="Иван")
#убеждаемся, что студент успешно создался и база не пуста
    assert db.get_student_by_id(student_id) is not None
#Удаляем созданного студента
    db.delete_student(student_id)



