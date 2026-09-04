class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        sorted_set = sorted(nums_set)
        seq_a = []
        sub_seq = [sorted_set[0]]
        # print(sub_seq)

        for i in range(1, len(sorted_set)):
            valid_s = sorted_set[i] - sorted_set[i-1]
            if valid_s == 1:
                sub_seq.append(sorted_set[i])
                # print(sub_seq)
            else:
                seq_a.append(sub_seq)
                sub_seq = [sorted_set[i]]
                # print(sub_seq)
            
        seq_a.append(sub_seq)
        # print(seq_a)
        longest = 0
        for l in seq_a:
            longest = max(longest, len(l))
        return longest