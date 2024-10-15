import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("Test")
root.geometry("1000x1000")

# ファイルを参照
background = tk.PhotoImage(file="23644744.png")

# Labelの作成
bg = tk.Label(root, image=background)
bg.pack(fill="x")

# ウィンドウの描画
root.mainloop()





