__author__ = 'Fanney'

# marker for the end of the string
marker = "$"

def run_bwt(str):
    # make sure that the input string itself does not contain the marker
    assert marker not in str, "Input cannot contain (%s)" % marker

     # add marker to end of the string
    str += "$"

    # create sorted suffix array of string
    suffix_array = sorted(str[i:] for i in range(len(str)))

    # create index array that contains the index at
    # which the suffix occurs in the original string
    index_array = [str.index(suffix) for suffix in suffix_array]

    # compute bwt of string by mapping the entries of index_array to
    # the corresponding (index-1) in the original string
    result = "".join(str[index-1] for index in index_array)

    return result

