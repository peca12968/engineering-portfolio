# Aevrynd 原生網格 BVH

這份實測以 Aevrynd 指定提交的 C++20 查詢路徑為準。上游基準在 128×128 格子的合成地形上，讓八個場景物件共用同一份網格，並以 512 條向下射線驗證命中。MSVC 19.44 x64 的樣本中，每份網格有 32,768 個三角形，每條射線平均檢查 16 個候選三角形、23 個 BVH 節點。基準驗證整批只建立一次索引。

## 觀察共用索引

`BvhProbe.cpp` 直接呼叫引擎的 `Scene3D::Raycast`，用另一份 8,192 個三角形的網格量測三個階段。

| 階段 | 命中物件 | 建立索引 | 候選三角形 | BVH 節點 |
| --- | ---: | ---: | ---: | ---: |
| 第一次查詢 | 0 | 1 次 | 64 | 27 |
| 變換後的共用網格 | 1 | 0 次 | 32 | 25 |
| 清除後再查詢 | 0 | 1 次 | 64 | 27 |

上表是 [sample.json](sample.json) 的本機擷取結果。不同編譯器或標準函式庫可能影響同值三角形的分割，所以 CI 核對固定輸入、命中、候選量門檻與索引狀態。耗時受機器與當下負載影響。

## 用 Windows 重跑

需要 Windows、PowerShell 7、Git，以及含 C++ x64 工具與 Windows SDK 的 Visual Studio 或 Build Tools。將 Aevrynd 的乾淨工作樹切到 `sample.json` 所列的提交，再從作品集根目錄執行。

```powershell
./examples/aevrynd-bvh/capture.ps1 -EngineRoot ../Aevrynd
```

加入 `-OutputFile ./examples/aevrynd-bvh/sample.json` 可更新樣本。腳本會編譯並執行原生 Smoke、Benchmark 與補充探針，輸出索引建立次數及快取前後的位元組數。

[上游基準程式](https://github.com/peca12968/Aevrynd/blob/6833d0a2a6d74322c150f4293dd5f681aaf5dee0/engine/native/tests/MeshRaycastBvhBenchmark.cpp) · [上游 Smoke](https://github.com/peca12968/Aevrynd/blob/6833d0a2a6d74322c150f4293dd5f681aaf5dee0/engine/native/tests/MeshRaycastBvhSmoke.cpp) · [專用 Windows 驗證](../../.github/workflows/aevrynd-bvh.yml)
