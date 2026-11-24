# peca12968｜軟體工程專案經歷

以下為 AI 輔助開發的個人作品。數字來自可重跑的合成案例與自動化測試。

### 禾日食堂｜點餐、營運與倉庫

整合掃碼內用、自取、LINE Pay 與全支付等示範付款。以 D1 付款快照核對跨日退款。倉庫透過 FastAPI 與 SQLite 實作多商品保留和整批取消，用兩台服務併發出貨與取消，核對已出貨數量、剩餘庫存與重送取得的同一份收據。[實作與重跑](https://github.com/peca12968/hey-table/blob/123657b0469d3fa21491211b311d64c46f7f324d/README.md) · [CI](https://github.com/peca12968/hey-table/actions/runs/45331707830)

### 交班與排班工作台

用瀏覽器分頁儲存復原交班草稿，以 HTTP ETag 處理多分頁寫入。Chromium 與 Firefox 共 26 項測試，涵蓋離線重新整理、另一分頁先儲存、寫入回應中斷與三方合併。[實作與重跑](https://github.com/peca12968/handoff-desk/blob/acfd9c6be86f02c34b7d6a918eab693ea6dac2c4/README.md) · [CI](https://github.com/peca12968/handoff-desk/actions/runs/45324046977)

### 工程發布與測試工具

以 Node.js 與 Git 規劃 PR 和提交前測試，分類暫存、未暫存、新增與衝突檔案。用真實 Git 儲存庫驗證搬移會納入兩側，且加入未追蹤的 API 路由後，範例從 3 個增加至 4 個受影響專案。[實作與重跑](https://github.com/peca12968/ci-impact-planner/blob/19b76b8df29b66544f8fe73058b23e233d5663fb/README.md) · [CI](https://github.com/peca12968/ci-impact-planner/actions/runs/45328829023)

### 服務觀測與執行可靠性

從重疊輪替日誌重算可用率，將 7 筆逐行計數去重為 5 筆。以固定 UTC 截止日重跑可用率報表，驗證 14 天中只有 11 天有資料時保留觀測值並暫緩達標判定。[實作與重跑](https://github.com/peca12968/slo-window/blob/7d2788d3992850bc8d71c546dfc50aaaf8c37799/README.md) · [CI](https://github.com/peca12968/slo-window/actions/runs/45327819348)

### 資料回溯與品質查核

以 DuckDB 雙時間查詢追溯單筆訂單的補登、更正、撤回與來源版本。在 6,144 筆歷史訂單中依價格縮小到一個 Parquet 分組，逐筆核對符合價格與數量的 1,024 筆命中。[實作與重跑](https://github.com/peca12968/price-as-of/blob/d3b8618210d558c75d3ea0b402766802782915b1/README.md) · [CI](https://github.com/peca12968/price-as-of/actions/runs/45322982222)

### 知識檢索與工單派送

以 SQLite FTS5 檢索中英文手冊，核對片段移位、內容改寫與原檔移除。驗證舊索引可讀取新的原文位置，另以同一批 26 個段落比較全文與向量檢索的範圍限制。[實作與重跑](https://github.com/peca12968/handbook-search/blob/adf7e1ec039d3c08a702d136ea4918114dcf9185/README.md) · [CI](https://github.com/peca12968/handbook-search/actions/runs/45325548587)

### 轉乘規劃與離線地圖

以 Python 搜尋跨午夜轉乘，加入班次延誤、停駛與到站期限。串接 C# 的單車站點搜尋後，以端對端測試驗證因轉乘時間只差一秒而改用直達車的情境。[實作與重跑](https://github.com/peca12968/transfer-clock/blob/6480aa2bbb6c0c4cfd01098227bcced2c100faa0/README.md) · [CI](https://github.com/peca12968/transfer-clock/actions/runs/45324797895)

### 媒體處理與檔案交付

以 C# 按音訊幀剪輯 16/24 位元 PCM，加入可選的接點淡出與淡入。用 Python 逐取樣核對單／雙聲道輸出，並在 60,001 幀範例驗證六句 WebVTT 字幕仍對應原剪輯時間軸。[實作與重跑](https://github.com/peca12968/take-splice/blob/49e47ad14c99c6b1d20093915f89966bc4155b33/README.md) · [CI](https://github.com/peca12968/take-splice/actions/runs/45329885516)
