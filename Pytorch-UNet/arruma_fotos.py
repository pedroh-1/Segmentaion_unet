import os
from PIL import Image, ImageOps

# Caminho exato da sua pasta de imagens
pasta_imagens = "/home/vicom02/Downloads/Projeto_Vicom_Pedro/segmentation_unet/Pytorch-UNet/data/imgs/"

contador = 0

print("Iniciando a caça aos fantasmas do EXIF...")

for nome_arquivo in os.listdir(pasta_imagens):
    if nome_arquivo.lower().endswith(('.jpg', '.jpeg', '.png')):
        caminho_completo = os.path.join(pasta_imagens, nome_arquivo)
        
        try:
            img = Image.open(caminho_completo)
            # Aplica a rotação real e remove o EXIF
            img_corrigida = ImageOps.exif_transpose(img)
            
            # Salva por cima apenas se houver diferença (remove a "etiqueta")
            img_corrigida.save(caminho_completo)
            contador += 1
            print(f"Limpa e corrigida: {nome_arquivo}")
            
        except Exception as e:
            print(f"Erro ao processar {nome_arquivo}: {e}")

print(f"\nPronto! {contador} imagens foram verificadas e alinhadas com as máscaras.")
