// 39 個形容詞列表
const adjectives = [
    "01_生硬的", "02_有力的", "03_快樂的", "04_吉祥的", "05_健康的", 
    "06_潔淨的", "07_溝通的", "08_誠實的", "09_男性的", "10_靜態的", 
    "11_悠閒的", "12_寫意的", "13_漂泊的", "14_緊張的", "15_縮小的", 
    "16_陰鬱的", "17_獨特的", "18_強烈的", "19_活潑的", "20_鮮明的", 
    "21_興奮的", "22_女性的", "23_浪漫的", "24_天真的", "25_實驗的", 
    "26_快速的", "27_科技的", "28_親切的", "29_中庸的", "30_樸素的", 
    "31_文化的", "32_實用的", "33_精緻的", "34_高雅的", "35_希望的", 
    "36_神聖的", "37_俗氣的", "38_華麗的", "39_撫媚的"
];

const adjListContainer = document.getElementById('adj-list');
const galleryContainer = document.getElementById('image-gallery');
const titleDisplay = document.getElementById('current-adj-title');

// 初始化：建立左側選單
adjectives.forEach((adj) => {
    const li = document.createElement('li');
    li.textContent = adj;
    li.addEventListener('click', () => updateGallery(adj, li));
    adjListContainer.appendChild(li);
});

// 切換形容詞與圖片的函數
function updateGallery(adjName, element) {
    // 1. 更新選單選中狀態
    document.querySelectorAll('.sidebar li').forEach(item => item.classList.remove('active'));
    element.classList.add('active');

    // 2. 更新標題
    titleDisplay.textContent = `目前類別：${adjName}`;

    // 3. 清空舊有圖片
    galleryContainer.innerHTML = '';

    // 4. 生成 55 張圖片 (01.png 到 55.png)
    for (let i = 1; i <= 55; i++) {
        const num = i.toString().padStart(2, '0'); // 補零，例如 01, 02...
        
        // 建立圖片容器
        const itemDiv = document.createElement('div');
        itemDiv.className = 'img-item';

        // 建立圖片標籤
        const img = document.createElement('img');
        // 路徑結構範例：images/01_生硬的/01.png
        img.src = `images/${adjName}/${num}.png`; 
        img.alt = `${adjName} - ${num}`;

        // 圖片載入失敗時的處理
        img.onerror = function() {
            this.src = 'https://via.placeholder.com/200x150?text=No+Image';
        };

        // 建立編號標籤
        const numberLabel = document.createElement('span');
        numberLabel.className = 'img-number';
        numberLabel.textContent = `${adjName}_${num}`;

        // 組合並加入網頁
        itemDiv.appendChild(img);
        itemDiv.appendChild(numberLabel);
        galleryContainer.appendChild(itemDiv);
    }

    // 點擊後自動捲動到最上方
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// 網頁開啟時預設點擊第一個形容詞
if (adjListContainer.firstChild) {
    adjListContainer.firstChild.click();
}
