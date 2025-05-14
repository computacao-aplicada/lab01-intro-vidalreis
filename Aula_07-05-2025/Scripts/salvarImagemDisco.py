# salvar_imagem_modificada.py
import numpy as np
from PIL import Image
import requests
import os

# Carregar imagem
url = "https://images.unsplash.com/photo-1745810187217-4d9e1ccfd9d5?ixlib=rb-4.1.0&q=85&fm=jpg&crop=entropy&cs=srgb&w=640"
image = Image.open(requests.get(url, stream=True).raw).convert("RGB")

# Converter para array e aplicar efeito simples (tirar azul)
np_image = np.array(image)
np_image[:, :, 2] = 0  # Zera o azul

# Caminho para pasta de Downloads
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
save_path = os.path.join(downloads_folder, "imagem_modificada.jpg")

# Salvar imagem
Image.fromarray(np_image).save(save_path)
print(f"Imagem modificada salva em: {save_path}")
