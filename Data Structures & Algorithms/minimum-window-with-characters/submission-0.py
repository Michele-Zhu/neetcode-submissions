class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        t_freq = {}
        for c in t:
            # t_freq.get(key, value=None)
            # if key is not present return value
            t_freq[c] = 1 + t_freq.get(c, 0)
        needed_chars = len(t_freq)
        print(f"{t_freq}; {needed_chars}")

        start, end = -1, -1
        res_len = float("inf")
        left, right = 0, 0
        window = {}
        have_chars = 0
        while right < len(s):
            char = s[right]
            window[char] = 1 + window.get(char, 0)
            if char in t_freq.keys() and window[char] == t_freq[char]:
                have_chars += 1 
            while have_chars == needed_chars:
                # update result
                if (right-left +1) < res_len:
                    start = left
                    end = right
                    res_len = end-start + 1
                window[s[left]] -= 1
                if s[left] in t_freq and window[s[left]] < t_freq[s[left]]:
                    have_chars -= 1
                left += 1
            right += 1

        if start == -1:
            return ""
        
        return s[start:end+1]