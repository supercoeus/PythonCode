# file_io.py
# 简单的文件写入与读取示例

FILENAME = 'sample.txt'


def main():
    text = '这是一个文件读写示例。\nHello from file_io.py'
    # 写入文件
    with open(FILENAME, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'已写入文件: {FILENAME}')

    # 读取文件
    with open(FILENAME, 'r', encoding='utf-8') as f:
        content = f.read()
    print('文件内容如下：')
    print(content)

if __name__ == '__main__':
    main()
