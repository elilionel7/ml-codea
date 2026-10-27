class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = [(-c, k) for k, c in count.items()]
        heapq.heapify(heap)

        results = []

        for _ in range(k):
            _, num = heapq.heappop(heap)
            results.append(num)
        
        return results



        