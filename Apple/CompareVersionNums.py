class Solution(object):
    def compare_version_nums(self, version1, version2):
        v1 = [int(k) for k in version1.split('.')]
        v2 = [int(k) for k in version2.split('.')]
        for i in range(max(len(v1), len(v2))):
            ver1 = v1[i] if i < len(v1) else 0
            ver2 = v2[i] if i < len(v2) else 0
            if ver1 > ver2:
                return 1
            elif ver2 > ver1:
                return -1
        return 0


print(Solution().compare_version_nums("1.1", "1.2"))