# copy-editor

copy-editor 에이전트 + 가상 원고 (extend).

## 규칙
- copy-editor.md는 책 원문을 따른다. tools 미명시 = 부모 상속, model: opus 그대로.
- 기계적 교정 3종만: ① 산문 끝 콜론 제거 ② Bold 한글 조사 위반 ③ 명백한 오탈자.
- 예외 케이스(시간 `12:30`, 코드 블록 내 콜론, 표 헤더)는 **수정하지 않는다**.
- 모호 케이스는 고치지 말고 **보류 항목**으로 보고.
- 리포트 형식: `## 처리 요약`(표) → `## 파일별 처리 내역` → `## 보류 항목`.
- diff 단위는 작게 — 한 라인 여러 변경은 분리.

## 재현 호출
```bash
claude --agent copy-editor "sample-doc/ch-07-draft.md 를 콜론·Bold조사·오탈자 기준으로 교정하고 reviews/copy-edit-report.md 에 리포트를 남겨라"
```
산출: result/copy-edit-report.md (이 sub-harness에는 예상 리포트를 미리 기록).
