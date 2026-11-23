# peca12968｜軟體工程專案經歷

以下為 AI 輔助開發的個人作品。數字來自可重跑的合成案例與自動化測試。

### 後端工程｜Stockroom Reservations

以 FastAPI 與 SQLite 實作庫存保留，加入 Prometheus 請求計數。用兩個 API 實例處理 842 個測試請求，核對 8 次注入故障皆回滾且記入 HTTP 500 指標，再以同一組指標重播 SLO 告警的觸發與解除。[故障注入與指標驗證](https://github.com/peca12968/stockroom-reservations/blob/a66c91ef763d83ba1c065e9ea8cae0a760862c48/monitoring_drill.py) · [CI](https://github.com/peca12968/stockroom-reservations/actions/runs/45087266022)

### 可靠性工程｜Pass Rail 廚房分站出單

以 Python、HTTP 與 SQLite 串接點餐服務和兩個廚房工作站。分站存好單據後強制終止配送程序，重啟可核對原單據且收件匣只有一張。另以八個配送者競領同一張單，並驗證停發與遲到送單同時抵達的結果。[中斷與競爭測試](https://github.com/peca12968/pass-rail/blob/e52bdb1468117899cf0b5c91d871208ae5ef6264/test_rail.py) · [CI](https://github.com/peca12968/pass-rail/actions/runs/45244734428)

### 資料工程｜Coldroom Inbox 與 Thaw Window

串接 MQTT QoS 1、SQLite 和 Python，建立可去重的冷庫讀值紀錄，按觀測時間估算超溫持續時間。在 15 秒合成案例中，把缺測與同時刻讀值歧異分開計算。經 MQTT 補回一筆晚到資料後，模型估算的超溫時間由 8–13 秒縮至 10–13 秒。[跨服務演練](https://github.com/peca12968/coldroom-inbox/blob/db3fbdab20811500e7269595828aeb794b367e21/coverage-demo.mjs) · [CI](https://github.com/peca12968/coldroom-inbox/actions/runs/45090567932)

### 前端工程｜Focus Receipt

以 JavaScript 和 Playwright 驗證 Chromium 與 Firefox 的鍵盤操作。七步流程跨越兩層 iframe 與 Shadow DOM；即使第三步落在另一個同名「確認」按鈕，測試仍能指出實際框架與元素。[跨來源焦點測試](https://github.com/peca12968/focus-receipt/blob/3bc0875c6ed74812c4ef2b3010348123dd045936/embedded.test.mjs) · [CI](https://github.com/peca12968/focus-receipt/actions/runs/45090951927)

### 全端工程｜禾日食堂線上與掃碼點餐

以 React、Cloudflare Workers 與 D1 建立線上自取、桌邊點餐及廚房接單流程。用獨立解碼器讀取 QR 桌號，再以兩個瀏覽器身分完成點餐與交餐。模擬訂單寫入後回應遺失，關閉分頁再開啟，手機能找回同一取餐號碼，廚房僅收到一張訂單。客人可直接在收據編輯逐菜分攤，測試核對重新整理與切換收據後的個別草稿。串接 TapPay 的四種線上付款方式，在私人預覽提供免扣款示範。用模擬金流測試授權、請款、退款及通知順序異常，另用實際 D1 併發送出兩次付款請求，確認只建立一筆待付交易。[金流整合測試](https://github.com/peca12968/hey-table/blob/d905ccfe1b8237f57e3e5092356c1929fc08587c/qa/tappay.test.mjs) · [CI](https://github.com/peca12968/hey-table/actions/runs/45247590698)

串接廚房匯出與 SQLite 庫存帳，將入庫、製作與訂單領料記為可查驗的收據。八個獨立連線競領最後一份煎茶，庫存只扣一次。煮飯缺水時整筆回滾，補水後可沿用原單號入帳。[領料交易與測試](https://github.com/peca12968/prep-sheet/blob/dcf6360a8530dadc6f11657ad0b69c605a319581/test_ledger.py) · [CI](https://github.com/peca12968/prep-sheet/actions/runs/45238425610)

### 排程演算法｜Pickup Window

以 JavaScript 排定廚房各站的製作批次，根據空位、已完成數量與鍋中剩餘時間估算何時可交整單。用獨立的逐秒模擬器窮舉 729 種工時組合，逐單核對最快、最慢完成時間，再用禾日食堂 Worker 和 D1 的店員匯出檔重跑同一支指令。[區間與窮舉驗證](https://github.com/peca12968/pickup-window/blob/d4ddf360a1ba141a4a27039b8276425638127e70/estimate.test.mjs) · [CI](https://github.com/peca12968/pickup-window/actions/runs/45250062382)

### 金流對帳｜Payout Ledger

以 Python 與 SQLite 核對店內付款和 TapPay 交易。在合成日結案例中追出同一餐單兩筆 NT$120 收款，並用原始金額找出部分退款單的 NT$5 差異。以禾日食堂的資料庫遷移驗證跨日付款歸屬，並測試分頁漏取時會中止報表。[日結整合測試](https://github.com/peca12968/payout-ledger/blob/78f01c6eb079f1d68fe8444f94342e419a6b1327/test_restaurant_close.py) · [CI](https://github.com/peca12968/payout-ledger/actions/runs/45248921613)

### 演算法工程｜現場找零與合菜分帳

以 C# 實作有限庫存的找零演算法，依序最佳化動用的預留枚數與交付總枚數。以 Python 獨立枚舉 64 個班次、512 筆交易，逐筆比對找零結果及錢櫃餘額。[獨立枚舉驗證](https://github.com/peca12968/till-change/blob/210ec2967f8c1394849fd68ae183c98d075ba9c8/test_change.py) · [CI](https://github.com/peca12968/till-change/actions/runs/45239129370)

以 Python 精確分數與最小費用流實作多人按比例分帳。把 A03 桌單的兩道共享小菜分到整元，逐菜金額和兩人應付總額都可對回收據。以 240 張合成帳單的窮舉結果驗證最佳分配，再逐格核對供手機收據使用的 JavaScript BigInt 模組。[分帳窮舉測試](https://github.com/peca12968/table-shares/blob/f96519878f9ac6ad79f7b3eae3602fa0c7a6afc0/test_split.py) · [CI](https://github.com/peca12968/table-shares/actions/runs/45241854623)
