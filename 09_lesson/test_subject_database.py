result = db.get_subjects()
    assert len(result) > 0


def test_add_subject():
    result1 = db.get_subjects()
    name = "Зельеварение"
    new_id = 15
    db.create_subject(new_id, name)
    result2 = db.get_subjects()
    assert result2[-1]['subject_title'] == name
    assert len(result1)<len(result2)
    assert len(result1) < len(result2)
    db.delete_subject(name)


def test_update_subject():
    name = 'Защита от злых чар'
    db.update_subject(213, name)
    result = db.get_subjects()
    assert result[-1]['subject_id'] != new_id
    db.delete_subject(name)


def test_delete_subject():
    name="Предмет на  удаление"
    new_id= 124
    name = "Предмет на  удаление"
    new_id = 124
    db.create_subject(new_id, name)
    res1 = db.get_subjects()
    db.delete_subject(name)
    res2=db.get_subjects()
    assert len(res1)>len(res2)
    res2 = db.get_subjects()
    assert len(res1) > len(res2)
#