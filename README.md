# peca12968｜軟體工程作品集

目前收錄 **9** 個可從原始碼重跑的工程作品。每個專案附繁中說明，下面的完整清單連到通過 CI 的實作與測試版本。

履歷專案欄可從後端、資料與前端各選一則。[繁中履歷專案摘錄](resume-projects.md)

## 依職缺挑一個作品開始

- **後端工程**　以批號查各品項的期限、已出貨量、保留量及可用庫存。用兩個 FastAPI 實例競爭 SQLite 寫入鎖，核對整批取消前後的數量及時間。[Stockroom Reservations](https://github.com/peca12968/hey-table/blob/70f83c0e8c1253d7f0ee5481524d9fc04ee981ca/modules/stockroom-reservations/README.md)
- **前端工程**　用兩個瀏覽器分頁重現交班衝突，檢查合併後的鍵盤焦點和儲存結果。[交班紀錄與衝突合併](https://github.com/peca12968/handoff-desk)
- **資料與實驗工程**　從同一份曝光紀錄逐人核對版本並檢查分流比例。[功能分流與曝光稽核](https://github.com/peca12968/ci-impact-planner/tree/main/modules/rollout-lab)
- **平台與可靠性工程**　在持續寫入的庫存服務取得 SQLite 備份，用實際還原核對已提交的狀態。[庫存復原演練](https://github.com/peca12968/hey-table/tree/main/modules/sqlite-recovery-drill)

## 完整作品清單

| 作品 | 使用技術 | 可重現的情境 | 驗證 |
| --- | --- | --- | --- |
| [禾日食堂｜點餐、營運與倉庫](https://github.com/peca12968/hey-table) | React、Workers、D1、TapPay、FastAPI、SQLite、Kubernetes、MQTT、gRPC | 店員可依管道或桌位暫停新單。倉庫以批號查同一時間點的各品項狀態與庫存。驗證原期限一到，套件餘量釋回，續期的包材仍保留。 | [實作](https://github.com/peca12968/hey-table/blob/70f83c0e8c1253d7f0ee5481524d9fc04ee981ca/modules/stockroom-reservations/README.md) · [測試](https://github.com/peca12968/hey-table/blob/70f83c0e8c1253d7f0ee5481524d9fc04ee981ca/modules/stockroom-reservations/tests/test_reservation_batches.py) · [CI](https://github.com/peca12968/hey-table/actions/runs/45356865776) |
| [轉乘規劃與離線地圖](https://github.com/peca12968/transfer-clock) | Python、C#、時刻表、球面近鄰、PMTiles、HTTP Range | 在跨午夜的正反查套用已確認的無階梯班次、站點與定向連接，處理電梯連接關閉、延誤及停駛。另支援單車還車與離線地圖。 | [實作](https://github.com/peca12968/transfer-clock/blob/bb7bb50eea3db4d8f6547fd7040babdee491d964/README.md) · [測試](https://github.com/peca12968/transfer-clock/blob/bb7bb50eea3db4d8f6547fd7040babdee491d964/test_connections.py) · [CI](https://github.com/peca12968/transfer-clock/actions/runs/45351701934) |
| [媒體處理與檔案交付](https://github.com/peca12968/take-splice) | C#、Python、WAVE、WebVTT、ZIP、校驗分片、SHA-256 | 將對時音訊與字幕打包成可重現的 ZIP。以雙重校驗還原指定區間，在完整封存無法讀回的範例中取回 32,768 B 並逐位元組比對。 | [實作](https://github.com/peca12968/take-splice/blob/e4156e31efe2aec7068d005659ff012aa2da84da/modules/shard-rescue/README.md) · [測試](https://github.com/peca12968/take-splice/blob/e4156e31efe2aec7068d005659ff012aa2da84da/modules/shard-rescue/test_rescue.py) · [CI](https://github.com/peca12968/take-splice/actions/runs/45346666679) |
| [資料回溯與品質查核](https://github.com/peca12968/price-as-of) | DuckDB、SQL、Parquet、Apache Iceberg、PostgreSQL、SQLite、HyperLogLog | 比較兩個資料截止點的 SKU 價格生效區間，追查改期、撤回與同價換版。另可固定舊訂單範圍並匯出 Parquet 稽核明細。 | [實作](https://github.com/peca12968/price-as-of/blob/1999f957bc1e0e81b3eec1080dc80d820b9bbb8f/README.md) · [測試](https://github.com/peca12968/price-as-of/blob/1999f957bc1e0e81b3eec1080dc80d820b9bbb8f/test_price_schedule.py) · [CI](https://github.com/peca12968/price-as-of/actions/runs/45358453663) |
| [交班與排班工作台](https://github.com/peca12968/handoff-desk) | JavaScript、ASP.NET Core、SQLite、HTTP ETag、Playwright、iCalendar、CP-SAT | 先確認跨時區成員可全程出席，再依人數及當地時段偏好排名。範例將偏好外時間從 60 人分鐘降至 0，並讀回 iCalendar 驗證兩地時間。 | [實作](https://github.com/peca12968/handoff-desk/blob/026e196b1030b7d48605b2155befaca702ed911c/modules/overlap-hours/README.md) · [測試](https://github.com/peca12968/handoff-desk/blob/026e196b1030b7d48605b2155befaca702ed911c/modules/overlap-hours/test_api.py) · [CI](https://github.com/peca12968/handoff-desk/actions/runs/45350677521) |
| [知識檢索與工單派送](https://github.com/peca12968/handbook-search) | SQLite FTS5、BM25、Faiss、TF-IDF、ONNX Runtime、Python | 依 BM25 排名補齊已驗證引用，保留現行原文行號和略過原因。達到掃描上限時回報可核對的筆數。同庫支援工單模型上線檢查。 | [實作](https://github.com/peca12968/handbook-search/blob/24f59867bd04df3241ea943ca13228c49f6dbc77/README.md) · [測試](https://github.com/peca12968/handbook-search/blob/24f59867bd04df3241ea943ca13228c49f6dbc77/test_handbook.py) · [CI](https://github.com/peca12968/handbook-search/actions/runs/45353888587) |
| [服務觀測與執行可靠性](https://github.com/peca12968/slo-window) | React、TypeScript、.NET、OpenTelemetry、JFR、Go、PostgreSQL | 以同一 UTC 截止日比較 2 天與 7 天的錯誤預算消耗，用 BigInt 精確比對門檻。區分短期升高、長期升高、雙區間超額與缺失觀測。 | [實作](https://github.com/peca12968/slo-window/blob/76c1488b10ed86f8bf9e13262af58b830c273395/README.md) · [測試](https://github.com/peca12968/slo-window/blob/76c1488b10ed86f8bf9e13262af58b830c273395/browser-tests/dashboard.spec.ts) · [CI](https://github.com/peca12968/slo-window/actions/runs/45352736689) |
| [工程發布與測試工具](https://github.com/peca12968/ci-impact-planner) | Git、Node.js、Python、JUnit XML、OpenAPI、Playwright、ICU、Go | 從 PR、分支推送和本機工作目錄規劃測試。強制推送移除舊契約時，從前後快照追到受影響的下游。缺少舊提交時執行全量測試。 | [實作](https://github.com/peca12968/ci-impact-planner/blob/79926156a79968704aa19832aae9caeca61ad1ea/README.md) · [測試](https://github.com/peca12968/ci-impact-planner/blob/79926156a79968704aa19832aae9caeca61ad1ea/test/git-input.test.js) · [CI](https://github.com/peca12968/ci-impact-planner/actions/runs/45345456441) |
| [離線文件轉 HTML](https://github.com/peca12968/document-to-html) | Python、PDFium、Pillow、OpenCV、HTML、Playwright | 桌面與命令列可指定來源頁碼，輸出可搜尋的圖片版或結構化 HTML。保留來源頁碼與 OCR 提醒，並在真實瀏覽器驗證只列印選取頁面。 | [實作](https://github.com/peca12968/document-to-html/blob/c006ecbf49b8aaa28715ac200037eacb5a04fb7d/README.md) · [測試](https://github.com/peca12968/document-to-html/blob/c006ecbf49b8aaa28715ac200037eacb5a04fb7d/tests/test_page_selection.py) · [CI](https://github.com/peca12968/document-to-html/actions/runs/45355375138) |

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
