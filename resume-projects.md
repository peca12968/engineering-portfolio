# peca12968｜軟體工程專案經歷

以下為 AI 輔助開發的個人作品。數字來自可重跑的合成案例與自動化測試。

### 禾日食堂｜點餐、營運與倉庫

整合掃碼內用、自取、LINE Pay 與全支付等示範付款。由舊收據帶入餐點時，按最新菜單計價並檢查售況與數量上限。端對端測試驗證同桌餐單合併、其他管道草稿隔離，以及先前送單結果待確認時的保護。店員可精確查找取餐號碼並列印交餐小票。若另一位店員已完成交餐，會先顯示最新狀態供核對。倉庫可依批號核對保留與可用庫存。[實作與重跑](https://github.com/peca12968/hey-table/blob/839fdcfd6e67088caa14139a15aa8d4ab3b4975f/README.md) · [CI](https://github.com/peca12968/hey-table/actions/runs/45460425575)

### 交班與排班工作台

用 JavaScript 接續三方合併，依原稿行位和三方段落文字辨識仍適用的選擇。用 Chromium 與 Firefox 驗證重新整理、第三位值班者競爭寫入，以及取消預覽和手動修改。儲存透過 HTTP ETag 核對版本，並以 SQLite 版本歷史驗證寫入結果。另支援定位歷史引文與跨時區排班。[實作與重跑](https://github.com/peca12968/handoff-desk/blob/49ec7d9eaac73e671ae7511059f0738f41a95b30/README.md) · [CI](https://github.com/peca12968/handoff-desk/actions/runs/45376782663)

### 工程發布與測試工具

以 Node.js 與 Git 規劃受影響的測試與所需的上游建置，為只需建置的專案列出使用其產物的下游。用 64 張相依圖及 1,024 組變更情境核對範圍與順序，並以實際分支推送驗證固定讀取提交內的相依清單。[實作與重跑](https://github.com/peca12968/ci-impact-planner/blob/30059a3b31d99df205e75a7da623a7207a77fa8f/README.md) · [CI](https://github.com/peca12968/ci-impact-planner/actions/runs/45365392953)

### 服務觀測與執行可靠性

以 React 與 TypeScript 匯入路由級統計，將分項加總到同一 UTC 區間的整體 SLO。以 BigInt 精確核對路由超額、餘額與整體淨差額，並用 Playwright 驗證缺日、零流量、錯誤檔案及舊格式相容。另支援由輪替日誌重算可用率與雙區間消耗比較。[實作與重跑](https://github.com/peca12968/slo-window/blob/5941558af3c98fc4934d251eb37f9b711e537c3a/README.md) · [CI](https://github.com/peca12968/slo-window/actions/runs/45362462438)

### 資料回溯與品質查核

以 DuckDB 雙時間查詢比較 SKU 的價格生效區間，追查特價改期、歧義消解與同價換版，並以獨立重播核對 540 個微秒級時點在兩個截止點的價格與來源。固定舊訂單範圍的比較明細也可匯出為 Parquet。[實作與重跑](https://github.com/peca12968/price-as-of/blob/1999f957bc1e0e81b3eec1080dc80d820b9bbb8f/README.md) · [CI](https://github.com/peca12968/price-as-of/actions/runs/45358453663)

### 知識檢索與工單派送

以 SQLite FTS5 檢索中英文手冊，保留 BM25 排名及原始引用，以索引留存的 SHA-256 確認改名後的唯一來源。用端對端測試核對重複檔案、目錄範圍、舊索引與失敗掃描。另以評估關卡核對 TF-IDF 工單模型的新增誤派及人工覆核量。[實作與重跑](https://github.com/peca12968/handbook-search/blob/27b1a7f82bea956b6896ba760e8470765bce2ddd/README.md) · [CI](https://github.com/peca12968/handbook-search/actions/runs/45366913430)

### 轉乘規劃與離線地圖

以 Python 共用班表掃描，比較多個上下車站與首尾步行的跨午夜門到門行程。把旅客預留的緩衝加到每次轉乘，並納入定向通道、延誤與無階梯條件。用 120 份合成班表窮舉核對兩個查詢方向與不同緩衝，並驗證多一秒就錯過到站期限的案例。[實作與重跑](https://github.com/peca12968/transfer-clock/blob/47e420edf4391891a6e45b900009aa4b398509a1/README.md) · [CI](https://github.com/peca12968/transfer-clock/actions/runs/45373876038)

### 媒體處理與檔案交付

以 C# 剪輯 16/24 位元 PCM，再以 Python 從已驗收的 ZIP 串流複製 13,200 幀，重算 WebVTT 字幕時碼並保留其版面設定。逐位元組核對輸出、驗證 SHA-256，並測試兩個程序競爭同一交付檔名。另支援雙重校驗分片的區間還原。[實作與重跑](https://github.com/peca12968/take-splice/blob/13856b72379b21adcdd5240855ec1b92fbbcd070/README.md) · [CI](https://github.com/peca12968/take-splice/actions/runs/45364058692)

### 離線文件轉 HTML

以 Python、PDFium 和 OpenCV 實作離線文件轉換，讓桌面與命令列可指定頁碼及範圍。圖片版和結構化 HTML 共用選頁邏輯，保留來源頁碼與 OCR 診斷。以 Playwright 核對輸出的搜尋結果及列印頁數。[實作與重跑](https://github.com/peca12968/document-to-html/blob/c006ecbf49b8aaa28715ac200037eacb5a04fb7d/README.md) · [CI](https://github.com/peca12968/document-to-html/actions/runs/45355375138)
