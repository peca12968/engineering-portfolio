# peca12968｜軟體工程專案經歷

以下為 AI 輔助開發的個人作品。數字來自可重跑的合成案例與自動化測試。

### 禾日食堂｜點餐、營運與倉庫

整合掃碼內用、自取、LINE Pay 與全支付等示範付款。以 D1 交易實作分流暫停新訂單，用手機、兩個店員分頁與併發送單驗證舊購物車、原收據與付款流程。餐廳可匯出對帳快照，倉庫可透過 FastAPI 與 SQLite 整批保留和取消多個商品。[實作與重跑](https://github.com/peca12968/hey-table/blob/018a6dd8f98669e17bc6f57cca11f1d28345f297/README.md) · [CI](https://github.com/peca12968/hey-table/actions/runs/45335744187)

### 交班與排班工作台

用瀏覽器分頁儲存復原交班草稿，並加入歷史對照與舊稿載入。在 Chromium 和 Firefox 共跑 30 個案例，驗證快速切換不會顯示過時回覆，並以 HTTP ETag 檢出並行寫入後逐字核對 SQLite 的四版紀錄。[實作與重跑](https://github.com/peca12968/handoff-desk/blob/e8c317ae66767846130d95c3eb9b70bb37f4cdb0/README.md) · [CI](https://github.com/peca12968/handoff-desk/actions/runs/45340793118)

### 工程發布與測試工具

以 Node.js 與 Git 規劃 PR、分支推送及提交前測試。用真實的分岔提交重現強制推送，辨識被移除的舊契約並納入下游 API，讓範例從 3 個增加到 5 個受影響專案。缺少舊提交時改走全量測試，並在 Linux 與 Windows 驗證行為。[實作與重跑](https://github.com/peca12968/ci-impact-planner/blob/79926156a79968704aa19832aae9caeca61ad1ea/README.md) · [CI](https://github.com/peca12968/ci-impact-planner/actions/runs/45345456441)

### 服務觀測與執行可靠性

從重疊輪替日誌重算可用率，將 7 筆逐行計數去重為 5 筆。以 BigInt 比對每日錯誤預算，依超額量排序連續區段。用 Playwright 驗證提高目標、匯入缺少一天的 CSV，以及調整 UTC 截止日後的區段分界。[實作與重跑](https://github.com/peca12968/slo-window/blob/4a35633e1beeb173e49e9ca7301b7327bb390150/README.md) · [CI](https://github.com/peca12968/slo-window/actions/runs/45338519189)

### 資料回溯與品質查核

以 DuckDB 雙時間查詢追溯補登、更正與撤回。固定訂單範圍比較兩個截止點，辨識單價不變的來源更新，並以精確整數保留互相抵銷的增減額。另在 6,144 筆訂單的 Parquet 中縮小到一個分組，核對全部 1,024 筆命中。[實作與重跑](https://github.com/peca12968/price-as-of/blob/0a1e6259aac617bc5e62e73a86ad8d81680858c3/README.md) · [CI](https://github.com/peca12968/price-as-of/actions/runs/45337526361)

### 知識檢索與工單派送

以 SQLite FTS5 檢索中英文手冊並核對原文位置。為 TF-IDF 工單模型加入上線關卡，在 11 件獨立評估工單逐筆核對新增誤派、各隊列人工覆核與精確率，並以 SHA-256 保存模型和評估資料的版本依據。[實作與重跑](https://github.com/peca12968/handbook-search/blob/d46fc7f88ab7b9fa0f81d195c9682a7b6680c890/README.md) · [CI](https://github.com/peca12968/handbook-search/actions/runs/45334063984)

### 轉乘規劃與離線地圖

以 Python 搜尋跨午夜轉乘，將定向的月台步行規則套用到最早抵達及最晚出發查詢。用 100 份合成班表對照獨立窮舉，並串接 C# 單車站點搜尋，重現轉乘只差一秒就需提早出發的情境。[實作與重跑](https://github.com/peca12968/transfer-clock/blob/da4f4e23bd793149188c5a9501db352e865515ec/README.md) · [CI](https://github.com/peca12968/transfer-clock/actions/runs/45339905886)

### 媒體處理與檔案交付

以 C# 剪輯 16/24 位元 PCM，將 WAV 和對時後的 WebVTT 字幕打包並驗證雜湊。以 Python 實作雙重校驗分片的區間還原，完整封存超過修復能力時仍從兩條受損條帶取回 32,768 B，並與原檔逐位元組比對。[實作與重跑](https://github.com/peca12968/take-splice/blob/e4156e31efe2aec7068d005659ff012aa2da84da/modules/shard-rescue/README.md) · [CI](https://github.com/peca12968/take-splice/actions/runs/45346666679)

### 離線文件轉 HTML

以 Python、PDFium 和 OpenCV 將同一份合成申請表轉成保留版面的 PNG 頁面與結構化 HTML。用 Playwright 驗證 320 × 427 像素影像、透明文字層可搜尋，以及 `Name` 與 `Example` 仍位於同一表格列。[實作與重跑](https://github.com/peca12968/document-to-html/blob/4ba5e1969ae21654973567625b1da906070f3442/README.md) · [CI](https://github.com/peca12968/document-to-html/actions/runs/45342510865)
