class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        res = []
        for i in s:
            # check if digit, digit cnt 1
            if i != ']':
                st.append(i)
            else:
                temp_st = ''
                # pop untill u get [
                while st[-1] != '[':
                    char = st.pop()
                    temp_st = char + temp_st
                st.pop()
                # store that string
                num_st = ''
                # pop till u get charac
                print(temp_st)
                print(st)
                while st and st[-1].isdigit():
                    num = st.pop()
                    num_st = num + num_st
                print(num_st)
                num = int(num_st)
                # # multiply the string
                subst = ''
                for i in range(num):
                    subst+=temp_st
                print(subst)
                st.append(subst)
        print(st) 
          
        return "".join(st)