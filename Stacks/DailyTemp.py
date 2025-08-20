class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force-> iterate thorugh every ele 
        # ans = []
        # for i in range(len(temperatures)):
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[i] < temperatures[j]:
        #             ans.append(j-i)
        #             break
            
        #     if len(ans) < i+1:
        #         ans.append(0)

        # return ans
        temps = temperatures
        n = len(temps)
        st = []
        ans = [0]*n
        for i, t in enumerate(temps):
            #print(i)
            while st and st[-1][0] < t:
                st_temp, st_idx = st.pop()
                ans[st_idx] = i - st_idx
                #print(ans)
            st.append((t,i))
            #print(st)
        return ans
