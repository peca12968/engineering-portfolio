# peca12968｜軟體工程專案經歷

以下為 AI 輔助開發的個人作品。數字來自可重跑的合成案例與自動化測試。

### 後端工程｜Stockroom Reservations

以 FastAPI 與 SQLite 實作庫存保留，加入 Prometheus 請求計數。用兩個 API 實例處理 842 個測試請求，核對 8 次注入故障皆回滾且記入 HTTP 500 指標，再以同一組指標重播 SLO 告警的觸發與解除。[故障注入與指標驗證](https://github.com/peca12968/stockroom-reservations/blob/a66c91ef763d83ba1c065e9ea8cae0a760862c48/monitoring_drill.py) · [CI](https://github.com/peca12968/stockroom-reservations/actions/runs/45087266022)

### 資料工程｜Coldroom Inbox 與 Thaw Window

串接 MQTT QoS 1、SQLite 和 Python，建立可去重的冷庫讀值紀錄，按觀測時間估算超溫持續時間。在 15 秒合成案例中，把缺測與同時刻讀值歧異分開計算。經 MQTT 補回一筆晚到資料後，模型估算的超溫時間由 8–13 秒縮至 10–13 秒。[跨服務演練](https://github.com/peca12968/coldroom-inbox/blob/db3fbdab20811500e7269595828aeb794b367e21/coverage-demo.mjs) · [CI](https://github.com/peca12968/coldroom-inbox/actions/runs/45090567932)

### 前端工程｜Focus Receipt

以 JavaScript 和 Playwright 建立 11 步鍵盤回歸測試，在第 8 步定位文件封存後的焦點遺失。修正後以 Chromium 與 Firefox 核對焦點能移到下一筆文件，清單清空時則移到空清單標題。[鍵盤回歸測試](https://github.com/peca12968/focus-receipt/blob/e339536fcfaba6cd909cd43234a3ebd723e23eb8/focus.test.mjs) · [CI](https://github.com/peca12968/focus-receipt/actions/runs/45068024391)
