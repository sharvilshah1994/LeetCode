def ransomNote(note, magazine):
    rn_dic = {}
    for _ in note:
        if _ in rn_dic:
            rn_dic[_] += 1
        else:
            rn_dic[_] = 1
    for _ in magazine:
        if _ in rn_dic:
            rn_dic[_] -= 1
    for _ in rn_dic:
        if rn_dic[_] > 0:
            return False
    return True

print(ransomNote('aaa', 'ab'))