# peca12968｜軟體工程專案經歷

以下為 AI 輔助開發的個人作品。數字來自可重跑的合成案例與自動化測試。

### 全端工程｜禾日食堂點餐與營運系統

- **顧客點餐與付款**　手機掃碼內用或線上自取，店員在另一裝置接單。支援 LINE Pay、全支付、街口支付、悠遊付、Pi 拍錢包、全盈+PAY、信用卡及現場付款。模擬金流收到請款後連線中斷，八次重送只發出一次請款，收據回到原交易。
- **廚房與退餐**　從接單台匯出實際餐單，重跑分站、取餐估算、備料與採購。345 元示範套餐可逐菜對回折扣與退餐金額。兩鍋飯可依原料收據算出 30 克報廢、10 克待追查短差及 11 元期末成本。
- **金流日結與倉庫**　從台灣日界核對跨日 LINE Pay 與全支付退款。倉庫以一致快照取得保留量，重播三批共 9 件出貨，另驗證多箱退貨的回滾與離線驗簽。
- **共同驗證**　網站、營運與倉庫功能置於一個儲存庫，中央 CI 重跑手機點餐、桌牌列印、金流替身、庫存並行與 C# 收銀演練。[模組與操作](https://github.com/peca12968/hey-table/blob/fd2b8b773e665771601a514706f0826dce502c1e/modules/README.md) · [整合驗證](https://github.com/peca12968/hey-table/blob/fd2b8b773e665771601a514706f0826dce502c1e/scripts/verify-operations.py) · [CI](https://github.com/peca12968/hey-table/actions/runs/45302026749)

### 開發工具｜Body Replay API 發布相容性檢查

讀取兩版 OpenAPI 與既有 JSON 請求，解析文件內引用、列出不相容的欄位位置及可重跑的請求內容。從 Git 歷史啟動兩版 Stockroom，將七個不同請求的離線判定與 FastAPI 回應逐一比對。加入每單最多五件的演練限制後，六件與十件的兩個範例都收到 422，依合成出現次數合計影響 15／75 筆。報表另列出舊樣本未覆蓋的新端點。[跨版本服務驗證](https://github.com/peca12968/body-replay/blob/a0fc354824900b390c7f3e3f46cb97282b84a624/demo.py) · [CI](https://github.com/peca12968/body-replay/actions/runs/45288603974)

### 後端可靠性｜Commit Gap 出貨斷線與到期重送

在 SQLite 提交前及 FastAPI 送出成功回應前終止服務，以同一箱號並行重送八次。原交易尚未提交且保留已到期時，八次均收到 409。若交易已提交，八次都能取回同一張三件出貨收據，另四件未出貨庫存如期釋回。以初版儲存程式建立無期限保留單，驗證遷移後在四種中斷與重啟時序中均保留原數量。[HTTP 重播與庫存核對](https://github.com/peca12968/commit-gap/blob/fcbfa9975c2fb05ff51714032c94f5ecb6fc9398/drill.py) · [CI](https://github.com/peca12968/commit-gap/actions/runs/45286601668)

### 測試工程｜Hold Model 庫存狀態模型測試

以獨立庫存模型核對 1,152 步操作，並擷取兩個 FastAPI 實例同時處理保留、部分取消、出貨與續期的請求。對每份紀錄搜尋符合實際起訖順序、收據內容與剩餘庫存的解釋。20 件庫存收到兩筆各 13 件的訂單時，可辨識兩筆均成功的合成反例。以三種實際競爭情境各跑五次，再以 160 份小型紀錄和枚舉全部排列的結果交叉驗證。[時序與並行驗證](https://github.com/peca12968/hold-model/blob/f69bb1ffb7592abf97713b4e58b578f112924ecd/test_history.py) · [CI](https://github.com/peca12968/hold-model/actions/runs/45279625800)

### 資料工程｜Coldroom Inbox 與 Thaw Window

串接 MQTT QoS 1、SQLite 和 Python，建立可去重的冷庫讀值紀錄，按觀測時間估算超溫持續時間。在 15 秒合成案例中，把缺測與同時刻讀值歧異分開計算。經 MQTT 補回一筆晚到資料後，模型估算的超溫時間由 8–13 秒縮至 10–13 秒。[跨服務演練](https://github.com/peca12968/coldroom-inbox/blob/db3fbdab20811500e7269595828aeb794b367e21/coverage-demo.mjs) · [CI](https://github.com/peca12968/coldroom-inbox/actions/runs/45090567932)

### 前端工程｜Focus Receipt

以 JavaScript 和 Playwright 驗證 Chromium 與 Firefox 的鍵盤操作。七步流程跨越兩層 iframe 與 Shadow DOM；即使第三步落在另一個同名「確認」按鈕，測試仍能指出實際框架與元素。[跨來源焦點測試](https://github.com/peca12968/focus-receipt/blob/3bc0875c6ed74812c4ef2b3010348123dd045936/embedded.test.mjs) · [CI](https://github.com/peca12968/focus-receipt/actions/runs/45090951927)
