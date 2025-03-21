import tkinter as tk
from tkinter import messagebox

from src.logic.Model import Model


class GomokuGUI:
    def __init__(self, model, cell_size=40):
        self.model = model
        self.cell_size = cell_size
        self.current_player = 1  # 黑方先手

        # 创建主窗口
        self.root = tk.Tk()
        self.root.title("五子棋")

        # 计算棋盘尺寸
        self.board_pixel_size = (model.size() - 1) * cell_size
        padding = 20

        # 创建画布
        self.canvas = tk.Canvas(
            self.root,
            width=self.board_pixel_size + 2 * padding,
            height=self.board_pixel_size + 2 * padding,
            bg="#DEB887"
        )
        self.canvas.pack(padx=10, pady=10)

        # 创建控制面板
        control_frame = tk.Frame(self.root)
        control_frame.pack(fill=tk.X, padx=10, pady=5)

        self.status_label = tk.Label(
            control_frame,
            text="当前玩家: 黑棋 ●",
            font=("Arial", 12)
        )
        self.status_label.pack(side=tk.LEFT)

        tk.Button(
            control_frame,
            text="重新开始",
            command=self.restart_game
        ).pack(side=tk.RIGHT)

        # 绑定事件
        self.canvas.bind("<Button-1>", self.on_click)

        # 绘制棋盘
        self.draw_board(padding)

    def draw_board(self, padding):
        """绘制棋盘网格"""
        size = self.model.size()
        for i in range(size):
            # 水平线
            y = padding + i * self.cell_size
            self.canvas.create_line(
                padding, y,
                padding + (size - 1) * self.cell_size, y
            )
            # 垂直线
            x = padding + i * self.cell_size
            self.canvas.create_line(
                x, padding,
                x, padding + (size - 1) * self.cell_size
            )

        # 绘制星位标记（专业棋盘标记）
        star_points = [(3, 3), (3, 11), (11, 3), (11, 11), (7, 7)]
        if size == 15:
            star_points = [(3, 3), (3, 11), (11, 3), (11, 11), (7, 7)]
        for x, y in star_points:
            self.draw_star(padding + x * self.cell_size,
                           padding + y * self.cell_size)

    def draw_star(self, x, y):
        """绘制星位标记"""
        r = 3
        self.canvas.create_oval(
            x - r, y - r, x + r, y + r,
            fill="black"
        )

    def on_click(self, event):
        """处理鼠标点击事件"""
        """高精度点击处理"""
        padding = 20
        board_start = padding
        board_end = padding + self.board_pixel_size

        # 过滤棋盘外点击
        if not (board_start <= event.x <= board_end and
                board_start <= event.y <= board_end):
            return

        # 精确坐标转换（四舍五入+边界约束）
        x = round((event.x - padding) / self.cell_size)
        y = round((event.y - padding) / self.cell_size)
        x = max(0, min(x, self.model.size() - 1))
        y = max(0, min(y, self.model.size() - 1))

        try:
            # 尝试落子
            self.model.add_piece(x, y, self.current_player)
            self.draw_piece(x, y)

            # 检查游戏状态
            if self.model.game_over:
                if self.model.winner:
                    winner = "黑棋" if self.model.winner == 1 else "白棋"
                    messagebox.showinfo("游戏结束", f"{winner} 获胜！")
                else:
                    messagebox.showinfo("游戏结束", "平局！")
                return

            # 切换玩家
            self.current_player = 2 if self.current_player == 1 else 1
            self.update_status()

        except ValueError as e:
            messagebox.showerror("错误", "无效的位置")

    def draw_piece(self, x, y):
        """在画布上绘制棋子"""
        padding = 20
        piece = self.model.piece(x, y)
        color = "black" if piece == 1 else "white"

        # 计算绘制坐标
        x0 = padding + x * self.cell_size - self.cell_size // 2.5
        y0 = padding + y * self.cell_size - self.cell_size // 2.5
        x1 = x0 + self.cell_size // 1.25
        y1 = y0 + self.cell_size // 1.25

        self.canvas.create_oval(
            x0, y0, x1, y1,
            fill=color,
            outline="black" if color == "white" else None
        )

    def update_status(self):
        """更新状态栏"""
        player = "黑棋 ●" if self.current_player == 1 else "白棋 ○"
        self.status_label.config(text=f"当前玩家: {player}")

    def restart_game(self):
        """重置游戏"""
        self.model.clear()
        self.model.game_over = False
        self.model.winner = 0
        self.current_player = 1
        self.canvas.delete("all")
        self.draw_board(20)
        self.update_status()


def main():
    # 初始化游戏模型
    game_model = Model(size=15)

    # 创建GUI
    gui = GomokuGUI(game_model)

    # 运行主循环
    gui.root.mainloop()


if __name__ == "__main__":
    main()
