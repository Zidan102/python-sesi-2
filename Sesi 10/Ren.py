import numpy as np
from numpy.conftest import dtype

students = np.array([2,0,10, False],dtype=int)
print(students)

students2 = ["Daffa","Riki","Nadira","Lutfi",10,False]
students3 = students2
students3.append(True)
students3.append(100)
print(students3)