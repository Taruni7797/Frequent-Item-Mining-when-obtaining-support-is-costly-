import heapq
from collections import Counter
class Solution:
    def survey_sampling(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :return type: List[str]
        """
        ctr = Counter(words)
        heap = [(-ctr[word], word) for word in ctr]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

if __name__ == '__main__':
    words = ['I1', 'I2', 'I5', #user1
            'I2', 'I4', #user2
            'I2', 'I3', #user3
            'I1', 'I2', 'I4', #user3
            'I1', 'I3', #user4
            'I2', 'I3', #user5
            'I1', 'I3', #user6
            'I1', 'I2', 'I3', 'I5', #user7
            'I1', 'I2', 'I3'] #user7
    k = 3
    s = Solution()
    print("3 most frequent elements:")
    print(s.survey_sampling(words, k))
