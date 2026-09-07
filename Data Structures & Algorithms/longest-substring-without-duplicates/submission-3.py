class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_list = list(s)
        sub_str = ''
        max_str = ''
        for i in range(len(s_list)):
            ch = s_list[i]
            if ch not in sub_str:
                sub_str = sub_str + ch
            else:
                last_sub = sub_str[sub_str.index(ch) + 1:]
                sub_str = last_sub + ch
            if len(sub_str) > len(max_str):
                max_str = sub_str
        
        return len(max_str)