strs = ["dog","racecar","car"]
# strs = ["flower","flow","flight"]
# strs = ["ab", "a"]

common_prefix = strs[0]

for s in strs[1:len(strs)]:
    count = 0
    for idx in range(len(s)):
        # print(idx)
        # print(common_prefix[idx])
        # print(s[idx])
        # print()
        if idx >= len(common_prefix):
            break

        if common_prefix[idx] != s[idx]:
            break
        count += 1

    common_prefix = common_prefix[:count]

print(f"Result: Common Prefix: {common_prefix}")