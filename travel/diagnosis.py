import random

def diagnose(answers, prefectures, categories, urban_rural, climate):
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
