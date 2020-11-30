def mxdiflg(a1, a2):
    if len(a1) == 0 or len(a2) == 0:
        return -1
    else:
        lens = []
        a1_lens = []
        a2_lens = []
        for s in a1:
            lens.append(len(s))
            a1_lens.append(len(s))
        for s in a2:
            lens.append(len(s))
            a2_lens.append(len(s))
        print("lens", lens, min(lens), max(lens))
        print("lens max all", max(lens) - min(lens))
        print("###")
        print("a1_lens", a1_lens, min(a1_lens), max(a1_lens))
        print("a2_lens", a2_lens, min(a2_lens), max(a2_lens))
        print("###")
        a1_a2 = max(a1_lens) - min(a2_lens)
        print("a1_a2", a1_a2)
        a2_a1 = max(a2_lens) - min(a1_lens)
        print("a2_a1", a2_a1)
        both_max = [a1_a2, a2_a1]
        print("both_max", max(both_max))
        return max(both_max)
