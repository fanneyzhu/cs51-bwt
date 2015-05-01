import sys
import color

# marker for the end of the string
marker = "$"

def suffix_index(str):
    # create sorted suffix array of string
    suffix_array = sorted(str[i:] for i in range(len(str)))

    # create index array that contains the index at
    # which the suffix occurs in the original string
    index_array = [str.index(suffix) for suffix in suffix_array]

    return index_array

def run_bwt(str):
    # make sure that the input string itself does not contain the marker
    assert marker not in str, "Input cannot contain (%s)" % marker

     # add marker to end of the string
    str += "$"

    index_array = suffix_index(str)

    # compute bwt of string by mapping the entries of index_array to
    # the corresponding (index-1) in the original string
    result = "".join(str[index-1] for index in index_array)

    return result

if __name__ == "__main__":
    try:
        print color.color.BOLD + run_bwt(sys.argv[1]) + color.color.END
    except:
        print color.color.RED + "Please run in command line: python bwt.py sequence.txt query" + color.color.END
        print color.color.RED + "Note: The sequence cannot contain \"%s\"" % marker + color.color.END