class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        counts = [[] for i in range(len(nums) + 1)]
        for num, cnt in freq.items():
            counts[cnt].append(num)

        res = []
        for i in range(len(counts) - 1, 0, -1):
            for num in counts[i]:
                res.append(num)
                if len(res) == k:
                    return res