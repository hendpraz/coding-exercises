class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        els_len = len(self.__elements)
        maxdiff = 0
        for i in range(els_len - 1):
            for j in range(i+1, els_len):
                temp = abs(self.__elements[i] - self.__elements[j])
                if(temp > maxdiff):
                    maxdiff = temp
        self.maximumDifference = maxdiff
# End of Difference class