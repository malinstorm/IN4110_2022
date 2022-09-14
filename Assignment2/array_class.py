#from array_class import Array


class Array:

    def __init__(self, shape, *values):

        self.shape = shape
        self.values = list(values)
        self.list = list

        for key in range(len(self.values)):
            self.values


    def is_scalar(self,number):
        if isinstance(number, (int, float)): # or isinstance(self.values, float):
            return True
        else: return False

    def scalar(self,shape,other,lenght):
        if shape == 1:
            scalar = []
            for key in range(lenght):
                scalar.append(other)

            return scalar, lenght
        else: print("Not defined")


    def __len__(self):
        return len(self.values) #, len(other.values)

    def __getitem__(self, key):

        return self.values[key]
        # homemade function to check the validity of the arrays regarding shape and datatypes
    def dtypes_uniformity_compatability(self,values,other,shape1,shape2):

        if all(type(key) is type(self.values[0]) for key in other) and all(type(key) is type(other[0]) for key in self.values):
            #dobbeltsjekker datatyper - plass for plass
            # Check that the amount of values corresponds to the shape
            if self.values.__len__() == shape1[0] and len(other) == shape2[0]: # om lengdene er lik shape
                for key in range(len(self.values)):
                # Check if the values are not of valid types and returns the values if TypeError not raised
                    if (isinstance(self.values[key], int) or isinstance(self.values[key],float) or isinstance(self.values[key],bool)
                        or isinstance(other[key], int) or isinstance(other[key],float) or isinstance(other[key],bool)):

                        if type(other[key]) == type(self.values[key]): # tester om indeksene er like seg i array
                            return True
                        else: return False

                        return True

                    else: raise TypeError("Not accepted datatypes")
                #return True
            else: raise ValueError("Not same lenght") #return False

            return True

        else: raise TypeError("Different datatypes")

    def __str__(self):

        return f"{self.values}" #return a string of the values

    def __add__(self, other):

        list = []

        if not(self.is_scalar(other)): # sjekker at other er et array

            if (self.dtypes_uniformity_compatability(self.values, other.values, self.shape,other.shape)): #checks the datatypes, checks if same lenght shape/values.

                for key in range(len(self.values)):
                        #Makes sure it is not boolean values
                        if type(self.values[key]) == bool or type(other.values[key]) == bool:
                            return NotImplemented
                        else: list.append(self.values[key] + other.values[key])

                return Array(self.shape,list)
            else: return NotImplemented

        else: # om other er en en skalar

            shape_scalar = 1
            other, lenght = Array.scalar(self,shape_scalar,other,len(self.values)) #omgjør til et array med lengde lik len(self.values) eks skalar 10 = [10,10,10,10]
            lenght = (lenght,)
            if (self.dtypes_uniformity_compatability(self.values, other, self.shape, lenght)): #checks the datatypes, checks if same lenght.

                for key in range(len(self.values)):
                    if type(self.values[key]) == bool or type(other[key]) == bool:
                        return NotImplemented
                    else:
                        list.append(self.values[key] + other[key])

                return Array(self.shape,list) #turn the list into an array by instansiating an object of class Array

            else: return NotImplemented


    def __radd__(self, other):

        list = []

        if not(self.is_scalar(other)): # sjekker at other er et array

            if (self.dtypes_uniformity_compatability(self.values, other.values, self.shape,other.shape)): #checks the datatypes, checks if same lenght shape/values.

                for key in range(len(self.values)):
                    #Makes sure it is not boolean values
                    if type(self.values[key]) == bool or type(other.values[key]) == bool:
                        return NotImplemented
                    else: list.append(self.values[key] + other.values[key])

                return Array(self.shape,list)
            else: return NotImplemented

        else: # om other er en en skalar

            shape_scalar = 1
            other, lenght = Array.scalar(self,shape_scalar,other,len(self.values)) #omgjør til et array med lengde lik len(self.values) eks skalar 10 = [10,10,10,10]
            lenght = (lenght,)
            if (self.dtypes_uniformity_compatability(self.values, other, self.shape, lenght)): #checks the datatypes, checks if same lenght.

                for key in range(len(self.values)):
                    if type(self.values[key]) == bool or type(other[key]) == bool:
                        return NotImplemented
                    else:
                        list.append(self.values[key] + other[key])

                return Array(self.shape,list) #turn the list into an array by instansiating an object of class Array

            else: return NotImplemented

    def __sub__(self, other):

        list = []

        if not(self.is_scalar(other)): # sjekker at other er et array ENDRET HER

            if (self.dtypes_uniformity_compatability(self.values, other.values, self.shape, other.shape)): #checks the datatypes, checks if same lenght shape/values.

                for key in range(len(self.values)):
                        #Makes sure it is not boolean values
                        if type(self.values[key]) == bool or type(other.values[key]) == bool:
                            return NotImplemented
                        else: list.append(self.values[key] - other.values[key])

                return Array(self.shape,list)
            else: return NotImplemented

        else: # om other er en en skalar

            shape_scalar = 1
            other, lenght = Array.scalar(self,shape_scalar,other,len(self.values)) #omgjør til et array med lengde lik len(self.values) eks skalar 10 = [10,10,10,10]
            lenght = (lenght,)

            if (self.dtypes_uniformity_compatability(self.values, other, self.shape, lenght)): #checks the datatypes, checks if same lenght.

                for key in range(len(self.values)):
                    if type(self.values[key]) == bool or type(other[key]) == bool:
                        return NotImplemented
                    else:
                        list.append(self.values[key] - other[key])
                return Array(self.shape,list) #turn the list into an array by instansiating an object of class Array

            else: return NotImplemented


    def __rsub__(self, other):

        list = []

        if not(self.is_scalar(other)): # sjekker at other er et array

            if (self.dtypes_uniformity_compatability(self.values, other.values, self.shape,other.shape)): #checks the datatypes, checks if same lenght shape/values.

                for key in range(len(self.values)):
                        #Makes sure it is not boolean values
                        if type(self.values[key]) == bool or type(other.values[key]) == bool:
                            return NotImplemented
                        else: list.append(self.values[key] - other.values[key])

                return Array(self.shape,list)
            else: return NotImplemented

        else: # om other er en en skalar

            shape_scalar = 1
            other, lenght = Array.scalar(self,shape_scalar,other,len(self.values)) #omgjør til et array med lengde lik len(self.values) eks skalar 10 = [10,10,10,10]
            lenght = (lenght,)
            if (self.dtypes_uniformity_compatability(self.values, other, self.shape, lenght)): #checks the datatypes, checks if same lenght.

                for key in range(len(self.values)):
                    if type(self.values[key]) == bool or type(other[key]) == bool:
                        return NotImplemented
                    else:
                        #list.append(self.values[key] - other[key])
                        list.append(other[key] - self.values[key])

                return Array(self.shape,list) #turn the list into an array by instansiating an object of class Array

            else: return NotImplemented


    def __mul__(self, other):

        list = []

        if not(self.is_scalar(other)): # sjekker at other er et array

            if (self.dtypes_uniformity_compatability(self.values, other.values, self.shape,other.shape)): #checks the datatypes, checks if same lenght shape/values.

                for key in range(len(self.values)):
                        #Makes sure it is not boolean values
                        if type(self.values[key]) == bool or type(other.values[key]) == bool:
                            return NotImplemented
                        else: list.append(self.values[key] * other.values[key])

                return Array(self.shape,list)
            else: return NotImplemented

        else: # om other er en en skalar

            shape_scalar = 1
            other, lenght = Array.scalar(self,shape_scalar,other,len(self.values)) #omgjør til et array med lengde lik len(self.values) eks skalar 10 = [10,10,10,10]
            lenght = (lenght,)
            if (self.dtypes_uniformity_compatability(self.values, other, self.shape, lenght)): #checks the datatypes, checks if same lenght.

                for key in range(len(self.values)):
                    if type(self.values[key]) == bool or type(other[key]) == bool:
                        return NotImplemented
                    else:
                        list.append(self.values[key] * other[key])

                return Array(self.shape,list) #turn the list into an array by instansiating an object of class Array

            else: return NotImplemented


    def __rmul__(self, other):

        list = []

        if not(self.is_scalar(other)): # sjekker at other er et array

            if (self.dtypes_uniformity_compatability(self.values, other.values, self.shape,other.shape)): #checks the datatypes, checks if same lenght shape/values.

                for key in range(len(self.values)):
                        #Makes sure it is not boolean values
                        if type(self.values[key]) == bool or type(other.values[key]) == bool:
                            return NotImplemented
                        else: list.append(self.values[key] * other.values[key])

                return Array(self.shape,list)
            else: return NotImplemented

        else: # om other er en en skalar

            shape_scalar = 1
            other, lenght = Array.scalar(self,shape_scalar,other,len(self.values)) #omgjør til et array med lengde lik len(self.values) eks skalar 10 = [10,10,10,10]
            lenght = (lenght,)
            if (self.dtypes_uniformity_compatability(self.values, other, self.shape, lenght)): #checks the datatypes, checks if same lenght.

                for key in range(len(self.values)):
                    if type(self.values[key]) == bool or type(other[key]) == bool:
                        return NotImplemented
                    else:
                        list.append(self.values[key] * other[key])

                return Array(self.shape,list) #turn the list into an array by instansiating an object of class Array

            else: return NotImplemented


    def __eq__(self, other): #skal brukes til å kalle når man tester om 2 array er like A == B True

        #Sjekker at arrays har samme shape
        if self.shape == other.shape:

        # Kryssjekker arrayene - om første plass i self.values ikke matcher datatype i other og omvendt
            if all(type(key) is type(self.values[0]) for key in other) and all(type(key) is type(other[0]) for key in self.values):

                #dobbeltsjekker datatyper - plass for plass
                for key in range(len(self.values)):
                    if type(other[key]) == type(self.values[key]):
                        return True
                    else: return False
            else: return False

        # Returnerer False og test feiler:
        else:
            print("Feil datatype")
            return False

    def is_equal(self, other): #oppretter en liste som returnerer boolske verdier for innholdet mellom arrayene

        list = []

        # sjekker om de er like
        if (self.shape == other.shape):

            for key in range(len(self.values)):
                #Sjekker om indexene er like og legger til True/False alt ettersom
                if type(other[key]) != type(self.values[key]):
                    list.append(False)
                else: list.append(True)
            A = Array(self.shape,list) #instansierer et nytt objekt av klassen Array, som gir tilbake bare True om arrayene som testes er kompatible
        else:
            raise ValueError

        return A


    def min_element(self):

        min = self.values[0]

        for key in range(len(self.values)):
            if type(self.values[key]) == bool:
                raise TypeError("Datatype Bool is not allowed for this operation")
            if self.values[key] < min:
                min = self.values[key]

        return min

    def mean_element(self):
        sum = 0
        for key in range(len(self.values)):
            if type(self.values[key]) == bool:
                raise TypeError("Datatype Bool is not allowed for this operation")
            sum += self.values[key]
        mean = float(sum/len(self.values))

        return mean
