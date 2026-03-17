# fibonacci.py
# 计算并打印前 n 个斐波那契数（演示函数和循环）

def fibonacci(n):
    if n <= 0:
        return []
    seq = [0]
    if n == 1:
        return seq
    seq.append(1)
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq


def main():
    n = 10
    seq = fibonacci(n)
    print(f"前 {n} 个斐波那契数: {seq}")

if __name__ == '__main__':
    main()
