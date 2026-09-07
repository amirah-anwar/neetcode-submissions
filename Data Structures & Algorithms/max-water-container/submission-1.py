class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areas = []
        i,j = 0, len(heights) - 1
        while i < j:
            width = abs(i - j)
            height = min(heights[i], heights[j])
            area = width * height
            areas.append(area)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        # for i in range(len(heights)):
        #     for j in range(len(heights) - 1, 0, -1):
        #         if (i,j) in seen:
        #             # print("in seen")
        #             continue
        #         else:
        #             # print("NOT in seen")
        #             width = abs(i - j)
        #             height = min(heights[i], heights[j])
        #             area = width * height
        #             seen.add((i,j))
        #             areas.append(area)

        max_area = 0
        for area in areas:
            max_area = max(max_area, area)

        return max_area