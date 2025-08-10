
inp = """6
402 0
390 0
816 2
848 2
777 0
815 1"""

"""
816 2
  81_
  _16
  8_6 

848 2
  84_
  8_8
  _48
"""

def get_match(code1, code2):
    """Returns None if no match is found, otherwise return the match"""
    if len(code1) != len(code2):
        return None

    match = ""
    for i in range(len(code1)):
        c1 = code1[i]
        c2 = code2[i]
        if c1 == "_":
            match += c2
        elif c2 == "_":
            match += c1
        elif c1 == c2:
            match += c1
        else:
            return None

    return match

def parse():
    lines = inp.split("\n")
    lines = lines[1:]

    candidates = []
    for line in lines:
        code, num_correct = line.split()
        N = len(code)
        num_correct = int(num_correct)
        if num_correct == 0:
            # TODO figure out what to do when nothing is correct
            continue
        elif num_correct == 1:
            subcandidates = []
            for i in range(N):
                subsubcandidate = ""
                for j in range(N):
                    if i == j:
                        subsubcandidate += code[i]
                    else:
                        subsubcandidate += "_"

                subcandidates.append(subsubcandidate)

            candidates.append(subcandidates)
            
        elif num_correct == 2:
            # TODO: handle inputs of length 4
            subcandidates = []
            for i in range(N):
                 subcandidates.append(code[:i] + "_" + code[i+1:])

            candidates.append(subcandidates)
        elif num_correct == 3:
            # TODO: inputs of length 4
            pass

    print("candidates", candidates)
    return candidates


def eval_helper(candidates, i, current):
    if i == len(candidates):
        return current

    subcandidates = candidates[i]
    for j in range(len(subcandidates)):
        code = subcandidates[j]
        match = get_match(current, code)
        if match is None:
            continue

        result = eval_helper(candidates, i+1, match)
        if result is not None:
            return result

    return None

def eval(candidates):
    # '___'
    # '_16' X
    # '8_6'
    # '846'
    # [['_16', '8_6', '81_'], ['_48', '8_8', '84_'], ['8__', '_1_', '__5']]
    i = 0
    return eval_helper(candidates, i, "___")


if __name__ == "__main__":
    cands = parse()
    result = eval(cands)
    print(result)
