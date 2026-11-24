# peca12968｜軟體工程專案經歷

以下為 AI 輔助開發的個人作品。數字來自可重跑的合成案例與自動化測試。

### 禾日食堂｜點餐、營運與倉庫

手機掃碼內用或線上自取，搭配 LINE Pay、全支付等模擬付款。倉庫以同一份庫存快照規劃揀貨，待揀量在部分出貨及到期後由 8 件降為 3 件。另可重跑離線收貨、MQTT 補回讀值與資料庫事故復原。[模組與操作](https://github.com/peca12968/hey-table/blob/7b18fce37f1315bbe9a4e70b5d756c791a7622bc/modules/README.md) · [CI](https://github.com/peca12968/hey-table/actions/runs/45313987792)

### 交班與排班工作台

交班遇到 HTTP 412 時可預覽三方合併，保留雙方修改並用 Chromium、Firefox 核對焦點。排班 API 找出跨時區候選並匯出 iCalendar，回撥時兩個 01:00 仍各自對應到正確時刻。[模組與操作](https://github.com/peca12968/handoff-desk/blob/6e9dfaa838b7a9f85f375e707d8416865acc2b0a/modules/README.md) · [CI](https://github.com/peca12968/handoff-desk/actions/runs/45313987768)

### 工程發布與測試工具

共用契約變更會選出 4 個專案的 6 個測試檔；在合成工時下按相依關係和平行分組，預估耗時由 119 降至 88 毫秒。部署前也檢查逐人分流、API 契約、翻譯格式與瀏覽器介面。[模組與操作](https://github.com/peca12968/ci-impact-planner/blob/fa9a2408299b970876d3ea5dba357bcedf69c72b/modules/README.md) · [CI](https://github.com/peca12968/ci-impact-planner/actions/runs/45314977388)

### 服務觀測與執行可靠性

從重疊的輪替日誌重算服務可用率，將 7 筆逐行計數去重為 5 筆，畫面由 57.143% 更新為 60.000%。同庫重跑追蹤時鐘差、佇列接管與快取競爭。[模組與操作](https://github.com/peca12968/slo-window/blob/b5e6f931624d66a345063a5882b5160c4fdbbc4a/modules/README.md) · [CI](https://github.com/peca12968/slo-window/actions/runs/45313987359)

### 資料回溯與品質查核

在 6,144 筆歷史訂單中依價格與數量縮小到一個 Parquet 分組，逐筆核對 1,024 筆命中。另可驗證 PostgreSQL 漸進遷移、快照與分頁一致性。[模組與操作](https://github.com/peca12968/price-as-of/blob/2ca9294f649536a6ba00b34f9e60b39b3f2d3939/modules/README.md) · [CI](https://github.com/peca12968/price-as-of/actions/runs/45313986867)

### 知識檢索與工單派送

同一批 26 個段落上比較全文與向量檢索，限制現行版本後找回兩段人工標註答案。比對 41 筆工單的 Python 與 ONNX 推論分數和派送決策。[模組與操作](https://github.com/peca12968/handbook-search/blob/7c99b64a5e798fab19d70870acb83afb7c89e807/modules/README.md) · [CI](https://github.com/peca12968/handbook-search/actions/runs/45313987362)

### 媒體處理與檔案交付

從 48 kHz 聲道標記量測延遲，按音訊幀剪輯並用瀏覽器核對 WebVTT 字幕。同庫驗證檔案續傳、圖集還原與分塊損壞後的復原。[模組與操作](https://github.com/peca12968/take-splice/blob/0708638ac038716ce1d5dea78bcbbf4188708161/modules/README.md) · [CI](https://github.com/peca12968/take-splice/actions/runs/45313988372)
