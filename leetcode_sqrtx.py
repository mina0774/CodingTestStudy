# 이분탐색 이용하여 sqrt(x) 구하는 문제

def mySqrt( x: int) -> int:
    start = 0
    end = x

    while start <= end:
        mid = (start + end) // 2

        if mid * mid == x:
            return mid
        elif mid * mid < x:
            start = mid + 1
        elif mid * mid > x:
            end = mid - 1
    return start - 1

print(mySqrt(1000))