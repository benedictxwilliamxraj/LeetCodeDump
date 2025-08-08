def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hp = defaultdict(list)
        for i in range(len(strs)):
            key = []
            for j in strs[i]:
                key.append(ord(j)-97)
            key.sort()
            tp = tuple(key)
            hp[tp].append(strs[i])
        res = []
        for i in hp.values():
            res.append(i)

        return res