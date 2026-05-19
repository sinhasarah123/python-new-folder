import numpy as np
datatype=[('name', 'S15'), ('class', int), ('height', float)]
studentinformation=[('larry', 9, 1.75), ('barry', 6, 1.80), ('garry', 7, 1.65)]
students=np.array(studentinformation, dtype=datatype)
print("originalarray:")
print(students)
print("sortedbyheight:")
print(np.sort(students,order='height'))