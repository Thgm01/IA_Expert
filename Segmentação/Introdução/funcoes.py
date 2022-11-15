import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#Mostra a imagem
def mostrar(imagem, cmap_=None):
    fig = plt.gcf()
    fig.set_size_inches(18,6)
    plt.imshow(imagem, cmap=cmap_)
    plt.axis('off')
    plt.show()

#Aplica o filtro de Otsu e mostra
def filtro_otsu(imagem):
    valor, otsu = cv.threshold(imagem, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print("Valor do limiar: ", valor)
    mostrar(otsu)

#Exibir os tipos de limiarização
def exibir_lim(img, limiar = 127):
    _, thresh_binary = cv.threshold(img, limiar, 255, cv.THRESH_BINARY)
    _, thresh_binary_inv = cv.threshold(img, limiar, 255, cv.THRESH_BINARY_INV)
    _, thresh_trunc = cv.threshold(img, limiar, 255, cv.THRESH_TRUNC)
    _, thresh_to_zero = cv.threshold(img, limiar, 255, cv.THRESH_TOZERO)
    _, thresh_to_zero_inv = cv.threshold(img, limiar, 255, cv.THRESH_TOZERO_INV)

    titulos = ['imagem original', 'Binary', 'Binary Inv', 'Trunc', 'To Zero', 'To Zero Inv']
    imagens = [img, thresh_binary, thresh_binary_inv, thresh_trunc, thresh_to_zero, thresh_to_zero_inv]

    fig = plt.gcf()
    fig.set_size_inches(18,12)
    for i in range(6):
        plt.subplot(2,3, i+1)
        plt.imshow(cv.cvtColor(imagens[i], cv.COLOR_BGR2RGB), cmap='gray')
        plt.title(titulos[i])
        plt.xticks([]),plt.yticks([])
    plt.show()

#Limiarização Adaptativa
def limiarizacao_adaptativa(img, limiar = 140, block_size = 11, c = 9):
    _, limiar_global = cv.threshold(img, limiar, 255, cv.THRESH_BINARY)
    limiar_media = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, block_size, c)
    limiar_gauss = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, block_size, c)
    
    imagens = [img, limiar_global, limiar_media, limiar_gauss]
    titulos = ["Imagem Original", "Limiarização Global", "Limiarização Adaptativa - Média", "Limiarização Adaptativa - Gaussiana"]

    fig = plt.gcf()
    fig.set_size_inches(18, 12)

    for i in range(4):
        plt.subplot(2,2, i+1)
        plt.imshow(cv.cvtColor(imagens[i], cv.COLOR_BGR2RGB), cmap='gray')
        plt.title(titulos[i])
        plt.xticks([]), plt.yticks([])


def segmentacao_bordas(img):
    desfoque = cv.GaussianBlur(img, (5,5), 0)

    sobel_x = cv.Sobel(desfoque, cv.CV_64F, 1, 0, ksize=3)
    sobel_y = cv.Sobel(desfoque, cv.CV_64F, 0, 1, ksize=3)

    sobel_x = cv.convertScaleAbs(sobel_x)
    sobel_y = cv.convertScaleAbs(sobel_y)

    sobel = cv.addWeighted(src1=sobel_x, alpha=0.5, src2=sobel_y, beta=0.5, gamma=100)

    canny = cv.Canny(desfoque, 80,140)

    kernel = np.ones((3,3), np.uint8)
    dilatacao = cv.dilate(canny, kernel, iterations=2)
    erosao = cv.erode(canny, kernel, iterations=1)

    imagens = [img, sobel, canny, erosao]
    titulos = ["Imagem Original", "Filtro de Sobel", "Canny Edge", "Canny Edge + Dilatação"]

    fig = plt.gcf()
    fig.set_size_inches(18, 12)

    for i in range(4):
        plt.subplot(2,2, i+1)
        plt.imshow(cv.cvtColor(imagens[i], cv.COLOR_BGR2RGB), cmap='gray')
        plt.title(titulos[i])
        plt.xticks([]), plt.yticks([])
        plt.subplots_adjust(wspace=0.1)