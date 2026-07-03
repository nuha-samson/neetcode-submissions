class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for i in range(len(strs)):
            l = sorted(strs[i])
            if tuple(l) not in hash:
                hash[tuple(l)] = [strs[i]]
            else:
                hash[tuple(l)].append(strs[i])
        col = []
        for i in hash.values():
            col.append(i)
        return col
