import random


def create_teams(members, team_num):
    # チーム分け結果
    result = {}

    # メンバに0~100の乱数を定義
    dct = {}
    for member in members:
        dct[member] = random.randint(0, 1000)

    # メンバ数とチーム数から、1チームあたりの人数を計算
    num = len(members) / team_num
    print("num: " + str(num))

    for team in range(team_num):
        # 仮のチームリスト
        tmp = []

        # value値を昇順でソートしてループ
        for k, v in sorted(dct.items(), key=lambda x: x[1]):
            # 仮のチームリストに追加
            tmp.append(k)
            # 乱数辞書から削除
            del dct[k]

            # 人数が埋まったら次のチームへ
            if len(tmp) >= num:
                break

        # 結果に仮のチームを追加
        result[team] = tmp

    return result
