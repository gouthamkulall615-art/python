class Vector:
    def __init__(self, vec):
        self.vec = vec

    # Overloading + operator
    def __add__(self, other):
        result = []
        for i in range(len(self.vec)):
            result.append(self.vec[i] + other.vec[i])
        return Vector(result)

    # Overloading * operator (Dot Product)
    def __mul__(self, other):
        dot = 0
        for i in range(len(self.vec)):
            dot += self.vec[i] * other.vec[i]
        return dot

    # String representation
    def __str__(self):
        return str(self.vec)


# Driver Code
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("Vector 1:", v1)
print("Vector 2:", v2)

print("Addition:", v1 + v2)
print("Dot Product:", v1 * v2)