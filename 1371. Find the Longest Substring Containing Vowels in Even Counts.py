class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        count_a = 0
        count_i = 0
        count_u = 0
        count_e = 0
        count_o = 0

        array_odd = [[0,0,0,0,0]]
        chosen_mask = [0, 0, 0, 0, 0]
        last_idx = 0 
        longest_subseq = 0
        triggered = False
        for curr_idx, c in enumerate(s):
            if c == 'a':
                count_a += 1
            elif c == 'i':
                count_i += 1
            elif c == 'u':
                count_u += 1
            elif c == 'e':
                count_e += 1
            elif c == 'o':
                count_o += 1
            
            current_mask = [count_a % 2, count_i % 2, count_u % 2, count_e % 2, count_o % 2]
            array_odd.append(current_mask)

            try:
                the_same_idx = array_odd.index(current_mask)
                # print(f"Checking, the same idx: {the_same_idx} and curr_idx: {curr_idx}")
                if curr_idx - the_same_idx >= longest_subseq:
                    # print(f"The same idx is triggered with {the_same_idx} and curr_idx {curr_idx}")
                    triggered = True
                    chosen_mask = current_mask
                    longest_subseq = curr_idx - the_same_idx
                    last_idx = curr_idx
                    # if curr_idx == the_same_idx

                    
            except:
                print("Exception Triggered")
                pass

        if not triggered:
            return 0

        longest_subseq += 1

        return longest_subseq 