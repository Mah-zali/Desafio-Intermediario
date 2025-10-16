#ARRUMANDO GIF
from PIL import Image, ImageEnhance
import imageio

# Arquivos de entrada e saída
input_gif = "kuromi.gif"                 # GIF animado original
background_img = "kuromi_fundo.png"      # Imagem com fundo completo
output_normal = "kuromi_final.gif"       # Saída normal
output_hd = "kuromi_final_hd.gif"        # Saída em alta resolução

# Carregar imagem de fundo
background_base = Image.open(background_img).convert("RGBA")
bg_w, bg_h = background_base.size

# Carregar GIF original
original = Image.open(input_gif)
frames = []
durations = []

# Definir proporção automática
target_height_ratio = 0.55  # Kuromi ocupa ~55% da altura do fundo
original.seek(0)
kuromi_frame = original.convert("RGBA")
scale = (bg_h * target_height_ratio) / kuromi_frame.height
new_size = (int(kuromi_frame.width * scale), int(kuromi_frame.height * scale))
offset_x = (bg_w - new_size[0]) // 2
offset_y = (bg_h - new_size[1]) // 2 + int(bg_h * 0.05)

# Criar todos os frames com fundo fixo
for frame_index in range(original.n_frames):
    original.seek(frame_index)
    frame = original.convert("RGBA")
    durations.append(original.info.get("duration", 100))
    frame_resized = frame.resize(new_size, Image.Resampling.LANCZOS)

    composed = background_base.copy()
    composed.paste(frame_resized, (offset_x, offset_y), frame_resized)

    composed = ImageEnhance.Sharpness(composed).enhance(1.4)
    composed = ImageEnhance.Contrast(composed).enhance(1.1)

    frames.append(composed)

# Salvar versão normal
frames[0].save(
    output_normal,
    save_all=True,
    append_images=frames[1:],
    duration=durations,
    loop=0,
    disposal=2
)

# Salvar versão HD (2x resolução)
frames_hd = [f.resize((f.width * 2, f.height * 2), Image.Resampling.LANCZOS) for f in frames]
frames_hd[0].save(
    output_hd,
    save_all=True,
    append_images=frames_hd[1:],
    duration=durations,
    loop=0,
    disposal=2
)

print("✅ GIFs salvos com sucesso:")
print("→ Normal:", output_normal)
print("→ HD:", output_hd)