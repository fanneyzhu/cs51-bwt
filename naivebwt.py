__author__ = 'Fanney'

# marker for the end of the string
marker = "$"

def bwt(str):
    # make sure that the input string itself does not contain the marker
    assert marker not in str, "Input cannot contain (%s)" % marker

    # add marker to end of the string
    str += "$"

    # create matrix of cyclic rotations of string
    matrix = sorted(str[i:]+str[:i] for i in range(len(str)))

    # get the last column of the matrix (i.e. last character of each rotation)
    last_col = "".join(row[-1] for row in matrix)

    return last_col