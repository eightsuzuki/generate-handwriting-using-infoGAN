import os
from PIL import Image, ImageDraw

def create_collage(input_folder, output_width, output_height, resolution, rows, columns):
    # 入力画像の読み込み
    input_images = []
    for filename in sorted(os.listdir(input_folder)):
        if filename.endswith(".png"):
            image_path = os.path.join(input_folder, filename)
            input_image = Image.open(image_path)
            input_images.append(input_image)
    
    # 出力画像の作成
    output_image = Image.new("RGB", (output_width, output_height), "black")
    output_draw = ImageDraw.Draw(output_image)
    
    # 入力画像の配置（名前順に）
    current_row = 0
    current_column = 0
    current_output = 0
    
    for input_image in input_images:
        # 入力画像の読み込みとリサイズ
        resized_input = input_image.resize((output_width // columns, output_height // rows), Image.LANCZOS)
        
        # 出力画像に入力画像を貼り付け
        output_image.paste(resized_input, (current_column * (output_width // columns), current_row * (output_height // rows)))
        
        # 次の配置位置の計算
        current_column += 1
        if current_column >= columns:
            current_column = 0
            current_row += 1
        
        # 出力画像が埋まった場合、次の出力画像を作成
        if current_row >= rows:
            current_row = 0
            current_output += 1
            output_image.save(f"output_{current_output}.png")
            output_image = Image.new("RGB", (output_width, output_height), "black")
            output_draw = ImageDraw.Draw(output_image)
    
    # 余った部分を黒塗り
    output_draw.rectangle([(current_column * (output_width // columns), current_row * (output_height // rows)),
                           ((current_column + 1) * (output_width // columns), (current_row + 1) * (output_height // rows))],
                          fill="black")
    
    # 出力画像の保存
    current_output += 1
    output_image.save(f"output_{current_output}.png")

# 入力画像のフォルダー
input_folder = "./input-祝"

# 出力画像の設定
output_width = 3200
output_height = 2520
resolution = 72
rows = 40
columns = 50

# コラージュの作成
create_collage(input_folder, output_width, output_height, resolution, rows, columns)
