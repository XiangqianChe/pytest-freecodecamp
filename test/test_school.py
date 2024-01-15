import pytest
from source.school import Classroom, Teacher, Student, TooManyStudentsError


@pytest.fixture
def sample_classroom():
    teacher = Teacher("Professor McGonagall")
    students = [Student(f"Student{i}") for i in range(9)]
    return Classroom(teacher, students, "Transfiguration")


def test_add_student(sample_classroom):
    new_student = Student("Neville Longbottom")
    sample_classroom.add_student(new_student)
    assert new_student in sample_classroom.students


def test_add_student_raises_error(sample_classroom):
    with pytest.raises(TooManyStudentsError):
        for i in range(5):
            sample_classroom.add_student(Student(f"Student{i + 9}"))


def test_remove_student(sample_classroom):
    student_to_remove = sample_classroom.students[0]
    sample_classroom.remove_student(student_to_remove.name)
    assert student_to_remove not in sample_classroom.students


def test_change_teacher(sample_classroom):
    new_teacher = Teacher("Professor Snape")
    sample_classroom.change_teacher(new_teacher)
    assert sample_classroom.teacher == new_teacher


@pytest.mark.parametrize("student_name", ["Harry Potter", "Hermione Granger", "Ron Weasley"])
def test_add_named_students(sample_classroom, student_name):
    new_student = Student(student_name)
    sample_classroom.add_student(new_student)
    assert new_student in sample_classroom.students
