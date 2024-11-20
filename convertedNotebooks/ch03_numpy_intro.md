#
 
`
N
u
m
P
y
`
:
 
N
u
m
e
r
i
c
a
l
 
o
p
e
r
a
t
i
o
n
s
 
i
n
 
P
y
t
h
o
n

T
h
i
s
 
t
u
t
o
r
i
a
l
 
u
s
e
s
 
m
a
t
e
r
i
a
l
 
a
l
s
o
 
f
o
u
n
d
 
i
n
 
t
h
e
 
[
S
c
i
P
y
 
1
.
0
 
N
a
t
u
r
e
 
M
e
t
h
o
d
s
]
(
h
t
t
p
s
:
/
/
w
w
w
.
n
a
t
u
r
e
.
c
o
m
/
a
r
t
i
c
l
e
s
/
s
4
1
5
9
2
-
0
1
9
-
0
6
8
6
-
2
)
 
a
n
d
 
[
N
u
m
P
y
 
A
r
r
a
y
 
I
E
E
E
]
(
1
0
.
1
1
0
9
/
M
C
S
E
.
2
0
1
1
.
3
7
)
 
a
r
t
i
c
l
e
 
a
n
d
 
a
t
 
[
h
t
t
p
s
:
/
/
n
u
m
p
y
.
o
r
g
/
]
(
h
t
t
p
s
:
/
/
n
u
m
p
y
.
o
r
g
/
)
.

#
#
#
 
L
e
a
r
n
i
n
g
 
o
u
t
c
o
m
e
s
:


 
-
 
U
n
d
e
r
s
t
a
n
d
 
P
y
t
h
o
n
 
L
i
b
r
a
r
y
 
`
N
u
m
P
y
`


 
-
 
U
s
e
 
`
n
u
m
p
y
 
a
r
r
a
y
s
`


 
-
 
A
p
p
l
y
 
l
o
o
p
s
 
a
n
d
 
l
o
g
i
c
a
l
 
o
p
e
r
a
t
o
r
s
 
o
n
 
`
n
u
m
p
y
 
a
r
r
a
y
s
`

D
a
t
a
 
s
c
i
e
n
t
i
s
t
s
 
s
p
e
n
d
 
a
 
l
o
t
 
o
f
 
t
i
m
e
 
–
 
w
a
i
t
 
f
o
r
 
i
t
 
–
 
w
o
r
k
i
n
g
 
w
i
t
h
 
*
*
*
d
a
t
a
*
*
*
!
 
T
o
 
w
o
r
k
 
w
i
t
h
 
*
*
d
a
t
a
*
*
 
i
t
 
i
s
 
c
r
i
t
i
c
a
l
 
t
o
 
o
r
g
a
n
i
z
e
 
t
h
e
 
d
a
t
a
 
i
n
 
a
 
w
a
y
 
t
h
a
t
 
f
a
c
i
l
i
t
a
t
e
 
t
h
e
 
w
o
r
k
 
o
n
 
t
h
e
 
p
o
t
e
n
t
i
a
l
 
a
n
a
l
y
s
e
s
 
w
e
 
m
i
g
h
t
 
n
e
e
d
 
t
o
 
d
o
.
 
S
o
 
o
r
g
a
n
i
z
i
n
g
 
d
a
t
a
 
m
e
a
n
s
 
g
u
e
s
s
i
n
g
 
w
h
a
t
 
t
y
p
e
 
o
f
 
w
o
r
k
 
w
e
 
w
i
l
l
 
w
a
n
t
 
t
o
 
d
o
 
w
i
t
h
 
t
h
e
 
d
a
t
a
s
e
t
.
 
A
n
d
,
 
o
d
d
 
i
s
 
i
t
 
m
a
y
 
s
e
e
m
,
 
g
o
o
d
 
g
u
e
s
s
i
n
g
 
r
e
q
u
i
r
e
s
 
s
o
m
e
 
p
r
a
c
t
i
c
e
.
 
T
h
e
 
d
a
t
a
 
o
r
g
a
n
i
z
a
t
i
o
n
 
p
r
o
c
e
s
s
 
w
i
l
l
 
r
e
q
u
i
r
e
:
 




*
 
s
t
o
r
e
 
t
h
e
 
d
a
t
a
 
a
 
c
l
e
a
r
 
a
n
d
 
s
y
s
t
e
m
a
t
i
c
 
w
a
y


*
 
p
r
o
v
i
d
e
 
m
e
t
h
o
d
s
 
t
o
 
a
c
c
e
s
s
 
t
h
e
 
d
a
t
a
 
t
h
a
t
 
a
r
e
 
s
i
m
p
l
e
 
a
n
d
 
s
t
r
a
i
g
h
t
f
o
r
w
a
r
d


*
 
b
e
 
f
l
e
x
i
b
l
e
 
e
n
o
u
g
h
 
s
o
 
t
o
 
a
n
d
 
a
l
l
o
w
 
t
o
 
m
o
d
i
f
y
 
t
h
e
 
f
o
r
m
a
t
 
o
f
 
t
h
e
 
d
a
t
a
 
f
o
r
 
v
a
r
i
o
u
s
 
n
e
e
d
s

N
u
m
P
y
 
i
s
 
t
h
e
 
f
u
n
d
a
m
e
n
t
a
l
 
`
l
i
b
r
a
r
y
`
 
f
o
r
 
m
a
t
h
e
m
a
t
i
c
a
l
 
o
p
e
r
a
t
i
o
n
s
 
a
n
d
 
c
o
m
p
u
t
a
t
i
o
n
s
 
i
n
 
P
y
t
h
o
n
.
 




T
h
e
 
N
u
m
P
y
 
l
i
b
r
a
r
y
 
p
r
o
v
i
d
e
s
 
a
 
s
e
r
i
e
s
 
o
f
 
o
b
j
e
c
t
s
 
t
h
a
t
 
c
a
n
 
b
e
 
u
s
e
d
 
t
o
 
s
t
o
r
e
 
d
a
t
a
 
(
r
e
p
r
e
s
e
n
t
 
t
h
e
 
n
u
m
b
e
r
s
 
i
n
 
a
 
d
a
t
a
s
e
t
 
f
o
r
 
P
y
t
h
o
n
)
 
a
n
d
 
a
 
s
e
r
i
e
s
 
o
f
 
m
e
t
h
o
d
s
 
t
o
 
a
n
a
l
y
z
e
 
d
a
t
a
 
(
p
r
o
v
i
d
e
 
o
p
e
r
a
t
i
o
n
s
 
t
h
a
t
 
c
a
n
 
c
o
m
p
u
t
e
,
 
s
a
y
 
t
h
e
 
m
e
a
n
 
o
r
 
t
h
e
 
s
t
a
n
d
a
r
d
 
d
e
v
i
a
t
i
o
n
 
o
f
 
s
o
m
e
 
n
u
m
b
e
r
s
 
i
n
 
a
 
d
a
t
a
s
e
t
)
.




T
h
e
 
N
u
m
P
y
 
`
a
r
r
a
y
`
 
i
s
 
t
h
e
 
w
o
r
k
h
o
r
s
e
 
o
f
 
N
u
m
P
y
 
a
n
d
 
w
e
 
w
i
l
l
 
s
p
e
n
d
 
q
u
i
t
e
 
s
o
m
e
 
t
i
m
e
 
w
i
t
h
 
i
t
 
b
e
l
o
w
.
 
T
h
e
 
n
u
m
p
y
 
a
r
r
a
y
 
i
s
 
a
 
m
u
l
t
i
d
i
m
e
n
s
i
o
n
a
l
 
a
r
r
a
y
 
o
b
j
e
c
t
,
 
t
h
a
t
 
m
e
a
n
s
 
t
h
a
t
 
i
t
 


 
 
-
 
(
1
)
 
i
s
 
a
n
 
o
b
j
e
c
t
 
f
o
r
 
p
r
o
g
r
a
m
m
i
n
g
 
(
s
o
 
i
t
 
h
a
s
 
m
e
t
h
o
d
s
 
a
n
d
 
p
r
o
p
r
t
i
e
s
 
o
f
 
a
n
 
o
b
j
e
c
t
,
 
j
u
s
t
 
l
i
k
e
 
y
o
u
 
c
u
p
 
h
o
l
d
s
 
c
o
f
f
e
e
 
a
n
d
 
h
a
s
 
c
o
l
o
r
s
,
 


 
 
-
 
(
2
)
 
t
h
e
 
N
u
m
p
y
 
a
r
r
a
y
 
c
a
n
 
h
o
l
d
 
d
a
t
a
 
a
n
d
 
h
a
v
e
 
a
 
b
u
n
c
h
 
o
f
 
p
r
o
p
e
r
t
i
e
s
 
t
h
a
t
 
w
e
 
c
a
n
 
l
o
o
k
 
a
s
 
w
e
 
l
o
o
k
 
a
t
 
t
h
e
 
c
o
l
o
r
s
 
o
n
 
t
h
e
 
c
u
p
.
 
T
h
e
 
p
r
o
p
e
r
t
i
e
s
 
o
f
 
t
h
e
 
a
r
r
a
y
 
h
e
l
p
 
u
s
 
r
e
c
o
g
n
i
z
e
 
a
n
d
 
u
n
d
e
r
s
t
a
n
d
 
w
h
a
t
 
i
s
 
i
n
 
t
h
e
 
a
r
r
a
y
 
a
n
d
 
s
o
m
e
t
i
m
e
s
 
t
h
a
t
 
i
s
 
r
e
a
l
l
y
 
i
m
p
o
r
t
a
n
t
,
 
f
o
r
 
e
x
a
m
p
l
e
,
 
y
o
u
 
w
o
u
l
d
 
n
o
t
 
w
a
n
t
 
t
o
 
d
r
i
n
k
 
f
r
o
m
 
s
o
m
e
o
n
e
 
e
l
s
e
'
s
 
c
u
p
,
 
w
o
u
l
d
 
y
o
u
?




A
 
v
a
r
i
e
t
y
 
o
f
 
f
a
s
t
 
n
u
m
e
r
i
c
a
l
 
o
p
e
r
a
t
i
o
n
s
 
o
n
 
a
r
r
a
y
s
 
a
r
e
 
p
r
o
v
i
d
e
d
 
b
y
 
N
u
m
P
y
.
 
T
h
e
s
e
 
i
n
c
l
u
d
e
 
o
p
e
r
a
t
i
o
n
s
 
t
h
a
t
 
a
r
e
 
m
a
t
h
e
m
a
t
i
c
a
l
,
 
l
o
g
i
c
a
l
,
 
s
h
a
p
e
 
m
a
n
i
p
u
l
a
t
i
o
n
,
 
s
o
r
t
i
n
g
,
 
s
e
l
e
c
t
i
n
g
,
 
I
/
O
,
 
d
i
s
c
r
e
t
e
 
F
o
u
r
i
e
r
 
t
r
a
n
s
f
o
r
m
s
,
 
b
a
s
i
c
 
l
i
n
e
a
r
 
a
l
g
e
b
r
a
,
 
b
a
s
i
c
 
s
t
a
t
i
s
t
i
c
a
l
 
o
p
e
r
a
t
i
o
n
s
,
 
r
a
n
d
o
m
 
s
i
m
u
l
a
t
i
o
n
 
a
n
d
 
m
u
c
h
 
m
o
r
e
.
 




N
u
m
P
y
 
i
s
 
t
h
e
 
b
a
s
e
 
o
f
 
s
c
i
e
n
t
i
f
i
c
 
c
o
m
p
u
t
i
n
g
 
a
n
d
 
d
a
t
a
 
s
c
i
e
n
c
e
 
l
i
b
r
a
r
i
e
s
 
s
u
c
h
 
a
s
 
[
P
a
n
d
a
s
]
(
h
t
t
p
s
:
/
/
p
a
n
d
a
s
.
p
y
d
a
t
a
.
o
r
g
/
)
 
[
s
c
i
p
y
.
o
r
g
]
(
h
t
t
p
s
:
/
/
s
c
i
p
y
.
o
r
g
/
)
,
 
a
n
d
 
[
s
c
i
k
i
t
-
l
e
a
r
n
.
o
r
g
]
(
h
t
t
p
s
:
/
/
s
c
i
k
i
t
-
l
e
a
r
n
.
o
r
g
/
)
 
a
m
o
n
g
 
m
a
n
y
 
o
t
h
e
r
s
.

I
n
 
o
t
h
e
r
 
(
s
i
m
p
l
e
r
?
)
 
w
o
r
d
s
,
 
N
u
m
p
y
 
a
r
r
a
y
s
 
a
r
e
 
g
r
i
d
s
 
o
r
 
t
a
b
l
e
s
 
f
o
r
 
h
o
l
d
i
n
g
,
 
a
c
c
e
s
s
i
n
g
,
 
a
n
d
 
m
a
n
i
p
u
l
a
t
i
n
g
 
d
a
t
a
.
 
T
h
e
y
 
a
r
e
 
c
r
e
a
t
e
d
 
a
n
d
 
a
c
c
e
s
s
e
d
 
i
n
 
w
a
y
s
 
t
h
a
t
 
a
r
e
 
v
e
r
y
 
s
i
m
i
l
a
r
 
t
o
 
t
h
e
 
w
a
y
s
 
P
y
t
h
o
n
 
`
l
i
s
t
s
`
 
c
a
n
 
b
e
 
a
c
c
e
s
s
e
d
.




S
o
 
w
h
a
t
 
w
e
 
a
r
e
 
g
o
i
n
g
 
t
o
 
d
o
 
i
s
 
t
o
 
r
e
c
a
l
l
 
h
o
w
 
`
l
i
s
t
s
`
 
w
o
r
k
 
(
l
i
s
t
s
 
a
r
e
 
h
a
n
d
y
!
)
,
 
t
h
e
n
 
w
e
 
w
i
l
l
 
g
r
a
d
u
a
t
e
 
t
o
 
`
n
u
m
p
y
 
a
r
r
a
y
s
`
 
a
n
d
 
s
e
e
 
w
h
a
t
 
t
h
e
y
 
c
a
n
 
d
o
.
 

#
#
#
 
P
y
t
h
o
n
 
l
i
s
t
s

W
e
 
h
a
v
e
 
c
o
v
e
r
e
d
 
P
y
t
h
o
n
 
`
l
i
s
t
s
`
 
(
a
n
d
 
o
t
h
e
r
 
d
a
t
a
t
y
p
e
s
)
 
i
n
 
p
r
e
v
i
o
u
s
 
t
u
t
o
r
i
a
l
s
.
 
P
y
t
h
o
n
 
`
l
i
s
t
s
`
 
(
a
 
l
i
s
t
 
o
f
 
t
h
i
n
g
s
)
 
i
s
 
b
u
i
l
d
 
b
y
 
c
o
l
l
e
c
t
i
n
g
,
 
a
h
e
m
,
 
a
 
l
i
s
t
 
o
f
 
t
h
i
n
g
s
 
u
s
i
n
g
 
`
[
s
q
u
a
r
e
 
b
r
a
c
k
e
t
s
]
`
.




F
o
r
 
e
x
a
m
p
l
e
:

```python
m
y
l
i
s
t
 
=
 
[
'
t
h
i
s
'
,
 
3
,
 
'
l
i
s
t
'
,
 
4
+
2
j
,
 
6
.
6
6
]
```

W
e
 
c
a
n
 
a
d
d
r
e
s
s
 
e
l
e
m
e
n
t
s
 
i
n
 
a
 
l
i
s
t
 
b
y
 
u
s
i
n
g
 
i
n
d
i
c
e
s
 
a
n
d
 
t
h
e
 
`
:
`
 
(
c
o
l
o
n
)
 
o
p
e
r
a
t
o
r
.

```python
m
y
l
i
s
t
[
0
:
3
]
```

W
e
 
c
a
n
 
r
e
a
d
 
t
h
i
s
 
a
s
 
"
G
i
v
e
 
m
e
 
a
l
l
 
t
h
e
 
e
l
e
m
e
n
t
s
 
i
n
 
t
h
e
 
i
n
t
e
r
v
a
l
 
b
e
t
w
e
e
n
 
0
 
*
*
i
n
c
l
u
s
i
v
e
*
*
 
t
o
 
3
 
*
*
e
x
c
l
u
s
i
v
e
*
*
.
"




I
 
k
n
o
w
 
t
h
i
s
 
i
s
 
w
e
i
r
d
.
 
B
u
t
 
a
t
 
l
e
a
s
t
 
f
o
r
 
a
n
y
 
t
w
o
 
i
n
d
e
x
e
s
 
`
a
`
 
a
n
d
 
`
b
`
,
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
e
l
e
m
e
n
t
s
 
y
o
u
 
g
e
t
 
b
a
c
k
 
f
r
o
m
 
`
m
y
l
i
s
t
[
a
,
b
]
`
 
i
s
 
a
l
w
a
y
s
 
e
q
u
a
l
 
t
o
 
`
b
`
 
m
i
n
u
s
 
`
a
`
,
 
s
o
 
I
 
g
u
e
s
s
 
t
h
a
t
'
s
 
g
o
o
d
!

W
e
 
c
a
n
 
g
e
t
 
a
n
y
 
c
o
n
s
e
c
u
t
i
v
e
 
h
u
n
k
 
o
f
 
e
l
e
m
e
n
t
s
 
u
s
i
n
g
 
`
:
`
.

```python
m
y
l
i
s
t
[
2
:
5
]
```

I
f
 
y
o
u
 
o
m
i
t
 
t
h
e
 
i
n
d
e
x
e
s
,
 
P
y
t
h
o
n
 
w
i
l
l
 
a
s
s
u
m
e
 
y
o
u
 
w
a
n
t
 
e
v
e
r
y
t
h
i
n
g
.

```python
m
y
l
i
s
t
[
:
]
```

L
i
s
t
 
c
a
n
 
o
b
v
i
o
u
s
l
y
 
h
o
s
t
 
a
l
s
o
 
h
o
m
o
g
e
n
e
o
u
s
 
t
y
p
e
s
 
o
f
 
d
a
t
a
,
 
s
u
c
h
 
a
s
 
`
i
n
t
`
 
o
r
 
`
f
l
o
a
t
`
:

```python
m
y
l
i
s
t
H
o
m
o
g
e
n
e
o
u
s
 
=
 
[
2
,
 
3
.
1
4
,
 
1
0
.
5
,
 
1
1
.
1
3
,
 
1
2
.
7
,
 
4
.
3
1
]
```

#
#
#
 
N
u
m
p
y
 
A
r
r
a
y
s

N
u
m
p
y
 
a
r
r
a
y
s
 
w
e
r
e
 
d
e
s
i
g
n
e
d
 
t
o
 
b
e
 
l
i
s
t
s
 
w
i
t
h
 
s
u
p
e
r
p
o
w
e
r
s
,
 
s
o
 
a
l
m
o
s
t
 
e
v
e
r
y
t
h
i
n
g
 
w
e
 
l
e
a
r
n
e
d
 
a
b
o
u
t
 
 
`
l
i
s
t
s
`
 
w
i
l
l
 
a
p
p
l
y
 
t
o
 
`
n
u
m
p
y
 
a
r
r
a
y
s
`
 
a
s
 
w
e
l
l
!
 
T
h
e
 
o
n
e
 
b
i
g
 
d
i
f
f
e
r
e
n
c
e
 
i
s
 
t
h
a
t
 
a
l
l
 
e
l
e
m
e
n
t
s
 
o
f
 
a
 
`
n
u
m
p
y
 
a
r
r
a
y
`
 
m
u
s
t
 
b
e
 
o
f
 
t
h
e
 
s
a
m
e
 
d
a
t
a
 
t
y
p
e
.
 
T
h
i
s
 
a
l
l
o
w
s
 
c
a
l
c
u
l
a
t
i
o
n
s
 
o
n
 
`
n
u
m
p
y
 
a
r
r
a
y
s
`
 
t
o
 
b
e
 
m
u
c
h
 
f
a
s
t
e
r
 
t
h
a
n
 
t
h
e
y
 
w
o
u
l
d
 
b
e
 
o
n
 
`
l
i
s
t
s
`
.

A
 
N
u
m
P
y
 
a
r
r
a
y
 
i
s
 
a
 
m
u
l
t
i
d
i
m
e
n
s
i
o
n
a
l
,
 
u
n
i
f
o
r
m
 
c
o
l
l
e
c
t
i
o
n
 
o
f
 
e
l
e
m
e
n
t
s
 
(
t
h
a
t
 
i
s
,
 
a
l
l
 
e
l
e
m
e
n
t
s
 
o
c
c
u
p
y
 
t
h
e
 
s
a
m
e
 
n
u
m
b
e
r
 
o
f
 
b
y
t
e
s
 
i
n
 
m
e
m
o
r
y
)
.
 
A
n
 
a
r
r
a
y
 
i
s
 
c
h
a
r
a
c
t
e
r
i
z
e
d
 
b
y


 
-
 
t
h
e
 
t
y
p
e
 
o
f
 
e
l
e
m
e
n
t
s
 
i
t
 
c
o
n
t
a
i
n
s
 
a
n
d


 
-
 
i
t
s
 
s
h
a
p
e
.
 


 


F
o
r
 
e
x
a
m
p
l
e
,
 
a
 
m
a
t
r
i
x
 
m
i
g
h
t
 
b
e
 
r
e
p
r
e
s
e
n
t
e
d
 
a
s
 
a
n
 
a
r
r
a
y
 
o
f
 
s
h
a
p
e
 
M
×
N
 
t
h
a
t
 
c
o
n
t
a
i
n
s
 
n
u
m
b
e
r
s
,
 
s
u
c
h
 
a
s
 
f
l
o
a
t
i
n
g
-
p
o
i
n
t
 
o
r
 
c
o
m
p
l
e
x
 
n
u
m
b
e
r
s
.
 
U
n
l
i
k
e
 
m
a
t
r
i
c
e
s
,
 
N
u
m
P
y
 
a
r
r
a
y
s
 
c
a
n
 
h
a
v
e
 
u
p
 
t
o
 
3
2
 
d
i
m
e
n
s
i
o
n
s
;
 
t
h
e
y
 
m
i
g
h
t
 
a
l
s
o
 
c
o
n
t
a
i
n
 
o
t
h
e
r
 
k
i
n
d
s
 
o
f
 
e
l
e
m
e
n
t
s
 
(
o
r
 
e
v
e
n
 
c
o
m
b
i
n
a
t
i
o
n
s
 
o
f
 
e
l
e
m
e
n
t
s
)
,
 
s
u
c
h
 
a
s
 
B
o
o
l
e
a
n
s
 
o
r
 
d
a
t
e
s
.
 
[
R
e
f
.
 
V
a
n
 
D
e
r
 
W
a
l
t
 
e
t
 
a
l
.
 
I
E
E
E
]
(
1
0
.
1
1
0
9
/
M
C
S
E
.
2
0
1
1
.
3
7
)

N
o
t
 
t
o
 
s
t
a
t
e
 
t
h
e
 
o
b
v
i
o
u
s
,
 
b
u
t
 
t
o
 
u
s
e
 
`
n
u
m
p
y
 
a
r
r
a
y
s
`
,
 
w
e
'
l
l
 
n
e
e
d
 
t
o
 
`
i
m
p
o
r
t
`
 
t
h
e
 
l
i
b
r
a
r
y
 
`
n
u
m
p
y
`
.
 
T
h
e
 
s
t
a
n
d
a
r
d
 
i
s
 
t
o
 
i
m
p
o
r
t
 
`
n
u
m
p
y
`
 
a
s
 
`
n
p
`
:

```python
i
m
p
o
r
t
 
n
u
m
p
y
 
a
s
 
n
p
```

`
a
r
r
a
y
s
`
 
c
a
n
 
b
e
 
m
a
d
e
 
b
y
 
s
i
m
p
l
y
 
a
s
k
i
n
g
 
f
o
r
 
o
n
e
 
a
n
d
 
f
i
l
l
i
n
g
 
i
t
 
o
u
t
 
w
i
t
h
 
v
a
l
u
e
s
,
 
i
n
 
m
u
c
h
 
t
h
e
 
s
a
m
e
 
w
a
y
 
w
e
 
m
a
k
e
 
a
 
`
l
i
s
t
`
.

```python
m
y
a
r
r
 
=
 
n
p
.
a
r
r
a
y
(
[
2
,
 
4
,
 
6
,
 
8
,
 
9
,
 
1
0
]
)
```

T
h
e
 
c
o
m
m
a
n
d
 
`
p
r
i
n
t
`
 
c
a
n
 
b
e
 
u
s
e
d
 
a
l
s
o
 
o
n
 
`
N
u
m
P
y
 
a
r
r
a
y
s
`
 
a
n
d
 
i
t
 
r
e
t
u
r
n
s
 
t
h
e
 
c
o
n
t
e
n
t
 
o
f
 
t
h
e
 
a
r
r
a
y
:

```python
p
r
i
n
t
(
m
y
a
r
r
)
```

B
y
 
s
i
m
p
l
y
 
r
e
t
u
r
n
i
n
g
 
t
h
e
 
a
r
r
a
y
 
o
b
j
e
c
t
 
n
a
m
e
 
(
`
m
y
a
r
r
`
)
 
t
h
e
 
o
u
t
p
u
t
 
i
s
 
a
 
b
i
t
 
m
o
r
e
 
i
n
f
o
r
m
a
t
i
v
e
 
a
n
d
 
i
t
 
r
e
t
u
r
n
s
 
t
h
e
 
t
y
p
e
 
(
`
a
r
r
a
y
`
)
:

```python
m
y
a
r
r
```

F
r
o
m
 
t
h
e
n
 
o
n
,
 
a
l
l
 
t
h
e
 
i
n
d
e
x
i
n
g
 
w
e
'
v
e
 
l
e
a
r
n
e
d
 
s
o
 
f
a
r
 
a
p
p
l
i
e
s
 
d
i
r
e
c
t
l
y
!
 
S
q
u
a
r
e
 
b
r
a
c
k
e
t
s
 
a
r
e
 
u
s
e
d
 
f
o
r
 
i
n
d
e
x
i
n
g
 
a
n
d
 
t
h
e
 
s
a
m
e
 
t
y
p
e
 
o
f
 
a
d
d
r
e
s
s
i
n
g
 
c
a
n
 
b
e
 
u
s
e
d
 
a
s
 
w
e
 
h
a
v
e
 
l
e
a
r
n
e
d
 
f
o
r
 
`
l
i
s
t
s
`
:

```python
m
y
a
r
r
[
4
]
```

```python
m
y
a
r
r
[
-
3
:
]
```

$
\
c
o
l
o
r
{
b
l
u
e
}
{
\
t
e
x
t
{
C
o
m
p
l
e
t
e
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
e
x
e
r
c
i
s
e
.
}
}
$




 
 
-
 
C
r
e
a
t
e
 
a
 
`
N
u
m
P
y
 
a
r
r
a
y
`
 
c
o
n
t
a
i
n
i
n
g
 
b
o
t
h
 
`
i
n
t
`
,
 
`
f
l
o
a
t
`
 
a
n
d
 
`
c
o
m
p
l
e
x
`
 
d
a
t
a
t
y
p
e
s
.




 
 
[
U
s
e
 
t
h
e
 
c
e
l
l
 
b
e
l
o
w
 
t
o
 
s
h
o
w
 
y
o
u
r
 
c
o
d
e
]

```python

```

 
 
-
 
C
r
e
a
t
e
 
a
 
`
N
u
m
P
y
 
a
r
r
a
y
`
 
c
o
n
t
a
i
n
i
n
g
 
b
o
t
h
 
`
s
t
r
`
 
a
s
 
d
a
t
a
t
y
p
e
s
.




 
 
[
U
s
e
 
t
h
e
 
c
e
l
l
 
b
e
l
o
w
 
t
o
 
s
h
o
w
 
y
o
u
r
 
c
o
d
e
]

```python

```

#
#
#
 
O
p
e
r
a
t
i
o
n
s
 
o
n
 
`
n
u
m
p
y
 
a
r
r
a
y
s
`
:
 
t
h
e
 
d
i
f
f
e
r
e
n
c
e
 
b
e
t
w
e
e
n
 
`
l
i
s
t
s
`
 
a
n
d
 
`
a
r
r
a
y
s
`


I
n
d
e
e
d
,
 
w
e
 
c
a
n
 
m
a
k
e
 
a
n
 
a
r
r
a
y
 
d
i
r
e
c
t
l
y
 
o
u
t
 
o
f
 
a
 
l
i
s
t
.

```python
m
y
A
r
r
F
r
o
m
L
i
s
t
 
=
 
n
p
.
a
r
r
a
y
(
m
y
l
i
s
t
H
o
m
o
g
e
n
e
o
u
s
)
```

```python
m
y
A
r
r
F
r
o
m
L
i
s
t
```

A
n
d
 
t
h
e
n
 
o
f
 
c
o
u
r
s
e
 
w
e
 
c
a
n
 
i
n
d
e
x
 
i
t
 
e
x
a
c
t
l
y
 
t
h
e
 
s
a
m
e
 
w
a
y
,
 
s
o
.
.
.
 
*
W
a
i
t
,
 
w
h
y
 
a
r
e
 
w
e
 
m
a
k
i
n
g
 
a
r
r
a
y
s
 
n
o
w
?
 
W
h
a
t
'
s
 
t
h
e
 
d
i
f
f
e
r
e
n
c
e
?
*

O
n
e
 
*
*
h
u
g
e
*
*
 
d
i
f
f
e
r
e
n
c
e
 
i
s
 
t
h
a
t
 
i
f
 
w
e
 
w
a
n
t
e
d
 
t
o
 
d
o
 
s
o
m
e
 
m
a
t
h
 
w
i
t
h
 
b
a
s
i
c
 
P
y
t
h
o
n
 
l
i
s
t
s
,
 
t
h
e
 
f
a
c
t
 
t
h
a
t
 
t
h
e
y
 
c
a
n
 
h
o
l
d
 
m
u
l
t
i
p
l
e
 
t
y
p
e
s
 
o
f
 
d
a
t
a
 
e
l
e
m
e
n
t
s
 
d
o
e
s
 
n
o
t
 
a
s
s
u
r
e
 
t
h
a
t
 
t
h
e
 
m
a
t
h
e
m
a
t
i
c
a
l
 
o
p
e
r
a
t
i
o
n
s
 
w
i
l
l
 
p
e
r
f
o
r
m
.

```python
m
y
l
i
s
t
 
+
 
5
```

`
n
u
m
p
y
`
 
a
r
r
a
y
s
 
i
n
s
t
e
a
d
 
c
o
n
t
a
i
n
 
n
u
m
e
r
i
c
a
l
 
e
l
e
m
e
n
t
s
 
b
y
 
d
e
f
i
n
i
t
i
o
n
.
 
T
h
i
s
 
d
e
f
i
n
i
t
i
o
n
 
a
s
s
u
r
e
s
 
t
h
e
 
a
b
i
l
i
t
y
 
t
o
 
p
e
r
f
o
r
m
 
m
a
t
h
 
o
n
 
t
h
e
 
a
r
r
a
y
s
.
 
S
o
,
 
w
h
e
r
e
a
s
 
t
h
e
 
a
d
d
i
t
i
o
n
 
a
b
o
v
e
 
d
i
d
 
n
o
t
 
w
o
r
k
 
w
h
e
n
 
u
s
i
n
g
 
t
h
e
 
`
l
i
s
t
`
,
 
i
t
 
d
o
e
s
 
w
o
r
k
 
w
h
e
n
 
u
s
i
n
g
 
t
h
e
 
`
n
u
m
p
y
`
 
a
r
r
a
y
,
 
e
v
e
n
 
t
h
o
u
g
h
 
b
o
t
h
 
`
l
i
s
t
`
 
a
n
d
 
`
a
r
r
a
y
`
 
c
o
n
t
a
i
n
 
t
h
e
 
s
a
m
e
 
e
l
e
m
e
n
t
s
!

```python
m
y
A
r
r
F
r
o
m
L
i
s
t
 
+
 
5
```

N
o
w
 
*
*
t
h
a
t
*
*
 
s
e
e
m
s
 
l
i
k
e
 
i
t
 
m
i
g
h
t
 
b
e
 
u
s
e
f
u
l
!

$
\
c
o
l
o
r
{
b
l
u
e
}
{
\
t
e
x
t
{
C
o
m
p
l
e
t
e
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
e
x
e
r
c
i
s
e
.
}
}
$




 
 
-
 
W
h
a
t
 
h
a
p
p
e
n
s
 
w
h
e
n
 
y
o
u
 
a
d
d
 
a
 
n
u
m
b
e
r
 
t
o
 
a
 
`
N
u
m
P
y
 
a
r
r
a
y
`
?
 
H
o
w
 
d
o
 
t
h
e
 
c
o
n
t
e
n
t
 
o
f
 
t
h
e
 
a
r
r
a
y
 
c
h
a
n
g
e
?




 
 
[
U
s
e
 
t
h
e
 
c
e
l
l
 
b
e
l
o
w
 
t
o
 
s
h
o
w
 
a
n
s
w
e
r
 
t
h
e
 
q
u
e
s
t
i
o
n
]



 
 
-
 
C
r
e
a
t
e
 
a
 
n
e
w
 
`
a
r
r
a
y
`
 
a
n
d
 
m
u
l
t
i
p
l
y
 
t
h
e
 
a
r
r
a
y
 
b
y
 
a
 
c
o
m
p
l
e
x
 
n
u
m
b
e
r
:




 
 
[
U
s
e
 
t
h
e
 
c
e
l
l
 
b
e
l
o
w
 
t
o
 
s
h
o
w
 
y
o
u
r
 
c
o
d
e
]

```python

```

 
 
 
 
[
U
s
e
 
t
h
e
 
c
e
l
l
 
b
e
l
o
w
 
t
o
 
d
e
s
c
r
i
b
e
 
i
n
 
y
o
u
r
 
o
w
n
 
w
o
r
d
s
 
w
h
a
t
 
h
a
p
p
n
e
s
 
t
o
 
t
h
e
 
e
l
e
m
e
n
t
s
 
o
f
 
t
h
e
 
a
r
r
a
y
 
a
f
t
e
r
 
m
u
l
t
i
p
l
y
i
n
g
 
f
o
r
 
a
 
c
o
m
p
l
e
x
 
n
u
m
b
e
r
]

 

#
#
#
 
M
o
r
e
 
o
p
e
r
a
t
i
o
n
s
 
o
n
 
`
a
r
r
a
y
s
`

T
w
o
 
a
r
r
a
y
s
 
c
a
n
 
b
e
 
a
d
d
e
d
,
 
o
r
 
s
u
b
t
r
a
c
t
e
d
,
 
o
r
 
m
u
l
t
i
p
l
i
e
d
 
o
r
 
w
h
a
t
e
v
e
r
!

```python
m
y
a
r
r
 
+
 
m
y
A
r
r
F
r
o
m
L
i
s
t
```

```python
m
y
a
r
r
 
*
 
m
y
A
r
r
F
r
o
m
L
i
s
t
```

```python
m
y
a
r
r
 
/
 
m
y
A
r
r
F
r
o
m
L
i
s
t
```

W
e
 
c
a
n
 
a
l
s
o
 
*
*
c
o
m
b
i
n
e
*
*
 
o
u
r
 
2
 
a
r
r
a
y
s
 
i
n
t
o
 
a
 
s
i
n
g
l
e
 
*
*
*
t
w
o
 
d
i
m
e
n
s
i
o
n
a
l
 
(
2
D
)
 
a
r
r
a
y
*
*
*
.

```python
t
w
o
D
a
r
r
 
=
 
n
p
.
a
r
r
a
y
(
[
m
y
a
r
r
,
 
m
y
A
r
r
F
r
o
m
L
i
s
t
]
)
```

```python
t
w
o
D
a
r
r
```

S
i
m
p
l
e
 
t
h
o
u
g
h
 
t
h
i
s
 
m
a
y
 
s
e
e
m
,
 
*
2
D
 
a
r
r
a
y
s
 
j
u
s
t
 
l
i
k
e
 
t
h
i
s
 
a
r
e
 
t
h
e
 
b
e
d
r
o
c
k
 
o
f
 
d
a
t
a
 
a
n
a
l
y
s
i
s
!
*
 
A
r
r
a
y
s
 
o
f
 
r
e
a
l
 
d
a
t
a
 
a
r
e
 
u
s
u
a
l
l
y
 
l
a
r
g
e
r
 
–
 
s
o
m
e
t
i
m
e
s
 
m
u
c
h
 
m
u
c
h
 
l
a
r
g
e
r
!
 
–
 
b
u
t
 
a
l
l
 
t
h
e
 
p
r
i
n
c
i
p
l
e
s
 
a
r
e
 
t
h
e
 
s
a
m
e
 
a
n
d
 
a
l
l
 
y
o
u
 
a
s
 
a
 
D
a
t
a
 
S
c
i
e
n
t
i
s
t
s
 
n
e
e
d
 
t
o
 
r
e
m
e
m
b
e
r
 
i
s
 
t
h
e
 
d
i
m
e
n
s
i
o
n
a
l
i
t
y
 
o
f
 
t
h
e
 
d
a
t
a
 
a
r
r
a
y
s
.
 
P
y
t
h
o
n
 
w
i
l
l
 
t
h
e
n
 
c
o
m
p
u
t
e
 
w
h
a
t
 
y
o
u
 
a
s
k
 
f
o
r
.

B
u
t
,
 
h
o
l
d
 
o
n
 
o
n
e
 
s
e
c
o
n
d
.
 
R
e
m
e
m
b
e
r
i
n
g
 
t
h
e
 
d
i
m
e
n
s
i
o
n
a
l
i
t
y
 
o
f
 
t
h
e
 
a
r
r
a
y
 
i
s
 
*
*
 
*
v
e
r
y
*
 
*
*
 
i
m
o
o
r
t
a
n
t
.
 
I
n
d
e
e
d
 
P
y
t
h
o
n
 
c
a
n
 
p
e
r
f
o
r
m
 
s
o
m
e
 
o
p
e
r
a
t
i
o
n
s
 
i
f
 
t
w
o
 
a
r
r
a
y
s
 
d
o
 
*
n
o
t
*
 
h
a
v
e
 
t
h
e
 
s
a
m
e
 
d
i
m
e
n
s
i
o
n
s
,
 
b
u
t
 
o
t
h
e
r
 
o
p
e
r
a
t
i
o
n
s
 
a
r
e
 
l
i
k
e
l
y
 
t
o
 
f
a
i
l
.




F
o
r
 
e
x
a
m
p
l
e
,
 
i
m
a
g
i
n
e
 
t
w
o
 
`
a
r
r
a
y
s
`
 
w
i
t
h
 
d
i
f
f
e
r
e
n
t
 
d
i
m
e
n
s
i
o
n
s
:

```python
s
m
a
l
l
A
r
r
a
y
 
=
 
[
2
,
 
3
,
 
4
]


l
a
r
g
e
A
r
r
a
y
 
=
 
[
2
,
 
3
,
 
4
,
 
5
,
 
6
,
 
7
]
```

T
h
e
 
t
w
o
 
a
r
r
a
y
s
 
c
a
n
 
b
e
 
a
d
d
e
d
 
t
o
g
e
t
h
e
r
 
b
y
 
u
s
i
n
g
 
t
h
e
 
s
y
m
b
o
l
 
`
+
`
:

```python
s
m
a
l
l
A
r
r
a
y
 
+
 
l
a
r
g
e
A
r
r
a
y
```

Y
e
t
,
 
t
h
e
 
s
a
m
e
 
t
w
o
 
a
r
r
a
y
s
 
c
a
n
n
o
t
 
b
e
 
m
u
l
t
i
p
l
i
e
d
:

```python
s
m
a
l
l
A
r
r
a
y
 
*
 
l
a
r
g
e
A
r
r
a
y
```

T
h
i
s
 
i
s
 
b
e
c
a
u
s
e
 
P
y
t
h
o
n
 
c
a
n
n
o
t
 
i
d
e
n
t
i
f
y
 
e
l
e
m
e
n
t
s
 
t
o
 
m
a
t
c
h
 
d
u
r
i
n
g
 
t
h
e
 
m
u
l
t
i
p
l
i
c
a
t
i
o
n
.

$
\
c
o
l
o
r
{
b
l
u
e
}
{
\
t
e
x
t
{
C
o
m
p
l
e
t
e
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
e
x
e
r
c
i
s
e
.
}
}
$




 
 
-
 
W
h
a
t
 
h
a
p
p
e
n
s
 
w
h
e
n
 
y
o
u
 
a
d
d
 
t
w
o
 
a
r
r
a
y
s
 
o
f
 
d
i
f
f
e
r
e
n
t
 
d
i
m
e
n
s
i
o
n
s
?
 
S
a
y
 
o
n
e
 
a
r
r
a
y
 
w
i
t
h
 
6
 
c
o
m
p
l
e
x
 
n
u
m
e
r
s
 
a
n
d
 
o
n
e
 
w
i
t
h
 
4
 
`
f
l
o
a
t
`
 
n
u
m
b
e
r
s
?




 
 
 
 
 
 
[
U
s
e
 
t
h
e
 
c
e
l
l
 
b
e
l
o
w
 
t
o
 
s
h
o
w
 
h
o
w
 
t
o
 
c
r
e
a
t
e
 
a
n
d
 
a
d
d
 
t
h
e
 
t
w
o
 
a
r
r
a
y
s
]

```python

```

 
 
 
 
[
U
s
e
 
t
h
e
 
c
e
l
l
 
b
e
l
o
w
 
t
o
 
d
e
s
c
r
i
b
e
 
i
n
 
y
o
u
r
 
o
w
n
 
w
o
r
d
s
 
w
h
a
t
 
h
a
p
p
e
n
s
 
t
o
 
t
h
e
 
a
r
r
a
y
s
 
a
s
 
r
e
s
u
l
t
 
o
f
 
t
h
e
 
m
u
l
t
i
p
l
i
c
a
t
i
o
n
]



#
#
#
 
M
e
t
h
o
d
s
 
o
f
 
`
n
u
m
p
y
 
a
r
r
a
y
s
`

S
o
 
t
h
e
 
s
h
a
p
e
 
o
f
 
t
h
e
 
a
r
r
a
y
 
(
t
h
e
 
d
i
m
e
n
s
i
o
n
a
l
i
t
y
)
 
i
s
 
k
e
y
,
 
e
s
p
e
c
i
a
l
l
y
 
i
f
 
w
e
 
p
l
a
n
 
o
n
 
d
o
i
n
g
 
m
a
t
h
 
w
i
t
h
 
t
h
e
 
a
r
r
a
y
s
,
 
w
h
i
h
c
 
i
s
 
t
h
e
 
p
r
i
m
a
r
y
 
g
o
a
l
 
o
f
 
t
h
e
 
a
r
r
a
y
s
!
 

`
n
u
m
p
y
 
a
r
r
a
y
s
`
 
a
r
e
 
P
y
t
h
o
n
 
o
b
j
e
c
t
s
 
a
n
d
 
a
s
 
s
u
c
h
 
t
h
e
y
 
h
a
v
e
 
`
m
e
t
h
o
d
s
`
.
 
A
 
v
a
r
i
e
t
y
 
o
f
 
m
e
t
h
o
d
s
 
e
x
i
s
t
 
f
o
r
 
t
h
e
 
a
r
r
a
y
 
a
n
d
 
`
s
h
a
p
e
`
 
i
s
 
t
h
e
 
o
n
e
 
t
h
a
t
 
a
l
l
o
w
 
u
s
 
t
o
 
r
e
t
r
i
e
v
e
 
t
h
e
 
d
i
m
e
n
s
i
o
n
a
l
i
t
y
 
o
f
 
a
n
 
a
r
r
a
y
.

```python
t
w
o
D
a
r
r
.
s
h
a
p
e
```

U
n
l
i
k
e
 
l
i
s
t
s
,
 
w
h
i
c
h
 
a
r
e
 
a
l
w
a
y
s
 
j
u
s
t
 
l
i
s
t
s
,
 
a
r
r
a
y
s
 
c
a
n
 
c
o
m
e
 
i
n
 
a
n
y
 
s
h
a
p
e
.
 
S
o
 
i
t
'
s
 
*
r
e
a
l
l
y
*
 
c
o
n
v
e
n
i
e
n
t
 
t
h
a
t
 
t
h
e
y
 
c
a
n
 
t
e
l
l
 
u
s
 
w
h
a
t
 
s
h
a
p
e
 
t
h
e
y
 
a
r
e
 
s
t
r
a
i
g
h
t
 
a
w
a
y
.

I
n
d
e
x
i
n
g
 
i
n
t
o
 
2
D
 
a
r
r
a
y
s
 
i
s
 
a
 
s
t
r
a
i
g
h
t
f
o
r
w
a
r
d
 
e
x
t
e
n
s
i
o
n
 
o
f
 
i
n
d
e
x
i
n
g
 
i
n
t
o
 
1
D
 
a
r
r
a
y
s
 
o
r
 
l
i
s
t
s
.
 
W
e
 
j
u
s
t
 
p
r
o
v
i
d
e
 
a
 
s
e
c
o
n
d
 
i
n
d
e
x
 
a
f
t
e
r
 
a
 
`
,
`
 
(
c
o
m
m
a
)
.
 
L
i
k
e
 
t
h
i
s
.

```python
t
w
o
D
a
r
r
[
1
,
3
]
```

T
h
e
 
f
i
r
s
t
 
i
n
d
e
x
 
r
e
f
e
r
s
 
t
o
 
t
h
e
 
*
*
r
o
w
 
i
n
d
e
x
*
*
,
 
a
n
d
 
t
h
e
 
s
e
c
o
n
d
 
t
o
 
t
h
e
 
*
*
c
o
l
u
m
n
 
i
n
d
e
x
*
*
.
 
I
n
 
t
h
i
s
 
c
a
s
e
,
 
w
e
'
r
e
 
a
s
k
i
n
g
 
f
o
r
 
t
h
e
 
v
a
l
u
e
 
i
n
 
t
h
e
 
s
e
c
o
n
d
 
r
o
w
 
a
n
d
 
t
h
e
 
f
o
u
r
t
h
 
c
o
l
u
m
n
,
 
w
h
i
c
h
 
i
s
 
i
n
d
e
e
d
 
7
 
(
r
e
m
e
m
b
e
r
 
*
t
h
e
 
f
i
r
s
t
 
r
o
w
 
a
n
d
 
c
o
l
u
m
n
 
a
r
e
 
i
n
d
e
x
=
0
!
*
)
.

W
e
 
c
a
n
 
p
l
a
y
 
a
l
l
 
t
h
e
 
s
a
m
e
 
g
a
m
e
s
 
i
n
d
e
x
i
n
g
 
w
i
t
h
 
2
D
 
a
r
r
a
y
s
 
a
s
 
w
e
 
c
a
n
 
w
i
t
h
 
1
D
 
a
r
r
a
y
s
,
 
w
e
 
j
u
s
t
 
h
a
v
e
 
t
o
 
r
e
m
e
m
b
e
r
 
t
h
a
t
 
e
v
e
r
y
t
h
i
n
g
 
b
e
f
o
r
e
 
t
h
e
 
c
o
m
m
a
 
`
,
`
 
r
e
f
e
r
s
 
t
o
 
t
h
e
 
*
r
o
w
s
*
 
i
n
 
t
h
a
t
 
i
t
 
s
p
e
c
i
f
i
e
s
 
l
o
c
a
t
i
o
n
s
 
a
l
o
n
g
 
t
h
e
 
*
v
e
r
t
i
c
a
l
 
d
i
m
e
n
s
i
o
n
*
,
 
a
n
d
 
e
v
e
r
y
t
h
i
n
g
 
a
f
t
e
r
 
t
h
e
 
c
o
m
m
a
 
`
,
`
 
r
e
f
e
r
s
 
t
o
 
t
h
e
 
*
c
o
l
u
m
n
s
*
 
i
n
 
t
h
a
t
 
i
t
 
s
p
e
c
i
f
i
e
s
 
l
o
c
a
t
i
o
n
s
 
a
l
o
n
g
 
t
h
e
 
*
h
o
r
i
z
o
n
t
a
l
 
d
i
m
e
n
s
i
o
n
*
.

S
o
 
t
h
i
s
:

```python
t
w
o
D
a
r
r
[
:
,
0
:
3
]
```

m
e
a
n
s
 
"
G
i
v
e
 
m
e
 
a
l
l
 
t
h
e
 
r
o
w
s
 
(
t
h
e
 
c
o
l
o
n
 
`
:
`
)
 
i
n
 
t
h
e
 
f
i
r
s
t
 
3
 
c
o
l
u
m
n
s
 
(
t
h
e
 
"
`
0
:
3
`
)
.
"




I
 
t
o
l
d
 
y
o
u
 
t
h
a
t
 
t
h
e
 
c
o
l
o
n
 
a
l
l
 
a
l
o
n
e
 
b
y
 
i
t
s
e
l
f
 
w
o
u
l
d
 
e
n
d
 
u
p
 
b
e
i
n
g
 
u
s
e
f
u
l
!
!
!
 
I
n
 
t
h
i
s
 
c
a
s
e
 
f
o
r
 
e
x
a
m
p
l
e
,
 
b
y
 
u
s
i
n
g
 
t
h
e
 
`
:
`
 
y
o
u
 
d
o
 
n
o
t
 
n
e
e
d
 
t
o
 
t
y
p
e
 
m
a
n
y
 
i
n
d
i
c
e
s
 
(
o
n
e
 
p
e
r
 
r
o
w
)
 
a
n
d
 
y
o
u
 
e
v
e
n
 
d
o
 
n
o
t
 
n
e
e
d
 
t
o
 
r
e
m
m
e
b
e
r
 
h
o
w
 
m
a
n
y
 
r
o
w
s
 
t
h
e
r
e
 
a
r
e
,
 
j
u
s
t
 
u
s
e
 
`
:
`
 
a
n
d
 
P
y
t
h
o
n
 
w
i
l
l
 
r
e
t
u
r
n
 
a
l
l
 
t
h
e
 
e
l
e
m
e
n
t
s
.

A
 
f
e
w
 
m
o
r
e
 
e
x
a
m
p
l
e
s
:

```python
#
 
t
h
e
 
l
a
s
t
 
r
o
w
 
(
r
e
g
a
r
d
l
e
s
s
 
o
f
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
r
o
w
s
,
 


#
 
a
g
a
i
n
 
y
o
u
 
d
o
 
n
o
t
 
n
e
e
d
 
t
o
 
k
n
o
w
h
o
w
 
m
a
n
y
 
r
o
w
s
 
e
x
i
s
t
)


t
w
o
D
a
r
r
[
-
1
,
:
]
 
```

```python
t
w
o
D
a
r
r
[
:
,
-
2
:
]
 
#
 
l
a
s
t
 
t
w
o
 
c
o
l
u
m
n
s
```

```python
t
w
o
D
a
r
r
[
0
,
:
:
2
]
 
#
 
f
i
r
s
t
 
r
o
w
,
 
e
v
e
r
y
 
o
t
h
e
r
 
c
o
l
u
m
n
```

T
o
 
g
e
t
 
g
o
o
d
 
a
t
 
t
h
i
s
,
 
y
o
u
 
d
o
n
'
t
 
n
e
e
d
 
n
a
t
u
r
a
l
 
b
o
r
n
 
t
a
l
e
n
t
 
o
r
 
a
n
y
t
h
i
n
g
 
l
i
k
e
 
t
h
a
t
.
 
L
i
k
e
 
s
o
 
m
u
c
h
 
i
n
 
l
i
f
e
,
 
t
h
e
 
k
e
y
 
i
s
 
*
p
r
a
c
t
i
c
e
,
 
p
r
a
c
t
i
c
e
,
 
p
r
a
c
t
i
c
e
*
!
!
!
 
S
o
 
p
l
a
y
 
a
r
o
u
n
d
!
 
Y
o
u
 
c
a
n
'
t
 
b
r
e
a
k
 
y
o
u
r
 
c
o
m
p
u
t
e
r
 
o
r
 
a
n
y
t
h
i
n
g
!

A
n
o
t
h
e
r
 
n
e
a
t
 
t
r
i
c
k
 
t
h
a
t
 
a
r
r
a
y
s
 
c
a
n
 
d
o
 
i
s
 
*
t
r
a
n
s
p
o
s
e
*
 
t
h
e
m
s
e
l
v
e
s
,
 
f
l
i
p
p
i
n
g
 
t
h
e
 
r
o
w
s
 
f
o
r
 
c
o
l
u
m
n
s
.




(
H
o
l
d
 
y
o
u
r
 
r
i
g
h
t
 
h
a
n
d
 
i
n
 
f
r
o
n
t
 
o
f
 
y
o
u
r
 
f
a
c
e
 
s
o
 
t
h
a
t
 
y
o
u
'
r
e
 
l
o
o
k
i
n
g
 
a
t
 
y
o
u
r
 
p
a
l
m
 
w
i
t
h
 
y
o
u
r
 
f
i
n
g
e
r
s
 
p
o
i
n
t
i
n
g
 
t
o
w
a
r
d
s
 
t
h
e
 
l
e
f
t
.
 
N
o
w
 
f
l
i
p
 
y
o
u
r
 
h
a
n
d
 
s
o
 
t
h
a
t
 
y
o
u
'
r
e
 
l
o
o
k
i
n
g
 
a
t
 
t
h
e
 
b
a
c
k
 
o
f
 
y
o
u
r
 
h
a
n
d
 
w
i
t
h
 
y
o
u
r
 
f
i
n
g
e
r
s
 
p
o
i
n
t
i
n
g
 
u
p
.
 
Y
o
u
 
j
u
s
t
 
*
t
r
a
n
s
p
o
s
e
d
*
 
y
o
u
r
 
h
a
n
d
 
s
u
c
h
 
t
h
a
t
 
t
h
e
 
f
i
r
s
t
 
r
o
w
 
(
y
o
u
r
 
p
o
i
n
t
e
r
 
f
i
n
g
e
r
)
 
b
e
c
a
m
e
 
t
h
e
 
f
i
r
s
t
 
c
o
l
u
m
n
!
)

```python
c
o
l
a
r
r
 
=
 
t
w
o
D
a
r
r
.
T
```

```python
c
o
l
a
r
r
```

W
h
y
 
w
o
u
l
d
 
w
e
 
w
a
n
t
 
t
o
 
d
o
 
t
h
a
t
?
 
B
y
 
c
o
n
v
e
n
t
i
o
n
,
 
*
v
a
r
i
a
b
l
e
s
*
 
i
n
 
d
a
t
a
s
e
t
s
 
s
h
o
u
l
d
 
c
o
r
r
e
s
p
o
n
d
 
t
o
 
t
h
e
 
c
o
l
u
m
n
s
,
 
a
n
d
 
*
o
b
s
e
r
v
a
t
i
o
n
s
*
 
s
h
o
u
l
d
 
c
o
r
r
e
s
p
o
n
d
 
t
o
 
t
h
e
 
r
o
w
s
.
 
S
o
 
w
e
 
h
a
v
e
 
t
a
k
e
n
 
d
a
t
a
 
i
n
 
w
h
i
c
h
 
t
h
i
s
 
w
a
s
 
n
o
t
 
s
o
 
a
n
d
 
t
u
r
n
e
d
 
i
t
 
i
n
t
o
 
a
n
 
a
r
r
a
y
 
i
n
 
w
h
i
c
h
 
t
h
e
 
c
o
l
u
m
n
s
 
a
r
e
 
t
h
e
 
f
i
r
s
t
 
f
e
w
 
n
o
n
-
p
r
i
m
e
 
n
u
m
b
e
r
s
 
a
n
d
 
t
h
e
 
p
r
i
m
e
 
n
u
m
b
e
r
s
,
 
r
e
s
p
e
c
t
i
v
e
l
y
,
 
a
n
d
 
t
h
e
 
r
o
w
s
 
c
o
r
r
e
s
p
o
n
d
 
t
o
 
t
h
e
 
i
n
s
t
a
n
c
e
s
 
i
n
 
o
r
d
e
r
 
(
1
s
t
 
,
 
2
n
d
,
 
3
r
d
,
 
.
.
.
.
)
.




S
o
 
t
h
a
t
 
r
e
a
l
l
y
 
s
p
e
e
d
s
 
u
p
 
a
 
c
o
m
m
o
n
 
*
*
d
a
t
a
 
w
r
a
n
g
l
i
n
g
*
*
 
o
p
e
r
a
t
i
o
n
.
 

N
o
w
 
t
h
a
t
 
w
e
 
h
a
v
e
 
t
h
e
 
d
a
t
a
 
i
n
t
o
 
s
h
a
p
e
,
 
w
e
 
c
a
n
 
u
n
l
e
a
s
h
 
a
l
l
 
t
h
e
 
p
o
w
e
r
s
 
o
f
 
n
u
m
p
y
 
a
r
r
a
y
s
,
 
p
o
w
e
r
s
 
w
h
i
c
h
 
p
a
n
d
a
s
 
D
a
t
a
F
r
a
m
e
s
 
w
i
l
l
 
i
n
h
e
r
i
t
 
a
n
d
 
b
u
i
l
d
 
u
p
o
n
!

F
o
r
 
e
x
a
m
p
l
e
,
 
w
h
o
'
s
 
b
i
g
g
e
r
 
o
v
e
r
a
l
l
,
 
t
h
e
 
p
r
i
m
e
s
 
o
r
 
t
h
e
 
n
o
n
-
p
r
i
m
e
s
?

```python
c
o
l
a
r
r
.
s
u
m
(
0
)
```

T
h
e
 
p
r
i
m
e
s
 
w
i
n
!
 


I
n
 
`
c
o
l
a
r
r
.
s
u
m
(
0
)
`
,
 
t
h
e
 
0
 
m
e
a
n
s
 
"
t
h
e
 
f
i
r
s
t
 
(
v
e
r
t
i
c
a
l
)
 
d
i
m
e
n
s
i
o
n
"
,
 
i
.
e
.
,
 
s
u
m
 
t
h
e
 
v
a
l
u
e
s
 
*
a
c
r
o
s
s
 
t
h
e
 
r
o
w
s
*
 
w
i
t
h
i
n
 
e
a
c
h
 
c
o
l
u
m
n
.
 
T
o
 
s
u
m
 
a
l
o
n
g
 
t
h
e
 
s
e
c
o
n
d
 
d
i
m
e
n
s
i
o
n
,
 
w
e
 
d
o
:

```python
c
o
l
a
r
r
.
s
u
m
(
1
)
```

S
o
 
a
n
y
 
n
u
m
p
y
 
a
r
r
a
y
 
k
n
o
w
s
 
h
o
w
 
t
o
 
a
d
d
 
u
p
 
t
h
e
 
n
u
m
b
e
r
s
 
i
n
 
i
t
 
b
y
 
r
o
w
 
o
r
 
b
y
 
c
o
l
u
m
n
 
(
s
e
e
 
w
h
a
t
 
h
a
p
p
e
n
s
 
i
f
 
y
o
u
 
l
e
a
v
e
 
o
f
f
 
t
h
e
 
d
i
m
e
n
s
i
o
n
,
 
l
i
k
e
 
t
h
i
s
 
`
c
o
l
a
r
r
.
s
u
m
(
)
`
.
 
T
h
e
 
l
i
s
t
 
o
f
 
t
h
i
n
g
s
 
t
h
a
t
 
n
u
m
p
y
 
a
r
r
a
y
s
 
c
a
n
 
d
o
 
t
h
e
m
s
e
l
v
e
s
 
i
s
 
p
r
e
t
t
y
 
i
m
p
r
e
s
s
i
v
e
.




C
h
e
c
k
 
i
t
 
o
u
t
 
[
h
e
r
e
]
(
h
t
t
p
s
:
/
/
n
u
m
p
y
.
o
r
g
/
d
o
c
/
s
t
a
b
l
e
/
r
e
f
e
r
e
n
c
e
/
g
e
n
e
r
a
t
e
d
/
n
u
m
p
y
.
n
d
a
r
r
a
y
.
h
t
m
l
)
.




(
o
r
 
p
a
s
t
e
 
t
h
i
s
 
i
n
t
o
 
y
o
u
r
 
b
r
o
w
s
e
r
:
 
h
t
t
p
s
:
/
/
n
u
m
p
y
.
o
r
g
/
d
o
c
/
s
t
a
b
l
e
/
r
e
f
e
r
e
n
c
e
/
g
e
n
e
r
a
t
e
d
/
n
u
m
p
y
.
n
d
a
r
r
a
y
.
h
t
m
l
)

$
\
c
o
l
o
r
{
b
l
u
e
}
{
\
t
e
x
t
{
C
o
m
p
l
e
t
e
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
e
x
e
r
c
i
s
e
.
}
}
$




 
 
-
 
H
o
w
 
m
a
n
y
 
m
e
t
h
o
d
s
 
d
o
e
s
 
a
 
n
u
m
p
y
 
a
r
r
a
y
 
h
a
v
e
?
 
[
R
e
p
o
r
t
 
y
o
u
r
 
a
n
s
w
e
r
 
h
e
r
e
]


 
 


 
 
-
 
C
r
e
a
t
e
 
a
 
n
e
w
 
2
-
d
i
m
e
n
s
i
o
n
a
l
 
a
r
r
a
y
,
 
a
n
d
 
s
h
o
w
 
t
h
e
 
u
s
e
 
o
f
 
t
w
o
 
m
e
t
h
o
d
s
 
n
o
t
 
u
s
e
d
 
a
b
o
v
e
 
(
`
p
r
o
d
`
 
a
n
d
 
`
r
o
u
n
d
`
 
c
o
u
l
d
 
b
e
 
t
w
o
 
s
i
m
p
l
e
 
o
n
e
s
,
 
b
u
t
 
n
o
 
p
r
e
s
s
u
r
e
)
:


 
 


 
 
[
U
s
e
 
t
h
e
 
c
e
l
l
 
b
e
l
o
w
 
t
o
 
s
h
o
w
 
h
o
w
 
t
o
 
c
r
e
a
t
e
 
a
n
d
 
a
d
d
 
t
h
e
 
t
w
o
 
a
r
r
a
y
s
]


 
 


*
H
i
n
t
:
*
 
T
h
e
 
s
y
m
b
o
l
 
`
?
`
 
c
a
n
 
b
e
 
u
s
e
d
 
a
t
 
t
h
e
 
e
n
d
 
o
f
 
a
 
m
e
t
h
o
d
 
a
n
d
 
t
h
a
t
 
c
a
n
 
h
e
l
p
 
u
n
d
e
r
s
t
a
n
d
 
h
o
w
 
t
o
 
u
s
e
 
t
h
e
 
m
e
t
h
o
d
,
 
f
o
r
 
e
x
a
m
p
l
e
,
 
`
m
y
a
r
r
a
y
.
s
h
a
p
e
?
`

```python

```

#
#
#
 
`
N
u
m
P
y
`
 
m
e
t
h
o
d
s
 
t
o
 
c
r
e
a
t
e
 
a
r
r
a
y
s

O
f
t
e
n
,
 
w
e
 
w
a
n
t
 
t
o
 
c
r
e
a
t
e
 
a
 
a
r
r
a
y
 
t
h
a
t
 
w
e
 
k
n
o
w
 
w
e
'
r
e
 
g
o
i
n
g
 
t
o
 
p
u
t
 
v
a
l
u
e
s
 
i
n
 
l
a
t
e
r
.
 
F
o
r
 
e
x
a
m
p
l
e
,
 
w
e
 
m
i
g
h
t
 
b
e
 
p
l
a
n
n
i
n
g
 
o
n
 
d
o
i
n
g
 
a
 
c
o
m
p
u
t
a
t
i
o
n
 
t
h
a
t
 
w
i
l
l
 
r
e
s
u
l
t
 
i
n
 
3
 
s
e
t
s
 
o
f
 
7
 
v
a
l
u
e
s
,
 
a
n
d
 
w
e
 
w
a
n
t
 
b
e
 
a
b
l
e
 
t
o
 
s
t
o
r
e
 
t
h
e
m
 
d
i
r
e
c
t
l
y
 
i
n
t
o
 
a
n
 
a
r
r
a
y
.
 
W
e
 
c
a
n
 
p
r
e
-
m
a
k
e
 
a
n
 
a
r
r
a
y
 
f
i
l
l
e
d
 
w
i
t
h
 
z
e
r
o
s
 
w
i
t
h
 
`
n
p
.
z
e
r
o
s
(
r
,
 
c
)
`
.

```python
m
y
z
e
r
o
s
 
=
 
n
p
.
z
e
r
o
s
(
(
7
,
 
3
)
)
```

```python
m
y
z
e
r
o
s
```

A
n
o
t
h
e
r
 
h
a
n
d
y
 
m
e
t
h
o
d
 
t
o
 
c
r
e
a
t
e
 
a
r
r
a
y
s
 
i
s
 
`
o
n
e
s
`

```python
m
y
o
n
e
s
 
=
 
n
p
.
o
n
e
s
(
(
3
,
4
)
)
```

```python
m
y
o
n
e
s
```

W
e
 
w
i
l
l
 
e
n
c
o
u
n
t
e
r
 
o
t
h
e
r
 
`
N
u
m
P
y
`
 
m
e
t
h
o
d
s
 
i
n
 
l
a
t
e
r
 
t
u
t
o
r
i
a
l
s
.
 
F
o
r
 
t
h
e
 
t
i
m
e
 
b
e
i
n
g
 
o
n
e
 
l
a
s
t
 
m
e
t
h
o
d
 
t
h
a
t
 
w
i
l
l
 
t
u
r
n
 
o
u
t
 
v
e
r
y
 
h
a
n
d
y
 
w
h
e
n
 
m
o
d
e
l
l
i
n
g
 
d
a
t
a
:

```python
m
y
R
a
n
d
o
m
N
u
m
A
r
r
a
y
 
=
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
n
(
1
0
,
1
)


p
r
i
n
t
(
m
y
R
a
n
d
o
m
N
u
m
A
r
r
a
y
)
```

T
h
e
 
`
n
u
m
p
y
`
 
s
u
b
m
o
d
u
l
e
 
`
r
a
n
d
o
m
`
 
c
o
n
t
a
i
n
s
 
a
 
v
a
r
i
e
t
y
 
o
f
 
m
e
t
h
o
d
s
 
t
o
 
c
r
e
a
t
e
 
a
r
r
a
y
s
 
c
o
n
t
a
i
n
i
n
g
 
r
a
n
d
o
m
 
n
u
m
b
e
r
s
.
 
G
e
n
e
r
a
t
i
n
g
 
r
a
n
d
o
m
 
n
u
m
b
e
r
s
 
i
s
 
h
e
l
p
f
u
l
 
i
n
 
m
a
n
y
 
a
p
p
l
i
c
a
t
i
o
n
s
,
 
f
o
r
 
e
x
a
m
p
l
e
,
 
t
h
e
y
 
c
a
n
 
b
e
 
u
s
e
d
 
t
o
 
c
r
e
a
t
e
 
n
o
r
m
a
l
l
y
 
d
i
s
t
r
i
b
u
t
e
d
 
n
o
i
s
e
,
 
o
r
 
d
a
t
a
 
w
i
t
h
 
n
o
r
m
a
l
l
y
 
d
i
s
t
r
i
b
u
t
e
d
 
n
o
i
s
e
,
 
e
t
c
.
 

$
\
c
o
l
o
r
{
b
l
u
e
}
{
\
t
e
x
t
{
C
o
m
p
l
e
t
e
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
e
x
e
r
c
i
s
e
.
}
}
$


 
 


 
 
-
 
C
r
e
a
t
e
 
a
 
n
e
w
 
1
-
d
i
m
e
n
s
i
o
n
a
l
 
a
r
r
a
y
 
o
f
 
u
n
i
f
o
r
m
l
y
-
d
i
s
t
r
i
b
u
t
e
d
 
r
a
n
d
o
m
 
n
u
m
b
e
r
:


 
 


 
 
[
U
s
e
 
t
h
e
 
c
e
l
l
 
b
e
l
o
w
 
t
o
 
s
h
o
w
 
y
o
u
r
 
c
o
d
e
]



```python

```

 
 


 
 
-
 
C
r
e
a
t
e
 
a
 
n
e
w
 
 
2
-
d
i
m
e
n
s
i
o
n
a
l
 
a
r
r
a
y
 
o
f
 
n
o
r
m
a
l
l
y
-
d
i
s
t
r
i
b
u
t
e
d
 
r
a
n
d
o
m
 
n
u
m
b
e
r
:


 
 


 
 
[
U
s
e
 
t
h
e
 
c
e
l
l
 
b
e
l
o
w
 
t
o
 
s
h
o
w
 
y
o
u
r
 
c
o
d
e
]



```python

```

L
e
t
'
s
 
n
o
w
 
c
r
e
a
t
e
 
a
 
s
i
m
p
l
e
 
1
-
D
 
a
r
r
a
y
 
a
n
d
 
e
x
p
l
o
r
e
 
w
h
a
t
 
h
a
p
p
e
n
s
 
w
h
e
n
 
w
e
 
a
d
d
 
a
 
n
u
m
b
e
r
 
t
o
 
t
h
e
 
v
a
l
u
e
s
 
a
n
d
 
w
h
a
t
 
h
a
p
p
e
n
s
 
w
h
e
n
 
w
e
 
m
u
l
t
i
p
l
y
 
t
h
e
 
n
u
m
b
e
r
s
 
i
n
 
t
h
e
 
a
r
r
a
y
:

```python
s
i
z
e
 
 
=
 
2
0


o
r
i
g
A
r
r
a
y
 
=
 
n
p
.
r
a
n
d
o
m
.
r
a
n
d
n
(
s
i
z
e
,
1
)
```

L
e
t
'
s
 
l
o
o
k
 
a
t
 
t
h
e
 
v
a
l
u
e
s
 
i
n
 
t
h
e
 
a
r
r
a
y
.

```python
p
r
i
n
t
(
o
r
i
g
A
r
r
a
y
)
```

T
h
e
r
e
 
s
e
e
m
 
t
o
 
b
e
 
a
 
v
a
r
i
e
t
y
 
o
f
 
n
u
m
b
e
r
s
,
 
s
o
m
e
 
p
o
s
i
t
i
v
e
,
 
s
o
m
e
 
n
e
g
a
t
i
v
e
,
 
a
s
 
e
x
p
e
c
t
e
d
 
b
e
c
a
u
s
e
 
`
r
a
n
d
n
`
 
i
s
 
s
u
p
p
o
s
e
d
 
t
o
 
g
e
n
e
r
a
t
e
 
n
u
m
b
e
r
s
 
c
e
n
t
e
r
e
d
 
a
t
 
0
 
(
i
.
e
.
,
 
w
i
t
h
 
m
e
a
n
 
0
)
 
a
n
d
 
s
t
a
n
d
a
r
d
 
d
e
v
i
a
t
i
o
n
 
o
f
 
1
.

L
e
t
'
s
 
c
o
m
p
u
t
e
 
t
h
e
 
s
t
a
n
d
a
r
d
 
d
e
v
i
a
t
i
o
n
 
a
n
d
 
m
e
a
n
 
o
f
 
t
h
e
s
e
 
n
u
m
b
e
r
s
.
 
N
u
m
p
y
 
p
r
o
v
i
d
e
s
 
t
o
 
h
a
n
d
y
 
m
e
t
h
o
d
s
:

```python
m
e
a
n
 
=
 
n
p
.
m
e
a
n
(
o
r
i
g
A
r
r
a
y
)


s
d
 
=
 
n
p
.
s
t
d
(
o
r
i
g
A
r
r
a
y
)


p
r
i
n
t
(
[
'
T
h
e
 
m
e
a
n
 
i
s
:
'
,
 
m
e
a
n
]
)


p
r
i
n
t
(
[
'
t
h
e
 
S
T
D
 
i
s
:
'
,
 
s
d
]
)
```

W
e
l
l
,
 
o
k
a
y
,
 
t
h
e
 
m
e
a
n
 
i
s
 
n
o
t
 
q
u
i
t
e
 
c
l
o
s
e
 
t
o
 
0
,
 
b
u
t
 
p
e
r
h
a
p
s
 
c
l
o
s
e
 
e
n
o
u
g
h
?
 
T
h
e
 
s
t
a
n
d
a
r
d
 
d
e
v
i
a
t
i
o
n
 
s
e
e
m
s
 
p
r
e
t
t
y
 
c
l
o
s
e
 
t
o
 
t
h
e
 
e
x
p
e
c
t
e
d
 
v
a
l
u
e
 
o
f
 
1
.

$
\
c
o
l
o
r
{
b
l
u
e
}
{
\
t
e
x
t
{
C
o
m
p
l
e
t
e
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
e
x
e
r
c
i
s
e
.
}
}
$


 
 


 
 
-
 
C
r
e
a
t
e
 
a
 
n
e
w
 
1
-
d
i
m
e
n
s
i
o
n
a
l
 
a
r
r
a
y
 
o
f
 
1
0
0
 
n
o
r
m
a
l
l
y
-
d
i
s
t
r
i
b
u
t
e
d
 
r
a
n
d
o
m
 
n
u
m
b
e
r
s
:


 
 


 
 
[
U
s
e
 
t
h
e
 
c
e
l
l
 
b
e
l
o
w
 
t
o
 
s
h
o
w
 
y
o
u
r
 
c
o
d
e
]



```python

```

 
 
 
-
 
W
h
a
t
 
h
a
p
p
e
n
s
 
t
o
 
t
h
e
 
m
e
a
n
 
a
n
d
 
s
t
a
n
d
a
r
d
 
d
e
v
i
a
t
i
o
n
 
a
f
t
e
r
 
i
n
c
r
e
a
s
i
n
g
 
t
h
e
 
s
i
z
e
 
o
f
 
t
h
e
 
a
r
r
a
y
?
 
A
r
e
 
t
h
e
y
 
c
l
o
s
e
r
 
o
f
 
f
u
r
t
h
e
r
 
f
r
o
m
 
t
h
e
 
e
x
p
e
c
t
e
d
 
v
a
l
u
e
s
?
 
W
h
y
?
 


 
 
 
 
 
 
 
 


 
 
[
U
s
e
 
t
h
e
 
c
e
l
l
 
b
e
l
o
w
 
t
o
 
s
h
o
w
 
y
o
u
r
 
c
o
d
e
]





W
h
a
t
 
h
a
p
p
e
n
s
 
i
f
 
w
e
 
a
d
d
 
5
 
t
o
 
t
h
e
 
a
r
r
a
y
?

```python
x
 
 
=
 
5
 
+
 
o
r
i
g
A
r
r
a
y
```

```python
p
r
i
n
t
(
x
)
```

I
t
 
l
o
o
k
s
 
l
i
k
e
 
t
h
e
 
v
a
l
u
e
s
 
s
h
i
f
t
e
d
.
 
B
u
t
 
h
o
w
 
m
u
c
h
?
 
I
t
 
l
o
o
k
s
 
l
i
k
e
 
t
h
e
y
 
r
e
c
e
n
t
e
r
e
d
 
a
t
 
5
,
 
t
h
e
 
v
a
l
u
e
 
w
e
 
a
d
d
e
d
.
 
S
o
 
w
e
 
c
a
n
 
p
e
r
h
a
p
s
 
a
s
s
u
m
e
 
t
h
a
t
 
n
o
w
 
t
h
e
 
d
i
s
t
r
i
b
u
t
i
o
n
 
o
f
 
n
u
m
b
e
r
s
 
i
s
 
n
o
r
m
a
l
l
y
 
d
i
s
t
r
i
b
u
t
e
d
 
b
u
t
 
w
i
t
h
 
a
 
m
e
a
n
 
o
f
 
5
.
 
T
h
e
 
s
t
a
n
d
a
r
d
 
d
e
v
i
a
t
i
o
n
 
h
a
s
 
n
o
t
 
b
e
e
 
c
h
a
n
g
e
d
.
 
I
t
 
i
s
 
s
t
i
l
l
 
a
t
 
1
,
 
t
r
u
s
t
 
m
e
 
f
o
r
 
t
h
e
 
m
o
m
e
n
t
 
a
n
d
 
l
e
t
 
t
r
y
 
m
u
l
t
i
p
l
y
i
n
g
 
t
h
e
 
n
u
m
b
e
r
s
.

```python
x
 
 
=
 
2
 
*
 
o
r
i
g
A
r
r
a
y


p
r
i
n
t
(
x
)
```

I
t
 
l
o
o
k
s
 
l
i
k
e
 
t
h
e
 
v
a
l
u
e
s
 
i
n
c
r
e
a
s
e
d
.
 
T
h
e
r
e
 
s
e
e
m
 
t
o
 
b
e
 
a
 
l
a
r
g
e
r
 
v
a
r
i
a
l
i
t
y
,
 
m
o
r
e
 
b
i
g
g
e
r
 
n
u
m
b
e
r
s
,
 
b
o
t
h
 
n
e
g
a
t
i
v
e
 
a
n
d
 
p
o
s
i
t
i
v
e
.
 
S
o
 
p
e
r
h
a
p
s
 
t
h
e
 
S
T
D
 
i
s
 
n
o
t
 
a
t
 
1
 
a
n
y
m
o
r
e
.
 
C
o
u
l
d
 
i
t
 
b
e
 
a
t
 
2
?

$
\
c
o
l
o
r
{
b
l
u
e
}
{
\
t
e
x
t
{
C
o
m
p
l
e
t
e
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
e
x
e
r
c
i
s
e
.
}
}
$


 
 


 
 
-
 
C
o
m
p
u
t
e
 
t
h
e
 
m
e
a
n
,
 
s
t
d
 
a
n
d
 
m
e
d
i
a
n
 
o
f
 
`
x
`
:


 
 


 
 
[
U
s
e
 
t
h
e
 
c
e
l
l
 
b
e
l
o
w
 
t
o
 
s
h
o
w
 
y
o
u
r
 
c
o
d
e
]



```python

```

 
 


 
 
-
 
W
h
a
t
 
a
r
e
 
t
h
e
 
m
e
a
n
,
 
s
t
d
 
a
n
d
 
m
e
d
i
a
n
 
o
f
 
`
x
`
?
 
W
h
y
,
 
w
h
a
t
 
i
s
 
g
o
i
n
g
 
o
n
 
h
e
r
e
?


 
 


 
 
[
U
s
e
 
t
h
e
 
c
e
l
l
 
b
e
l
o
w
 
t
o
 
s
h
o
w
 
a
n
s
w
e
r
 
i
n
 
y
o
u
r
 
o
w
n
 
w
o
r
d
s
]



#
#
#
 
S
u
m
m
a
r
y

S
o
 
i
n
 
t
h
i
s
 
t
u
t
o
r
i
a
l
 
w
e
 
h
a
v
e
 
s
h
o
w
n
 
h
o
w
 
t
o
 
o
r
g
a
n
i
z
e
 
a
n
d
 
m
a
n
i
p
u
l
a
t
e
 
d
a
t
a
 
u
s
i
n
g
 
P
y
t
h
o
n
 
`
n
u
m
p
y
`
 
`
a
r
r
a
y
s
`
.




S
o
 
t
h
o
s
e
 
a
r
e
 
t
h
e
 
b
a
s
i
c
s
 
o
f
 
n
u
m
p
y
 
a
r
r
a
y
s
.
 
T
h
e
y
:




*
 
s
t
o
r
e
 
v
a
l
u
e
s
 
i
n
 
r
o
w
s
 
a
n
d
 
c
o
l
u
m
n
s


*
 
e
a
c
h
 
d
i
m
e
n
s
i
o
n
 
s
t
a
r
t
s
 
a
t
 
i
n
d
e
x
 
z
e
r
o
 
(
l
i
k
e
 
l
i
s
t
s
)


*
 
c
a
n
 
b
e
 
a
c
c
e
s
s
e
d
 
u
s
i
n
g


 
 
 
 
-
 
s
q
u
a
r
e
 
b
r
a
c
k
e
t
s
 
`
[
]
`
 
w
i
t
h
 
r
o
w
 
a
n
d
 
c
o
l
u
m
n
 
i
n
d
e
x
e
s
 
s
e
p
a
r
a
t
e
d
 
b
y
 
a
 
c
o
m
m
a


 
 
 
 
-
 
i
n
t
e
g
e
r
 
i
n
d
e
x
e
s
 
(
i
n
c
l
u
d
i
n
g
 
n
e
g
a
t
i
v
e
 
"
s
t
a
r
t
 
f
r
o
m
 
t
h
e
 
e
n
d
"
 
i
n
d
e
x
e
s
)


 
 
 
 
-
 
a
 
c
o
l
o
n
 
`
:
`
 
(
o
r
 
t
w
o
 
i
f
 
y
o
u
 
w
a
n
t
 
a
 
s
t
e
p
 
v
a
l
u
e
 
o
t
h
e
r
 
t
h
a
n
 
1
)


*
 
c
a
n
 
h
a
v
e
 
m
a
t
h
s
 
d
o
n
e
 
t
o
 
e
v
e
r
y
 
e
l
e
m
e
n
t
 
i
n
 
o
n
e
 
g
o


*
 
c
a
n
 
b
e
 
a
d
d
e
d
,
 
s
u
b
t
r
a
c
t
e
d
,
 
e
t
c
.
 
f
r
o
m
 
o
n
e
 
a
n
o
t
h
e
r


*
 
h
a
v
e
 
s
u
p
e
r
p
o
w
e
r
s
!
 
t
h
e
y
 
c
a
n
 
c
o
m
p
u
t
e
 
s
t
u
f
f
 
a
l
o
n
g
 
t
h
e
i
r
 
r
o
w
s
 
a
n
d
 
c
o
l
u
m
n
s
!




T
h
e
 
o
p
e
r
a
t
i
o
n
s
 
t
h
a
t
 
a
r
e
 
a
v
a
i
l
a
b
l
e
 
f
o
r
 
t
h
e
s
e
 
t
w
o
 
d
a
t
a
 
t
y
p
e
s
 
w
i
l
l
 
b
e
 
t
h
e
 
b
a
s
e
 
f
o
r
 
m
a
n
y
 
t
h
i
n
g
s
 
t
h
a
t
 
y
o
u
 
m
i
g
h
t
 
n
e
e
d
 
t
o
 
d
o
 
a
s
 
a
 
D
a
t
a
 
S
c
i
e
n
t
i
s
t
.
 

`
N
u
m
p
y
 
a
r
r
a
y
s
`
 
C
a
n
 
h
o
s
t
 
a
 
v
a
r
i
e
t
y
 
o
f
 
d
a
t
a
 
t
y
p
e
s
.
 
A
l
t
h
o
u
g
h
 
t
h
i
s
 
m
i
g
h
t
 
b
e
 
t
o
o
 
m
u
c
h
 
f
o
r
 
n
o
w
,
 
b
e
l
o
w
 
a
 
t
a
b
l
e
 
o
f
 
a
l
l
 
t
h
e
 
d
a
t
a
 
t
y
p
e
s
 
a
n
 
`
a
r
r
a
y
`
 
c
a
n
 
s
u
p
p
o
r
t
:

|
 
T
y
p
e
	
|
 
D
e
s
c
r
i
p
t
i
o
n
 
|


|
 
-
-
-
 
|
 
-
-
-
 
|


|
 
b
o
o
l
 
|
	
B
o
o
l
e
a
n
 
(
T
r
u
e
 
o
r
 
F
a
l
s
e
)
 
s
t
o
r
e
d
 
a
s
 
a
 
b
i
t
 
(
0
,
 
1
)
 
|


|
 
i
n
t
i
	
|
 
P
l
a
t
f
o
r
m
 
i
n
t
e
g
e
r
 
(
n
o
r
m
a
l
l
y
 
e
i
t
h
e
r
 
i
n
t
3
2
 
o
r
 
i
n
t
6
4
)
 
|


|
 
i
n
t
8
	
|
 
B
y
t
e
 
(
-
1
2
8
 
t
o
 
1
2
7
)
 
|


|
 
i
n
t
1
6
	
|
 
I
n
t
e
g
e
r
 
(
-
3
2
7
6
8
 
t
o
 
3
2
7
6
7
)
 
|


|
 
i
n
t
3
2
	
|
 
I
n
t
e
g
e
r
 
(
-
2
 
*
*
 
3
1
 
t
o
 
2
 
*
*
 
3
1
 
-
1
)
 
|


|
 
i
n
t
6
4
	
|
 
I
n
t
e
g
e
r
 
(
-
2
 
*
*
 
6
3
 
t
o
 
2
 
*
*
 
6
3
 
-
1
)
 
|


|
 
u
i
n
t
8
	
|
 
U
n
s
i
g
n
e
d
 
i
n
t
e
g
e
r
 
(
0
 
t
o
 
2
5
5
)
 
|


|
 
u
i
n
t
1
6
	
|
 
U
n
s
i
g
n
e
d
 
i
n
t
e
g
e
r
 
(
0
 
t
o
 
6
5
5
3
5
)
 
|


|
 
u
i
n
t
3
2
	
|
 
U
n
s
i
g
n
e
d
 
i
n
t
e
g
e
r
 
(
0
 
t
o
 
2
 
*
*
 
3
2
 
–
 
1
)
 
|


|
 
u
i
n
t
6
4
	
|
 
U
n
s
i
g
n
e
d
 
i
n
t
e
g
e
r
 
(
0
 
t
o
 
2
 
*
*
 
6
4
 
–
 
1
)
 
|


|
 
f
l
o
a
t
1
6
	
|
 
H
a
l
f
 
p
r
e
c
i
s
i
o
n
 
f
l
o
a
t
:
 
s
i
g
n
 
b
i
t
,
 
5
 
b
i
t
s
 
e
x
p
o
n
e
n
t
,
 
a
n
d
 
1
0
 
b
i
t
s
 
m
a
n
t
i
s
s
a
 
|


|
 
f
l
o
a
t
3
2
	
|
 
S
i
n
g
l
e
 
p
r
e
c
i
s
i
o
n
 
f
l
o
a
t
:
 
s
i
g
n
 
b
i
t
,
 
8
 
b
i
t
s
 
e
x
p
o
n
e
n
t
,
 
a
n
d
 
2
3
 
b
i
t
s
 
m
a
n
t
i
s
s
a
 
|


|
 
f
l
o
a
t
6
4
 
o
r
 
f
l
o
a
t
	
|
 
D
o
u
b
l
e
 
p
r
e
c
i
s
i
o
n
 
f
l
o
a
t
:
 
s
i
g
n
 
b
i
t
,
 
1
1
 
b
i
t
s
 
e
x
p
o
n
e
n
t
,
 
a
n
d
 
5
2
 
b
i
t
s
 
m
a
n
t
i
s
s
a
 
|


|
 
c
o
m
p
l
e
x
6
4
	
|
 
C
o
m
p
l
e
x
 
n
u
m
b
e
r
,
 
r
e
p
r
e
s
e
n
t
e
d
 
b
y
 
t
w
o
 
3
2
-
b
i
t
 
f
l
o
a
t
s
 
(
r
e
a
l
 
a
n
d
 
i
m
a
g
i
n
a
r
y
 
c
o
m
p
o
n
e
n
t
s
)
 
|


|
 
c
o
m
p
l
e
x
1
2
8
 
o
r
 
c
o
m
p
l
e
x
	
|
 
C
o
m
p
l
e
x
 
n
u
m
b
e
r
,
 
r
e
p
r
e
s
e
n
t
e
d
 
b
y
 
t
w
o
 
6
4
-
b
i
t
 
f
l
o
a
t
s
 
(
r
e
a
l
 
a
n
d
 
i
m
a
g
i
n
a
r
y
 
c
o
m
p
o
n
e
n
t
s
)
 
|

$
\
c
o
l
o
r
{
b
l
u
e
}
{
\
t
e
x
t
{
C
o
m
p
l
e
t
e
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
e
x
e
r
c
i
s
e
.
}
}
$


 
 


 
 
-
 
G
e
n
e
r
a
t
e
 
a
n
 
1
-
D
 
a
r
r
a
y
 
o
f
 
m
e
a
n
 
=
 
1
0
 
a
n
d
 
s
t
d
 
=
 
1
.
5
:


 
 


 
 
[
U
s
e
 
t
h
e
 
c
e
l
l
 
b
e
l
o
w
 
t
o
 
s
h
o
w
 
y
o
u
r
 
c
o
d
e
]

```python

```
