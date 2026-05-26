---
name: tip-collect
description: Claude Code 사용 팁의 소재를 신뢰 가능한 소스에서 모으는 절차. 주제가 주어지면 어떤 소스를 어떤 순서로 뒤져야 하는지 정의한다.
---

# tip-collect

Claude Code 팁 소재 수집 표준 절차.

## 소스 우선순위
1. **공식 문서**: https://docs.claude.com/claude-code (features, hooks, slash-commands, mcp, skills, settings, subagents)
2. **공식 저장소**: https://github.com/anthropics/claude-code (릴리즈 노트, 이슈, CHANGELOG)
3. **사용자 설정**: `~/.claude/` (settings.json, agents/, skills/, commands/)
4. **세션 관찰**: 현재 대화에서 드러난 기능/에러/도구 목록

## 수집 단계
1. 주제 확정 — 예: "훅", "서브에이전트", "MCP"
2. 위 소스에서 관련 키워드 검색 (WebFetch/WebSearch/Grep)
3. 각 후보마다 다음 4가지를 메모:
   - **제목(한글)**
   - **한 줄 요약**
   - **출처 URL 또는 파일 경로**
   - **검증 방법** (실행해볼 명령/설정)
4. 중복 제거 — 이미 `tips/`에 있는 항목은 제외 (Grep으로 체크)
5. 추측·미검증 내용 제외

## 출력
Markdown 체크리스트:
```
## 주제: <주제>
- [ ] <제목> — <요약> (출처: <링크>)
```
