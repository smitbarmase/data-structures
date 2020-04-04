class SuffixArray {
    def __init__(self, text):
        # The sorted suffix array values.
        self._sa = []

        # Longest Common Prefix array
        self._lcp = []

        self.__constructedSa = False
        self.__constructedLcpArray = False

        if text == None:
            raise Exception('Text cannot be none.')
        # T is the text
        this._T = text
        # Length of the suffix array
        this._N = len(text)

    def getTextLength(self):
        return len(self._T)

    # Returns the suffix array.
    def getSa(self):
        self._buildSuffixArray()
        return self._sa

    # Returns the LCP array.
    def getLcpArray(self):
        self._buildLcpArray()
        return self._lcp

    # Builds the suffix array by calling the construct() method.
    def _buildSuffixArray(self):
        if self._constructedSa:
            return
        self._construct()
        self._constructedSa = True

    # Builds the LCP array by first creating the SA and then running the kasai algorithm.
    def _buildLcpArray(self):
        if self._constructedLcpArray:
            return
        self._buildSuffixArray()
        self.__kasai()
        self._constructedLcpArray = True

    def __toIntArray(self, s):
        if s == None:
            return None
        t = [s[i] for i in range(len(s))]
        return t

    # The suffix array construction algorithm is left undefined
    # as there are multiple ways to do this.
    def _construct(self):
        pass

    # Use Kasai algorithm to build LCP array
    # http://www.mi.fu-berlin.de/wiki/pub/ABI/RnaSeqP4/suffix-array.pdf
    def __kasai(self):
        lcp = [0 for i in range(self._N)]
        inv = [self._sa[i] for i in range(self._N)]
        len = 0
        for i in range(self._N):
            if inv[i] > 0:
                k = self._sa[inv[i] - 1]
                while i + len < self._N and k + len < self._N and self._T[i + len] == self._T[k + len]:
                    len += 1
                lcp[inv[i]] = len
                if len > 0:
                    len -= 1
