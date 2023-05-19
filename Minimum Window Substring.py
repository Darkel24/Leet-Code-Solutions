class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Hashmap to store the character frequency of t
        t_map = {}
        for char in t:
            if char in t_map:
                t_map[char] += 1
            else:
                t_map[char] = 1
        
        # Two pointers left and right to keep track of the window
        left = 0
        right = 0
        min_len = float('inf')
        min_start = 0
        
        # Counter to keep track of the number of characters needed from t
        char_needed = len(t_map)
        
        # Hashmap to keep track of the frequency of characters in the current window
        window_map = {}
        
        while right < len(s):
            # Add the character at right pointer to the window
            char = s[right]
            if char in t_map:
                if char in window_map:
                    window_map[char] += 1
                else:
                    window_map[char] = 1
                
                # If the frequency of the character in the window matches the frequency in t_map, decrement char_needed
                if window_map[char] == t_map[char]:
                    char_needed -= 1
            
            # If all the characters in t have been found, move the left pointer
            while char_needed == 0:
                # Update the minimum length and start index if a smaller window is found
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left
                
                # Remove the character at left pointer from the window
                char = s[left]
                if char in t_map:
                    window_map[char] -= 1
                    if window_map[char] < t_map[char]:
                        char_needed += 1
                left += 1
            
            right += 1
        
        # If no window is found, return an empty string
        if min_len == float('inf'):
            return ""
        # Otherwise, return the minimum window
        else:
            return s[min_start:min_start + min_len]
