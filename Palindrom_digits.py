class Solution(object):
    def isPalindrome(self, x):
        str_x = str(x)
        for i in range(len(str_x)//2):
            if str_x[i] != str_x[-(i+1)]:
                return False
        return True


x = int(input("Put your number here:"))
solution = Solution()
if solution.isPalindrome(x):
    print(f"{x} is a palindrom")
