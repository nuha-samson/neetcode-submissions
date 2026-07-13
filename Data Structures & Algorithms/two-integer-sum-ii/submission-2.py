class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in numbers:
            for j in numbers:
                if i+j == target and i != j:
                    return [numbers.index(i)+1,numbers.index(j)+1]

        
        