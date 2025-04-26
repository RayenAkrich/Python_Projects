class Polynome:
    def __init__(self, coefs):
        if not coefs:
            coefs = [0]
        last_non_zero = len(coefs) - 1
        while last_non_zero >= 0 and coefs[last_non_zero] == 0:
            last_non_zero -= 1
        if last_non_zero == -1:
            self.coefs = [0]
            self.degre = -1
        else:
            self.coefs = coefs[:last_non_zero + 1]
            self.degre = last_non_zero

    def __repr__(self):
        if self.degre == -1:
            return "0"
        terms = []
        for i in range(len(self.coefs)):
            coef = self.coefs[i]
            if coef < 0:
                term = "(" + str(coef) + ")*X**" + str(i)
            else:
                term = str(coef) + "*X**" + str(i)
            terms.append(term)
        
        result = ""
        for term in terms:
            result += term + " + "
        result = result.rstrip(" + ").replace("+ -", "- ")
        return result

    def __getitem__(self, i):
        if i < 0 or i > self.degre:
            return 0
        return self.coefs[i]

    def __call__(self, x):
        result = 0
        for i in range(len(self.coefs)):
            result += self.coefs[i] * (x ** i)
        return result

    def __add__(self, other):
        max_deg = max(self.degre, other.degre)
        new_coefs = [0] * (max_deg + 1)
        for i in range(max_deg + 1):
            new_coefs[i] = self[i] + other[i]
        return Polynome(new_coefs)

class Monome(Polynome):
    def __init__(self, coefficient, degre):
        if degre < 0:
            raise ValueError("Degré invalide")
        coefs = [0 for _ in range(degre + 1)]
        coefs[degre] = coefficient
        super().__init__(coefs)

    def __repr__(self):
        if self.degre == -1:
            return "0"
        coef = self.coefs[self.degre]
        if coef == 0:
            return "0"
        if coef < 0:
            return "(" + str(coef) + ")*X**" + str(self.degre)
        else:
            return str(coef) + "*X**" + str(self.degre)

    def __call__(self, x):
        return self.coefs[self.degre] * (x ** self.degre)
