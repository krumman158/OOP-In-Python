# MRO = Method Resolution Order — the order Python follows to search for a method/attribute in a class hierarchy (especially in multiple inheritance), based on the C3 linearization algorithm.

# It solves the diamond problem


class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

# It first checks D as D don't has show then it looks first class inherited i: B then so on.
d = D()
d.show()  # Output: B (searches D -> B -> C -> A)

print(D.__mro__)  
# (D, B, C, A, object)
