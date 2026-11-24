[CmdletBinding()]
param(
    [Parameter(Mandatory)][string]$EngineRoot,
    [string]$OutputFile
)
$ErrorActionPreference = 'Stop'
$engine = (Resolve-Path -LiteralPath $EngineRoot).Path
$revision = git -C $engine rev-parse HEAD
if ($LASTEXITCODE -ne 0 -or $revision -notmatch '^[a-f0-9]{40}$') {
    throw '無法取得 Aevrynd 提交'
}
$dirty = git -C $engine status --porcelain -- engine/native/include engine/native/src engine/native/tests
if ($LASTEXITCODE -ne 0 -or $dirty) { throw '請使用乾淨的引擎原始碼工作樹' }

$vswhere = Join-Path ${env:ProgramFiles(x86)} 'Microsoft Visual Studio/Installer/vswhere.exe'
$install = & $vswhere -latest -products '*' -requires Microsoft.VisualStudio.Component.VC.Tools.x86.x64 -property installationPath
if (!$install) { throw '找不到含 x64 C++ 工具的 Visual Studio' }
$vc = Join-Path $install 'VC/Auxiliary/Build/vcvars64.bat'
$native = Join-Path $engine 'engine/native'
$output = if ($OutputFile) { [IO.Path]::GetFullPath($OutputFile) }
$scratch = (Resolve-Path -LiteralPath ([IO.Path]::GetTempPath())).Path
$build = New-Item -ItemType Directory -Path (Join-Path $scratch ('aevrynd-bvh-' + [guid]::NewGuid()))

Push-Location -LiteralPath $build.FullName
try {
    $flags = '/nologo /std:c++20 /EHsc /O2 /permissive- /utf-8 /DNOMINMAX /DWIN32_LEAN_AND_MEAN /I"{0}\include"' -f $native
    $library = '"{0}\src\VisibilityBvh3D.cpp" "{0}\src\Memory.cpp" psapi.lib' -f $native
    function Invoke-Case([string]$Source, [string]$Name) {
        $command = 'call "{0}" >nul && cl {1} "{2}" {3} /Fe:{4}.exe' -f $vc, $flags, $Source, $library, $Name
        cmd /d /c $command | Out-Host
        if ($LASTEXITCODE -ne 0) { throw "編譯失敗 $Name" }
        $stdout = & ".\$Name.exe"
        if ($LASTEXITCODE -ne 0) { throw "測試失敗 $Name" }
        return $stdout
    }
    $benchmark = Invoke-Case (Join-Path $native 'tests/MeshRaycastBvhBenchmark.cpp') 'Benchmark'
    $smoke = Invoke-Case (Join-Path $native 'tests/MeshRaycastBvhSmoke.cpp') 'Smoke'
    Write-Host $smoke
    $trace = Invoke-Case (Join-Path $PSScriptRoot 'BvhProbe.cpp') 'Probe' | ConvertFrom-Json
    if ($benchmark -notmatch '^triangles=(?<triangles>\d+) queries=(?<queries>\d+) averageCandidates=(?<candidates>\d+) averageNodes=(?<nodes>\d+) elapsedUs=\d+$') {
        throw '基準測試輸出格式已變更'
    }
    $report = [ordered]@{
        engine_sha = $revision
        msvc = $trace.msvc
        benchmark = [ordered]@{
            triangles = [int]$Matches.triangles
            queries = [int]$Matches.queries
            average_candidates = [int]$Matches.candidates
            average_nodes = [int]$Matches.nodes
        }
        probe = [ordered]@{ triangles = $trace.triangles; stages = $trace.stages }
    }
    $json = $report | ConvertTo-Json -Depth 8
    if ($output) {
        $staged = $output + '.' + [guid]::NewGuid() + '.tmp'
        try {
            [IO.File]::WriteAllText($staged, $json + [Environment]::NewLine)
            [IO.File]::Move($staged, $output, $true)
        } finally {
            if (Test-Path -LiteralPath $staged) { Remove-Item -LiteralPath $staged }
        }
    }
    $json
} finally {
    Pop-Location
    $built = (Resolve-Path -LiteralPath $build.FullName).Path
    if ([IO.Path]::GetDirectoryName($built) -eq [IO.Path]::TrimEndingDirectorySeparator($scratch)) {
        Remove-Item -LiteralPath $built -Recurse -Force -ErrorAction Continue
    }
}
