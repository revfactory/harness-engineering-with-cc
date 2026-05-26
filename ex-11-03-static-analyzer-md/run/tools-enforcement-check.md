# tools 강제 검증 메모

> 본 sub-harness는 실 Claude Code 호출 없이 mock으로 산출(예상 출력)을 작성했다. 권한 검증은 정의 파일(.md)을 기준으로 한다.

## 정의 파일 검증

`.claude/agents/static-analyzer.md` 프론트매터:

```
tools: Read, Grep, Glob, Bash
```

- `Edit` 없음 ✓
- `Write` 없음 ✓

## 호출 시도 매트릭스 (mock)

| 도구 | 정의 부여 | 보고서 작성 중 시도 | 비고 |
|------|---------|-----------------|------|
| Read | ✓ | (소스 인용) | OK |
| Grep | ✓ | (중복 패턴 탐지) | OK |
| Glob | ✓ | (변경 파일 탐색) | OK |
| Bash | ✓ | tsc --noEmit, eslint | OK (화이트리스트) |
| Edit | ✗ | 0회 | 발견만 보고, patch 제안은 refactorer에 전달 |
| Write | ✗ | 0회 | 보고서는 표준 경로(_workspace/review/01_static.md)에 한정 |

## 검증 결론
- Edit·Write 호출 시도 **0건** (mock 출력 기준).
- live 모드 실행 시 위 매트릭스로 검증할 것.
