import math
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y, nom):
        self.x = x
        self.y = y
        self.nom = nom

    def __repr__(self):
        return self.nom + "(" + "{:.1f}".format(self.x) + ", " + "{:.1f}".format(self.y) + ")"

    def dessiner(self):
        plt.scatter(self.x, self.y)
        plt.annotate(self.nom, (self.x, self.y))

    def milieu(self, B):
        mid_x = (self.x + B.x) / 2
        mid_y = (self.y + B.y) / 2
        return Point(mid_x, mid_y, "M_" + self.nom + B.nom)

class Polygone:
    
    def __init__(self, sommets):
        self.sommets = sommets
        
    def aire(self):
        n = len(self.sommets)
        if n < 3:
            return 0.0
        s = 0.0
        for i in range(n):
            xi, yi = self.sommets[i].x, self.sommets[i].y
            xj, yj = self.sommets[(i+1)%n].x, self.sommets[(i+1)%n].y
            s += (xi + xj) * (yi - yj)
        return abs(s) / 2
        
    def __repr__(self):
        points = ""
        for s in self.sommets:
            points += str(s) + ", "
        points = points.rstrip(", ")
        return "polygone [" + points + "]"
    
    
    def dessiner(self):
        x = [p.x for p in self.sommets] + [self.sommets[0].x]
        y = [p.y for p in self.sommets] + [self.sommets[0].y]
        plt.plot(x, y, marker='o')
        for p in self.sommets:
            p.dessiner()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.show()
        

class Triangle(Polygone):
    def __init__(self, a, b, c):
        super().__init__([a, b, c])

class Rectangle(Polygone):
    def __init__(self, xMin, xMax, yMin, yMax):
        a = Point(xMin, yMin, 'A')
        b = Point(xMax, yMin, 'B')
        c = Point(xMax, yMax, 'C')
        d = Point(xMin, yMax, 'D')
        super().__init__([a, b, c, d])

class PolygoneRegulier(Polygone):
    def __init__(self, c, n):
        self.centre = c
        self.n = n
        sommets = []
        for k in range(n):
            angle = 2 * math.pi * k / n
            x = c.x + math.cos(angle)
            y = c.y + math.sin(angle)
            sommets.append(Point(x, y, "P" + str(k)))
        super().__init__(sommets)

# Programme de test
if __name__ == "__main__":
    # Test Polynôme
    P = Polynome([5, 12, 0, -9, 0, 7])
    print("Polynôme P:", P)
    print("Coeff degré 3:", P[3])
    print("P(2) =", P(2))
    M = Monome(2, 3)
    print("Monôme M:", M)
    print("M(2) =", M(2))
    S = P + M
    print("Somme P + M:", S)
    # P._trace(-2, 2)

    # Test Polygone
    A = Point(1, 1, 'A')
    B = Point(5, 1, 'B')
    C = Point(3, 3, 'C')
    poly = Polygone([A, B, C])
    print(poly)
    print("Aire:", poly.aire())
    # poly.dessiner()

    tri = Triangle(A, B, C)
    rect = Rectangle(0, 4, 0, 2)
    print(rect)
    print("Aire rectangle:", rect.aire())

    pentagone = PolygoneRegulier(Point(0, 0, 'O'), 5)
    print(pentagone)
    # pentagone.dessiner()