# peca12968｜軟體工程專案經歷

以下為 AI 輔助開發的個人作品。數字來自可重跑的合成案例與自動化測試。

### 禾日食堂｜點餐、營運與倉庫

整合掃碼內用、自取、LINE Pay 與全支付等示範付款，以 D1 交易與版本檢查實作單桌及接單管道暫停。倉庫用 FastAPI 與 SQLite 整批保留多個商品，並以同一筆交易查詢各品項的出貨、保留、釋回與可用庫存。兩個服務實例並行驗證，快照與整批取消維持一致。[實作與重跑](https://github.com/peca12968/hey-table/blob/70f83c0e8c1253d7f0ee5481524d9fc04ee981ca/modules/stockroom-reservations/README.md) · [CI](https://github.com/peca12968/hey-table/actions/runs/45356865776)

### 交班與排班工作台

用 JavaScript 依引文與前後文在 SQLite 歷史版本中找回移動的段落。以 Chromium 與 Firefox 驗證四版紀錄的定位、並列、移除、同分頁復原與鍵盤操作。交班紀錄以 HTTP ETag 保護並行修改，排班支援跨時區偏好排序與 iCalendar 匯出。[實作與重跑](https://github.com/peca12968/handoff-desk/blob/6b0856a744761bcd915f670c993274eafd7d6eb8/README.md) · [CI](https://github.com/peca12968/handoff-desk/actions/runs/45361019668)

### 工程發布與測試工具

以 Node.js 與 Git 規劃 PR、分支推送及提交前測試。用真實的分岔提交重現強制推送，辨識被移除的舊契約並納入下游 API，讓範例從 3 個增加到 5 個受影響專案。缺少舊提交時改走全量測試，並在 Linux 與 Windows 驗證行為。[實作與重跑](https://github.com/peca12968/ci-impact-planner/blob/79926156a79968704aa19832aae9caeca61ad1ea/README.md) · [CI](https://github.com/peca12968/ci-impact-planner/actions/runs/45345456441)

### 服務觀測與執行可靠性

以 React 與 TypeScript 匯入路由級統計，將分項加總到同一 UTC 區間的整體 SLO。以 BigInt 精確核對路由超額、餘額與整體淨差額，並用 Playwright 驗證缺日、零流量、錯誤檔案及舊格式相容。另支援由輪替日誌重算可用率與雙區間消耗比較。[實作與重跑](https://github.com/peca12968/slo-window/blob/5941558af3c98fc4934d251eb37f9b711e537c3a/README.md) · [CI](https://github.com/peca12968/slo-window/actions/runs/45362462438)

### 資料回溯與品質查核

以 DuckDB 雙時間查詢比較 SKU 的價格生效區間，追查特價改期、歧義消解與同價換版，並以獨立重播核對 540 個微秒級時點在兩個截止點的價格與來源。固定舊訂單範圍的比較明細也可匯出為 Parquet。[實作與重跑](https://github.com/peca12968/price-as-of/blob/1999f957bc1e0e81b3eec1080dc80d820b9bbb8f/README.md) · [CI](https://github.com/peca12968/price-as-of/actions/runs/45358453663)

### 知識檢索與工單派送

以 SQLite FTS5 檢索中英文手冊，依 BM25 原排名跳過內容失效或位置重複的段落，逐筆保留可引用的現行行號及掃描結果。另為 TF-IDF 工單模型加入上線關卡，核對新增誤派、人工覆核量和精確率。[實作與重跑](https://github.com/peca12968/handbook-search/blob/24f59867bd04df3241ea943ca13228c49f6dbc77/README.md) · [CI](https://github.com/peca12968/handbook-search/actions/runs/45353888587)

### 轉乘規劃與離線地圖

以 Python 共用班表掃描，比較多個上下車站與首尾步行的跨午夜門到門行程。支援最早抵達、最晚出發、定向轉乘、班次異動與確認的無階梯步行。以 120 份合成班表窮舉核對兩種方向，並驗證既有 C# 單車站點串接。[實作與重跑](https://github.com/peca12968/transfer-clock/blob/e6b0ad3da3081264cc18b823d9d5949480edca36/README.md) · [CI](https://github.com/peca12968/transfer-clock/actions/runs/45359793917)

### 媒體處理與檔案交付

以 C# 剪輯 16/24 位元 PCM，再以 Python 從已驗收的 ZIP 串流複製 13,200 幀，重算 WebVTT 字幕時碼並保留其版面設定。逐位元組核對輸出、驗證 SHA-256，並測試兩個程序競爭同一交付檔名。另支援雙重校驗分片的區間還原。[實作與重跑](https://github.com/peca12968/take-splice/blob/13856b72379b21adcdd5240855ec1b92fbbcd070/README.md) · [CI](https://github.com/peca12968/take-splice/actions/runs/45364058692)

### 離線文件轉 HTML

以 Python、PDFium 和 OpenCV 實作離線文件轉換，讓桌面與命令列可指定頁碼及範圍。圖片版和結構化 HTML 共用選頁邏輯，保留來源頁碼與 OCR 診斷。以 Playwright 核對輸出的搜尋結果及列印頁數。[實作與重跑](https://github.com/peca12968/document-to-html/blob/c006ecbf49b8aaa28715ac200037eacb5a04fb7d/README.md) · [CI](https://github.com/peca12968/document-to-html/actions/runs/45355375138)
