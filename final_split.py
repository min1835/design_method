import os
from PIL import Image

# --- 設定你的路徑 ---
# 使用 r'' 確保 Windows 路徑不會因為斜線出錯
TARGET_PATH = r'D:\ADT\04_2四下\大一設計方法\39個形容詞'

def process_design_method():
    # 檢查路徑是否存在
    if not os.path.exists(TARGET_PATH):
        print(f"錯誤：找不到路徑 {TARGET_PATH}")
        return

    # 遍歷資料夾內所有檔案
    for root, dirs, files in os.walk(TARGET_PATH):
        for file in files:
            # 檢查是否為 PNG (且排除掉已經切好的檔案，避免無限循環)
            if file.lower().endswith('.png') and '_切片' not in root:
                input_path = os.path.join(root, file)
                
                # 取得檔名（不含副檔名）作為資料夾名稱
                file_stem = os.path.splitext(file)[0]
                output_folder = os.path.join(root, f"{file_stem}_切片")

                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)

                print(f"處理中：{file} -> 輸出至 {file_stem}_切片")

                try:
                    img = Image.open(input_path).convert("RGBA")
                    w, h = img.size
                    tw, th = w // 8, h // 8

                    count = 1
                    for i in range(8):      # 垂直 8 份
                        for j in range(8):  # 水平 8 份
                            left, upper = j * tw, i * th
                            right = (j + 1) * tw if j < 7 else w
                            lower = (i + 1) * th if i < 7 else h
                            
                            tile = img.crop((left, upper, right, lower))
                            # 儲存為 01.png, 02.png ... 64.png
                            tile.save(os.path.join(output_folder, f"{count:02d}.png"), "PNG")
                            count += 1
                    print(f"   ✅ 已完成 {file} 的 64 張切割")
                except Exception as e:
                    print(f"   ❌ 處理 {file} 時發生錯誤: {e}")

if __name__ == "__main__":
    process_design_method()
    print("\n--- 全數處理完畢！ ---")