# FracNew.ipynb: Class Frac

import gcd


class Frac:

    """ Fractional class. A Frac is a pair of integers num, den

        (with den != 0) whose GCD is 1.

    """

    def __init__(self, n, d):

        """ Construct a Frac from integers n and d.

            Needs error message if d = 0!

        """

        ########################################################################

        # TODO 1:                                                              # 

        # warn the user and execute the return statement to terminate the      #

        # function if argument d is zero.                                      #

        #                                                                      #

        ########################################################################

        pass

        if d==0:

            print("WARNING d=0")

            return

        hcf = gcd.gcd(n, d)

        self.num, self.den = n/hcf, d/hcf



    def __str__(self):

        """ Generate a string representation of a Frac. """

        ########################################################################

        # TODO 2:                                                              # 

        # rvise the __str__ function so that self.num only is returned if      #

        # self.den is 1.                                                       #

        #                                                                      #

        ########################################################################

        pass

        if self.den == 1:

            return "%d" %(self.num )

        return "%d/%d" %(self.num, self.den)



    def __mul__(self, another):

        """ Multiply two Fracs to product a Frac. """

        return Frac(self.num * another.num, self.den * another.den)



    def __add__(self, another):

        """ Add two Fracs to product a Frac. """

        return Frac(self.num * another.den + self.den * another.num, self.den * another.den)



    def to_real(self):

        """ return floating point value of Frac. """

        return float(self.num)/float(self.den)



    def __sub__(self, another):

        """ Subtract one Frac from the other. """

        ########################################################################

        # TODO 3:                                                              # 

        # fill in the __sub__ function to implement fraction subtraction.      #

        #                                                                      #

        ########################################################################

        pass

        return Frac(self.num * another.den - self.den * another.num, self.den * another.den)



    def __truediv__(self, another):

        """ Divide one Frac from the other. """

        ########################################################################

        # TODO 4:                                                              # 

        # fill in the __truediv__ function to implement fraction division.     #

        #                                                                      #

        ########################################################################

        pass

        return Frac(self.num * another.den, self.den * another.num)


import gcd

class Frac:

    """ Fractional class. A Frac is a pair of integers num, den

        (with den != 0) whose GCD is 1.

    """

    def __init__(self, n, d):

        """ Construct a Frac from integers n and d.

            Needs error message if d = 0!

        """

        ########################################################################

        # TODO 1:                                                              # 

        # warn the user and execute the return statement to terminate the      #

        # function if argument d is zero.                                      #

        #                                                                      #

        ########################################################################

        pass

        if d==0:

            print("WARNING d=0")

            return

        hcf = gcd.gcd(n, d)

        self.num, self.den = n/hcf, d/hcf



    def __str__(self):

        """ Generate a string representation of a Frac. """

        ########################################################################

        # TODO 2:                                                              # 

        # rvise the __str__ function so that self.num only is returned if      #

        # self.den is 1.                                                       #

        #                                                                      #

        ########################################################################

        pass

        if self.den == 1:

            return "%d" %(self.num )

        return "%d/%d" %(self.num, self.den)



    def __mul__(self, another):

        """ Multiply two Fracs to product a Frac. """

        return Frac(self.num * another.num, self.den * another.den)



    def __add__(self, another):

        """ Add two Fracs to product a Frac. """

        return Frac(self.num * another.den + self.den * another.num, self.den * another.den)



    def to_real(self):

        """ return floating point value of Frac. """

        return float(self.num)/float(self.den)



    def __sub__(self, another):

        """ Subtract one Frac from the other. """

        ########################################################################

        # TODO 3:                                                              # 

        # fill in the __sub__ function to implement fraction subtraction.      #

        #                                                                      #

        ########################################################################

        pass

        return Frac(self.num * another.den - self.den * another.num, self.den * another.den)



    def __truediv__(self, another):

        """ Divide one Frac from the other. """

        ########################################################################

        # TODO 4:                                                              # 

        # fill in the __truediv__ function to implement fraction division.     #

        #                                                                      #

        ########################################################################

        pass

        return Frac(self.num * another.den, self.den * another.num)


x = Frac(3, 0)

y = Frac(4, 12)

print("y=", y)

z = Frac(4, 1)

print("z=", z)

a = Frac(24, 56)

b = Frac(3, 8)

print("sum=", a + b)

print("difference=", a - b)

print("product=", a * b)

print("ratio=", a / b)