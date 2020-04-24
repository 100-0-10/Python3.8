# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 15:23:28 2020

@author: USER
"""

'''
Numpy 라이브러리

Numpy란 Numerical Python의 약자로
대규모 다차원 배열과 행렬 연산에 필요한 다양한 함수를 제공한다.
데이터 분석할 때 사용되는 다른 라이브러리 pandas와 matplotblib의 기반이 된다
기본적으로 array라는 단위로 데이터를 관리하는데, 행렬 개념으로 생각하면 된다.

Numpy 특징: 일반 list에 비해 빠르고 메모리에 효율적이다.
선영대수와 관련된 다양한 기능을 제공하고,
for 문, while 문 같은 반복문 없이 데이터 배열에 대한 처리를 지원한다.

Numpy가 빠른 이유 : numpy는 메모리에 차례대로 생성/할당을 해준다
반면 기존의 List는 이 값(value)가 어디에 있는지 주소만 저장을 해놓고 그 주소를 알려준다.
그래서 List를 for 문을 돌리면 그 주소마다 하나하나씩 다 찾아가면서 연산을 해줘야 하는데,
numpy는 같은 곳에 몰려있기 때문에 연산이 더 빠르게 이루어진다.

'''

'''
Numpy 호출 : "import numpy as np" 로 numpy를 호출하는데
모두 np라는 별칭(alias)로 호출하지만 특별한 이유는 없다.

Numpy로 array 생성하는 방법: ex) test_array = np.array([1,3,5,7], float)
type(test_array[3])을 하면 4바이트씩 numpy.float64라는 값이 반환된다.
float32 같은 데이터 타입은 하나씩 모여서 메모리 블럭을 구성한다.
32bit(비트) = 4byte(바이트) 이다.(8bit가 1byte)

'''
import numpy as np
test_array = np.array([1,3,5,7], float)
type(test_array[3])

'''
vector 는 일차원의 행렬을 말하고 하나의 행에 열만 있는 것이다.
각 숫자는 value(요소)라고도 부른다.
shape 를 보는 코드 예시는 그림 상에 없지만 결과적으로( 4,) 의 결과를 보여줄 것이다.
'''
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
np.array(matrix, int).shape
# 결과 = (3, 4)


'''
tensor 는 매트릭스가 여러개 있는 것으로 3차원, 4차원, 5차원... 이 다 표현된다.
'''

tensor = [[[1,2,3,4],[5,6,7,8],[9,10,11,12]],
          [[1,2,3,4],[5,6,7,8],[9,10,11,12]],
          [[1,2,3,4],[5,6,7,8],[9,10,11,12]]]
np.array(tensor, int).shape
np.array(tensor, int).ndim  # number of dimension
np.array(tensor, int).size  # data의 개수

# Ndarray의 single element가 가지는 data type
# 각 element가 차지하는 memory의 크기가 결정됨
np.array([[1,2.6, 3.2], [4, 5.1, 6]], dtype = int)

np.array([[1,2.6, 3.2], [4, "5", 6]], dtype = np.float32)

# nbyte : ndarray object 의 메모리 크기 리턴


np.array( [[1, 2.6, 3.2], [4, "5", 6]], dtype = np.float32).nbytes
# 결과 : 24
np.array( [[1, 2.6, 3.2], [4, "5", 6]], dtype = np.float64).nbytes
# 결과 : 48
np.array( [[1, 2.6, 3.2], [4, "5", 6]], dtype = np.int8).nbytes
# 결과 : 6
'''
하나의 value 가 4바이트를 가지는
요소가 6개 있으니까, 이게 메모리에서 차지하는 건 총 24바이트가 된다.
그 다음 타입은 하나가 8바이트니까 48바이트를 차지한다.
'''

# Array의 shape의 크기를 변경함 (element)의 개수는 동일
t_matrix = [[1,2,3,4], [5,6,7,8]]
np.array(t_matrix).shape
# 결과 : (2, 4)
np.array(t_matrix).reshape(8,)
# 결과 : array([1, 2, 3, 4, 5, 6, 7, 8])
np.array(t_matrix).reshape(8,).shape
# 결과 : (8,)


# Array의 size만 같다면 다차원으로 자유로이 변형 가능
np.array(t_matrix).reshape(2, 4).shape
# 결과 : (2, 4)
np.array(t_matrix).reshape(-1, 2).shape
# 결과 : (4, 2)  => -1은 size 를 기반으로 row개수 산정한다
np.array(t_matrix).reshape(2,2,2)
''' 
결과 : 
array([[[1, 2],
        [3, 4]],

       [[5, 6],
        [7, 8]]])
'''
np.array(t_matrix).reshape(2,2,2).shape
# 결과 : (2, 2, 2)


########flatten
# 다차원 array를 1차원 array로 변환
t_matrix = [ [[1,2], [3,4]], [[1,2], [3,4]], [[1,2], [3,4]]]
np.array(t_matrix).flatten()
# 결과 : array([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4])



#######indexing
a = np.array( [[1,2.2,3], [4,5,6.3]], int)
print(a)

print(a[0,0])

print(a[0][0])

a[0, 0] = 7
print(a)

a[0][0] = 8
print(a)


########slicing
# list와 달리 행과 열 부분을 나눠서 slicing이 가능함
# matrix 부분 집합 추출할 때 유용

a = np.array([[1,2,3,4,5], [6,7,8,9,10]], int)

a[:, 1:]    # 전체 row의 1열 이상
a[1, 2:4]   # 1row의 2열~3열
a[1:3]      # 1row~로우전체


a = np.array([[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14]], int)
print(a)
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
'''
a[:, ::2]  #::2 => 첫번째 : = 시작점, 두번째 : = 끝점, '2' = step
'''
array([[ 0,  2,  4],
       [ 5,  7,  9],
       [10, 12, 14]])
'''

a[::2, ::2]
'''
array([[ 0,  2,  4],
       [10, 12, 14]])
'''


# array의 범위를 지정하여, 값의 list를 생성하는 명령어
np.arange(20)  # list의 range와 같은 역할, integer로 0부터 19까지 배열추출
'''
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19])
'''
np.arange(0, 1, 0.2)  # float 가능
'''
array([0. , 0.2, 0.4, 0.6, 0.8])
'''
np.arange(20).reshape(4, 5)
'''
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19]])
'''


np.zeros(shape = (5,2), dtype = np.int8) # 5 by 2 zero matrix 생성, int8
'''
array([[0, 0],
       [0, 0],
       [0, 0],
       [0, 0],
       [0, 0]], dtype=int8)
'''
np.ones(shape = (5, 2), dtype = np.int8) # 5 by 2 one matrix 생성, int8
'''
array([[1, 1],
       [1, 1],
       [1, 1],
       [1, 1],
       [1, 1]], dtype=int8)
'''
np.empty(shape = (3,2), dtype = np.int8)
'''
array([[1, 2],
       [3, 4],
       [5, 6]], dtype=int8)
'''

'''
empty는 주어진 shape대로 비어있는 것을 생성한다.
이런식으로 array를 만드는데 메모리를 어느정도 할당시켜준다.
그런데 메모리에 기존에 있었던 값을 보여준다

zeros나 ones는 0과 1로 메모리 할당값을 초기화 시켜주는데
empty는 초기화시키지 않고 기존에 메모리에 있는 찌꺼기 그대로 보여준다.
'''

# 기존 ndarray의 shape 크기만큼 1 or 0 empty array 반환
t_matrix = np.arange(15).reshape(3, 5)
np.ones_like(t_matrix)
'''
array([[1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
'''


t_matrix1 = np.arange(15).reshape(3, 5)
np.zeros_like(t_matrix1)
'''
array([[0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]])
'''
t_matrix2 = np.arange(15).reshape(3, 5)
np.empty_like(t_matrix2)
'''
array([[4128860, 6029375, 3801155, 4259932, 6357102],
       [7274595, 6553710, 3342433, 7077980, 6422633],
       [6815836, 7143540, 6029420, 6357104, 7536754]])
'''


# 단위 행렬(i 행렬)을 생성
# n => number of rows

np.identity(n = 3, dtype = np.int8)
'''
array([[1, 0, 0],
       [0, 1, 0],
       [0, 0, 1]], dtype=int8)
'''
np.identity(n = 5)
'''
array([[1., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0.],
       [0., 0., 1., 0., 0.],
       [0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 1.]])
'''

np.eye(N = 3, M = 4, dtype = np.int)
'''
array([[1, 0, 0, 0],
       [0, 1, 0, 0],
       [0, 0, 1, 0]])
'''
np.eye(4) # identity행렬과 같게 출력
'''
array([[1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.]])
'''
np.eye(3, 6, k = 3) # k => start index
'''
array([[0., 0., 0., 1., 0., 0.],
       [0., 0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 0., 1.]])
'''

t_matrix = np.arange(16).reshape(4, 4)
np.diag(t_matrix)  # 대각선 값만 빼내옴
'''
array([ 0,  5, 10, 15])
'''
np.diag(t_matrix, k = 1) # 1번째 위치에서 시작
'''
array([ 1,  6, 11])
'''

########Random Sampling
np.random.uniform(0,1,12).reshape(4, 3) # 균등분포
# np.random.uniform(최소값, 최대값, data 개수)
'''
array([[0.11192311, 0.62359282, 0.19744694],
       [0.15803027, 0.09091027, 0.0410109 ],
       [0.21752734, 0.32140977, 0.79129831],
       [0.01348298, 0.48707369, 0.45851178]])
'''
np.random.normal(0,1,12,).reshape(4,3) # 정규분포
'''
array([[ 1.27604609,  0.20532721, -0.94110582],
       [-0.24397179, -0.72678685, -0.49534384],
       [ 0.28499925, -1.49350215,  0.37308449],
       [ 1.14111183,  0.05763815, -1.21300561]])
'''

##########axis
# 모든 operation function을 실행할 때, 기준이 되는 dimension 축
t_array = np.arange(1, 13).reshape(3, 4)
t_array
'''
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
'''
t_array.sum(axis = 0), t_array.sum(axis = 1)
'''
(array([15, 18, 21, 24]), array([10, 26, 42]))
'''


tensor = np.array([t_array, t_array, t_array])
tensor
'''
array([[[ 1,  2,  3,  4],
        [ 5,  6,  7,  8],
        [ 9, 10, 11, 12]],

       [[ 1,  2,  3,  4],
        [ 5,  6,  7,  8],
        [ 9, 10, 11, 12]],

       [[ 1,  2,  3,  4],
        [ 5,  6,  7,  8],
        [ 9, 10, 11, 12]]])
'''


t_array = np.arange(1, 13).reshape(3, 4)
t_array
'''
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
'''
t_array.mean(), t_array.mean(axis=0)
# (6.5, array([5., 6., 7., 8.]))
t_array.std(), t_array.std(axis = 0)
# (3.452052529534663, array([3.26598632, 3.26598632, 3.26598632, 3.26598632]))


np.exp(t_array) # 지수함수
'''
array([[2.71828183e+00, 7.38905610e+00, 2.00855369e+01, 5.45981500e+01],
       [1.48413159e+02, 4.03428793e+02, 1.09663316e+03, 2.98095799e+03],
       [8.10308393e+03, 2.20264658e+04, 5.98741417e+04, 1.62754791e+05]])
'''
np.sqrt(t_array) # 루트
'''
array([[1.        , 1.41421356, 1.73205081, 2.        ],
       [2.23606798, 2.44948974, 2.64575131, 2.82842712],
       [3.        , 3.16227766, 3.31662479, 3.46410162]])
'''
np.sin(t_array) # sin 함수
'''
array([[ 0.84147098,  0.90929743,  0.14112001, -0.7568025 ],
       [-0.95892427, -0.2794155 ,  0.6569866 ,  0.98935825],
       [ 0.41211849, -0.54402111, -0.99999021, -0.53657292]])
'''


# Numpy array를 합치는 함수
a = np.array([1,2,3])
b = np.array([4,5,6])
np.vstack((a,b))
'''
array([[1, 2, 3],
       [4, 5, 6]])
'''
a = np.array([ [1], [2], [3]])
b = np.array([ [4], [5], [6]])
np.hstack((a, b))
'''
array([[1, 4],
       [2, 5],
       [3, 6]])
'''

###########concatenate
# Numpy array를 합치는 함수
a = np.array([1,2,3])
b = np.array([4,5,6])
np.concatenate((a,b), axis = 0)
# array([1, 2, 3, 4, 5, 6])

a = np.array([[ 1,2], [3,4]])
b = np.array([[5,6]])
np.concatenate((a,b.T), axis = 1) # a.T는 a의 역행렬
'''
array([[1, 2, 5],
       [3, 4, 6]])
'''

############Op
a = np.array( [[1,2,3], [4,5,6]], float)
a + a # matrix + matrix 연산

a - a # matrix - matrix 연산

a * a # matrix 내 요소들간 같은 위치에 있는 값들끼리 연산


# 이렇게 같은 index에 있는 것 끼리 더하고 빼고 곱해줘서 그자리에
# = Element-wise Operation 이라고 한다.


##########Dot product
# matrix의 기본연산
# dot 함수 사용
dot_a = np.arange(1, 7).reshape(2, 3)
dot_b = np.arange(1, 7).reshape(3, 2)
dot_a.dot(dot_b)


# scalar-matrix 외에도, vector-matrix간의 연산도 지원
t_matrix = np.arange(1, 13).reshape(4, 3)
t_vector = np.arange(100, 400, 100)
t_matrix + t_vector

########## All, Any
# All : Array의 데이터가 전부 조건에 만족하면 True
# Any : Array의 데이터 중하나라도 조건에 만족하면 True
a = np.arange(5)
a
np.all(a > 3)

np.all(a < 5)

np.any(a > 3)

np.any(a > 5)


a = np.array( [1,5,3], float)
b = np.array( [4,7,2], float)
a > b

a == b

(a > b).any()

(a > b).all()




a = np.array([2,3,1], float)
np.logical_and( a > 0, a < 3) # and 조건의 비교

b = np.array( [False, True, True], bool)
np.logical_not(b) # not 조건의 비교

c = np.array( [False,False, False], bool)
np.logical_or(b,c) # or 조건의 비교



##########np.where
# where(조건, True, False)
a = np.array([2,3,1], float)
np.where(a > 1, 0,3)

a = np.arange(3, 10)
np.where(a > 6) # True 값의 index 값 반환

a = np.array([2, np.NaN, np.Inf], float)
np.isnan(a) # null인 경우 True

np.isfinite(a) # 한정된 수인 경우 True
'''
isnan은 null 값인 경우에만 true가 나온다.
np.Nan은 numpy의 null값을 입력하는 함수이고, null값이니까 True

np.Inf는 무한대이다.
np.isinfite()는 한정된 수의 경우 True가 나오고
한정되지 않은 NaN이나 Inf의 경우에는 False가 나온다.
'''


############argmax, argmin
# array내 최대값 또는 최소값의 index 반환
a = np.array([2,3,1,5,6,22,11])
np.argmax(a), np.argmin(a)

# axis 기반의 반환
a = np.array([[1,4,2,22],[45,32,4,7],[34,54,9,8]])
np.argmax(a, axis = 0), np.argmin(a, axis = 1)


######boolean index
# numpy의 배열은 특정 조건에 따른 값을 배열 형태로 추출 가능
# comparison operation 함수들도 모두 사용 가능
t_a = np.array([3,5,8,0,7,4], float)
t_a > 4

t_a[t_a > 4] # 조건이 True 인 index의 요소값만 추출

t_c = t_a < 4
t_c

t_a[t_c]



















