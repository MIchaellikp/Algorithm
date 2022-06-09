class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = collections.defaultdict(list)
        
        for i in strs:
            array = [0] * 26
            for j in i:
                array[ord(j) - ord('a')] += 1
                
            hmap[tuple(array)].append(i)
            
        return hmap.values()