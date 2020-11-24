class Solution(object):
    @classmethod
    def lengthOfLongestSubstring(cls,s: str) -> int:
        res = 0
        mark = set()  # 用集合标明是否有出现重复字母
        r = 0  # 右指针
        for i in range(len(s)):
            if i != 0:
                mark.remove(s[i - 1])
            while r < len(s) and s[r] not in mark:  # 如果不满足条件说明r走到了s的尽头或r指向的元素
                mark.add(s[r])  # 将当前r指向的字母加入集合
                r += 1
            res = max(res, r - i)  # 在每一个位置更新最大值
        return res
if __name__ == '__main__':
    print(Solution.lengthOfLongestSubstring('23dadaasdsfdsjhfsdhfdhsfhdgs'))