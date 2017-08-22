class Solution(object):
    def convert(self, s, numRows):
        if numRows <= 1 or len(s) <= 1 or len(s) <= numRows:
            return s
        res = ''
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                if i == 0:
                    mid = 0
                else:
                    mid = numRows - 1

                res += s[mid]
                while mid < len(s):
                    if mid + 2 * numRows - 2 < len(s):
                        mid = mid + 2 * numRows - 2
                        res += s[mid]
                    else:
                        break
            else:
                mid = i
                res += s[mid]
                while mid < len(s):
                    if mid + 2 * numRows - 2 - 2 * i < len(s):
                        mmid = mid + 2 * numRows - 2 - 2 * i
                        res += s[mmid]
                        mid = mmid
                        if mid + 2 * i < len(s):
                            mmid = mid + 2 * i
                            res += s[mmid]
                            mid = mmid
                        else:
                            break
                    else:
                        break;

        return res

a = Solution()
print(a.convert('ab', 3))

