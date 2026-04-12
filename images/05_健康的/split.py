from PIL import Image
import os

# --- 設定區 ---
INPUT_FILE = 'test.png'    # 你的原始圖片檔名
OUTPUT_DIR = 'results'     # 輸出的資料夾名稱
# --------------

def split_image():
    if not os.path.exists(INPUT_FILE):
        print(f"錯誤：找不到檔案 {INPUT_FILE}，請確認檔名是否正確。")
        return

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    img = Image.open(INPUT_FILE).convert("RGBA")
    w, h = img.size
    tw, th = w // 8, h // 8

    count = 1
    for i in range(8):
        for j in range(8):
            left, upper = j * tw, i * th
            right = (j + 1) * tw if j < 7 else w
            lower = (i + 1) * th if i < 7 else h
            
            tile = img.crop((left, upper, right, lower))
            tile.save(os.path.join(OUTPUT_DIR, f"{count:02d}.png"), "PNG")
            count += 1
    print(f"完成！請查看 {OUTPUT_DIR} 資料夾。")

if __name__ == "__main__":
    split_image()