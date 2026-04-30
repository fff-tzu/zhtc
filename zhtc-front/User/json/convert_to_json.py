import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
JSON_DIR = BASE_DIR.parent / "json"
JSON_DIR.mkdir(exist_ok=True)

def read_csv_file(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

official = read_csv_file(BASE_DIR / "公园管理中心停车场信息_2920000101036.csv")
nanshan = read_csv_file(BASE_DIR / "nanshan_parking.csv")

coord_by_name = {}
for row in nanshan:
    coord_by_name.setdefault(row["name"], row)

fallback = {
    "莲花山公园东南门、东北门和西侧停车场": {"lat": "22.544", "lon": "113.906", "risk_level": "低风险"},
    "荔枝公园通心岭停车场": {"lat": "22.552", "lon": "114.092", "risk_level": "中风险"}
}

def to_int(value, default=0):
    try:
        return int(float(str(value).strip()))
    except Exception:
        return default

def to_float(value, default=None):
    try:
        return float(str(value).strip())
    except Exception:
        return default

seen = set()
source_rows = []
for row in official:
    key = (
        row["停车场名称"].strip(),
        row["停车场地址"].strip(),
        row["停车泊位总数"].strip(),
        row["公园"].strip()
    )
    if key in seen:
        continue
    seen.add(key)
    source_rows.append(row)

parking_base = []
risk_seed = []

for idx, row in enumerate(source_rows, start=1):
    name = row["停车场名称"].strip()
    matched = coord_by_name.get(name) or fallback.get(name) or {}
    lat = to_float(matched.get("lat"))
    lng = to_float(matched.get("lon"))

    if lat is None or lng is None:
        lat = 22.54 + (idx % 7) * 0.003
        lng = 113.92 + (idx % 11) * 0.004

    parking_base.append({
        "id": idx,
        "name": name,
        "park": row["公园"].strip(),
        "capacity": to_int(row["停车泊位总数"]),
        "lat": round(lat, 6),
        "lng": round(lng, 6)
    })

    risk_seed.append((matched.get("risk_level", "中风险") or "中风险").replace("风险", ""))

def risk_by_rate(rate):
    if rate >= 0.85:
        return "高"
    if rate >= 0.70:
        return "中"
    return "低"

base_rate = {
    "低": {"08:00": 0.42, "12:00": 0.62, "18:00": 0.74},
    "中": {"08:00": 0.52, "12:00": 0.74, "18:00": 0.84},
    "高": {"08:00": 0.62, "12:00": 0.88, "18:00": 0.93}
}

prediction_data = []
for base, risk in zip(parking_base, risk_seed):
    risk = risk if risk in base_rate else "中"
    for time in ["08:00", "12:00", "18:00"]:
        variation = ((base["id"] * 17 + int(time[:2])) % 7 - 3) * 0.01
        rate = max(0.05, min(0.98, base_rate[risk][time] + variation))
        capacity = base["capacity"]
        occupied = min(capacity, max(0, round(capacity * rate)))
        available = max(0, capacity - occupied)
        pred_add = {"08:00": 0.08, "12:00": 0.10, "18:00": 0.06}[time]
        prediction = min(capacity, max(occupied, round(capacity * min(0.99, rate + pred_add))))
        recommend_score = round(
            0.45 * (available / capacity if capacity else 0)
            + 0.35 * (1 - rate)
            + 0.20 * (1 - prediction / capacity if capacity else 0),
            2
        )
        prediction_data.append({
            "parking_id": base["id"],
            "time": time,
            "occupied": occupied,
            "available": available,
            "occupancy_rate": round(occupied / capacity, 2) if capacity else 0,
            "prediction": prediction,
            "risk": risk_by_rate(occupied / capacity if capacity else 0),
            "recommend_score": recommend_score
        })

with open(JSON_DIR / "parking_base.json", "w", encoding="utf-8") as f:
    json.dump(parking_base, f, ensure_ascii=False, indent=2)

with open(JSON_DIR / "parking_prediction_simulated.json", "w", encoding="utf-8") as f:
    json.dump(prediction_data, f, ensure_ascii=False, indent=2)

print(f"转换完成：{len(parking_base)} 个停车场，{len(prediction_data)} 条预测记录")
