class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "}": "{", "]": "["}
        st = []
        for i in s:
            if i in mapping.values():
                st.append(i)
            else:
                if not st or st.pop()!=mapping[i]:
                    return False
        print(st)
        return True if len(st) ==0 else False