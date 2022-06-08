
import operations

import students
from students import student

from teachers import Teachers #teachers is the name of file, Teachers is name of the class

print (operations.add_numbers(3, 5))
print(operations.div_numbers(600, 20))
operations.mult_numbers(5, 10)

new_student= student('Holland', 'cycling', '2003' )
new_student.student_INFO()

new_teacher= Teachers('Mr. John', 'literature & poetry', '34345', '60,000')
print(new_teacher.get_TSC_no())
