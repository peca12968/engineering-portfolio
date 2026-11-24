# peca12968｜軟體工程專案經歷

以下為 AI 輔助開發的個人作品。數字來自可重跑的合成案例與自動化測試。

### 禾日食堂｜點餐、營運與倉庫

整合掃碼內用、自取、LINE Pay 與全支付等示範付款。以店員授權和欄位白名單匯出 D1 付款快照，驗證同一檔案可核對兩種日結報表及跨日退款。倉庫同步實物盤點，將已保留的商品計入應盤實體庫存。[實作與重跑](https://github.com/peca12968/hey-table/blob/c875b18026cc891314c062bd6e55b725f6fde06c/README.md) · [CI](https://github.com/peca12968/hey-table/actions/runs/45326691515)

### 交班與排班工作台

用瀏覽器分頁儲存復原交班草稿，以 HTTP ETag 處理多分頁寫入。Chromium 與 Firefox 共 26 項測試，涵蓋離線重新整理、另一分頁先儲存、寫入回應中斷與三方合併。[實作與重跑](https://github.com/peca12968/handoff-desk/blob/acfd9c6be86f02c34b7d6a918eab693ea6dac2c4/README.md) · [CI](https://github.com/peca12968/handoff-desk/actions/runs/45324046977)

### 工程發布與測試工具

共用契約變更會選出 4 個專案的 6 個測試檔；在合成工時下按相依關係和平行分組，預估耗時由 119 降至 88 毫秒。部署前也檢查逐人分流、API 契約、翻譯格式與瀏覽器介面。[模組與操作](https://github.com/peca12968/ci-impact-planner/blob/fa9a2408299b970876d3ea5dba357bcedf69c72b/modules/README.md) · [CI](https://github.com/peca12968/ci-impact-planner/actions/runs/45314977388)

### 服務觀測與執行可靠性

從重疊的輪替日誌重算服務可用率，將 7 筆逐行計數去重為 5 筆，畫面由 57.143% 更新為 60.000%。同庫重跑追蹤時鐘差、佇列接管與快取競爭。[模組與操作](https://github.com/peca12968/slo-window/blob/b5e6f931624d66a345063a5882b5160c4fdbbc4a/modules/README.md) · [CI](https://github.com/peca12968/slo-window/actions/runs/45313987359)

### 資料回溯與品質查核

以 DuckDB 雙時間查詢追溯單筆訂單的補登、更正、撤回與來源版本。在 6,144 筆歷史訂單中依價格縮小到一個 Parquet 分組，逐筆核對符合價格與數量的 1,024 筆命中。[實作與重跑](https://github.com/peca12968/price-as-of/blob/d3b8618210d558c75d3ea0b402766802782915b1/README.md) · [CI](https://github.com/peca12968/price-as-of/actions/runs/45322982222)

### 知識檢索與工單派送

以 SQLite FTS5 檢索中英文手冊，核對片段移位、內容改寫與原檔移除。驗證舊索引可讀取新的原文位置，另以同一批 26 個段落比較全文與向量檢索的範圍限制。[實作與重跑](https://github.com/peca12968/handbook-search/blob/adf7e1ec039d3c08a702d136ea4918114dcf9185/README.md) · [CI](https://github.com/peca12968/handbook-search/actions/runs/45325548587)

### 轉乘規劃與離線地圖

以 Python 搜尋跨午夜轉乘，加入班次延誤、停駛與到站期限。串接 C# 的單車站點搜尋後，以端對端測試驗證因轉乘時間只差一秒而改用直達車的情境。[實作與重跑](https://github.com/peca12968/transfer-clock/blob/6480aa2bbb6c0c4cfd01098227bcced2c100faa0/README.md) · [CI](https://github.com/peca12968/transfer-clock/actions/runs/45324797895)

### 媒體處理與檔案交付

從 48 kHz 聲道標記量測延遲，按音訊幀剪輯並用瀏覽器核對 WebVTT 字幕。同庫驗證檔案續傳、圖集還原與分塊損壞後的復原。[模組與操作](https://github.com/peca12968/take-splice/blob/0708638ac038716ce1d5dea78bcbbf4188708161/modules/README.md) · [CI](https://github.com/peca12968/take-splice/actions/runs/45313988372)
