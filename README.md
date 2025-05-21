# 🖼️ PillowExercise - Image Processing with Python

本專案使用 [Pillow](https://python-pillow.org/) 套件，完成基本圖像處理功能，包括格式轉換、影像翻轉、旋轉、縮放與多種濾鏡效果。適合作為 Python 初學者學習圖像處理與 Conda 環境管理的入門實作。

---

## 📁 專案結構

```
PillowExercise/
├── environment.yml          # Conda 虛擬環境設定檔
├── setup_env.sh             # macOS / Linux 一鍵環境建立腳本
├── setup_env.ps1            # Windows PowerShell 一鍵環境建立腳本
├── imgs/                    # 原始圖片資料夾（請放 .jpg/.png）
├── results/                 # 處理後圖片的輸出位置
└── src/
    ├── test.py              # 圖片格式轉換工具（jpg <-> png）
    └── imtool.py            # 多功能圖片處理工具
```

---

## 🛠️ 安裝與啟用環境

### 使用 Conda 手動建立環境：
```bash
conda env create -f environment.yml
conda activate 1132_PY_Pillow
```

### 一鍵執行（建議）：

#### macOS / Linux：
```bash
bash setup_env.sh
```

#### Windows PowerShell：
```powershell
.\setup_env.ps1
```

---

## 🚀 使用方式

請將圖片（如 testimg.jpg）放入 `imgs/` 資料夾中，然後在 `src/` 資料夾執行指令：

### 圖片格式轉換
```bash
python test.py -jpg2png     # 將 imgs/*.jpg → results/*.png
python test.py -png2jpg     # 將 imgs/*.png → results/*.jpg
```

### 圖片處理功能
```bash
python imtool.py testimg.jpg -resize 0.5
python imtool.py testimg.jpg -VFlip
python imtool.py testimg.jpg -HFlip
python imtool.py testimg.jpg -R90
python imtool.py testimg.jpg -R180
python imtool.py testimg.jpg -R270
python imtool.py testimg.jpg -thumbnail 200 150
python imtool.py testimg.jpg -BLUR
python imtool.py testimg.jpg -CONTOUR
python imtool.py testimg.jpg -DETAIL
python imtool.py testimg.jpg -EDGE_ENHANCE
python imtool.py testimg.jpg -EDGE_ENHANCE_MORE
python imtool.py testimg.jpg -EMBOSS
python imtool.py testimg.jpg -SHARPEN
python imtool.py testimg.jpg -SMOOTH
python imtool.py testimg.jpg -SMOOTH_MORE
python imtool.py testimg.jpg -FIND_EDGES
```

---

## 🧑‍🎓 作者資訊
本專案為圖像處理課程作業，目標為學習：
- Pillow 基本操作
- Conda 虛擬環境建立
- 指令列工具撰寫
- 可重現的專案結構

---
## 📜 使用說明
歡迎下載與學習本專案，請勿直接修改本 GitHub 上的原始倉庫。如需修改請 fork 後使用。