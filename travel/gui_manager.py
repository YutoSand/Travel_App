import tkinter as tk
from tkinter import messagebox
from travel.prefectures_module import load_prefectures, get_categories, get_urban_rural, get_climate
from diagnosis import diagnose

class GUIManager:
    def __init__(self, master):
        self.master = master
        self.master.title("旅行先診断アプリ")
        self.master.geometry("500x300")  # 画面サイズを設定

        self.answers = []
        self.current_question_index = 0

        # 質問表示用のフレーム
        self.question_frame = tk.Frame(master)
        self.question_frame.pack(expand=True)

        self.questions_label = tk.Label(self.question_frame, text=questions[self.current_question_index], font=("Helvetica", 16, "bold"))
        self.questions_label.pack(pady=20)  # 上下の余白を設定

        # 選択肢表示用のフレーム
        self.answers_frame = tk.Frame(master)
        self.answers_frame.pack(expand=True)

        # 都道府県データの読み込み
        self.prefectures = load_prefectures()

        # 質問に合わせて適切なデータをセットアップ
        self.categories = get_categories(self.prefectures)
        self.urban_rural = get_urban_rural(self.prefectures)
        self.climate = get_climate(self.prefectures)

        self.display_answer_options()

    def display_answer_options(self):
        for i, answer_option in enumerate(answers_options[self.current_question_index]):
            button = tk.Button(self.answers_frame, text=answer_option, command=lambda i=i: self.select_answer(i), font=("familly",12),borderwidth=5)
            button.pack(side=tk.LEFT, padx=5,pady=100)  # 左右の余白を設定

    def select_answer(self, answer_index):
        self.answers.append(answers_options[self.current_question_index][answer_index])

        self.current_question_index += 1
        if self.current_question_index < len(questions):
            self.questions_label.config(text=questions[self.current_question_index])

            # 回答選択ボタンを削除
            for widget in self.answers_frame.winfo_children():
                widget.destroy()

            self.display_answer_options()
        else:
            recommendation, is_random = diagnose(self.answers, self.prefectures, self.categories, self.urban_rural, self.climate)
            if is_random:
                messagebox.showinfo("診断結果", f"条件に合致する都道府県が見つかりませんでした。\nしかし、厚かましいですが適当に都道府県を決定しました！\n参考にしてください。\nおすすめの旅行先は、　{recommendation} 　です。")
            else:
                messagebox.showinfo("診断結果", f"おすすめの旅行先は、　{recommendation} 　です。")
            self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = GUIManager(root)
    root.mainloop()