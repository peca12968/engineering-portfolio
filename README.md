# peca12968｜軟體工程作品集

七個可以從原始碼跑到測試的工程作品。後端與平台工程可從庫存交易和背景工作佇列開始，全端工程可從跨時區日誌一路看到瀏覽器裡的服務指標。搜尋工程則可執行手冊檢索的品質評估，檢視每題的排名與原文。每一列的實作與測試都連到右側 CI 實際驗證的提交版本。

| 作品 | 使用技術 | 可重現的情境 | 驗證 |
| --- | --- | --- | --- |
| [Handbook Search](https://github.com/peca12968/handbook-search) | Python、SQLite FTS5、BM25 | 13 題合成問題中有 12 題的第一名命中相關段落。可查閱中英文結果的原文行號，以及剩下一題跨語言詞彙未命中的原因。 | [實作](https://github.com/peca12968/handbook-search/blob/5af290407411abe1f2282bcae8f8149a27815c4c/handbook.py) · [測試](https://github.com/peca12968/handbook-search/blob/5af290407411abe1f2282bcae8f8149a27815c4c/test_handbook.py) · [CI](https://github.com/peca12968/handbook-search/actions/runs/45004005399) |
| [Relay Job Queue](https://github.com/peca12968/relay-job-queue) | Node.js、PostgreSQL | 12 個送件端同時重送，資料庫仍只建立一筆工作。工作者中斷後，接手者取得新租約，遲到的舊結果會被拒絕。 | [實作](https://github.com/peca12968/relay-job-queue/blob/349baa8e6e9067323423d9ea875666db8ef45534/queue.js) · [測試](https://github.com/peca12968/relay-job-queue/blob/349baa8e6e9067323423d9ea875666db8ef45534/test/queue.test.js) · [CI](https://github.com/peca12968/relay-job-queue/actions/runs/45003581826) |
| [Stockroom Reservations](https://github.com/peca12968/stockroom-reservations) | Python、FastAPI、SQLite | 庫存 20 件，24 筆請求各搶 2 件，驗證只有 10 筆成功。也驗證取消與到期回收同時發生時只歸還一次。 | [實作](https://github.com/peca12968/stockroom-reservations/blob/1bec99199cf0ee8ed9d9b3d34ddbaad10dc01930/stockroom/store.py) · [測試](https://github.com/peca12968/stockroom-reservations/blob/1bec99199cf0ee8ed9d9b3d34ddbaad10dc01930/tests/test_api.py) · [CI](https://github.com/peca12968/stockroom-reservations/actions/runs/45002616288) |
| [Payout Ledger](https://github.com/peca12968/payout-ledger) | Python、SQL | 比較兩份入帳快照，區分新增、持續待查、已結清與從來源消失的差異，保留每種幣別的金額。 | [實作](https://github.com/peca12968/payout-ledger/blob/6c1e51cb1e526000513c5bf985269501f9b0cd92/ledger.py) · [測試](https://github.com/peca12968/payout-ledger/blob/6c1e51cb1e526000513c5bf985269501f9b0cd92/test_ledger.py) · [CI](https://github.com/peca12968/payout-ledger/actions/runs/45003050000) |
| [Access Log Rollup](https://github.com/peca12968/access-log-rollup) | C#、.NET | 逐行讀取跨時區 HTTP 日誌，按 UTC 日期輸出請求數與 5xx 數。錯誤輸入會回報行號並避免輸出半份報表。 | [實作](https://github.com/peca12968/access-log-rollup/blob/e5ad3b15e8d2cf7ee425b2d68e4c7ea0c3681b25/src/Program.cs) · [測試](https://github.com/peca12968/access-log-rollup/blob/e5ad3b15e8d2cf7ee425b2d68e4c7ea0c3681b25/test_cli.py) · [CI](https://github.com/peca12968/access-log-rollup/actions/runs/45002778547) |
| [SLO Window](https://github.com/peca12968/slo-window) | React、TypeScript、Playwright | 將前一個專案產生的 CSV 匯入實際瀏覽器。測試驗證 5 筆請求、2 筆失敗顯示 60% 可用率，無資料的日期也會標示。 | [實作](https://github.com/peca12968/slo-window/blob/db128f94a546b99ab0b1077d5ccbfa5ecb991c0f/src/metrics.ts) · [測試](https://github.com/peca12968/slo-window/blob/db128f94a546b99ab0b1077d5ccbfa5ecb991c0f/browser-tests/dashboard.spec.ts) · [CI](https://github.com/peca12968/slo-window/actions/runs/45002864087) |
| [CI Impact Planner](https://github.com/peca12968/ci-impact-planner) | Node.js、Git、圖演算法 | 依變更檔案與反向相依圖選出重測範圍。五個套件的範例中，只改前端需測兩個；修改共用契約需測四個。 | [實作](https://github.com/peca12968/ci-impact-planner/blob/e1246ec1071614ced10960b2b39c01017f611c6e/planner.js) · [測試](https://github.com/peca12968/ci-impact-planner/blob/e1246ec1071614ced10960b2b39c01017f611c6e/test/planner.test.js) · [CI](https://github.com/peca12968/ci-impact-planner/actions/runs/45000286899) |

## 面試展示路線

**後端與平台工程**　從 Stockroom 的限量商品下單開始，解釋資料庫交易如何維持可用庫存。接著打開 Relay Job Queue 的並行測試，分別展示「送件重試建立幾筆工作」與「同一筆工作可嘗試幾次」。前者由請求鍵去重，後者由有期限的租約管理。這兩個作品使用各自的資料庫，可獨立操作。

**全端與資料工具**　在 Access Log Rollup 依 README 建置 CLI，用範例日誌產生 CSV，接著在 SLO Window 選取這份檔案並展開逐日數值。可現場指出台北時間 5 月 2 日上午 7:30 的請求如何被歸入 UTC 5 月 1 日，以及為什麼無流量和缺資料需要不同顯示。兩個專案的端對端流程已納入 SLO Window 的瀏覽器測試。

**資料一致性與開發工具**　執行 Payout Ledger 的兩次對帳示範，找出已補入帳的訂單與從來源消失的紀錄。CI Impact Planner 則可用一份相依圖展示如何避免漏測下游套件，適合討論測試策略與建置流程。

各專案附繁中執行說明、合成資料或可重現的測試情境。這些作品使用 AI 輔助開發。上列數字來自示範與自動化測試。
