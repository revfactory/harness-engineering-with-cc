# ex-13-04 dependency-mapper.md + sample-src → batches.json

책의 `dependency-mapper.md` 전문을 그대로 보존하고, 자체 sample-src/에 mock-mapper.sh를 적용해 결정론적 batches.json을 산출한다.

## 실행

```sh
bash mock-mapper.sh        # batches.json 생성 (LLM 비용 0)
bash verify.sh
```
