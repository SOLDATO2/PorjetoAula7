import cv2
import numpy as np

#algoritimo de detectar cantos


def main():
    
    imagem = cv2.imread("salaestar.jpg", cv2.IMREAD_GRAYSCALE)
    imagem2 = cv2.imread("fliperama.jpg", cv2.IMREAD_GRAYSCALE)
    imagem3 = cv2.imread("decoracao-de-halloween.jpg", cv2.IMREAD_GRAYSCALE)
    
    #blocksize = tamanho da vizinhança
    #ksize = tamanho da abertura do sobel para vizinhança
    #k = constante de Harris
    
    #sala de estar
    
    
    for i in range(0, 3):
        if i == 0:
            harris1_1 = cv2.cornerHarris(imagem, 2, 3, 0.04)
            imagem[harris1_1 > 0.01 * harris1_1.max()] = 255
            cv2.imshow("Harris Bordas - Sala de Estar (2,3)", imagem)
            
            harris1_2 = cv2.cornerHarris(imagem, 3, 5, 0.04)
            imagem[harris1_2 > 0.01 * harris1_2.max()] = 255
            cv2.imshow("Harris Bordas - Sala de Estar (3,5)", imagem)
            
            harris1_3 = cv2.cornerHarris(imagem, 5, 7, 0.04)
            imagem[harris1_3 > 0.01 * harris1_3.max()] = 255
            cv2.imshow("Harris Bordas - Sala de Estar (5,7)", imagem)
            
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif i == 1:
            harris2_1 = cv2.cornerHarris(imagem2, 2, 3, 0.04)
            imagem2[harris2_1 > 0.01 * harris2_1.max()] = 255
            cv2.imshow("Harris Bordas - Fliperama (2, 3)", imagem2)
            
            harris2_2 = cv2.cornerHarris(imagem2, 3, 5, 0.04)
            imagem2[harris2_2 > 0.01 * harris2_2.max()] = 255
            cv2.imshow("Harris Bordas - Fliperama (3, 5)", imagem2)
            
            harris2_3 = cv2.cornerHarris(imagem2, 5, 7, 0.04)
            imagem2[harris2_3 > 0.01 * harris2_3.max()] = 255
            cv2.imshow("Harris Bordas - Fliperama (5, 7)", imagem2)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif i == 2:
            harris3_1 = cv2.cornerHarris(imagem3, 2, 3, 0.04)
            imagem3[harris3_1 > 0.01 * harris3_1.max()] = 255
            cv2.imshow("Harris Bordas - Decoracao de Halloween (2, 3)", imagem3)
            
            harris3_2 = cv2.cornerHarris(imagem3, 3, 5, 0.04)
            imagem3[harris3_2 > 0.01 * harris3_2.max()] = 255
            cv2.imshow("Harris Bordas - Decoracao de Halloween (3, 5)", imagem3)
            
            harris3_3 = cv2.cornerHarris(imagem3, 5, 7, 0.04)
            imagem3[harris3_3 > 0.01 * harris3_3.max()] = 255
            cv2.imshow("Harris Bordas - Decoracao de Halloween (5,7)", imagem3)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    

if __name__ == "__main__":
    main()