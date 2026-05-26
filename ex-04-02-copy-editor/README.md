# ex-04-07 — copy editor

copy-editor(검수 1단계, 기계적 교정 3종)를 작성하고 의도적 위반을 심은 가상 원고에 적용해 책 명세 형식 리포트를 산출 (extend).

## 실행 (메인 batch)
```
claude --agent copy-editor "sample-doc/ch-07-draft.md 를 콜론·Bold조사·오탈자 기준으로 교정하라"
```
예상 산출: `result/copy-edit-report.md`(교정 리포트), `result/diff-trace.md`(변경 추적).
