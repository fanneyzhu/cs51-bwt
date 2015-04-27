import bwt
import color
import sys

class Aligner(object):
    def __init__(self, sequence):
        self.sequence = sequence
        
    # find the first occurrence of c in sorted sequence with marker
    def __occ(self, c):
        try:
            return sorted(self.sequence+bwt.marker).index(c)
        except ValueError:
            return 0

    # find the number of occurrences of c before position i in bwt(sequence)
    def __count(self, i, c):
        str = bwt.run_bwt(self.sequence)
        n = 0
        for i in range(i):
            if str[i] == c:
                n += 1
        return n

    # add result of occ and count
    def __lf(self, i, c):
        return self.__occ(c) + self.__count(i, c)

    # find the first and last suffix positions for the query seq
    # in the BWT transformed string
    def __bounds(self, query):
        top = 0
        bot = len(self.sequence)+1

        # iterate over letters in reversed query string
        for c in query[::-1]:

            # use LF function to map the position in the last
            # column to the position in the first column
            top = self.__lf(top, c)
            bot = self.__lf(bot, c)

            # if top bound = bottom bound, then the string is not found.
            if top == bot:
                return (-1,-1)

        return (top,bot)
        
    # returns the index at which the match occurs in the query string
    def __find_index(self, query):
        matches = self.__bounds(query)

        if matches == (-1, -1):
            return None
        else:
            index_array = bwt.suffix_index(self.sequence+bwt.marker)
            result = [index_array[x] for x in range(matches[0], matches[1])]
            return result

    def align(self, query):
        matches = self.__find_index(query)
        bold = color.color.BOLD
        end = color.color.END
        print bold + "Your query \"%s\"" % query,
        if matches == None:
            print "does not align in the sequence \"%s\"" % self.sequence + end
        else:
            print "aligns to the sequence \"%s\": " % self.sequence
            for match in sorted(matches):
                for x in range(0, len(self.sequence)):
                    if match == x:
                        query_end = x+len(query)
                        found = color.color.PURPLE + self.sequence[x:query_end] + end
                        print bold+self.sequence[0:x]+found+bold+self.sequence[query_end:],
                        if match == query_end-1:
                            print "(index: %s)" % match,
                        else:
                            print "(index: %s to %s)" % (match, query_end-1),
                        print end
                        break

if __name__ == "__main__":
    try:
        x = Aligner(sys.argv[1])
        x.align(sys.argv[2])
    except:
        print color.color.RED + "Please run in command line: python aligner.py sequence query" + color.color.END
        print color.color.RED + "Note: The sequence cannot contain \"%s\"" % bwt.marker + color.color.END