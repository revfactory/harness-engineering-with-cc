# 책 원문 vs 우리 파일 충실도

## static-analyzer.md 프론트매터

| 필드 | 책 (p189-191) | 우리 |
|------|--------------|------|
| name | static-analyzer | static-analyzer |
| description | 트리거 키워드 5종 (정적 분석·린트·타입 체크·복잡도·중복) | 동일 (5종 그대로) |
| type | general-purpose | general-purpose |
| model | haiku | haiku |
| tools | Read, Grep, Glob, Bash | Read, Grep, Glob, Bash |

## 본문 6 섹션

| 섹션 | 책 | 우리 |
|------|----|----|
| 핵심 역할 | 있음 | 있음 |
| 작업 원칙 | 4항 | 4항 (변경 라인 우선·도구 우선·거짓 양성 명시·중복/순환의존성) |
| 입출력 | 입력·출력 + 포맷 예시 | 동일 |
| 팀 통신 프로토콜 | 수신/발신 명시 | 동일 |
| 에러 핸들링 | 도구 부재·diff 부재 | 동일 |
| 자체 검증 체크리스트 | 4항 | 4항 (파일·행 / 도구 근거 / Edit·Write 미사용 / 리더 직접 보고) |

## 경계 문단

책: "경계. **코드를 편집하지 않는다.**"
우리: 동일.

## diff 평가
- 프론트매터·트리거 키워드·모델·도구: **diff = 0**
- 본문 섹션 구조: **diff = 0**
- 경계 문단: **diff = 0**
- 출력 포맷 예시 (`### [P0] src/api/users.ts:42 — TypeError: property 'id' is possibly undefined`): **그대로**
