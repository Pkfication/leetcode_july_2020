class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        current_index = len(digits) - 1
        while (current_index >= 0):
            digits[current_index] = (digits[current_index] + carry)
            carry = digits[current_index] // 10
            digits[current_index] %= 10
            current_index -= 1
        
        if carry != 0:
            digits.insert(0,1)
        
        return digits
        
