
class Value:
    def __init__(self, value, is_none=False):
        self.is_none = is_none
        self.value = value

    def internal_number(self):
        return self.value

    def change_value(self, new_value):
        if new_value is None:
            self.value = None
            self.is_none = True
        else:
            self.value = new_value

    def internal_string(self):
        return str(self.value)

    def internal_array(self):
        return list(self.value)

    def actual_array(self):
        arr = []
        for el in self.internal_array():
            arr.append(el.value)
        return arr

    def internal_float(self):
        return float(self.value)

    def is_string(self):
        return isinstance(self.value, str)

    def is_number(self):
        return isinstance(self.value, int) or isinstance(self.value, float)

    def is_float(self):
        return isinstance(self.value, float)

    def is_array(self):
        return isinstance(self.value, list)

    def check_none(self):
        return self.is_none

    def is_true(self):
        try:
            if self.is_number():
                return self.internal_number() != 0
            else:
                raise ValueError(f"Value {self.value} is not a number")
        except ValueError:
            raise

    def is_false(self):
        try:
            if self.is_number():
                return self.internal_number() == 0
            else:
                raise ValueError(f"Value {self.value} is not a number")
        except ValueError:
            raise

    def arithm_eval(self, right, lam):
        try:
            if self.is_number() and right.is_number():
                return Value(lam(self.internal_number(), right.internal_number()))
            else:
                raise ValueError(f"Some of values is not a number")
        except ValueError:
            raise

    def mul(self, right):
        return self.arithm_eval(right, lambda x, y: x * y)

    def div(self, right):
        return self.arithm_eval(right, lambda x, y: x / y)

    def idiv(self, right):
        return self.arithm_eval(right, lambda x, y: x // y)

    def mod(self, right):
        return self.arithm_eval(right, lambda x, y: x % y)

    def add(self, right):
        if self.is_string() or right.is_string():
            if self.is_array():
                return Value(str(self.actual_array())+str(right.value))
            elif right.is_array():
                return Value(str(self.value) + str(right.actual_array()))

            return Value(str(self.value) + str(right.value))



        return self.arithm_eval(right, lambda x, y: x + y)

    def sub(self, right):
        return self.arithm_eval(right, lambda x, y: x - y)

    def relations_eval(self, right, lam):
        try:
            if self.is_number() and right.is_number():
                if lam(self.internal_number(), right.internal_number()):
                    return Value(1)
                else:
                    return Value(0)
            else:
                raise ValueError(f"Both of values must be ints or strings")
        except ValueError:
            raise

    def gt(self, right):
        return self.relations_eval(right, lambda x, y: x > y)

    def gte(self, right):
        return self.relations_eval(right, lambda x, y: x >= y)

    def lt(self, right):
        return self.relations_eval(right, lambda x, y: x < y)

    def lte(self, right):
        return self.relations_eval(right, lambda x, y: x <= y)

    def eq(self, right):
        if self.is_string() and right.is_string():
            if self.internal_string() == right.internal_string():
                return Value(1)
            else:
                return Value(0)

        return self.relations_eval(right, lambda x, y: x==y)

    def neq(self, right):
        val = self.eq(right)
        if val.internal_number() == 1:
            return Value(0)
        else:
            return Value(1)

    def mnot(self):
        try:
            if self.is_number():
                if self.internal_number() == 0:
                    return Value(1)
                else:
                    return Value(0)
            else:
                raise ValueError(f"Incorrect value")
        except ValueError:
            raise

    def mand(self, right):
        if self.is_true() and right.is_true():
            return Value(1)
        else:
            return Value(0)

    def mor(self, right):
        if self.is_true() or right.is_true():
            return Value(1)
        else:
            return Value(0)

    def exp(self, right):
        try:
            if self.is_number() and right.is_number():
                return Value(round(self.internal_number()**right.internal_number()))
            else:
                raise ValueError(f"Both of values must be numbers")
        except ValueError:
            raise
