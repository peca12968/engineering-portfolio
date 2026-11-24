# peca12968｜軟體工程專案經歷

以下為 AI 輔助開發的個人作品。數字來自可重跑的合成案例與自動化測試。

### 全端工程｜禾日食堂點餐、營運與倉庫系統

- **點餐與金流**　手機掃碼內用或線上自取，店員在另一裝置接單。LINE Pay、全支付等付款方式在私人預覽使用模擬交易。請款回覆中斷後，八次重送只發出一次請款。
- **廚房與營運**　從餐單接續備料、採購、分批驗收與退餐試算。演練取消一包生米後只補買一包，驗收入庫與取消同時處理最後一包時只有一方成功。
- **倉庫與可靠性**　從一致的庫存快照規劃揀貨。部分出貨和兩次到期後，待揀量從 8 件降至 3 件再清空。用並行模型、提交前後斷線、Kubernetes 更換 Pod、WAL 和分塊還原重播故障。庫存也接收離線收貨收據與 gRPC 貨單。
- **共同驗證**　從 API 與資料庫到手機和倉庫維運皆可在同一份程式碼重跑。[模組與操作](https://github.com/peca12968/hey-table/blob/2314f6351886829197e82701a12efe6388e7227d/modules/README.md) · [整合驗證](https://github.com/peca12968/hey-table/blob/2314f6351886829197e82701a12efe6388e7227d/.github/workflows/system.yml) · [CI](https://github.com/peca12968/hey-table/actions/runs/45311446338)

### 資料工程｜冷庫監測與超溫估算

串接 MQTT QoS 1、SQLite 和 Python。程序在提交後、回覆前異常終止，重送仍只記一筆觀測。15 秒合成案例中，經 MQTT 補回晚到讀值後，超溫估計由 8–13 秒縮至 10–13 秒。[收集與超溫演練](https://github.com/peca12968/coldroom-inbox/blob/57488d3f06749a20b2987f58b814bea462bf5955/coverage-demo.mjs) · [CI](https://github.com/peca12968/coldroom-inbox/actions/runs/45308242212)

### 前端工程｜交班紀錄與衝突合併

兩個班別在不同分頁編輯同一份紀錄。遇到 HTTP 412 時用三方合併逐段處理衝突；以 Chromium、Firefox 和實際 SQLite 歷史驗證鍵盤焦點、重送與雙方文字。[鍵盤與雙分頁整合測試](https://github.com/peca12968/handoff-desk/blob/5675046d4ce5266663e78ddd8386e3d4ea7cbcd2/tests/desk.spec.js) · [CI](https://github.com/peca12968/handoff-desk/actions/runs/45308246715)
