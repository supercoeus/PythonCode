import tkinter as tk
from tkinter import messagebox

class GobangGame:
    def __init__(self, root):
        self.root = root
        self.root.title("五子棋游戏")
        self.root.resizable(False, False)

        # 游戏参数
        self.board_size = 15  # 棋盘大小 15x15
        self.cell_size = 40   # 每个格子的大小
        self.padding = 30     # 棋盘边缘留白
        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 1  # 1: 黑棋, 2: 白棋
        self.game_over = False

        # 创建画布
        canvas_size = self.cell_size * (self.board_size - 1) + 2 * self.padding
        self.canvas = tk.Canvas(root, width=canvas_size, height=canvas_size + 50, bg='#DEB887')
        self.canvas.pack()

        # 绘制棋盘
        self.draw_board()

        # 绑定点击事件
        self.canvas.bind('<Button-1>', self.on_click)

        # 创建重新开始按钮
        self.restart_button = tk.Button(root, text="重新开始", command=self.restart_game, font=('Arial', 12))
        self.restart_button.pack(pady=10)

        # 创建状态标签
        self.status_label = tk.Label(root, text="当前玩家: 黑棋", font=('Arial', 14))
        self.status_label.pack()

    def draw_board(self):
        """绘制棋盘"""
        # 绘制横线和竖线
        for i in range(self.board_size):
            # 横线
            x1 = self.padding
            y1 = self.padding + i * self.cell_size
            x2 = self.padding + (self.board_size - 1) * self.cell_size
            y2 = y1
            self.canvas.create_line(x1, y1, x2, y2, width=1)

            # 竖线
            x1 = self.padding + i * self.cell_size
            y1 = self.padding
            x2 = x1
            y2 = self.padding + (self.board_size - 1) * self.cell_size
            self.canvas.create_line(x1, y1, x2, y2, width=1)

        # 绘制天元和星位（中间的5个点）
        star_points = [(3, 3), (11, 3), (7, 7), (3, 11), (11, 11)]
        for x, y in star_points:
            cx = self.padding + x * self.cell_size
            cy = self.padding + y * self.cell_size
            self.canvas.create_oval(cx-3, cy-3, cx+3, cy+3, fill='black')

    def on_click(self, event):
        """处理点击事件"""
        if self.game_over:
            return

        # 计算点击位置对应的棋盘坐标
        x = round((event.x - self.padding) / self.cell_size)
        y = round((event.y - self.padding) / self.cell_size)

        # 检查坐标是否在有效范围内
        if x < 0 or x >= self.board_size or y < 0 or y >= self.board_size:
            return

        # 检查该位置是否已有棋子
        if self.board[y][x] != 0:
            return

        # 落子
        self.place_stone(x, y)

    def place_stone(self, x, y):
        """在指定位置落子"""
        # 更新棋盘数据
        self.board[y][x] = self.current_player

        # 计算棋子的屏幕坐标
        cx = self.padding + x * self.cell_size
        cy = self.padding + y * self.cell_size

        # 绘制棋子
        color = 'black' if self.current_player == 1 else 'white'
        outline = 'black' if self.current_player == 1 else 'white'
        self.canvas.create_oval(cx-17, cy-17, cx+17, cy+17, fill=color, outline=outline, width=2)

        # 检查是否获胜
        if self.check_win(x, y):
            self.game_over = True
            winner = "黑棋" if self.current_player == 1 else "白棋"
            messagebox.showinfo("游戏结束", f"{winner}获胜！")
            return

        # 检查是否平局
        if self.check_draw():
            self.game_over = True
            messagebox.showinfo("游戏结束", "平局！")
            return

        # 切换玩家
        self.current_player = 3 - self.current_player  # 1->2, 2->1

        # 更新状态标签
        player_text = "黑棋" if self.current_player == 1 else "白棋"
        self.status_label.config(text=f"当前玩家: {player_text}")

    def check_win(self, x, y):
        """检查是否获胜（五子连珠）"""
        player = self.board[y][x]

        # 检查四个方向：水平、垂直、对角线、反对角线
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]

        for dx, dy in directions:
            count = 1  # 当前落子算1个

            # 正方向检查
            i = 1
            while True:
                nx, ny = x + dx * i, y + dy * i
                if 0 <= nx < self.board_size and 0 <= ny < self.board_size and self.board[ny][nx] == player:
                    count += 1
                    i += 1
                else:
                    break

            # 反方向检查
            i = 1
            while True:
                nx, ny = x - dx * i, y - dy * i
                if 0 <= nx < self.board_size and 0 <= ny < self.board_size and self.board[ny][nx] == player:
                    count += 1
                    i += 1
                else:
                    break

            if count >= 5:
                return True

        return False

    def check_draw(self):
        """检查是否平局"""
        for row in self.board:
            if 0 in row:
                return False
        return True

    def restart_game(self):
        """重新开始游戏"""
        # 清空棋盘数据
        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 1
        self.game_over = False

        # 清空画布并重新绘制
        self.canvas.delete("all")
        self.draw_board()

        # 更新状态标签
        self.status_label.config(text="当前玩家: 黑棋")


def main():
    root = tk.Tk()
    game = GobangGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
