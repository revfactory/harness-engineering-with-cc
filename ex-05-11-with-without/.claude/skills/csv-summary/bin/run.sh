#!/usr/bin/env bash
# csv-summary 실제 구현 — stdlib만 사용 (pandas 불필요).
# 사용: bash run.sh <csv_path> <out_md>
set -euo pipefail
CSV="${1:?csv path required}"
OUT="${2:?out md required}"

python3 - "$CSV" "$OUT" <<'PY'
import sys, csv, statistics
csv_path, out_path = sys.argv[1], sys.argv[2]
with open(csv_path, newline="") as f:
    rows = list(csv.DictReader(f))
cols = list(rows[0].keys()) if rows else []

def is_num(v):
    try:
        float(v); return True
    except: return False

lines = ["# CSV 요약 (csv-summary 스킬)\n"]
lines.append(f"- 행 수: {len(rows)}")
lines.append(f"- 열 수: {len(cols)}\n")

lines.append("## 열별 dtype 추론\n")
lines.append("| 열 | dtype |")
lines.append("|----|-------|")
num_cols = []
for c in cols:
    vals = [r[c] for r in rows]
    numeric = all(is_num(v) for v in vals if v != "")
    dtype = "numeric" if numeric else "string"
    if numeric: num_cols.append(c)
    lines.append(f"| {c} | {dtype} |")
lines.append("")

lines.append("## 숫자 열 통계\n")
lines.append("| 열 | 평균 | 중앙값 | 표준편차 |")
lines.append("|----|------|--------|----------|")
for c in num_cols:
    vals = [float(r[c]) for r in rows if r[c] != ""]
    mean = round(statistics.mean(vals), 2)
    med = round(statistics.median(vals), 2)
    sd = round(statistics.pstdev(vals), 2)
    lines.append(f"| {c} | {mean} | {med} | {sd} |")
lines.append("")

# 그룹 요약: department별 salary 평균 (프롬프트가 부서별 평균 연봉을 요청)
if "department" in cols and "salary" in cols:
    groups = {}
    for r in rows:
        groups.setdefault(r["department"], []).append(float(r["salary"]))
    lines.append("## 부서별 평균 연봉 (그룹 집계)\n")
    lines.append("| 부서 | 평균 연봉 | 인원 |")
    lines.append("|------|-----------|------|")
    for dept in sorted(groups):
        vals = groups[dept]
        lines.append(f"| {dept} | {round(statistics.mean(vals),2)} | {len(vals)} |")
    lines.append("")

with open(out_path, "w") as f:
    f.write("\n".join(lines) + "\n")
print(f"wrote {out_path}")
PY
