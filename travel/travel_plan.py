import random
import curses

# 質問
questions = [
    "旅行の目的は？",
    "都会と地方どっち？",
    "旅行中は、どのような気候を希望しますか？",
]

# 回答の選択肢
answers_options = [
    ["観光", "リゾート", "温泉", "グルメ", "アウトドア", "歴史", "自然"],
    ["都会", "地方"],
    ["亜熱帯", "温暖湿潤", "暖温帯", "寒冷地"],
]

# 都道府県をオブジェクトとして扱うクラス
class Prefecture:
    def __init__(self, name, categories, urban_rural, climate, is_cheap, is_active):
        self.name = name
        self.categories = categories
        self.urban_rural = urban_rural
        self.climate = climate
        self.is_cheap = is_cheap
        self.is_active = is_active

    def has_interest(self, interest):
        return interest.lower() in self.categories

# 都道府県のリストを生成
prefectures = [
    Prefecture("北海道", ["観光", "アウトドア", "自然"], "地方", "寒冷地", True, True),
    Prefecture("青森県", ["観光", "アウトドア", "自然"], "地方", "寒冷地", True, True),
    Prefecture("岩手県", ["観光", "アウトドア", "自然"], "地方", "寒冷地", True, True),
    Prefecture("宮城県", ["観光", "アウトドア", "自然"], "地方", "寒冷地", True, True),
    Prefecture("秋田県", ["観光", "アウトドア", "自然"], "地方", "寒冷地", True, True),
    Prefecture("山形県", ["観光", "アウトドア", "自然"], "地方", "寒冷地", True, True),
    Prefecture("福島県", ["観光", "アウトドア", "自然"], "地方", "寒冷地", True, True),
    Prefecture("茨城県", ["観光", "アウトドア", "自然"], "地方", "暖温帯", True, True),
    Prefecture("栃木県", ["観光", "アウトドア", "自然"], "地方", "暖温帯", True, True),
    Prefecture("群馬県", ["観光", "アウトドア", "自然"], "地方", "暖温帯", True, True),
    Prefecture("新潟県", ["観光", "アウトドア", "自然"], "地方", "暖温帯", True, True),
    Prefecture("長野県", ["観光", "アウトドア", "自然"], "地方", "暖温帯", False, True),
    Prefecture("静岡県", ["観光", "リゾート", "温泉", "アウトドア", "自然"], "地方", "暖温帯", True, True),
    Prefecture("岐阜県", ["観光", "アウトドア", "自然"], "地方", "暖温帯", True, True),
    Prefecture("愛知県", ["観光", "アウトドア", "自然"], "地方", "暖温帯", True, True),
    Prefecture("三重県", ["リゾート", "アウトドア", "自然"], "地方", "暖温帯", True, True),
    Prefecture("鳥取県", ["リゾート", "アウトドア", "自然"], "地方", "暖温帯", True, True),
    Prefecture("島根県", ["リゾート", "アウトドア", "自然"], "地方", "暖温帯", True, True),
    Prefecture("岡山県", ["リゾート", "アウトドア", "自然"], "地方", "暖温帯", True, True),
    Prefecture("広島県", ["リゾート", "アウトドア", "自然"], "地方", "暖温帯", True, True),
    Prefecture("山口県", ["リゾート", "アウトドア", "自然"], "地方", "暖温帯", True, True),
    Prefecture("香川県", ["リゾート", "アウトドア", "自然"], "地方", "暖温帯", True, True),
    Prefecture("愛媛県", ["リゾート", "アウトドア", "自然"], "地方", "暖温帯", True, True),
    Prefecture("高知県", ["リゾート", "アウトドア", "自然"], "地方", "暖温帯", True, True),
    Prefecture("福岡県", ["リゾート", "アウトドア", "自然"], "地方", "温暖湿潤", True, True),
    Prefecture("佐賀県", ["リゾート", "アウトドア", "自然"], "地方", "温暖湿潤", True, True),
    Prefecture("長崎県", ["リゾート", "アウトドア", "自然"], "地方", "温暖湿潤", True, True),
    Prefecture("熊本県", ["リゾート", "アウトドア", "自然"], "地方", "温暖湿潤", True, True),
    Prefecture("大分県", ["リゾート", "アウトドア", "自然"], "地方", "温暖湿潤", True, True),
    Prefecture("宮崎県", ["リゾート", "アウトドア", "自然"], "地方", "温暖湿潤", True, True),
    Prefecture("鹿児島県", ["リゾート", "アウトドア", "自然"], "地方", "亜熱帯", True, True),
    Prefecture("沖縄県", ["リゾート", "アウトドア", "自然"], "地方", "亜熱帯", True, True),
    Prefecture("東京都", ["観光", "グルメ", "歴史", "アウトドア"], "都会", "暖温帯", True, True),
    Prefecture("神奈川県", ["観光", "グルメ", "歴史", "アウトドア"], "都会", "暖温帯", True, True),
    Prefecture("千葉県", ["観光", "グルメ", "歴史", "アウトドア"], "都会", "暖温帯", True, True),
    Prefecture("埼玉県", ["観光", "グルメ", "歴史", "アウトドア"], "都会", "暖温帯", True, True),
    Prefecture("大阪府", ["観光", "グルメ", "歴史", "アウトドア"], "都会", "暖温帯", True, True),
    Prefecture("兵庫県", ["観光", "グルメ", "歴史", "アウトドア"], "都会", "暖温帯", True, True),
    Prefecture("京都府", ["観光", "グルメ", "歴史", "アウトドア"], "都会", "暖温帯", True, True),
    Prefecture("福岡県", ["観光", "グルメ", "歴史", "アウトドア"], "都会", "温暖湿潤", True, True),
    Prefecture("愛知県", ["観光", "グルメ", "歴史", "アウトドア"], "都会", "暖温帯", True, True),
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
        print("条件に合致する都道府県が見つかりませんでした。もう一度試してください。")
        return None
    else:
        # ランダムに一つ選んで返す
        recommendation = random.choice(candidates)
        return recommendation

# メイン処理
if __name__ == "__main__":
    # 質問を表示
    answers = []

    for i, question in enumerate(questions):
        print(question)
        for j, answer_option in enumerate(answers_options[i]):
            print(f"{j+1}:{answer_option}", end=" ")

        # 回答を入力
        while True:
            try:
                answer = int(input("\n回答: "))
                if 1 <= answer <= len(answers_options[i]):
                    answers.append(answers_options[i][answer - 1])
                    break
                else:
                    print("有効な番号を選択してください。")
            except ValueError:
                print("回答は数字で入力してください。")

    # 旅行先を診断
    recommendation = diagnose(answers)

    # 診断結果を表示
    if recommendation:
        print("おすすめの旅行先は、", recommendation, "です。")

