import cv2
import numpy as np

def processa_imagem_com_parametros(imagem, maxCantos, nivelQualidade, distanciaMinima):
    img_copia = imagem.copy()
    cantos = cv2.goodFeaturesToTrack(
        img_copia,
        maxCorners=maxCantos,
        qualityLevel=nivelQualidade,
        minDistance=distanciaMinima
    )
    if cantos is not None:
        cantos = np.int64(cantos)
        for canto in cantos:
            x, y = canto.ravel()
            cv2.circle(img_copia, (x, y), 3, 255, -1)
    return img_copia

def main():
    imagem = cv2.imread("salaestar.jpg", cv2.IMREAD_GRAYSCALE)
    imagem2 = cv2.imread("fliperama.jpg", cv2.IMREAD_GRAYSCALE)
    imagem3 = cv2.imread("decoracao-de-halloween.jpg", cv2.IMREAD_GRAYSCALE)

    #(maxCantos, nívelQualidade, distânciaMínima)
    lista_params = [
        (100, 0.01, 10),
        (200, 0.02, 15),
        (150, 0.03, 8)
    ]

    imagens = [
        ("Sala de Estar", imagem),
        ("Fliperama", imagem2),
        ("Decoração de Halloween", imagem3)
    ]

    for titulo, img in imagens:
        for maxCantos, nivelQualidade, distanciaMinima in lista_params:
            resultado = processa_imagem_com_parametros(img, maxCantos, nivelQualidade, distanciaMinima)
            titulo_janela = f"Cantos - {titulo} ({maxCantos}, {nivelQualidade}, {distanciaMinima})"
            cv2.imshow(titulo_janela, resultado)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

if __name__ == "__main__":
    main()