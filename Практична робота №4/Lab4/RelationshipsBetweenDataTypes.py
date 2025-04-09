class Address:
    def __init__(self, street, city, state, postal_code, country):
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country

    def validate(self):
        return all([self.street, self.city, self.state, self.postal_code, self.country])

    def output_as_label(self):
        return f"{self.street}, {self.city}, {self.state}, {self.postal_code}, {self.country}"


class Person:
    def __init__(self, name, phone_number, email_address, address=None):
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address
        self.address = address

    def purchase_parking_pass(self):
        print(f"{self.name} has purchased a parking pass.")

    def __str__(self):
        address_info = self.address.output_as_label() if self.address else "No address"
        return f"Name: {self.name}\nPhone: {self.phone_number}\nEmail: {self.email_address}\nAddress: {address_info}"


class Student(Person):
    def __init__(self, name, phone_number, email_address, student_number, average_mark, address=None):
        super().__init__(name, phone_number, email_address, address)
        self.student_number = student_number
        self.average_mark = average_mark

    def is_eligible_to_enroll(self, course_name):
        return self.average_mark >= 50

    def get_seminars_taken(self):
        return 6

    def __str__(self):
        return super().__str__() + f"\nStudent Number: {self.student_number}\nAverage Mark: {self.average_mark}"


class Professor(Person):
    def __init__(self, name, phone_number, email_address, staff_number, years_of_service, number_of_classes, address=None):
        super().__init__(name, phone_number, email_address, address)
        self._staff_number = staff_number
        self._years_of_service = years_of_service
        self.number_of_classes = number_of_classes
        self.supervised_students = []

    @property
    def salary(self):
        return 50000 + self._years_of_service * 2000

    def supervise(self, student):
        if len(self.supervised_students) < 5:
            self.supervised_students.append(student)

    def __str__(self):
        students_info = "\n---\n".join(str(s) for s in self.supervised_students)
        return (super().__str__() +
                f"\nStaff Number: {self._staff_number}\nYears of Service: {self._years_of_service}\n"
                f"Number of Classes: {self.number_of_classes}\nSalary: {self.salary}\n\nSupervised Students:\n{students_info}")

addr_prof = Address("326 Main St", "Kyiv", "Kyivska", 18345, "Ukraine")
addr_sd1 = Address("24 Front St", "Kyiv", "Kyivska", 18567, "Ukraine")
addr_sd2 = Address("113 Back St", "Kyiv", "Kyivska", 18423, "Ukraine")
addr_sd3 = Address("58 Left St", "Kyiv", "Kyivska", 18496, "Ukraine")

# Створення професора
prof = Professor("Dr. Ivanenko", "0501234567", "ivanenko@example.com", 1001, 10, 3, addr_prof)

# Створення студентів
student1 = Student("Petro Petrenko", "0671112233", "petro@example.com", 2001, 85, addr_sd1)
student2 = Student("Olena Kostenko", "0634567890", "olena@example.com", 2002, 75, addr_sd2)
student3 = Student("Andriy Boyko", "0971234567", "andriy@example.com", 2003, 65, addr_sd3)

# Додаємо студентів під нагляд професора
prof.supervise(student1)
prof.supervise(student2)
prof.supervise(student3)

# Вивід інформації
print(prof)