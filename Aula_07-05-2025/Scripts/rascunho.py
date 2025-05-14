# Importação das bibliotecas necessárias
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Exibir gráficos inline
# %matplotlib inline

print('teste')

# Carregar imagem de exemplo
from PIL import Image
import requests

url = "https://images.unsplash.com/photo-1745810187217-4d9e1ccfd9d5?ixlib=rb-4.1.0&q=85&fm=jpg&crop=entropy&cs=srgb&w=640"
image = Image.open(requests.get(url, stream=True).raw)
image = image.convert("RGB")  # Garante 3 canais

# Separar os canais
r, g, b = image.split()

# Criar arrays com zero
zeros = Image.new("L", image.size)

# Criar imagens RGB para cada canal com as outras cores zeradas
red_image = Image.merge("RGB", (r, zeros, zeros))
green_image = Image.merge("RGB", (zeros, g, zeros))
blue_image = Image.merge("RGB", (zeros, zeros, b))

# Exibir os canais com suas cores
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
for ax, channel_image, color in zip(axs, [red_image, green_image, blue_image], ['Vermelho', 'Verde', 'Azul']):
    ax.imshow(channel_image)
    ax.set_title(f'Canal {color}')
    ax.axis('off')
plt.tight_layout()
plt.show()


# Mostrar imagem
# plt.imshow(image)
# plt.title("Imagem Original")
# plt.axis('off')
# plt.show()

# Converter para escala de cinza
# gray_image = image.convert("L")

# Mostrar imagem em tons de cinza
# plt.imshow(gray_image, cmap='gray')
# plt.title("Imagem em Escala de Cinza")
# plt.axis('off')
# plt.show()

# Converter para numpy e mostrar valor de alguns pixels
# np_image = np.array(image)
# print("Formato da imagem:", np_image.shape)
# print("Valor do pixel (0, 0):", np_image[0, 0])
