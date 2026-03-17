# guess_number.py
# 非交互的猜数模拟：程序会随机生成一个目标，然后用二分法模拟猜测直到找到

import random


def simulate_guess(target, low=1, high=100):
    guesses = 0
    lo, hi = low, high
    while lo <= hi:
        guesses += 1
        mid = (lo + hi) // 2
        if mid == target:
            return guesses, mid
        if mid < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return guesses, None


def main():
    random.seed(42)
    target = random.randint(1, 100)
    guesses, found = simulate_guess(target)
    print(f"目标数字: {target}")
    print(f"使用二分法模拟猜测，猜中数字 {found}，共尝试 {guesses} 次")

if __name__ == '__main__':
    main()
