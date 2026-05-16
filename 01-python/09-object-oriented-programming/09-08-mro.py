class A:
    name = "Hello"
    label = "A: Base class"

class B(A):
    label = "B: Derived class"

class C(A):
    label = "C: Derived class"

class D(B, C):
    label = "D: Derived class"

test = D()

print(test.label) # Output: B: Derived class, because of MRO (Method Resolution Order) - B is listed before C in the class definition of D
print(test.name) # Output: Hello
print(D.__mro__) # Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
print(B.__mro__) # Output: (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
print(A.__mro__) # Output: (<class '__main__.A'>, <class 'object'>)
