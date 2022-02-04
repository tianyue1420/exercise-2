from numbers import Number


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        # if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        elif isinstance(other, Polynomial):
            # Work out how many coefficient places.
            common = min(self.degree(), other.degree()) + 1
            # Sum the common coefficient positions.
            coefs = tuple(a + b for a, b in zip(self.coefficients[:common],
                                                other.coefficients[:common]))

            # Append the high degree coefs from the higher degree summand.
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):

        if isinstance(other, Number):
            return Polynomial((self.coefficients[0] - other,)
                              + self.coefficients[1:])
        elif isinstance(other, Polynomial):
            # Work out how many coeff places the two polys have in common.
            common = min(self.degree(), other.degree()) + 1
            # Sum the common coefficient positions.
            coefs = tuple(a - b for a, b in zip(self.coefficients[:common],
                                                other.coefficients[:common]))

            # Append the high degree coeffs from the higher degree summand.
            coefs += self.coefficients[common:] + tuple(-a for a in other.coefficients[common:])

            return Polynomial(coefs)

        else:
            return NotImplemented

    def __rsub__(self, other):

        return ((self - other) - (self - other)) - (self - other)

    def __mul__(self, other):
        if isinstance(other, Number):
            coefs = tuple(n * other for n in self.coefficients)
            return Polynomial(coefs)

        elif isinstance(other, Polynomial):
            zhuzhulist = [0]*(self.degree() + other.degree() + 1)
            for i, self.c in enumerate(self.coefficients):
                for j, other.c in enumerate(other.coefficients):
                    zhuzhulist[i + j] += self.c * other.c
            coefs = tuple(zhuzhulist)
            return Polynomial(coefs)

        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __pow__(self, other):
        a = 1
        for i in range(other):
            a = a * self
        return a

    def __call__(self, other):
        zhuzhu = 0
        for n, zhucoef in enumerate(self.coefficients):
            zhuzhu += zhucoef * other ** n
        return zhuzhu

    def dx(self):
        if self.degree() == 0:
            return Polynomial((0,))
        elif self.degree() > 0:
            zhulist = [0] * (self.degree())
            for n, zhucoef in enumerate(self.coefficients[1:]):
                zhulist[n] = (n + 1) * zhucoef
            coefs = tuple(zhulist)
            return Polynomial(coefs)
        else:
            return NotImplemented


def derivative(a):
    return Polynomial.dx(a)