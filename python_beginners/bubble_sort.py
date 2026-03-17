def bubble_sort(arr):
    """
    冒泡排序算法
    时间复杂度: O(n^2)
    空间复杂度: O(1)
    """
    n = len(arr)

    # 外层循环控制排序轮数
    for i in range(n):
        # 优化标志：如果某一轮没有发生交换，说明已经有序
        swapped = False

        # 内层循环进行相邻元素比较和交换
        # 每轮会将最大的元素"冒泡"到末尾
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # 交换相邻元素
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # 如果这一轮没有发生交换，说明数组已经有序，可以提前结束
        if not swapped:
            break

    return arr


# 测试代码
if __name__ == "__main__":
    # 测试用例
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1, 2, 3, 4, 5],  # 已排序
        [5, 4, 3, 2, 1],  # 逆序
        [42],             # 单个元素
        []                # 空数组
    ]

    print("冒泡排序测试：\n")
    for arr in test_arrays:
        original = arr.copy()
        sorted_arr = bubble_sort(arr)
        print(f"原始数组: {original}")
        print(f"排序结果: {sorted_arr}")
        print("-" * 40)

    # 交互式测试
    print("\n自定义测试：")
    user_input = input("请输入要排序的数字（用空格分隔）: ")
    if user_input.strip():
        user_array = list(map(int, user_input.split()))
        print(f"原始数组: {user_array}")
        result = bubble_sort(user_array)
        print(f"排序结果: {result}")
    else:
        print("未输入数据")
