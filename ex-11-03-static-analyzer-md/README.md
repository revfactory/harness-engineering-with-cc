# ex-11-03 static-analyzer.md + sample TS PR

> static-analyzer 에이전트 실물 + 의도된 정적 이슈 심긴 TS PR. mock 모드 산출.

## 빠른 실행 (mock — 산출 확인)

```bash
ls /Users/robin/Documents/harness-book-example/built-harnesses/ex-11-03-static-analyzer-md/result/
# 01_static.md
ls /Users/robin/Documents/harness-book-example/built-harnesses/ex-11-03-static-analyzer-md/.claude/agents/
# static-analyzer.md
```

## 실 Claude Code 호출 (옵션)

```
cd fixtures/sample-pr
# claude  (이 환경에서는 미실행)
# > static-analyzer로 pr-001.diff 분석
```
