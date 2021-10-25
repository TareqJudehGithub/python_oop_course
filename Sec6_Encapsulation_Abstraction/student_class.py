class Student:
  
  id_generator = 1

  def __init__(self, name, age, gpa):
    self.student_id = Student.id_generator
    self.name = name
    self._age = age   # _age attribute is non-public
    self.gpa = gpa

    Student.id_generator += 1

  def __repr__(self):
    print("")
    return f"<Student(\nID: {self.student_id}\nName: {self.name}\nAge: \
{self._age}\nGPA: {self.gpa}\n)>"

  


student_nora = Student("Nora Nav", 15, 3.96)
student_sarah = Student("Sarah", 14, 6.85)

print(student_nora)
print(student_sarah)