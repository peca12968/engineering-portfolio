# 個人 AI 助理｜離線評測發布檢查

用同一套題目和評分標準比較改版前後的結果。實作先沿用個人 AI 助理的 `review_understanding.compare`，核對原始題庫的 SHA-256、案例選取、版本可比性，以及逐題評讀和答案的綁定。接著檢查每題每項標準。任何一項從通過變為失敗，都會列出案例與標準序號。待評讀、缺少來源、評讀未綁定、評讀者更換或固定測試器缺少指紋，也會阻擋閘門。

合成示範中，候選版本把通過數從 2 題提升到 3 題，同時漏掉原本正確的引用行號。閘門會攔下這次改版。另有全面改善、待評讀及更換評讀者三個情境。所有評分與答案均為自行編寫的合成資料，僅用來驗證評測工具。

## 重跑合成展示

用 Python 3.12 搭配 `sample.json` 所記錄的助理 Git 提交。從作品集根目錄執行下列命令。

```sh
python -B examples/assistant-eval/make_demo.py --assistant-root ../personal-ai-assistant --check
```

## 比較本機報告

```sh
python -B examples/assistant-eval/regression.py --assistant-root ../personal-ai-assistant --suite suite.json --baseline before.json --candidate after.json
```

結果 JSON 列出前後通過數、可配對數、每題結果及阻擋理由。通過閘門的結束碼為 0；證據有效但有阻擋原因為 1；題庫、報告或讀取發生錯誤為 2。原始題庫與實際報告留在本機。整個比較流程只讀取現有報告。

[合成輸出](sample.json) · [離線檢查測試](test_regression.py) · [GitHub CI 設定](../../.github/workflows/assistant-eval.yml)
