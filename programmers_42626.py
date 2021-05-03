# LV 2 - 힙 사용 더맵게
import heapq


def solution(scoville, K):
    answer = 0
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)

    mix_cnt = 0
    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        mix_cnt += 1

    return mix_cnt