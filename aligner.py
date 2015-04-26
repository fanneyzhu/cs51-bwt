import bwt

print(bwt.run_bwt("banana"))

class Align(object):
    def __init__(self, query, sequence):
        self.query = query
        self.sequence = sequence

    marker = "$"

    # find the first occurrence of c in sorted sequence with marker
    def occ(self, c):
        return sorted(self.sequence+self.marker).index(c)

    # find the number of occurrences of c before position i in bwt(sequence)
    def count(self, i, c):
        str = bwt.run_bwt(self.sequence)
        n = 0
        for i in range(i):
            if str[i] == c:
                n += 1
        return n

    # add result of occ and count
    def lf(self, i, c):
        return self.occ(c) + self.count(i, c)

    # find the first and last suffix positions for the query seq
    # in the BWT transformed string
    def bounds(self):

        top = 0
        bot = len(self.sequence)+1

        # iterate over letters in reversed query string
        for c in self.query[::-1]:

            # use LF function to map the position in the last
            # column to the position in the first column
            top = self.lf(top, c)
            bot = self.lf(bot, c)

            # if top bound = bottom bound, then the string is not found.
            if top == bot:
                return (-1,-1)

        return (top,bot)
        
    # returns the index of the query string
    # function walks left from query until $ is reached and
    #  counts number of steps (i.e., index of query)
    def from_start (self, idx):
        qidx = 0
        i = idx
        while self.sequence[i] != "$":
            qidx += 1
        return qidx
