# 하네스엔지니어링 with Claude Code — 예제 모음

> 책 **《하네스엔지니어링 with Claude Code》** 의 실습 예제 저장소입니다.
> [한빛미디어 도서 페이지](https://www.hanbit.co.kr/store/books/look.php?p_code=B2817272480)

Claude Code를 "한 번의 대화를 잘 굴리는 도구"가 아니라 **작업 환경(=하네스)을 미리 세팅해두는 도구** 로 다루기 위한 실습들을 챕터·절 단위로 묶어 두었습니다. 각 예제 폴더에는 자체 `README.md` 가 들어 있으니 실행 방법과 결과 비교는 해당 폴더의 문서를 참고하세요.

---

## 예제 인덱스

| 예제 | 주제 | 설명 |
|---|---|---|
| [`ex-02-01-ab-comparison`](./ex-02-01-ab-comparison) | 하네스 적용 전/후 A/B 비교 | 동일한 한 줄 프롬프트(`claude code 사용 팁 정리해주세요`)를 **맨몸**과 **하네스 적용** 두 가지 방식으로 실행한 결과를 2단 페이지로 비교합니다. |
| [`ex-02-02-my-first-harness`](./ex-02-02-my-first-harness) | 첫 하네스 만들기 — 2인 팀 커밋 메시지 생성 | `commit-msg-author` 와 `commit-msg-reviewer` 두 에이전트, 그리고 이들을 순차 호출하는 `commit-message` 스킬로 구성한 최소 하네스. 스테이지된 변경을 받아 Conventional Commits 형식의 커밋 메시지를 author·reviewer 협업으로 생성합니다. |
| [`ex-04-01-security-analyst`](./ex-04-01-security-analyst) | 읽기 전용 보안 분석 에이전트 | `tools` 에서 `Write`/`Edit` 을 의도적으로 제외해 **수정 권한을 물리적으로 차단**한 `security-analyst` 에이전트. 의도적으로 취약점을 심은 Flask 샘플 앱(`sample-app/`)에 적용해 심각도·위치·권장 수정안 형식의 보고서를 산출합니다. |
| [`ex-04-02-copy-editor`](./ex-04-02-copy-editor) | 기계적 교정 에이전트 — 1단계 검수 | 산문 끝 콜론·Bold 한글 조사·명백한 오탈자 3종만 기계적으로 잡는 `copy-editor` 에이전트. 위반을 의도적으로 심은 가상 원고(`sample-doc/ch-07-draft.md`)에 적용해 처리 요약·파일별 내역·보류 항목 형식의 리포트를 만듭니다. |
| [`ex-13-01-dependency-mapper`](./ex-13-01-dependency-mapper) | 의존성 그래프 → 병렬 배치 계획 | `Read, Grep, Bash` 만으로 동작하는 `dependency-mapper` 에이전트가 `sample-src/` 의 import 그래프를 분석해 위상정렬 결과를 결정론적 `batches.json` 으로 산출. 기본은 mock 모드(LLM 호출 0), `USE_LIVE_LLM=1` 환경변수에서 실제 sonnet 호출 모드로 동작합니다. |

> 추가 예제는 챕터 진행에 따라 같은 컨벤션으로 계속 추가될 예정입니다.

---

## 시작하기

```bash
# 1. 저장소 클론
git clone https://github.com/revfactory/harness-engineering-with-cc.git
cd harness-engineering-with-cc

# 2. 원하는 예제 폴더로 이동
cd ex-02-01-ab-comparison

# 3. 폴더 안의 README를 따라 실습 진행
open README.md
```

Claude Code 설치 및 기본 사용법은 [공식 문서](https://docs.claude.com/en/docs/claude-code/overview) 를 참고하세요.

---

## 라이선스

이 저장소의 코드 예제는 [Apache License 2.0](./LICENSE) 을 따릅니다. 책의 본문·도판 등 출판물 콘텐츠 자체의 저작권은 저자 및 한빛미디어에 귀속됩니다.
