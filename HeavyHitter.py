import operator

class Solution:

    def heavyHitter(self, nums: list[int], k: int) -> list[int]:
        elements = {}

        for i in nums:
            if i in elements:
                elements[i] += 1
            else:
                elements[i] = 1
        sortedelements = sorted(elements.items(), key=operator.itemgetter(1), reverse=True)
        count = 0
        value = []
        for key in sortedelements:
            count += 1
            value.append(key[0])
            if count == k:
                return value
        return value

list = ['I1', 'I2', 'I5', #user1
            'I2', 'I4', #user2
            'I2', 'I3', #user3
            'I1', 'I2', 'I4', #user3
            'I1', 'I3', #user4
            'I2', 'I3', #user5
            'I1', 'I3', #user6
            'I1', 'I2', 'I3', 'I5', #user7
            'I1', 'I2', 'I3'] #user7
S = Solution()
print(S.heavyHitter(list,3))
