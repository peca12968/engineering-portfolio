# peca12968｜軟體工程專案經歷

以下為 AI 輔助開發的個人作品。數字來自可重跑的合成案例與自動化測試。

### 測試工程｜Hold Model 庫存狀態模型測試

以逐件追蹤去向的獨立模型核對兩個 FastAPI 實例，在 24 組可重播的操作中驗證續期、重送、部分出貨、取消與到期。1,152 步都符合模型預期。另注入到期漏還庫存的故障，將 8 步縮為 3 步，重現可用量應為 17 件卻只有 12 件的差異；刪除任一步，該差異就消失。[縮減與重播測試](https://github.com/peca12968/hold-model/blob/bb4bd5a5d80429a46e64a1fe03bb46a8055124dc/test_check.py) · [CI](https://github.com/peca12968/hold-model/actions/runs/45278528956)

### 演算法工程｜Remit Match 無批號匯款追查

在金流合成報表中，兩筆各 60 元的匯款都只有同一個候選批號，兩筆卻不能同時認列。依撥款餘額與日期建立二分圖，從所有最多筆數配法中列出每筆可能批號與落單情形。以 643 組案例的獨立窮舉結果逐筆比對，另驗證 5,000 筆連鎖日期限制，並從上游核帳程式重新產生測試輸入。[配對與跨專案測試](https://github.com/peca12968/remit-match/blob/ec46694f1774e9a4e625d929f4e9c6db95ce14a6/test_remit.py) · [CI](https://github.com/peca12968/remit-match/actions/runs/45275813561)

### 影像處理與測試工程｜Table Scan Check 桌牌掃碼驗收

用 Playwright 從點餐頁輸出兩頁 A4 桌牌，以 PDFium 和獨立 QR 解碼器核對八桌的位置與目的地。保留原桌號文字、交換 A01 和 A02 的 QR 圖後，驗收能指出兩桌各自掃到哪一桌。少印第二頁時，報表會列出 A05 到 A08。另以 OpenCV 模擬縮印、斜拍與模糊，24 次必要影像檢查皆符合預期。[送印檔回歸測試](https://github.com/peca12968/table-scan-check/blob/cbd3a32b2290b9f07f126f7f2c9d9a097c8ccd27/test_sheet.py) · [CI](https://github.com/peca12968/table-scan-check/actions/runs/45273405947)

### 交易系統｜Receipt Returns 部分退餐試算

以 Python 和 SQLite 從成交收據還原每份餐點的套餐折扣，支援退餐預覽、分批登記與重送。用禾日食堂本機 Worker 建立全支付與 LINE Pay 示範收據，驗證單點及搭不同套餐的同一道菜可有三種實付價格。以 44 種分批順序核對 345 元餐單的每次金額，再以兩個獨立連線測試舊報價與最後一份的競爭條件。[分批與並行測試](https://github.com/peca12968/receipt-returns/blob/d6dc1490e568ced896b62f7adfb56b3ba1714cb6/test_returns.py) · [CI](https://github.com/peca12968/receipt-returns/actions/runs/45266726797)

### 後端工程｜Stockroom Reservations

以 FastAPI 和 SQLite 實作庫存保留與續期。保留 8 件、分箱寄出 3 件、部分取消 2 件後，續期只涵蓋剩下 3 件。兩個服務實例同時對同一舊期限送出 12 個不同續期單號，只有一筆成功。模擬寫入收據失敗時驗證期限回滾，並驗證重啟、到期後重送皆可取回原收據。[交易、升級與並行測試](https://github.com/peca12968/stockroom-reservations/blob/34165f1adceb2baceaa53997b7a79a86656e959b/tests/test_api.py) · [CI](https://github.com/peca12968/stockroom-reservations/actions/runs/45277380492)

### 可靠性工程｜Pass Rail 廚房分站出單

以 Python、HTTP 與 SQLite 串接點餐服務和兩個廚房工作站。分站存好單據後強制終止配送程序，重啟可核對原單據且收件匣只有一張。另以八個配送者競領同一張單，並驗證停發與遲到送單同時抵達的結果。[中斷與競爭測試](https://github.com/peca12968/pass-rail/blob/e52bdb1468117899cf0b5c91d871208ae5ef6264/test_rail.py) · [CI](https://github.com/peca12968/pass-rail/actions/runs/45244734428)

### 資料工程｜Coldroom Inbox 與 Thaw Window

串接 MQTT QoS 1、SQLite 和 Python，建立可去重的冷庫讀值紀錄，按觀測時間估算超溫持續時間。在 15 秒合成案例中，把缺測與同時刻讀值歧異分開計算。經 MQTT 補回一筆晚到資料後，模型估算的超溫時間由 8–13 秒縮至 10–13 秒。[跨服務演練](https://github.com/peca12968/coldroom-inbox/blob/db3fbdab20811500e7269595828aeb794b367e21/coverage-demo.mjs) · [CI](https://github.com/peca12968/coldroom-inbox/actions/runs/45090567932)

### 前端工程｜Focus Receipt

以 JavaScript 和 Playwright 驗證 Chromium 與 Firefox 的鍵盤操作。七步流程跨越兩層 iframe 與 Shadow DOM；即使第三步落在另一個同名「確認」按鈕，測試仍能指出實際框架與元素。[跨來源焦點測試](https://github.com/peca12968/focus-receipt/blob/3bc0875c6ed74812c4ef2b3010348123dd045936/embedded.test.mjs) · [CI](https://github.com/peca12968/focus-receipt/actions/runs/45090951927)

### 全端工程｜禾日食堂線上與掃碼點餐

- 用 React、Cloudflare Workers 與 D1 建立線上自取、桌邊掃碼及廚房接單流程。以獨立解碼器讀取 QR 桌號，再用兩個瀏覽器身分完成交餐。即使寫入訂單後遺失回應，手機重新開啟仍可找回原取餐號碼。
- 串接 TapPay 的 LINE Pay、全支付、街口支付、悠遊付、Pi 拍錢包、全盈+PAY 與信用卡。依錢包規格取得付款憑證、傳送成交品項並查證交易。以三種錢包分別完成 200 元示範單的取消、重試與收據復原。另測試同時發起付款只建立一筆待付交易、金額相同但錢包不符時維持待確認。[手機金流測試](https://github.com/peca12968/hey-table/blob/e0596f05039ff0520bfb1207c20fee05c1e7894b/qa/payments.spec.mjs) · [CI](https://github.com/peca12968/hey-table/actions/runs/45269228719)
- 以廚房工時估算出餐，支援店員比較與匯入校準值。購物車依已完成訂單推薦加點，並將成交套餐與逐菜折扣寫入 D1。用全支付示範單核對折扣後付款與分帳均為 415 元，也可依取餐號碼匯出舊單試算部分退餐。

串接廚房匯出與 SQLite 庫存帳，將入庫、製作與訂單領料記為可查驗的收據。八個獨立連線競領最後一份煎茶，庫存只扣一次。煮飯缺水時整筆回滾，補水後可沿用原單號入帳。另串接採購單分批驗收，依供應商與 SKU 追蹤欠貨；八個連線同收最後一包，僅一筆入庫。[採購驗收交易與測試](https://github.com/peca12968/prep-sheet/blob/00e56da3bf47a32819652a69bdcc9862fa6f56e7/test_receiving.py) · [CI](https://github.com/peca12968/prep-sheet/actions/runs/45256730270)

### 計價引擎｜Combo Counter 套餐最佳配對

以有容量的二分圖配對處理重疊套餐與限用次數，依單品價格將折扣分攤到整元。禾日食堂的合成 A03 收據原價 NT$490，單取最大折扣可省 NT$45，重配兩組可省 NT$75。以 512 組小型購物車的窮舉解核對最低價、同價時的最少套數與逐菜金額，並用本機 Worker 和 D1 收據驗證試算流程。[計價與獨立驗證](https://github.com/peca12968/combo-counter/blob/25fbf7ae239c8ca8c465588b0fe8ab1756a04ff9/quote.test.mjs) · [CI](https://github.com/peca12968/combo-counter/actions/runs/45262807712)

### 推薦系統｜Menu Pairs 餐點搭配

以 Node.js 和 SQLite 讀取兩份先後留存的點餐快照，按共購單數與整體人氣計算加點排序。用同一批 7 張合成餐單比較首選，兩種方法都命中 2 張、只有搭配模型命中 3 張、只有熱銷榜命中 1 張。另以 256 組購買歷史逐筆重算排名，並測試停售、未見品項、訓練後才完成的舊單及買法改變時的結果。[模型與留後測試](https://github.com/peca12968/menu-pairs/blob/388bf24e0b90538191fcf05994106bfb90a991bd/pairs.test.mjs) · [CI](https://github.com/peca12968/menu-pairs/actions/runs/45261102196)

### 最佳化｜Pantry Freight 廚房採購

將備料短缺量、整包規格、供應商庫存與免運門檻建成動態規劃模型，找出滿足儲存限制的最低含運總價。用 320 組小型詢價單枚舉所有包數組合，核對可行性、總價與同價選擇。另串接 Prep Sheet 的 SQLite 庫存帳，驗收後重算，同一批原料的追加採購金額為零。[窮舉與限制測試](https://github.com/peca12968/pantry-freight/blob/c8f00428928e410d3cb098fa0cfe8a8d36f67452/test_purchase.py) · [CI](https://github.com/peca12968/pantry-freight/actions/runs/45255645162)

### 排程演算法｜Pickup Window

以 JavaScript 排定廚房各站的製作批次，根據空位、已完成數量與鍋中剩餘時間估算何時可交整單。用獨立的逐秒模擬器窮舉 729 種工時組合，逐單核對最快、最慢完成時間，再用禾日食堂 Worker 和 D1 的店員匯出檔重跑同一支指令。[區間與窮舉驗證](https://github.com/peca12968/pickup-window/blob/1e86c05effd8ebd102ea92629df68dda6ab1bb6d/estimate.test.mjs) · [CI](https://github.com/peca12968/pickup-window/actions/runs/45250645551)

以 Python 和 SQLite 記錄實作份數和每批耗時，按完成時間切分校準與驗證資料。八個程序同時開工只會有一個取得同一工作位。將 20 批合成煎茶工時匯入排程模型，保留次日四批獨立核對命中數與超時秒數。[批次工時與留後驗證](https://github.com/peca12968/batch-clock/blob/b7802ce073aca960aa5c5b81de40a1c81b9e83ba/test_batch_clock.py) · [CI](https://github.com/peca12968/batch-clock/actions/runs/45252370915)

### 現金交班核帳｜Drawer Count

以 Python 逐筆重建 C# 收銀程式的現金收據，把補零、投庫和實點依序併入交班帳。午間實點與帳面都是 NT$330，仍辨識出一張百元與兩枚五十元的面額差異；交班的新增短差則定位到一枚十元。用獨立的硬幣清單核對 200 個合成班次、1,200 次盤點。[交班與上游整合測試](https://github.com/peca12968/drawer-count/blob/74275174d91db9534aa002bf95a2d806835288d3/test_drawer.py) · [CI](https://github.com/peca12968/drawer-count/actions/runs/45258250132)

### 金流對帳｜Payout Ledger

用 Python 與 SQLite 核對餐單、電子支付退款、撥款和銀行入帳。兩筆同日各 70 元的匯款在演算法中都可能屬於 C 或 D 批次，取得個別水單編號後才由店員補登。連同另一帳戶的扣款，合成案例的無批號流水由 8 筆減為 5 筆。匯出前逐筆核對日期及金額，並驗證重複匯入同一決定、併行輸出同名檔案時均能保留完整結果。[跨專案覆核測試](https://github.com/peca12968/payout-ledger/blob/b6b28c18089627cd273119ee8f3559bdf16d72a2/test_bank_review.py) · [CI](https://github.com/peca12968/payout-ledger/actions/runs/45276670251)

### 演算法工程｜現場找零與合菜分帳

以 C# 實作有限庫存的找零演算法，依序最佳化動用的預留枚數與交付總枚數。以 Python 獨立枚舉 64 個班次、512 筆交易，逐筆比對找零結果及錢櫃餘額。[獨立枚舉驗證](https://github.com/peca12968/till-change/blob/210ec2967f8c1394849fd68ae183c98d075ba9c8/test_change.py) · [CI](https://github.com/peca12968/till-change/actions/runs/45239129370)

以 Python 精確分數與最小費用流實作多人分帳。串接套餐報價後，逐項核對優惠使用份數、逐菜折扣及折後金額，再分配尾差。A03 桌原價 385 元、折 40 元，兩人實付 222 與 123 元。以 240 張一般餐單及 256 組合成套餐報價的窮舉解核對最佳分配，再逐格比對 JavaScript BigInt 模組。[折後分帳與跨語言驗證](https://github.com/peca12968/table-shares/blob/91ff344a99838d91906d90328ac31f2533da1407/test_combo.py) · [CI](https://github.com/peca12968/table-shares/actions/runs/45263973016)
