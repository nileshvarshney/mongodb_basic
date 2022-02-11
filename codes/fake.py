from faker import Faker

def get_student_dake_data(no_of_records, lang="en_US"):
    fake = Faker(lang)
    students = []
    for i in range(1,no_of_records +1):
        student_data = {}
        student_data['id'] = i
        student_data['name'] = fake.name()
        student_data['address']= fake.address()
        student_data['latitude']= str(fake.latitude())
        student_data['longitude']= str(fake.longitude())
        students.append(student_data)

    return students