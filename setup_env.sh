#!/bin/bash
# setup_env.sh

# 檢查 conda 是否可用
if ! command -v conda &> /dev/null
then
    echo "❌ 請先安裝 Anaconda 或 Miniconda 後再執行"
    exit 1
fi

echo "📦 建立 Conda 環境..."
conda env create -f environment.yml

echo "✅ 環境建立完成，請執行：conda activate 1132_PY_Pillow"
#bash setup_env.sh         # macOS/Linux 用戶