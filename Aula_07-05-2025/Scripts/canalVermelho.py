# exibir_canal_vermelho.py
from PIL import Image
import matplotlib.pyplot as plt
import requests

# Carregar imagem
url = "https://images.unsplash.com/photo-1745810187217-4d9e1ccfd9d5?ixlib=rb-4.1.0&q=85&fm=jpg&crop=entropy&cs=srgb&w=640"
image = Image.open(requests.get(url, stream=True).raw).convert("RGB")
r, _, _ = image.split()

# Mostrar canal vermelho
red_image = Image.merge("RGB", (r, Image.new("L", image.size), Image.new("L", image.size)))

plt.imshow(red_image)
plt.title("Canal Vermelho")
plt.axis("off")
plt.show()
