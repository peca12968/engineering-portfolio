# peca12968｜軟體工程作品集

目前收錄 **8** 個可從原始碼重跑的工程作品。每個專案附繁中說明，下面的完整清單連到通過 CI 的實作與測試版本。

履歷專案欄可從後端、資料與前端各選一則。[繁中履歷專案摘錄](resume-projects.md)

## 依職缺挑一個作品開始

- **後端工程**　用 FastAPI 與 SQLite 在同一時點查兩張訂單和商品庫存。讓另一個實例同時出貨 5 件，核對提交前後的快照、箱單與可用量。[Stockroom Reservations](https://github.com/peca12968/hey-table/tree/main/modules/stockroom-reservations)
- **前端工程**　用兩個瀏覽器分頁重現交班衝突，檢查合併後的鍵盤焦點和儲存結果。[交班紀錄與衝突合併](https://github.com/peca12968/handoff-desk)
- **資料與實驗工程**　從同一份曝光紀錄逐人核對版本並檢查分流比例。[功能分流與曝光稽核](https://github.com/peca12968/ci-impact-planner/tree/main/modules/rollout-lab)
- **平台與可靠性工程**　在持續寫入的庫存服務取得 SQLite 備份，用實際還原核對已提交的狀態。[庫存復原演練](https://github.com/peca12968/hey-table/tree/main/modules/sqlite-recovery-drill)

## 完整作品清單

| 作品 | 使用技術 | 可重現的情境 | 驗證 |
| --- | --- | --- | --- |
| [禾日食堂｜點餐、營運與倉庫](https://github.com/peca12968/hey-table) | React、Workers、D1、TapPay、FastAPI、SQLite、Kubernetes、MQTT、gRPC | 掃碼內用與自取可獨立暫停，顧客保留購物車，舊單仍能付款和製作。以 D1 交易和版本檢查處理新單及雙店員競爭。同庫支援退款對帳與多商品庫存保留。 | [實作](https://github.com/peca12968/hey-table/blob/018a6dd8f98669e17bc6f57cca11f1d28345f297/README.md) · [測試](https://github.com/peca12968/hey-table/blob/018a6dd8f98669e17bc6f57cca11f1d28345f297/qa/intake.spec.mjs) · [CI](https://github.com/peca12968/hey-table/actions/runs/45335744187) |
| [轉乘規劃與離線地圖](https://github.com/peca12968/transfer-clock) | Python、C#、時刻表、球面近鄰、PMTiles、HTTP Range | 將延誤與停駛套用到跨午夜的轉乘及單車接駁。依還車空位與最晚到站時間規劃行程，並用版本固定的圖磚包保留離線地圖。 | [實作](https://github.com/peca12968/transfer-clock/blob/6480aa2bbb6c0c4cfd01098227bcced2c100faa0/README.md) · [測試](https://github.com/peca12968/transfer-clock/blob/6480aa2bbb6c0c4cfd01098227bcced2c100faa0/test_router.py) · [CI](https://github.com/peca12968/transfer-clock/actions/runs/45324797895) |
| [媒體處理與檔案交付](https://github.com/peca12968/take-splice) | C#、Python、WAVE、WebVTT、ZIP、SHA-256、HTTP Range | 將 16/24 位元 WAV 與逐幀對時的字幕打包成可重現的 ZIP，驗收時核對檔案雜湊與時間軸。以端對端測試驗證字幕遭替換、匯出失敗及同名並行發布。 | [實作](https://github.com/peca12968/take-splice/blob/af4c2630eb3f1d07f49d866aa926dcd8865c2ece/README.md) · [測試](https://github.com/peca12968/take-splice/blob/af4c2630eb3f1d07f49d866aa926dcd8865c2ece/test_delivery.py) · [CI](https://github.com/peca12968/take-splice/actions/runs/45332993223) |
| [資料回溯與品質查核](https://github.com/peca12968/price-as-of) | DuckDB、SQL、Parquet、Apache Iceberg、PostgreSQL、SQLite、HyperLogLog | 固定訂單範圍比較兩次價格查核，逐筆區分單價、狀態或來源異動，並以整數加總各 SKU 的增額、減額與淨額。 | [實作](https://github.com/peca12968/price-as-of/blob/0a1e6259aac617bc5e62e73a86ad8d81680858c3/README.md) · [測試](https://github.com/peca12968/price-as-of/blob/0a1e6259aac617bc5e62e73a86ad8d81680858c3/test_cutoff_comparison.py) · [CI](https://github.com/peca12968/price-as-of/actions/runs/45337526361) |
| [交班與排班工作台](https://github.com/peca12968/handoff-desk) | JavaScript、ASP.NET Core、SQLite、HTTP ETag、Playwright、iCalendar、CP-SAT | 斷線重整後復原各分頁的草稿，以 HTTP ETag 核對伺服器版本並整合兩班變更。同庫可產出跨時區排班行事曆。 | [實作](https://github.com/peca12968/handoff-desk/blob/acfd9c6be86f02c34b7d6a918eab693ea6dac2c4/README.md) · [測試](https://github.com/peca12968/handoff-desk/blob/acfd9c6be86f02c34b7d6a918eab693ea6dac2c4/tests/desk.spec.js) · [CI](https://github.com/peca12968/handoff-desk/actions/runs/45324046977) |
| [知識檢索與工單派送](https://github.com/peca12968/handbook-search) | SQLite FTS5、BM25、Faiss、TF-IDF、ONNX Runtime、Python | 核對索引引用是否移位或失效。同庫以未參與訓練的工單逐筆比較現行與候選模型，以新增誤派和各隊列的人工覆核量做上線檢查。 | [實作](https://github.com/peca12968/handbook-search/blob/d46fc7f88ab7b9fa0f81d195c9682a7b6680c890/README.md) · [測試](https://github.com/peca12968/handbook-search/blob/d46fc7f88ab7b9fa0f81d195c9682a7b6680c890/modules/ticket-triage/test_release_gate.py) · [CI](https://github.com/peca12968/handbook-search/actions/runs/45334063984) |
| [服務觀測與執行可靠性](https://github.com/peca12968/slo-window) | React、TypeScript、.NET、OpenTelemetry、JFR、Go、PostgreSQL | 由輪替日誌重算可用率，用 BigInt 找出連續超額的 UTC 區段，依超額量排序並標記缺資料或零請求造成的分界。 | [實作](https://github.com/peca12968/slo-window/blob/4a35633e1beeb173e49e9ca7301b7327bb390150/README.md) · [測試](https://github.com/peca12968/slo-window/blob/4a35633e1beeb173e49e9ca7301b7327bb390150/browser-tests/dashboard.spec.ts) · [CI](https://github.com/peca12968/slo-window/actions/runs/45338519189) |
| [工程發布與測試工具](https://github.com/peca12968/ci-impact-planner) | Git、Node.js、Python、JUnit XML、OpenAPI、Playwright、ICU、Go | 從 PR 或本機工作目錄追蹤測試影響。保留搬移的舊、新路徑，納入未追蹤檔案，再依專案相依分配平行測試。 | [實作](https://github.com/peca12968/ci-impact-planner/blob/19b76b8df29b66544f8fe73058b23e233d5663fb/README.md) · [測試](https://github.com/peca12968/ci-impact-planner/blob/19b76b8df29b66544f8fe73058b23e233d5663fb/test/git-input.test.js) · [CI](https://github.com/peca12968/ci-impact-planner/actions/runs/45328829023) |

## 面試展示路線

**地圖與離線讀取**　在 Return Radius 執行換日線範例，說明兩個鄰近站點為何分別落在第 65535 欄與第 0 欄，以及四張圖磚的預算如何決定縮放層級。接著執行 Tile Satchel 的換版測試，展示區段讀取途中回傳新版內容時，既有離線地圖仍可使用。

**模型部署**　用 Ticket Triage 匯出已訓練模型，比對 41 筆工單在 Python 與 ONNX Runtime 的各類分數和派送決策。再用 Batch Parity 重現分類標籤相同、分數卻從 4.0 降至 0.8 的案例，說明部署測試為什麼需要逐類核對分數。

**AI 檢索工程**　先用 Vector Sieve 比較不同版本的 recall@5，再用 Handbook Search 檢查實際回傳的兩段原文。前者衡量近似索引能否找回精確近鄰；後者能回答另一個面試問題：找到的段落是否真是適用版本的答案？

**可靠性與延遲**　用 Access Log Rollup 從兩組輪替日誌產生延遲直方圖，再用 Bucket Verdict 判定 80% 的請求能否在 120 毫秒內完成。檢查兩組原始資料，一組達標、一組失敗，卻產生完全相同的彙總。這個例子可用來解釋何時需要把分桶邊界設在服務承諾的時間點。

**實驗與發布品質**　先用 Exposure Audit 說明如何從整體對半的資料找出平台分流異常。再用 Rollout Lab 示範另一種故障：即使人數符合計畫，個別帳號仍可能收到錯誤版本。兩份合成案例可分別展示統計檢定與確定性重算。

**後端與平台工程**　從 Stockroom 的限量商品下單開始，解釋資料庫交易如何維持可用庫存。接著打開 Relay Job Queue 的並行測試，分別展示「送件重試建立幾筆工作」與「同一筆工作可嘗試幾次」。前者由請求鍵去重，後者由有期限的租約管理。這兩個作品使用各自的資料庫，可獨立操作。

**全端與資料工具**　用 Access Log Rollup 對同一批輪替日誌產生兩份報表，依序在 SLO Window 匯入。第一份逐行計數，畫面顯示 7 個請求與 57.143% 可用率。第二份按請求 ID 去重，顯示 5 個請求與 60.000%。展開逐日數值可看到 5 月 3 日仍缺資料。兩份報表都由固定版本的 CLI 產生並由瀏覽器測試核對。

**資料一致性與開發工具**　執行 Payout Ledger 的兩次對帳，在第二次加入 `--explain`。沿著入帳 ID 檢查哪三筆新增、哪一筆從來源消失，再核對它們如何合計為 7 美元的變動。CI Impact Planner 則可用一份相依圖展示如何避免漏測下游套件，適合討論測試策略與建置流程。

**跨服務互通**　在 Overlap Hours 查詢台北與紐約的 45 分鐘交班，再用 Slot Calendar 選取台北 21:30 的候選。打開匯出的行事曆，核對紐約 08:30 與三位出席者，再執行整合測試，觀察兩個看似相同的紐約 01:00 如何因夏令時間回撥而對應不同時刻。

**搜尋與品質評估**　在 Handbook Search 用同一份索引查「背景執行者當機由誰接手」，分別執行預設查詢與詞彙表查詢。打開第一筆結果的原文行號核對答案，再執行評估，比較每題找回多少相關段落，以及第一個相關段落排第幾。

各專案附繁中執行說明、合成資料或可重現的測試情境。這些作品使用 AI 輔助開發。上列數字來自示範與自動化測試。
