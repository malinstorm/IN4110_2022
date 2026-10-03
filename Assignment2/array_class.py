class Array:
    """
    Homemade array class with simple numpy-like operations.
    Supports 1D and 2D arrays with int, float and bool values.
    """

    def __init__(self, shape, *values):

        # gjør om shape til tuple hvis bare et tall blir sendt inn
        if isinstance(shape, int):
            shape = (shape,)

        if not isinstance(shape, tuple) or len(shape) == 0:
            raise TypeError("Shape must be an int or tuple")

        for dim in shape:
            if not isinstance(dim, int) or dim <= 0:
                raise ValueError("Shape must contain positive integers")

        self.shape = shape

        # flater ut verdiene slik at både
        # Array((4,), 1,2,3,4) og Array((4,), [1,2,3,4]) fungerer
        self.values = self._flatten(values)

        expected_length = 1

        for dim in self.shape:
            expected_length *= dim

        if len(self.values) != expected_length:
            raise ValueError(
                f"Shape {self.shape} needs {expected_length} values, "
                f"got {len(self.values)}"
            )

        for value in self.values:
            if not isinstance(value, (int, float, bool)):
                raise TypeError("Only int, float and bool are accepted")


    def _flatten(self, values):

        result = []

        for value in values:
            if isinstance(value, (list, tuple)):
                result.extend(self._flatten(value))
            else:
                result.append(value)

        return result


    def is_scalar(self, number):

        return isinstance(number, (int, float)) and not isinstance(number, bool)


    def __len__(self):

        return len(self.values)


    def __getitem__(self, key):

        # vanlig 1D-indeksering
        if isinstance(key, int):
            return self.values[key]

        # enkel 2D-indeksering: array[row, col]
        if isinstance(key, tuple) and len(self.shape) == 2 and len(key) == 2:

            row, col = key
            rows, cols = self.shape

            if row < 0:
                row += rows

            if col < 0:
                col += cols

            if row < 0 or row >= rows or col < 0 or col >= cols:
                raise IndexError("Array index out of range")

            return self.values[row * cols + col]

        raise TypeError("Invalid index")


    def _nested_values(self):

        # brukes bare for å skrive 2D-array litt penere
        if len(self.shape) == 1:
            return self.values

        if len(self.shape) == 2:

            rows, cols = self.shape

            return [
                self.values[row * cols:(row + 1) * cols]
                for row in range(rows)
            ]

        return self.values


    def __str__(self):

        return str(self._nested_values())


    def __repr__(self):

        return f"Array(shape={self.shape}, values={self._nested_values()})"


    def _check_array(self, other):

        if not isinstance(other, Array):
            raise TypeError("Expected another Array")

        if self.shape != other.shape:
            raise ValueError("Arrays must have the same shape")


    def _check_arithmetic_values(self, values):

        # bool brukes som egen datatype, men ikke i regneoperasjoner
        for value in values:
            if isinstance(value, bool):
                raise TypeError("Datatype bool is not allowed for this operation")


    def __add__(self, other):

        self._check_arithmetic_values(self.values)

        if isinstance(other, Array):

            self._check_array(other)
            self._check_arithmetic_values(other.values)

            result = []

            for key in range(len(self.values)):
                result.append(self.values[key] + other.values[key])

            return Array(self.shape, *result)

        if self.is_scalar(other):

            result = []

            for value in self.values:
                result.append(value + other)

            return Array(self.shape, *result)

        return NotImplemented


    def __radd__(self, other):

        return self.__add__(other)


    def __sub__(self, other):

        self._check_arithmetic_values(self.values)

        if isinstance(other, Array):

            self._check_array(other)
            self._check_arithmetic_values(other.values)

            result = []

            for key in range(len(self.values)):
                result.append(self.values[key] - other.values[key])

            return Array(self.shape, *result)

        if self.is_scalar(other):

            result = []

            for value in self.values:
                result.append(value - other)

            return Array(self.shape, *result)

        return NotImplemented


    def __rsub__(self, other):

        self._check_arithmetic_values(self.values)

        if self.is_scalar(other):

            result = []

            for value in self.values:
                result.append(other - value)

            return Array(self.shape, *result)

        return NotImplemented


    def __mul__(self, other):

        self._check_arithmetic_values(self.values)

        if isinstance(other, Array):

            self._check_array(other)
            self._check_arithmetic_values(other.values)

            result = []

            for key in range(len(self.values)):
                result.append(self.values[key] * other.values[key])

            return Array(self.shape, *result)

        if self.is_scalar(other):

            result = []

            for value in self.values:
                result.append(value * other)

            return Array(self.shape, *result)

        return NotImplemented


    def __rmul__(self, other):

        return self.__mul__(other)


    def __eq__(self, other):

        # samme shape og samme verdier
        if not isinstance(other, Array):
            return False

        return self.shape == other.shape and self.values == other.values


    def is_equal(self, other):

        # hjemmelaget variant av elementvis equality
        self._check_array(other)

        result = []

        for key in range(len(self.values)):
            result.append(self.values[key] == other.values[key])

        return Array(self.shape, *result)


    def min_element(self):

        self._check_arithmetic_values(self.values)

        minimum = self.values[0]

        for value in self.values:
            if value < minimum:
                minimum = value

        return minimum


    def mean_element(self):

        self._check_arithmetic_values(self.values)

        total = 0

        for value in self.values:
            total += value

        return float(total / len(self.values))