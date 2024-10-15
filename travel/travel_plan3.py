import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from prefectures_module import prefectures,Prefecture

# 質問
questions = [
    "旅行の目的は？",
    "都会と地方どっち？",
    "どのような気候を希望しますか？",
]

# 回答の選択肢
answers_options = [
    ["観光", "リゾート", "温泉", "グルメ", "アウトドア", "歴史", "自然"],
    ["都会", "地方"],
    ["亜熱帯", "温暖湿潤", "暖温帯", "寒冷地"],
]


# 質問に合わせて適切なデータをセットアップ
categories = {prefecture.name: prefecture.categories for prefecture in prefectures}
urban_rural = {prefecture.urban_rural: [p.name for p in prefectures if p.urban_rural == prefecture.urban_rural] for prefecture in prefectures}
climate = {prefecture.climate: [p.name for p in prefectures if p.climate == prefecture.climate] for prefecture in prefectures}

# 診断ロジック
def diagnose(answers):
    # 旅行の目的
    purpose = answers[0]

    # 都会と地方
    urban_rural_answer = answers[1]

    # 気候
    climate_answer = answers[2]

    # 推奨県の候補
    candidates = []

    # 目的の細分化
    candidates += [prefecture.name for prefecture in prefectures if purpose in prefecture.categories]

    # 都会と地方の選択
    candidates = list(set(candidates) & set(urban_rural[urban_rural_answer]))

    # 気候の選択
    candidates = list(set(candidates) & set(climate[climate_answer]))

    if not candidates:
        print("条件に合致する都道府県が見つかりませんでした。しかし、厚かましいですが適当に都道府県を決定しました！参考にしてください")
        recommendation = random.choice(prefectures).name
        return recommendation, True
    else:
        # ランダムに一つ選んで返す
        recommendation = random.choice(candidates)
        return recommendation, False

# メイン処理


class TravelApp:
    def __init__(self, master):
        self.master = master
        self.master.title("旅行先診断アプリ")
        self.master.geometry("1200x1000")  # 画面サイズを設定

        # 背景画像の表示
        background_image_path = "23644744.png"
        background_image = Image.open(background_image_path)
        self.background_photo = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(master, image=self.background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)


        self.answers = []

        self.current_question_index = 0


        # 説明表示用のラベル
        self.description_label = tk.Label(self.master, text="旅行先診断アプリ\n\n三つの質問に答えて、あなたに合った旅行先を見つけよう！", font=("Helvetica", 20, "bold"))
        self.description_label.place(x=200,y=300)

        #スタートボタン
        self.start_button = tk.Button(master, text="診断スタート", command=self.start_diagnosis, font=("Helvetica", 20), borderwidth=5, width=20, height=2)
        self.start_button.pack(side=tk.BOTTOM,fill = 'x',pady=300,padx=200)

    def start_diagnosis(self):

        # 説明表示用のラベルを非表示にする
        self.description_label.place_forget()

        #スタートボタン非表示にする
        self.start_button.pack_forget()

        # 質問表示用のフレーム
        self.question_frame = tk.Frame(self.master)
        self.question_frame.pack(expand=True)

        self.questions_label = tk.Label(self.question_frame, text=questions[self.current_question_index], font=("Helvetica", 30, "bold"))
        self.questions_label.pack(side=tk.TOP)  # 上下の余白を設定

        # 選択肢表示用のフレーム
        self.answers_frame = tk.Frame(self.master)
        self.answers_frame.pack(expand=True)
        
        self.display_answer_options()


    def display_answer_options(self):
        for i, answer_option in enumerate(answers_options[self.current_question_index]):
            button = tk.Button(self.answers_frame, text=answer_option, command=lambda i=i: self.select_answer(i), font=("familly",20),borderwidth=5, width=10, height=2)
            button.pack(side = tk.LEFT)  # 左右の余白を設定

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
            recommendation, is_random = diagnose(self.answers)
            
            if is_random:
                messagebox.showinfo("診断結果", f"条件に合致する都道府県が見つかりませんでした。\nしかし、厚かましいですが適当に都道府県を決定しました！\n参考にしてください。\nおすすめの旅行先は、　{recommendation} 　です。")
            else:
                messagebox.showinfo("診断結果", f"おすすめの旅行先は、　{recommendation} 　です。")
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TravelApp(root)
    root.mainloop()