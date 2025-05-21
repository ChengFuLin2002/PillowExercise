# setup_env.ps1

# 檢查 Conda 是否存在
if (-not (Get-Command conda -ErrorAction SilentlyContinue)) {
    Write-Host "❌ 請先安裝 Anaconda 或 Miniconda 後再執行"
    exit 1
}

# 建立環境
Write-Host "📦 建立 Conda 環境..."
conda env create -f environment.yml

# 啟動環境（需手動執行 activate）
Write-Host "✅ 環境建立完成，請手動執行：conda activate 1132_PY_Pillow"
#.\setup_env.ps1           # Windows 用戶