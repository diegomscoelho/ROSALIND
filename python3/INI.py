# http://rosalind.info/problems/ini/

def count_bases(strand, verbose = False):
    '''
    Input: ACTG bases (string)
    Output: Space separated string (string)
    '''
    bases = ["A", "C", "G", "T"]
    count = [strand.count(base) for base in bases]

    if verbose:
        message = " ".join([str(num) for num in count])
        print(message)

    return count

with open("INI.txt", "r") as f:
    data = f.read()

count_bases(data, True)