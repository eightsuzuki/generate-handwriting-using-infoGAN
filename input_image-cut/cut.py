from PIL import Image
import os

# 入力画像のパス
input_image_path = "image.png"

# 出力画像のサイズ
output_width = 50
output_height = 40

# 出力ディレクトリのパス
output_dir = "output_images"

# 入力画像の読み込み
input_image = Image.open(input_image_path)

# 切り取る範囲の幅と高さ
crop_width = input_image.width // output_width
crop_height = input_image.height // output_height

# 出力ディレクトリの作成
os.makedirs(output_dir, exist_ok=True)

# 切り取り位置の初期化
x = 0
y = 0

# 出力画像の名前に使用するカウンター
counter = 0

# 画像を切り取って出力画像に貼り付ける
for i in range(output_height):
    for j in range(output_width):        

        # 切り取る範囲を指定
        box = (x, y, x + crop_width, y + crop_height)
        # 入力画像から切り取り
        cropped_image = input_image.crop(box)
        # 出力ファイル名の設定
        output_filename = f"{counter // 160 + 1}-{1 + counter % 160}.png"
        # 出力ファイルのパス
        output_path = os.path.join(output_dir, output_filename)
        # 切り取った画像を出力画像として保存
        cropped_image.save(output_path)
        # x座標を更新
        x += crop_width
        # 出力画像のカウンターをインクリメント
        counter += 1

    # x座標を初期化し、y座標を更新
    x = 0
    y += crop_height