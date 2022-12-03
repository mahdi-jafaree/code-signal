def common_chars(s1, s2):
    s1_dict = {i:s1.count(i) for i in s1}
    s2_dict = {i:s2.count(i) for i in s2}
    intersect = set(s1).intersection(s2)
    result = 0
    print(intersect)
    for i in intersect:
        result += min(s1_dict[i],s2_dict[i])
    print(result)
common_chars("abad","dda")