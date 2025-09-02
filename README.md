# charcount-api
공백(스페이스/개행/탭 + 0폭 공백 옵션)을 제외한 글자수 계산 API

## 사용
GET  /charcount?text=안녕%20하세요
POST /charcount
{ "text": "안녕 하세요\n\t친구들" }

헬스체크: /healthz
