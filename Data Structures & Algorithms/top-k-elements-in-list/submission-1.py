class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        results = []

        for nk, cv in count.items():
            buckets[cv].append(nk)
        
        for i in range(len(nums), 0, -1):
            for n in buckets[i]:
                results.append(n)
                if len(results) == k:
                    return results
  



        