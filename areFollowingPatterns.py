def areFollowingPatterns(strings, patterns):
    flag = False
    flag_pattern = False
    flag_1 = False
    strings_map = {}
    patterns_map = {}
    ans = []
    if (len(strings) and len(patterns))==1:
        return True
    for i in range(0, len(strings)):
        if strings[i] in strings_map:
            strings_map[strings[i]].append(i)
        else:
            strings_map[strings[i]] = [i]
    for i in range(0, len(patterns)):
        if patterns[i] in patterns_map:
            patterns_map[patterns[i]].append(i)
        else:
            patterns_map[patterns[i]] = [i]
    print(patterns_map)
    print(strings_map)
    for key in strings_map:
        if len(strings_map[key]) >= 2:
            flag = True
            strings_map[key].sort()
            ans.append(strings_map[key])
    for key in patterns_map:
        if len(patterns_map[key]) >= 2:
            flag_pattern = True
            patterns_map[key].sort()
            if patterns_map[key] in ans:
                flag_1 = True
            else:
                flag_1 = False
    if not flag and not flag_pattern:
        return True
    else:
        if flag and flag_1:
            return True
        else:
            return False

print(areFollowingPatterns(strings = ["kwtfpzm",
 "kwtfpzm",
 "kwtfpzm",
 "kwtfpzm",
 "kwtfpzm",
 "wfktjrdhu",
 "anx",
 "kwtfpzm"], patterns = ["z",
 "z",
 "z",
 "hhwdphhnc",
 "zejhegjlha",
 "xgxpvhprdd",
 "e",
 "u"]))