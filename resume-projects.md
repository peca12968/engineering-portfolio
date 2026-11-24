# peca12968｜軟體工程專案經歷

以下為 AI 輔助開發的個人作品。數字來自可重跑的合成案例與自動化測試。

### 禾日食堂｜點餐、營運與倉庫

整合掃碼內用、自取、LINE Pay 與全支付等示範付款。以 D1 交易與版本檢查實作單桌及全店接單管道暫停。用手機、兩個店員分頁與併發送單驗證單桌隔離、購物車保留及原收據付款。倉庫可透過 FastAPI 與 SQLite 整批保留和取消多個商品。[實作與重跑](https://github.com/peca12968/hey-table/blob/eaa78c18fc2fa40afdb00852489db24dd20d98b7/README.md) · [CI](https://github.com/peca12968/hey-table/actions/runs/45347931706)

### 交班與排班工作台

用 ASP.NET Core 依全程出席與時段偏好排序跨時區交班，透過 UTC 分鐘計算夏令時間回撥的兩個同名時段，再用 Python 與獨立 JavaScript 解析器核對 iCalendar。交班紀錄另以 HTTP ETag 保護並行修改，並可從 SQLite 查閱歷史版本。[實作與重跑](https://github.com/peca12968/handoff-desk/blob/026e196b1030b7d48605b2155befaca702ed911c/modules/overlap-hours/README.md) · [CI](https://github.com/peca12968/handoff-desk/actions/runs/45350677521)

### 工程發布與測試工具

以 Node.js 與 Git 規劃 PR、分支推送及提交前測試。用真實的分岔提交重現強制推送，辨識被移除的舊契約並納入下游 API，讓範例從 3 個增加到 5 個受影響專案。缺少舊提交時改走全量測試，並在 Linux 與 Windows 驗證行為。[實作與重跑](https://github.com/peca12968/ci-impact-planner/blob/79926156a79968704aa19832aae9caeca61ad1ea/README.md) · [CI](https://github.com/peca12968/ci-impact-planner/actions/runs/45345456441)

### 服務觀測與執行可靠性

從重疊輪替日誌重算可用率，將 7 筆逐行計數去重為 5 筆。以 BigInt 比較同一 UTC 截止日的 2 天與 7 天錯誤預算消耗，保留缺資料及零請求狀態。用 Playwright 驗證調整目標與門檻後，短期及長期判定如何改變。[實作與重跑](https://github.com/peca12968/slo-window/blob/76c1488b10ed86f8bf9e13262af58b830c273395/README.md) · [CI](https://github.com/peca12968/slo-window/actions/runs/45352736689)

### 資料回溯與品質查核

以 DuckDB 雙時間查詢追溯價格補登、更正與撤回，並將固定訂單範圍的比較明細匯出為 Parquet。逐筆讀回核對兩時點的來源、異動分類與 DECIMAL 差額，分辨 NULL 和零，並以雙程序測試保護既有檔案。[實作與重跑](https://github.com/peca12968/price-as-of/blob/7f74ff72531426dda6b170c822ee154302ef8305/README.md) · [CI](https://github.com/peca12968/price-as-of/actions/runs/45349531612)

### 知識檢索與工單派送

以 SQLite FTS5 檢索中英文手冊，依 BM25 原排名跳過內容失效或位置重複的段落，逐筆保留可引用的現行行號及掃描結果。另為 TF-IDF 工單模型加入上線關卡，核對新增誤派、人工覆核量和精確率。[實作與重跑](https://github.com/peca12968/handbook-search/blob/24f59867bd04df3241ea943ca13228c49f6dbc77/README.md) · [CI](https://github.com/peca12968/handbook-search/actions/runs/45353888587)

### 轉乘規劃與離線地圖

以 Python 搜尋跨午夜轉乘，將已確認的無階梯班次、上下車站與定向連接套用到最早抵達及最晚出發查詢。用合成班表驗證連接關閉後改走直達、指定期限可能無可行路線，並驗證既有 C# 單車站點串接。[實作與重跑](https://github.com/peca12968/transfer-clock/blob/bb7bb50eea3db4d8f6547fd7040babdee491d964/README.md) · [CI](https://github.com/peca12968/transfer-clock/actions/runs/45351701934)

### 媒體處理與檔案交付

以 C# 剪輯 16/24 位元 PCM，將 WAV 和對時後的 WebVTT 字幕打包並驗證雜湊。以 Python 實作雙重校驗分片的區間還原，完整封存超過修復能力時仍從兩條受損條帶取回 32,768 B，並與原檔逐位元組比對。[實作與重跑](https://github.com/peca12968/take-splice/blob/e4156e31efe2aec7068d005659ff012aa2da84da/modules/shard-rescue/README.md) · [CI](https://github.com/peca12968/take-splice/actions/runs/45346666679)

### 離線文件轉 HTML

以 Python、PDFium 和 OpenCV 將同一份合成申請表轉成保留版面的 PNG 頁面與結構化 HTML。用 Playwright 驗證 320 × 427 像素影像、透明文字層可搜尋，以及 `Name` 與 `Example` 仍位於同一表格列。[實作與重跑](https://github.com/peca12968/document-to-html/blob/4ba5e1969ae21654973567625b1da906070f3442/README.md) · [CI](https://github.com/peca12968/document-to-html/actions/runs/45342510865)
