---
name: tip-publish
description: 작성된 팁 문서를 tips/에 저장하고 tips/README.md 인덱스를 갱신하는 발행 절차.
---

# tip-publish

팁 문서 발행/인덱싱 절차.

## 단계
1. `tip-format` 규약 준수 여부 확인 (프론트매터, 본문 구조).
2. 파일을 `tips/<kebab-case>.md`로 저장.
3. `tips/README.md`를 갱신:
   - 태그/카테고리별 섹션 유지
   - 항목 포맷: `- [<제목>](<파일명>.md) — <한 줄 요약>`
   - 알파벳/업데이트일 기준 정렬
4. 같은 주제 기존 파일이 있으면 **Edit로 병합**하고 `updated` 갱신. 새 파일을 중복 생성하지 않는다.
5. 변경 요약을 응답으로 돌려준다.

## tips/README.md 템플릿
```markdown
# Claude Code 사용 팁 인덱스

마지막 갱신: YYYY-MM-DD

## 훅 (Hooks)
- ...

## 서브에이전트
- ...

## 스킬
- ...

## 설정/키바인딩
- ...

## MCP
- ...
```
