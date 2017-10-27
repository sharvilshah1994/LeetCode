class Solution(object):
    def merge_two_arrays(self, nums1, nums2):
        num = list()
        while len(nums1) != 0 and len(nums2) != 0:
            if nums1[0] < nums2[0]:
                num.append(nums1[0])
                nums1.remove(nums1[0])
            else:
                num.append(nums2[0])
                nums2.remove(nums2[0])
        if len(nums1) > 0:
            num += nums1
        else:
            num += nums2
        return num


if __name__ == "__main__":
    s = Solution()
    l = s.merge_two_arrays([1], [1])
    print(l)
