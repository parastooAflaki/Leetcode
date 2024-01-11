class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        indices_pos = [(indices[i], i) for i in range(len(indices))]
        indices_pos = sorted(indices_pos)
        print(indices_pos)
        last_index = -1
        updated = False
        for i in range(len(indices_pos), 0, -1):
            
            index = indices_pos[i-1][0]
            if last_index == index and updated:
                continue
            
            last_index = index
            
            source_str = sources[indices_pos[i-1][1]]
            if s[index:len(source_str) + index] == source_str:
                s = s[:index] + targets[indices_pos[i-1][1]] + s[len(source_str) + index :] 
                updated = True
            else:
                updated = False
        return s