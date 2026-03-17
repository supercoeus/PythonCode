# calculator.py
# 演示简单的算术函数以及错误处理

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

def main():
    x, y = 10, 3
    print(f"{x} + {y} = {add(x, y)}")
    print(f"{x} - {y} = {sub(x, y)}")
    print(f"{x} * {y} = {mul(x, y)}")
    result = div(x, y)
    print(f"{x} / {y} = {result}")
    # 展示除以 0 的处理
    print(f"10 / 0 = {div(10, 0)}")

if __name__ == '__main__':
    main()
