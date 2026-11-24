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
| [禾日食堂｜點餐、營運與倉庫](https://github.com/peca12968/hey-table) | React、Workers、D1、TapPay、FastAPI、SQLite、Kubernetes、MQTT、gRPC | 掃碼、自取、付款與廚房共用餐單。倉庫規劃揀貨、盤點、冷庫監測及收發貨，對入庫重送、期限與備份復原做整合演練。 | [實作](https://github.com/peca12968/hey-table/blob/7b18fce37f1315bbe9a4e70b5d756c791a7622bc/modules/README.md) · [測試](https://github.com/peca12968/hey-table/blob/7b18fce37f1315bbe9a4e70b5d756c791a7622bc/.github/workflows/system.yml) · [CI](https://github.com/peca12968/hey-table/actions/runs/45313987792) |
| [轉乘規劃與離線地圖](https://github.com/peca12968/transfer-clock) | Python、C#、時刻表、球面近鄰、PMTiles、HTTP Range | 從還車空位與站點距離找出可接續的班次，按實際候車與轉乘時間比較行程，再用指定版本的圖磚包保留離線地圖。 | [實作](https://github.com/peca12968/transfer-clock/blob/8d112a5dcbb63c656378d7268da521e59ca6fb74/dock_trip.py) · [測試](https://github.com/peca12968/transfer-clock/blob/8d112a5dcbb63c656378d7268da521e59ca6fb74/dock_checks.py) · [CI](https://github.com/peca12968/transfer-clock/actions/runs/45308242311) |
| [媒體處理與檔案交付](https://github.com/peca12968/take-splice) | C#、WAVE、WebVTT、SciPy、PNG、PDF、HTTP Range、SHA-256 | 從精確幀剪輯和字幕對時開始，接續圖集、印刷成冊、檔案續傳及分塊恢復，各工具共用 CI。 | [實作](https://github.com/peca12968/take-splice/blob/0708638ac038716ce1d5dea78bcbbf4188708161/modules/README.md) · [測試](https://github.com/peca12968/take-splice/blob/0708638ac038716ce1d5dea78bcbbf4188708161/.github/workflows/system.yml) · [CI](https://github.com/peca12968/take-splice/actions/runs/45313988372) |
| [資料回溯與品質查核](https://github.com/peca12968/price-as-of) | DuckDB、SQL、Parquet、Apache Iceberg、PostgreSQL、SQLite、HyperLogLog | 按資料當時可見版本重算價格和留存，估算檔案掃描與不同使用者數，再驗證資料庫漸進遷移及分頁一致性。 | [實作](https://github.com/peca12968/price-as-of/blob/2ca9294f649536a6ba00b34f9e60b39b3f2d3939/modules/README.md) · [測試](https://github.com/peca12968/price-as-of/blob/2ca9294f649536a6ba00b34f9e60b39b3f2d3939/.github/workflows/system.yml) · [CI](https://github.com/peca12968/price-as-of/actions/runs/45313986867) |
| [交班與排班工作台](https://github.com/peca12968/handoff-desk) | JavaScript、ASP.NET Core、SQLite、HTTP ETag、Playwright、iCalendar、CP-SAT | 處理兩個班別的同步編輯與文稿覆核，找出符合出席及值班條件的時段，再匯出跨時區行事曆。 | [實作](https://github.com/peca12968/handoff-desk/blob/6e9dfaa838b7a9f85f375e707d8416865acc2b0a/modules/README.md) · [測試](https://github.com/peca12968/handoff-desk/blob/6e9dfaa838b7a9f85f375e707d8416865acc2b0a/.github/workflows/system.yml) · [CI](https://github.com/peca12968/handoff-desk/actions/runs/45313987768) |
| [知識檢索與工單派送](https://github.com/peca12968/handbook-search) | SQLite FTS5、BM25、Faiss、TF-IDF、ONNX Runtime、Python | 查詢現行手冊並核對原文，逐筆比對 Python 與 ONNX 的工單分數、門檻和批次推論結果。 | [實作](https://github.com/peca12968/handbook-search/blob/7c99b64a5e798fab19d70870acb83afb7c89e807/modules/README.md) · [測試](https://github.com/peca12968/handbook-search/blob/7c99b64a5e798fab19d70870acb83afb7c89e807/.github/workflows/system.yml) · [CI](https://github.com/peca12968/handbook-search/actions/runs/45313987362) |
| [服務觀測與執行可靠性](https://github.com/peca12968/slo-window) | React、TypeScript、.NET、OpenTelemetry、JFR、Go、PostgreSQL | 從原始請求重現可用率與延遲，沿分散式追蹤找出重疊工作；再檢查快取競爭、分區副本、租約與排隊飽和。 | [實作](https://github.com/peca12968/slo-window/blob/b5e6f931624d66a345063a5882b5160c4fdbbc4a/modules/README.md) · [測試](https://github.com/peca12968/slo-window/blob/b5e6f931624d66a345063a5882b5160c4fdbbc4a/.github/workflows/system.yml) · [CI](https://github.com/peca12968/slo-window/actions/runs/45313987359) |
| [工程發布與測試工具](https://github.com/peca12968/ci-impact-planner) | Git、Node.js、Python、JUnit XML、OpenAPI、Playwright、ICU、Go | 從 Git 差異選出受影響的測試並分組。用同庫工具核對 API 契約、覆蓋率、套件、翻譯、介面與上線分流。 | [實作](https://github.com/peca12968/ci-impact-planner/blob/fa9a2408299b970876d3ea5dba357bcedf69c72b/modules/README.md) · [測試](https://github.com/peca12968/ci-impact-planner/blob/fa9a2408299b970876d3ea5dba357bcedf69c72b/.github/workflows/system.yml) · [CI](https://github.com/peca12968/ci-impact-planner/actions/runs/45314977388) |

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
