# imagem_negativa.py
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import requests

# Carregar imagem
url = "https://images.unsplash.com/photo-1745810187217-4d9e1ccfd9d5?ixlib=rb-4.1.0&q=85&fm=jpg&crop=entropy&cs=srgb&w=640"
image = Image.open(requests.get(url, stream=True).raw).convert("RGB")

# Converter para array e inverter
np_image = np.array(image)
negative_image = 255 - np_image

# Mostrar imagem negativa
img = Image.fromarray(negative_image)
plt.imshow(img)
plt.title("Imagem Negativa")
plt.axis("off")
plt.show()
