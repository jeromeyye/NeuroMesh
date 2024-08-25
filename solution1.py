def min_subsequences(source,target):
    source_len = len(source)
    target_len = len(target)
    target_index = 0
    ans = 0
    
    while target_index < target_len:
        subsequence_length = 0
        source_index = 0
        
        while source_index < source_len and target_index < target_len:
            if source[source_index] == target[target_index]:
                target_index += 1
                subsequence_length += 1
            source_index += 1
        
        if subsequence_length == 0:
            return -1
            
        ans += 1
    
    return ans

print(min_subsequences("abc", "abcbc"))  
print(min_subsequences("abc", "acdbc"))  
print(min_subsequences("xyz", "xzyxz"))