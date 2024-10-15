
# 都道府県をオブジェクトとして扱うクラス
class Prefecture:
    def __init__(self, name, categories, urban_rural, climate, url):
        self.name = name
        self.categories = categories
        self.urban_rural = urban_rural
        self.climate = climate
        self.url = url


    def has_interest(self, interest):
        return interest.lower() in self.categories

# 都道府県のリストを生成
prefectures = [
    Prefecture("北海道", ["観光", "アウトドア", "自然"], "都会", "寒冷地",'https://www.ikyu.com/kankou/area8010/'), 
    Prefecture("青森県", ["観光", "アウトドア", "自然"], "地方", "寒冷地",'https://www.ikyu.com/kankou/area8012/'),
    Prefecture("岩手県", ["観光", "アウトドア", "自然"], "地方", "寒冷地",'https://www.ikyu.com/kankou/area8013/'),
    Prefecture("宮城県", ["観光", "アウトドア", "自然"], "都会", "寒冷地",'https://www.ikyu.com/kankou/area8015/'),
    Prefecture("秋田県", ["観光", "アウトドア", "自然"], "地方", "寒冷地",'https://www.ikyu.com/kankou/area8014/'),
    Prefecture("山形県", ["観光", "アウトドア", "自然"], "地方", "寒冷地",'https://www.ikyu.com/kankou/area8016/'),
    Prefecture("福島県", ["観光", "アウトドア", "自然"], "地方", "寒冷地",'https://www.ikyu.com/kankou/area8017/'),
    Prefecture("茨城県", ["観光", "アウトドア", "自然"], "地方", "暖温帯",'https://www.ikyu.com/kankou/area8018/'),
    Prefecture("栃木県", ["観光", "アウトドア", "自然"], "地方", "暖温帯",'https://www.ikyu.com/kankou/area8019/'),
    Prefecture("群馬県", ["観光", "アウトドア", "自然"], "地方", "暖温帯",'https://www.ikyu.com/kankou/area8020/'),
    Prefecture("埼玉県", ["観光", "アウトドア", "自然"], "地方", "暖温帯",'https://www.ikyu.com/kankou/area8021/'),
    Prefecture("千葉県", ["観光", "アウトドア", "自然"], "都会", "暖温帯",'https://www.ikyu.com/kankou/area8025/'),
    Prefecture("東京都", ["観光", "アウトドア"], "都会", "暖温帯",'https://www.ikyu.com/kankou/area8023/'),
    Prefecture("神奈川県", ["観光", "アウトドア"], "都会", "暖温帯",'https://www.ikyu.com/kankou/area8024/'),
    Prefecture("新潟県", ["観光", "アウトドア", "自然"], "地方", "暖温帯",'https://www.ikyu.com/kankou/area8027/'),
    Prefecture("富山県", ["観光", "アウトドア", "自然"], "地方", "暖温帯",'https://www.ikyu.com/kankou/area8028/'),
    Prefecture("石川県", ["観光", "アウトドア", "自然"], "地方", "暖温帯",'https://www.ikyu.com/kankou/area8029/'),
    Prefecture("福井県", ["観光", "アウトドア", "自然"], "地方", "暖温帯",'https://www.ikyu.com/kankou/area8030/'),
    Prefecture("山梨県", ["観光", "アウトドア", "自然"], "地方", "暖温帯",'https://www.ikyu.com/kankou/area8031/'),
    Prefecture("長野県", ["観光", "アウトドア", "自然"], "地方", "暖温帯",'https://www.ikyu.com/kankou/area8026/'),
    Prefecture("岐阜県", ["観光", "アウトドア", "自然"], "地方", "暖温帯",'https://www.ikyu.com/kankou/area8033/'),
    Prefecture("静岡県", ["観光", "リゾート", "温泉", "アウトドア", "自然"], "地方", "暖温帯",'https://www.ikyu.com/kankou/area8031/'),
    Prefecture("愛知県", ["観光", "アウトドア", "自然"], "地方", "暖温帯",'https://www.ikyu.com/kankou/area8032/'),
    Prefecture("三重県", ["リゾート", "アウトドア", "自然"], "地方", "暖温帯",'https://www.ikyu.com/kankou/area8034/'),
    Prefecture("滋賀県", ["観光", "アウトドア", "自然"], "地方", "暖温帯",'https://www.ikyu.com/kankou/area8035/'),
    Prefecture("京都府", ["観光", "アウトドア", "自然"], "都会", "暖温帯",'https://www.ikyu.com/kankou/area8037/'),
    Prefecture("大阪府", ["観光", "アウトドア", "自然"], "都会", "暖温帯",'https://www.ikyu.com/kankou/area8036/'),
    Prefecture("兵庫県", ["観光", "アウトドア", "自然"], "都会", "暖温帯",'https://www.ikyu.com/kankou/area8038/'),
    Prefecture("奈良県", ["観光", "アウトドア", "自然"], "地方", "暖温帯",'https://www.ikyu.com/kankou/area8039/'),
    Prefecture("和歌山県", ["観光", "アウトドア", "自然"], "地方", "暖温帯",'https://www.ikyu.com/kankou/area8040/'),
    Prefecture("鳥取県", ["リゾート", "アウトドア", "自然"], "地方", "暖温帯",'https://www.ikyu.com/kankou/area8041/'),
    Prefecture("島根県", ["リゾート", "アウトドア", "自然"], "地方", "暖温帯",'https://www.ikyu.com/kankou/area8042/'),
    Prefecture("岡山県", ["リゾート", "アウトドア", "自然"], "地方", "暖温帯",'https://www.ikyu.com/kankou/area8043/'),
    Prefecture("広島県", ["リゾート", "アウトドア", "自然"], "都会", "暖温帯",'https://www.ikyu.com/kankou/area8044/'),
    Prefecture("山口県", ["リゾート", "アウトドア", "自然"], "地方", "暖温帯",'https://www.ikyu.com/kankou/area8045/'),
    Prefecture("徳島県", ["リゾート", "アウトドア", "自然"], "地方", "暖温帯",'https://www.ikyu.com/kankou/area8048/'),
    Prefecture("香川県", ["リゾート", "アウトドア", "自然"], "地方", "暖温帯",'https://www.ikyu.com/kankou/area8046/'),
    Prefecture("愛媛県", ["リゾート", "アウトドア", "自然"], "地方", "暖温帯",'https://www.ikyu.com/kankou/area8047/'),
    Prefecture("高知県", ["リゾート", "アウトドア", "自然"], "地方", "暖温帯",'https://www.ikyu.com/kankou/area8049/'),
    Prefecture("福岡県", ["リゾート", "観光", "グルメ", "歴史", "アウトドア"], "都会", "温暖湿潤",'https://www.ikyu.com/kankou/area8050/'),
    Prefecture("佐賀県", ["リゾート", "アウトドア", "自然"], "地方", "温暖湿潤",'https://www.ikyu.com/kankou/area8051/'),
    Prefecture("長崎県", ["リゾート", "アウトドア", "自然"], "地方", "温暖湿潤",'https://www.ikyu.com/kankou/area8052/'),
    Prefecture("熊本県", ["リゾート", "アウトドア", "自然"], "地方", "温暖湿潤",'https://www.ikyu.com/kankou/area8053/'),
    Prefecture("大分県", ["リゾート", "アウトドア", "自然"], "地方", "温暖湿潤",'https://www.ikyu.com/kankou/area8054/'),
    Prefecture("宮崎県", ["リゾート", "アウトドア", "自然"], "地方", "温暖湿潤",'https://www.ikyu.com/kankou/area8055/'),
    Prefecture("鹿児島県", ["リゾート", "アウトドア", "自然"], "地方", "亜熱帯",'https://www.ikyu.com/kankou/area8056/'),
    Prefecture("沖縄県", ["リゾート", "アウトドア", "自然"], "地方", "亜熱帯",'https://www.ikyu.com/kankou/area8011/')
]
