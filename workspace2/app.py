import numpy as np

# a = np.array([1, 2, 3, 4, 5])

# print(a.shape)
# print('Element extracted of index 2: ',a.shape)

# b= np.array([[1, 2, 3], [21, 22, 23]])
# print(b.shape)
# print('Extrative element of row 1 and column 2',b[1,2])

# print(b)

# print ('OKAY!!!')

# import numpy as np 

# a=np.array([1,2,3,4,5])

# #shape signfica formato
# print(a.shape)
# print('Element extracted of index 2:', a[2])

# b=np.array([[1,2,3],[11,22,33]])
# print(b.shape)
# print(f'Element extracted of index 1 and column 2: {b[1, 2]}')


# print(b)

# print ("Ok !!!")



# print('MARTES 13 DE MAYO')
# c=np.zeros((5,4))
# print('The matrix x is> ')
# print (c)import numpy as np

# a = np.array([1, 2, 3, 4, 5])

# print(a.shape)
# print('Element extracted of index 2: ',a.shape)

# b= np.array([[1, 2, 3], [21, 22, 23]])
# print(b.shape)
# print('Extrative element of row 1 and column 2',b[1,2])

# print(b)

# print ('OKAY!!!')

# import numpy as np 

# a=np.array([1,2,3,4,5])

# #shape signfica formato
# print(a.shape)
# print('Element extracted of index 2:', a[2])

# b=np.array([[1,2,3],[11,22,33]])
# print(b.shape)
# print(f'Element extracted of index 1 and column 2: {b[1, 2]}')


# print(b)

# print ("Ok !!!")



# print('MARTES 13 DE MAYO')
# c=np.zeros((5,4))
# print('The matrix x is> ')
# print (c)

# print("*******************************")
# d=np.ones((3,4))
# print('Matrix of values ones=')
# print(d)

# print("*******************************")
# e=np.full((3,4),8)
# print('Matrix of a unique value')
# print(e)

# print("*******************************")
# f=np.random.randint(1,11,size=(5,5))
# print(f)

# print("*******************************")
# print("MATRIZ FLOTANTE")
# g=np.random.random((5,5))
# print(g)

# print("*******************************")
# print("Submatrix ")
# h=np.eye(10)
# print(h)

# print("*******************************")
# f=np.random.randint(1,21,size=(3,4))
# print(f)

# print("*******************************")
# m=f[:2,:2]
# print(m)


# print("*******************************")
# print("----submatrix, extraer valores de la matrix---")
# n=np.random.randint(1,101, size=(7,5))
# print(n)

# print("*******************************")
# p=n[4:6,2:4]
# print(p)

# print("*******************************")
# # q=n[2:5,1:4]
# # print(q)
# # 0,0
# # 6,0
# # 6,4
# # 0,4

# h=n[[0,6,6,0,],[0,0,4,4]]
# print(h.ndim)   # Número de dimensiones
# print(h.shape)  # Tamaño de cada dimensión
# print(h.shape)
# print(h.ndim)  



# print("*******************************")
# p=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# print(p)
# b=np.array([0,2,0,1])
# a=np.arange(4)
# # print(a)
# print(np.arange(4),b)
# p[a,b]+=100
# print(p)

# print('******************************')
# a = np.array([0, 1, 2])  
# b = np.array([0, 1, 2])  
# p[a, b] += 200 
# print(p)

# print('***************************************')
# a=np.array([0,1,2])
# b=np.array([0,1,2])
# p = np.zeros((10, 10))  # or define it with your desired shape
# a, b = 2, 3  # Example indices
# p[a, b] += 200




# print('***********MIERCOLES 14************')
# p=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# print(p)
# filter=(p>5)
# print(filter)
# print(type(filter))
# print(filter.ndim)
# print(filter.shape)
# z=p[filter]
# print(type(z))
# print(z.shape)
# print(z.ndim)


# print(z)#COPIAR EL OTRO CODIGO


# # print('*********************************************')
# # # Crear una matriz de 1 a 100
# # matriz = np.arange(1, 101).reshape(10, 10)

# # # Filtrar los valores entre 40 y 60
# # valores_filtrados = matriz[(matriz >= 40) & (matriz <= 60)]

# # #Cambiar los valores que terminan en 0 a 0
# # valores_filtrados[valores_filtrados % 10 == 0] = 0print('***********MIERCOLES 14************')

# # print("Matriz original:")
# # print(matriz)
# # print("\nValores filtrados entre 40 y 60:")
# # print(valores_filtrados)


# # #Remplazar los valores a 0
# # for i in range(len(matriz)):
# #     for j in range(len(matriz[i]))
# #     if 40<=matriz[i][j]<=60:
# #         matriz[i][j]=0

# # print("Matriz con valores entre 40 y 60 convertidos en 0: ")
# # for fila in matriz:
# #     print(fila)

# print('*******************************')
# f = np.random.randint(1, 101, size=[7, 7])
# print(f)
# print('*************************************')

# filter1=(f>40)
# filter2=(f<60)
# print('filter1')
# print(filter1)
# print('***********************')

# print('filter2')
# print(filter2)
# print('**************************************')

# f[filter1 & filter2]=0
# print(f)
# print(f.shape)
# print(type(f))


# print('************************************')

# matriz = list(range(1, 101))


# for i in range(len(matriz)):
#     if matriz[i] % 10 == 0:
#         matriz[i] = 200

# impares = [num for num in matriz if num % 2 != 0]
# # impares= [num**2 for num in matriz if num % 2 != 0]

# # Mostrar los resultados en una sola línea
# print(impares)


# print('******ARREGLOS************')


# a = np.random.randint(1, 101, size=[2, 2])
# b = np.random.randint(1, 101, size=[2, 2])

# print('MATRIX A')
# print(a)
# print('MATRIX B')
# print(b)


# print('ADDING MATRICES')
# adding_matrices = np.add(a, b)
# print(adding_matrices)
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)


# aux1 = np.subtract(a, b)
# aux2 = np.multiply(a, b)
# aux3 = np.divide(a, b)

# print('Resultado de dividir a y b:')
# print(aux3)


# sqrt_a = np.sqrt(a)
# print('Raíz cuadrada de la matriz A:')
# print(sqrt_a)

# print('*******************************************')


# a = np.random.randint(1, 101, size=(2, 2))
# b = np.random.randint(1, 101, size=(2, 2))  
# c = np.dot(a, b)  
# print('Matriz resultante de la multiplicación de A y B:')
# print(c)
# print('Shape de la matriz resultante:')
# print(c.shape)
# print('Número de dimensiones de la matriz resultante:')
# print(c.ndim)


# print('*********Multiplicación De Matriz**************')
# #crear 2 matrices q no tienen q ser cuadradas y realizar la multiplicacion
# a = np.random.randint(1, 10, size=(3, 4))  
# b = np.random.randint(1, 10, size=(4, 2))

# print("Matriz a (3x4):")
# print(a)
# print("\nMatriz b (4x2):")
# print(b)

# # Multiplicación de matrices
# c = np.matmul(a, b)
# # Alternativamente: c = a @ b

# print("\nC de la multiplicación (3x2):")
# print(c)
# print('Matrix of a unique value')
# print(e)

# print("*******************************")
# f=np.random.randint(1,11,size=(5,5))
# print(f)

# print("*******************************")
# print("MATRIZ FLOTANTE")
# g=np.random.random((5,5))
# print(g)

# print("*******************************")
# print("Submatrix ")
# h=np.eye(10)
# print(h)

# print("*******************************")
# f=np.random.randint(1,21,size=(3,4))
# print(f)

# print("*******************************")
# m=f[:2,:2]
# print(m)


# print("*******************************")
# print("----submatrix, extraer valores de la matrix---")
# n=np.random.randint(1,101, size=(7,5))
# print(n)

# print("*******************************")
# p=n[4:6,2:4]
# print(p)

# print("*******************************")
# # q=n[2:5,1:4]
# # print(q)
# # 0,0
# # 6,0
# # 6,4
# # 0,4

# h=n[[0,6,6,0,],[0,0,4,4]]
# print(h.ndim)   # Número de dimensiones
# print(h.shape)  # Tamaño de cada dimensión
# print(h.shape)
# print(h.ndim)  



# print("*******************************")
# p=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# print(p)
# b=np.array([0,2,0,1])
# a=np.arange(4)
# # print(a)
# print(np.arange(4),b)
# p[a,b]+=100
# print(p)

# print('******************************')
# a = np.array([0, 1, 2])  
# b = np.array([0, 1, 2])  
# p[a, b] += 200 
# print(p)

# print('***************************************')
# a=np.array([0,1,2])
# b=np.array([0,1,2])
# p = np.zeros((10, 10))  # or define it with your desired shape
# a, b = 2, 3  # Example indices
# p[a, b] += 200




# print('***********MIERCOLES 14************')
# p=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# print(p)
# filter=(p>5)
# print(filter)
# print(type(filter))
# print(filter.ndim)
# print(filter.shape)
# z=p[filter]
# print(type(z))
# print(z.shape)
# print(z.ndim)


# print(z)#COPIAR EL OTRO CODIGO


# # print('*********************************************')
# # # Crear una matriz de 1 a 100
# # matriz = np.arange(1, 101).reshape(10, 10)

# # # Filtrar los valores entre 40 y 60
# # valores_filtrados = matriz[(matriz >= 40) & (matriz <= 60)]

# # #Cambiar los valores que terminan en 0 a 0
# # valores_filtrados[valores_filtrados % 10 == 0] = 0print('***********MIERCOLES 14************')

# # print("Matriz original:")
# # print(matriz)
# # print("\nValores filtrados entre 40 y 60:")
# # print(valores_filtrados)


# # #Remplazar los valores a 0
# # for i in range(len(matriz)):
# #     for j in range(len(matriz[i]))
# #     if 40<=matriz[i][j]<=60:
# #         matriz[i][j]=0

# # print("Matriz con valores entre 40 y 60 convertidos en 0: ")
# # for fila in matriz:
# #     print(fila)

# print('*******************************')
# f = np.random.randint(1, 101, size=[7, 7])
# print(f)
# print('*************************************')

# filter1=(f>40)
# filter2=(f<60)
# print('filter1')
# print(filter1)
# print('***********************')

# print('filter2')
# print(filter2)
# print('**************************************')

# f[filter1 & filter2]=0
# print(f)
# print(f.shape)
# print(type(f))


# print('************************************')

# matriz = list(range(1, 101))


# for i in range(len(matriz)):
#     if matriz[i] % 10 == 0:
#         matriz[i] = 200

# impares = [num for num in matriz if num % 2 != 0]
# # impares= [num**2 for num in matriz if num % 2 != 0]

# # Mostrar los resultados en una sola línea
# print(impares)


# print('******ARREGLOS************')


# a = np.random.randint(1, 101, size=[2, 2])
# b = np.random.randint(1, 101, size=[2, 2])

# print('MATRIX A')
# print(a)
# print('MATRIX B')
# print(b)


# print('ADDING MATRICES')
# adding_matrices = np.add(a, b)
# print(adding_matrices)
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)


# aux1 = np.subtract(a, b)
# aux2 = np.multiply(a, b)
# aux3 = np.divide(a, b)

# print('Resultado de dividir a y b:')
# print(aux3)


# sqrt_a = np.sqrt(a)
# print('Raíz cuadrada de la matriz A:')
# print(sqrt_a)

# print('*******************************************')


# a = np.random.randint(1, 101, size=(2, 2))
# b = np.random.randint(1, 101, size=(2, 2))  
# c = np.dot(a, b)  
# print('Matriz resultante de la multiplicación de A y B:')
# print(c)
# print('Shape de la matriz resultante:')
# print(c.shape)
# print('Número de dimensiones de la matriz resultante:')
# print(c.ndim)


# print('*********Multiplicación De Matriz**************')
# #crear 2 matrices q no tienen q ser cuadradas y realizar la multiplicacion
# a = np.random.randint(1, 10, size=(3, 4))  
# b = np.random.randint(1, 10, size=(4, 2))

# print("Matriz a (3x4):")
# print(a)
# print("\nMatriz b (4x2):")
# print(b)

# # Multiplicación de matrices
# c = np.matmul(a, b)
# # Alternativamente: c = a @ b

# print("\nC de la multiplicación (3x2):")
# print(c)




print('*********JUEVES 15**************')

# # a=np.array([[1,2],[3,4]])
# # b=np.array([[5,6],[7,8]])
# # print(a)
# # print(b)

# # w=np.array([9,10])
# # v=np.array([11,12])


# # tmp1=np.dot(w,v)
# # tmp2=w.dot(v)

# # print(tmp1)
# # print(tmp2)
# # print(type(tmp1))
# # print(type(tmp2))


# # print('****DOT PRODUCT BETWEEN A VECTOR AND MATRIX**')
# # tmp3=a.dot(v)
# # tmp4=np.dot(a,v)
# # print(type(tmp3))
# # print(tmp3.ndim)
# # print(tmp3.shape)


# # a=np.array([[1,2],[3,4]])

# # print(a)

# # #result=np.sum(a)
# # print('THE RESULT OF THE SUM THE WHOLE ELEMENTS INSIDE THE ,ATRIX IS: ', np.sum(a))



# print('***********************************************************')

# a = np.random.randint(1, 21, size=(15, 20))
# print(a)
# columns_sum=np.sum(a,axis=0)
# # #Número de filas
# # num_filas = a.shape[0]

# # # Calcular el promedio de cada columna
# # average_columns = columns_sum / num_filas

# # # Mostrar el promedio de cada columna

# print('sun each eements od the columns:', columns_sum)
# print(columns_sum.shape)
# import numpy as np
# print('The total elements of my columns sum is: ',len(columns_sum))
# print(columns_sum.ndim)
# print('The average of each column are:', np.sum(a,axis=0)/len(np.sum(a,axis=0)))



# #print('The average of each column are:', np.mean(a,axis=0))
# print('The average of each column are:', np.average(a,axis=0))


# print('TRANSPORT MATRIX')
# f=np.random.randint(1, 2, size=(4, 4))
# print(f)
# print(f.T)

# print('///////////////////////////////////////////')

# g=np.random.randint(1, 4, size=(6, 5))
# print(g)
# print(g.T)

# x=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# v=np.array([1,0,1])
# emptyMatrix=np.empty_like(x)


# # result = x + v
# # print("Matriz x:")
# # print(x)
# # print("Vector v:")
# # print(v)
# # print("Resultado de sumar el vector v a cada fila de x:")
# # print(result)
# import numpy as np

# print(x)
# print(v)
# print(x.shape)
# print('rows: ',x.shape[0])
# print('columns: ',x.shape[1])
# for i in range(x.shape[0]):
#     emptyMatrix[i,:]=x[1,:]+v
# print(emptyMatrix)

# vv = np.tile(v, (4, 1))
# print(vv)
# print(x+vv)


# print(x+v)

# hstack
# vstack






# Matriz x de tamaño 4x3
x = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12]])

# Vector v de tamaño 4
v = np.array([1, 0, 1, 2])

# Agregar una columna extra a x para que tenga el mismo número de columnas que v
x_new = np.hstack([x, v.reshape(-1, 1)])  # Ahora x tiene 4 columnas

# Agregar el vector v como una fila
x_new = np.vstack([x_new, v])  # Ahora x_new tiene 5 filas y 4 columnas

print(x_new)


