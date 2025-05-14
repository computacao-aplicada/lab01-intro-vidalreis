# modificar_canal_vermelho.py
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import requests

# Carregar imagem
url = "https://images.unsplash.com/photo-1745810187217-4d9e1ccfd9d5?ixlib=rb-4.1.0&q=85&fm=jpg&crop=entropy&cs=srgb&w=640"
image = Image.open(requests.get(url, stream=True).raw).convert("RGB")

# Converter para array
np_image = np.array(image)

# Substituir canal vermelho por valores aleatórios
np_image[:, :, 0] = np.random.randint(0, 256, size=(np_image.shape[0], np_image.shape[1]))

# Mostrar imagem
modified = Image.fromarray(np_image)
plt.imshow(modified)
plt.title("Canal Vermelho Aleatório")
plt.axis("off")
plt.show()