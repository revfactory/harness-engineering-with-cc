# 책 원문 vs 우리 프론트매터 충실도

## security-auditor.md
| 필드 | 책 p191 | 우리 | diff |
|------|--------|------|------|
| name | security-auditor | security-auditor | 0 |
| model | sonnet | sonnet | 0 |
| tools | Read, Grep, Glob, Bash | Read, Grep, Glob, Bash | 0 |
| 트리거 키워드 | 보안 감사·취약점·SQL 인젝션·XSS·인증·OWASP | 동일 | 0 |
| Bash 명령 | npm audit, semgrep | npm audit, semgrep | 0 |

## design-reviewer.md
| 필드 | 책 p191 | 우리 | diff |
|------|--------|------|------|
| name | design-reviewer | design-reviewer | 0 |
| model | opus | opus | 0 |
| tools | Read, Grep, Glob (**Bash 없음**) | Read, Grep, Glob | 0 |
| 트리거 키워드 | 설계 검토·경계면·구조 리뷰 | 동일 | 0 |
| 경계면 7패턴 | 응답 래핑·케이스 변환·파일경로↔링크·상태 전이·API↔훅 매핑·즉시응답↔비동기·옵셔널 필드 | 동일 | 0 |

## refactorer.md
| 필드 | 책 p192 | 우리 | diff |
|------|--------|------|------|
| name | refactorer | refactorer | 0 |
| model | opus | opus | 0 |
| tools | Read, Grep, Glob, **Edit** | Read, Grep, Glob, Edit | 0 |
| 트리거 키워드 | 리팩토링·patch·수정 제안·리뷰 반영 | 동일 | 0 |
| Edit 대상 | `_workspace/patches/*.diff`만 | 동일 | 0 |
| 생성-검증 루프 상한 | 3회 | 3회 | 0 |
| 자동 커밋 금지 | 명시 | 명시 | 0 |

## 본문 6 섹션 (static-analyzer 구조 복제 — 책에 없는 보완)
- 핵심 역할 / 작업 원칙 / 입출력 / 팀 통신 / 에러 / 자체 검증 — 3 .md 모두 동일 뼈대.
- 본문 텍스트는 책 가이드에 맞게 작성. 프론트매터·경계 문단·핵심 표현은 그대로.
