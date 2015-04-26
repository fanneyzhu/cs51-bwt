import bwt

print(bwt.run_bwt("banana"))

class Aligner(object):
    def __init__(self, sequence):
        self.sequence = sequence

    # find the first occurrence of c in sorted sequence with marker
    def occ(self, c):
        try:
            return sorted(self.sequence+bwt.marker).index(c)
        except ValueError:
            return 0

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
    def bounds(self, query):
        top = 0
        bot = len(self.sequence)+1

        # iterate over letters in reversed query string
        for c in query[::-1]:

            # use LF function to map the position in the last
            # column to the position in the first column
            top = self.lf(top, c)
            bot = self.lf(bot, c)

            # if top bound = bottom bound, then the string is not found.
            if top == bot:
                return (-1,-1)

        return (top,bot)
        
    # returns the index at which the match occurs in the query string
    def find_index(self, query):
        matches = self.bounds(query)

        if matches == (-1, -1):
            return None
        else:
            index_array = bwt.suffix_index(self.sequence+bwt.marker)
            result = [index_array[x] for x in range(matches[0], matches[1])]
            return result

    def align(self, query):
        matches = self.find_index(query)
        print "Your query \"%s\" ..." % query
        if matches == None:
            print "does not align to the sequence \"%s\"" % self.sequence
        else:
            print "aligns to the sequence \"%s\" at index(es):" % self.sequence
            print ", ".join(map(str, matches))


andy = Aligner("banana")
andy.align("anana")