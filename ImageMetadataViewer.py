from PIL import Image
import exifread
import os
from termcolor import colored

def mostrar_dados_imagem(caminho_imagem):
    # Verificar se o arquivo existe
    if not os.path.isfile(caminho_imagem):
        print(colored("O arquivo de imagem não foi encontrado.", "red"))
        return
    
    # Abrir imagem com Pillow para informações básicas
    with Image.open(caminho_imagem) as img:
        print(colored("Informações Básicas da Imagem:", "cyan"))
        print(colored(f"Formato: {img.format}", "yellow"))
        print(colored(f"Dimensões: {img.size} pixels", "yellow"))
        print(colored(f"Modo de cor: {img.mode}", "yellow"))

    # Abrir imagem com exifread para metadados EXIF
    with open(caminho_imagem, 'rb') as f:
        tags = exifread.process_file(f)
        if tags:
            print(colored("\nMetadados EXIF:", "cyan"))
            for tag in tags.keys():
                if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                    print(colored(f"{tag}: {tags[tag]}", "green"))
        else:
            print(colored("Não foram encontrados metadados EXIF.", "red"))

# Exemplo de uso
if __name__ == "__main__":
    caminho_da_imagem = input(colored("Digite o caminho da imagem: ", "blue"))
    mostrar_dados_imagem(caminho_da_imagem)
