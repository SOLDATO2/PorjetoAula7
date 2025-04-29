import cv2

imagem = cv2.imread("salaestar.jpg", cv2.IMREAD_GRAYSCALE)

sift = cv2.SIFT_create()

keypoints, descriptors = sift.detectAndCompute(imagem, None)

imagem_sift = cv2.drawKeypoints(imagem, keypoints, None)

cv2.imshow("SIFT - Sala de Estar", imagem_sift)
cv2.waitKey(0)
cv2.destroyAllWindows()