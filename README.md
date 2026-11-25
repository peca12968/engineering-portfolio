# peca12968｜軟體工程作品集

目前收錄 **9** 個可從原始碼重跑的工程作品。每個專案附繁中說明，下面的完整清單連到通過 CI 的實作與測試版本。

履歷專案欄可從後端、資料與前端各選一則。[繁中履歷專案摘錄](resume-projects.md)

## 依職缺挑一個作品開始

- **AI 品質評測**　固定題庫和評讀條件，逐題檢查改版是否造成退步。用合成資料重現「總通過數增加，單題卻退步」的發布閘門。[離線評測實作與重跑](examples/assistant-eval/README.md)
- **原生圖形與效能**　用 C++20 重跑 Aevrynd 的網格射線測試，觀察共用網格的 BVH 如何建立、重用及清除後重建。[原生 BVH 實測與重跑](examples/aevrynd-bvh/README.md)
- **後端工程**　以批號查各品項的期限、已出貨量、保留量及可用庫存。用兩個 FastAPI 實例競爭 SQLite 寫入鎖，核對整批取消前後的數量及時間。[Stockroom Reservations](https://github.com/peca12968/hey-table/blob/70f83c0e8c1253d7f0ee5481524d9fc04ee981ca/modules/stockroom-reservations/README.md)
- **前端工程**　用兩個瀏覽器分頁重現交班衝突，檢查合併後的鍵盤焦點和儲存結果。[交班紀錄與衝突合併](https://github.com/peca12968/handoff-desk)
- **資料與實驗工程**　從同一份曝光紀錄逐人核對版本並檢查分流比例。[功能分流與曝光稽核](https://github.com/peca12968/ci-impact-planner/tree/main/modules/rollout-lab)
- **平台與可靠性工程**　在持續寫入的庫存服務取得 SQLite 備份，用實際還原核對已提交的狀態。[庫存復原演練](https://github.com/peca12968/hey-table/tree/main/modules/sqlite-recovery-drill)

## 完整作品清單

| 作品 | 使用技術 | 可重現的情境 | 驗證 |
| --- | --- | --- | --- |
| [禾日食堂｜點餐、營運與倉庫](https://github.com/peca12968/hey-table) | React、Workers、D1、TapPay、FastAPI、SQLite、Kubernetes、MQTT、gRPC | 自取與內用共用每日供應份數。未付線上單保留 15 分鐘，到期回收份數並保護進行中的付款。店員可模擬全額退款，未交餐時一併取消、釋回份數，已交餐則保留紀錄。交班可按退款日查閱、列印及下載退款明細，也可按餐號查沒有退款時間的舊單。送單和查單逾時時會保留原餐單，可手動查回原收據。同一瀏覽器的多分頁可接續同一桌或自取餐單的送單結果。結帳時付款方式下線可改選，付款環境變更則須重新確認。尚未開始付款的已成立線上單可在原收據改用現場付款。顧客可從原查單頁下載餐單明細及示範退款收據，核對品項、金額與付款狀態。自取顧客可回報到店，接單台會優先列出已備妥且到店的餐單，交班可依到店日比較實際等候時間，也可依付款方式與金流環境核對已交餐單。從待核對餐號可查回較早的結單、補登現金並回到原日期報表。查詢金流會直接顯示本次核對結果或需重試的原因。預約報表依取餐日統計備妥準時率，並可從異常餐號開啟原預約。餐點備妥後，顧客可分享有效 30 分鐘的 QR 代取連結，並可隨時撤銷。親友可在代取頁回報到店，首次時間同步到原收據與接單台。製作延誤時，店員可在顧客原收據更新預計備妥時間。內用餐單換桌會同步到分站、收據與小票。支援店員代建與斷線找回自取單，與自助點餐共用限量。電話代建與線上自取可預約 7 天內的時段，按取餐日共用餐點限量。跨日改期先核對目的日的餐點份數，並可尋找下一個可用日期與時段。確認後同步轉移時段與日限量。顧客與店員切回改期表單或恢復連線時會重查時段，容量不足時保留原預約。備料單可按日期查看。七天總覽比較每日預約與時段容量，可依取餐日查閱未完成備料份數，並下載同一份快照的 CSV。自取預約清單按時段顯示餐號、份數和付款狀態，可列印指定時段或整日。點餐號即可開啟單張預約並按餐單狀態處理。現場收銀可保存應收、實收和找零，防止重複登記。店員可附原因更正實收，顧客收據同步更新，已保存的日結可查回原版。現金日結按登記日核對收款與盤點差額，標出交餐後登記，並可從當天更正回到原收款日查閱。盤點可保存、重試及下載歷史版本。每日摘要分列自取與內用的已交餐份數，可匯出 CSV 或列印交班摘要。備料單可列出各分站的待接單與製作中份數，按同一次擷取列印或匯出所選分站的未完成品項。分站看板可核對並整批回報 2 至 20 張餐單，任何一張已變更時整批保留原狀。斷線重整後可查回原批次結果，查無紀錄時可重送同一批。交班可按台灣回報日期、分站與餐號查批次，並在另一台店員裝置開啟同一查詢。可從批次或接單台查閱歷史餐號的品項、付款狀態和進度。顧客可跨手機分享餐點清單，接收端依目前供應預覽加入份數，保留原有備註與付款選擇。掃描桌牌後可貼入分享清單，預覽與送單沿用目前桌號。清單也可顯示或下載 QR 碼，掃描後會先核對可加入份數。店員可按原收據試算部分退餐，查看不同單點與套餐的實付單價，並保存試算紀錄供其他店員接續。誤登可附原因撤銷，恢復該筆原本的份數與實付金額。交班可按台灣異動日期核對登記、撤銷和淨額，列印或匯出同一份結果。限量品項可按新增份數補貨，手機斷線可重送原操作。補貨紀錄可按日期與品項查詢並分頁匯出。店員可比較兩天的供應上限，勾選品項後整批複製。供應歷程整合手動儲存、跨日複製、補貨及還原，可按品項查閱與匯出。誤設上限可核對既有占用後，從紀錄還原並保留新版。顧客餐單可預覽供應變動後的份數，確認再調整。線上自取與店員代建會重查所選時段，也可在供應不足時尋找下個可用日期，保留餐點、備註與付款選擇。店員可預覽並批次調整同日的多個時段，也可暫停整日的新預約及改入。店員可比較兩天的時段上限和占用，勾選差異後跨日複製。交班可按取餐日核對變更前後值、複製來源，並預覽還原。既有餐單與時段上限保留。收據可下載取餐行事曆，改期與取消沿用原事件識別碼。倉庫可按盤點場次整批入帳或沖回多品項差異，並按批號查各品項狀態與庫存，也可按截止時間查即將到期的保留單與已回收紀錄，選定多張後整批續期，也可按保留編號核對續期歷程。跨單減量會一起核對剩餘保留量，成功後可按批號重取收據。客服可按保留編號分頁查減量，可先預覽整批到期餘量與各品項缺口，再重新保留。正式送出時會再次核對庫存，任一品項缺貨時整批退回。整車交運前可試算各箱保留餘量、缺件數及重複箱號。 | [實作](https://github.com/peca12968/hey-table/blob/beeb3cb921d404e5fc50ddf321404285455091e1/README.md) · [測試](https://github.com/peca12968/hey-table/blob/beeb3cb921d404e5fc50ddf321404285455091e1/qa/ordering.spec.mjs) · [CI](https://github.com/peca12968/hey-table/actions/runs/45615433503) |
| [轉乘規劃與離線地圖](https://github.com/peca12968/transfer-clock) | Python、C#、時刻表、球面近鄰、PMTiles、HTTP Range | 跨午夜的門到門正查與反查支援定向月台步行、額外轉乘緩衝、延誤停駛與無階梯路徑。範例驗證延誤後可留 60 秒緩衝，多一秒就無法準時抵達。另支援單車還車與離線地圖。 | [實作](https://github.com/peca12968/transfer-clock/blob/47e420edf4391891a6e45b900009aa4b398509a1/README.md) · [測試](https://github.com/peca12968/transfer-clock/blob/47e420edf4391891a6e45b900009aa4b398509a1/test_area_trip.py) · [CI](https://github.com/peca12968/transfer-clock/actions/runs/45373876038) |
| [媒體處理與檔案交付](https://github.com/peca12968/take-splice) | C#、Python、WAVE、WebVTT、ZIP、校驗分片、SHA-256 | 將對時音訊與字幕打包成可重現的 ZIP，並從已驗收的交付包逐幀取出複核片段、重算字幕時碼。另支援受損封存的區間還原。 | [實作](https://github.com/peca12968/take-splice/blob/13856b72379b21adcdd5240855ec1b92fbbcd070/README.md) · [測試](https://github.com/peca12968/take-splice/blob/13856b72379b21adcdd5240855ec1b92fbbcd070/test_delivery.py) · [CI](https://github.com/peca12968/take-splice/actions/runs/45364058692) |
| [資料回溯與品質查核](https://github.com/peca12968/price-as-of) | DuckDB、SQL、Parquet、Apache Iceberg、PostgreSQL、SQLite、HyperLogLog | 比較兩個資料截止點的 SKU 價格生效區間，追查改期、撤回與同價換版。另可固定舊訂單範圍並匯出 Parquet 稽核明細。 | [實作](https://github.com/peca12968/price-as-of/blob/1999f957bc1e0e81b3eec1080dc80d820b9bbb8f/README.md) · [測試](https://github.com/peca12968/price-as-of/blob/1999f957bc1e0e81b3eec1080dc80d820b9bbb8f/test_price_schedule.py) · [CI](https://github.com/peca12968/price-as-of/actions/runs/45358453663) |
| [交班與排班工作台](https://github.com/peca12968/handoff-desk) | JavaScript、ASP.NET Core、SQLite、HTTP ETag、Playwright、iCalendar、CP-SAT | 在同一分頁接續三方合併。另一位值班者寫入新版時，只沿用仍相符的衝突選項。另支援定位歷史引文、跨時區排班與 iCalendar 匯出。 | [實作](https://github.com/peca12968/handoff-desk/blob/49ec7d9eaac73e671ae7511059f0738f41a95b30/README.md) · [測試](https://github.com/peca12968/handoff-desk/blob/49ec7d9eaac73e671ae7511059f0738f41a95b30/tests/merge.spec.js) · [CI](https://github.com/peca12968/handoff-desk/actions/runs/45376782663) |
| [知識檢索與工單派送](https://github.com/peca12968/handbook-search) | SQLite FTS5、BM25、Faiss、TF-IDF、ONNX Runtime、Python | 保留 BM25 排名及舊引用，以檔案雜湊確認改名後的唯一來源。重複檔案列出候選，可依手冊目錄縮小範圍。同庫支援工單模型上線檢查。 | [實作](https://github.com/peca12968/handbook-search/blob/27b1a7f82bea956b6896ba760e8470765bce2ddd/README.md) · [測試](https://github.com/peca12968/handbook-search/blob/27b1a7f82bea956b6896ba760e8470765bce2ddd/test_renames.py) · [CI](https://github.com/peca12968/handbook-search/actions/runs/45366913430) |
| [服務觀測與執行可靠性](https://github.com/peca12968/slo-window) | React、TypeScript、.NET、OpenTelemetry、JFR、Go、PostgreSQL | 按路由拆解錯誤預算，以 BigInt 核對超額、餘額與整體差額。另可在相同 UTC 截止日比較 2 天與 7 天的消耗，保留缺日與零流量狀態。 | [實作](https://github.com/peca12968/slo-window/blob/5941558af3c98fc4934d251eb37f9b711e537c3a/README.md) · [測試](https://github.com/peca12968/slo-window/blob/5941558af3c98fc4934d251eb37f9b711e537c3a/browser-tests/dashboard.spec.ts) · [CI](https://github.com/peca12968/slo-window/actions/runs/45362462438) |
| [工程發布與測試工具](https://github.com/peca12968/ci-impact-planner) | Git、Node.js、Python、JUnit XML、OpenAPI、Playwright、ICU、Go | 從 Git 變更選出下游測試，再按相依順序列出所需建置。只改網頁時，範例建置 4 個專案，並執行 2 個專案的測試。 | [實作](https://github.com/peca12968/ci-impact-planner/blob/30059a3b31d99df205e75a7da623a7207a77fa8f/README.md) · [測試](https://github.com/peca12968/ci-impact-planner/blob/30059a3b31d99df205e75a7da623a7207a77fa8f/test/build-plan.test.js) · [CI](https://github.com/peca12968/ci-impact-planner/actions/runs/45365392953) |
| [離線文件轉 HTML](https://github.com/peca12968/document-to-html) | Python、PDFium、Pillow、OpenCV、HTML、Playwright | 桌面與命令列可指定來源頁碼，輸出可搜尋的圖片版或結構化 HTML。保留來源頁碼與 OCR 提醒，並在真實瀏覽器驗證只列印選取頁面。 | [實作](https://github.com/peca12968/document-to-html/blob/c006ecbf49b8aaa28715ac200037eacb5a04fb7d/README.md) · [測試](https://github.com/peca12968/document-to-html/blob/c006ecbf49b8aaa28715ac200037eacb5a04fb7d/tests/test_page_selection.py) · [CI](https://github.com/peca12968/document-to-html/actions/runs/45355375138) |

## 履歷連結稽核

在本機登入 GitHub CLI 後執行 `python verify.py`。想把各項結果交給別的工具處理，可執行 `python verify.py --json`。報告列出每個專案的 CI 執行編號、CI 實際測試的提交、兩個檔案的提交及存在狀態，以及發現的問題。

稽核先確認 CI 已成功完成，並核對受測提交是否就是履歷所連的版本。如果 GitHub 截斷整棵目錄樹，程式只沿著需要核對的兩條路徑向下查找。已完成稽核但有落差時結束碼為 1。文件格式有誤或 API 無法確認時為 2。當 CI 或提交不符合時，報告以 `null` 表示尚未查核的檔案。

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
