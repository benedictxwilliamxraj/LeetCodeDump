class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #monotonic increasing stack
        # have max_area = 0
        # check if next number is greater
        maxa = 0
        n = len(heights)
        st = []
        for i in range(n):
            start = i
            while st and st[-1][0] > heights[i]:
                height, idx = st.pop()
                width = i - idx
                area = height*width
                maxa = max(maxa, area)
                start = idx
                print(start)
            
            st.append((heights[i], start))
            print(st)

        while st:
            height, idx = st.pop()
            width = n - idx
            area = height*width
            maxa = max(maxa, area)
        return maxa