# security-analyst

책 security-analyst 에이전트 + 샘플 취약 코드 (extend).

## 규칙
- security-analyst.md는 책 원문을 따른다 (tools에 Write/Edit 의도적 제외 — 핵심 패턴).
- 에이전트는 코드를 **읽고 분석만** 한다. 수정 시도 금지(tools가 물리적으로 차단).
- sample-app은 의도적 취약 데모 — 격리 디렉토리에서만. 실제 배포 금지.
- 보고서는 심각도(C/H/M/L) + 위치(파일:라인) + 설명 + 권장 수정안 형식.

## 재현 호출
```bash
claude --agent security-analyst "sample-app/ 디렉토리의 보안 취약점을 분석하고
심각도(Critical/High/Medium/Low)·위치·설명·권장 수정안 형식으로 보고하라. 코드는 수정하지 말 것."
```
산출: result/security-report.md (이 sub-harness에는 예상 보고서를 미리 기록).
