from datetime import datetime
import json
def modelbuild(data: dict) -> dict:
    ret = dict()  # 結果を格納する辞書
    for i in data:
        # data[i]["Words"] と data[i]["Tags"] の値を取得
        words = data[i].get("Words", [])
        tags = data[i].get("Tags", [])
        
        for j in words:
            for k in tags:
                # jとkがretに存在しない場合は初期化
                if j not in ret:
                    ret[j] = {}  # jの初期化（辞書）
                if k not in ret[j]:
                    ret[j][k] = 0  # kの初期化（カウント）
                
                # カウントをインクリメント
                ret[j][k] += 1

    for i in ret:
        cnt = 0
        for j in ret[i]:
            cnt += ret[i][j]
        for j in ret[i]:
            ret[i][j]/=cnt
    now = datetime.now().strftime(r"%Y%m%d_%H%M%S")
    with open(f"model_{now}.json", 'w') as f:
        json.dump(ret, f, indent=2)
    return ret