import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from skimage.color import rgb2gray

#Mostra a imagem em RGB
def mostrar(imagem, cmap_=None):
    fig = plt.gcf()
    fig.set_size_inches(18,6)
    plt.imshow(cv.cvtColor(imagem, cv.COLOR_BGR2RGB), cmap=cmap_)
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


#Segmentação de bordas usando variedades 
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

def flatten_img(img):
    altura, largura = img.shape[:2]
    img_flat = img.reshape(altura * largura)
    return img_flat

#Segmenta a imagem em 2 regioes separadas pela média dos valores dos pixels
def segmenta2regioes(img):
    pixels = flatten_img(img).copy()
    media = pixels.mean()
    for i in range(len(pixels)):
        if pixels[i] > media:
            pixels[i] = 255
        else:
            pixels[i] = 0
    seg_regiao = pixels.reshape(img.shape[0], img.shape[1])
    return seg_regiao

def segmenta3regioes(img):
    pixels = flatten_img(img).copy()
    for i in range(len(pixels)):
        if pixels[i] > 0.66:
            pixels[i] = 2
        elif pixels[i] > 0.33:
            pixels[i] = 1
        else:
            pixels[i] = 0
    seg_regiao = pixels.reshape(img.shape[0], img.shape[1])
    return seg_regiao

def segmenta4regioes(img):
    pixels = flatten_img(img).copy()
    for i in range(len(pixels)):
        if pixels[i] > (1/4*3):
            pixels[i] = 3
        elif pixels[i] > (1/4*2):
            pixels[i] = 2
        elif pixels[i] > (1/4):
            pixels[i] = 1
        else:
            pixels[i] = 0
    seg_regiao = pixels.reshape(img.shape[0], img.shape[1])
    return seg_regiao

def segmenta5regioes(img):
    pixels = flatten_img(img).copy()
    for i in range(len(pixels)):
        if pixels[i] > (1/5*4):
            pixels[i] = 4
        elif pixels[i] > (1/5*3):
            pixels[i] = 3
        elif pixels[i] > (1/5*2):
            pixels[i] = 2
        elif pixels[i] > (1/5):
            pixels[i] = 1
        else:
            pixels[i] = 0
    seg_regiao = pixels.reshape(img.shape[0], img.shape[1])
    return seg_regiao

#mostra a diferença da segmentação por regioes variando a quantidade de regiões
def segmentacao_regiao(img, cmap='gray'):
    original = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    gray = rgb2gray(img)
    segment2R = segmenta2regioes(gray)
    segment3R = segmenta3regioes(gray)
    segment4R = segmenta4regioes(gray)
    segment5R = segmenta5regioes(gray)

    titulos = ['Imagem Original', '2 Regiões', '3 Regiões', '4 Regiões', '5 Regiões', 'Original (1 Canal)']
    imagens = [original, segment2R, segment3R, segment4R, segment5R, gray]
    
    fig = plt.gcf()
    fig.set_size_inches(18,10)
    for i in range(6):
        plt.subplot(2,3, i+1)
        plt.imshow(imagens[i], cmap)
        plt.title(titulos[i])
        plt.xticks([]),plt.yticks([])
    plt.subplots_adjust(wspace=0.05)
    plt.show()

#Segmentação utilizando a tecnica de clusters
def segmentacao_cluster(img, k=2):
    vetorizado = np.float32(img).reshape(-1,3)
    criterio = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 20, 1, 0)
    ret, label, centros = cv.kmeans(vetorizado, k, None, criterio, 10, cv.KMEANS_RANDOM_CENTERS)
    centros = np.uint8(centros)
    img_final = centros[label.flatten()]
    img_final = img_final.reshape(img.shape)
    return img_final

#Aplicando a segmentação variando a quantidade de clusters da imagem
def segmentacao_clustering(img):
    titulos = ["Imagem Original"]
    imagens = [img]

    segmentacoes = 6
    for k in range(2, segmentacoes+1):
        titulo = 'k = ' + str(k)
        titulos.append(titulo)
        seg = segmentacao_cluster(img, k)
        imagens.append(seg)
    
    fig = plt.gcf()
    fig.set_size_inches(18, 12)
    for i in range(6):
        plt.subplot(2, 3, i+1)
        plt.imshow(cv.cvtColor(imagens[i], cv.COLOR_BGR2RGB))
        plt.title(titulos[i])
        plt.xticks([]), plt.yticks([])
    
    plt.subplots_adjust(wspace=0.05)
    plt.show()

#Função para preencher o interior de objetos
def preenche_buracos(img_thresh, limiar=1000):
    contornos, _ = cv.findContours(img_thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) #cv.RETR_TREE: Retorna todos os contornos
    buracos = []
    for con in contornos:
        area = cv.contourArea(con)
        if area < limiar:
            buracos.append(con)
    
    cv.drawContours(img_thresh, buracos, -1, 255, -1)
    return img_thresh

#função para aplicar e retornar o processod e watershed
def segmentacao_watershed(img, preenchimento=1000):
    original = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    filtro = cv.pyrMeanShiftFiltering(img, 20, 40) #diminui o ruido da imagem
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]

    if preenchimento > 0:
        thresh = preenche_buracos(thresh, preenchimento)
    
    dist = ndi.distance_transform_edt(thresh)
    local_max = peak_local_max(dist, indices=False, min_distance=20, labels=thresh)
    markers = ndi.label(local_max, structure=np.ones((3,3)))[0]
    labels = watershed(-dist, markers, mask=thresh)

    titulos = ['Imagem Original', 'Limiarização (objetos juntos)', 'Distance Transform', 'Watershed (objetos separados)']
    imagens = [original, thresh, dist, labels]

    fig = plt.gcf()
    fig.set_size_inches(16,12)
    for i in range(4):
        plt.subplot(2, 2, i+1)
        if i == 3:
            cmap='jet'
        else:
            cmap='gray'
        plt.imshow(imagens[i], cmap)
        plt.title(titulos[i])
        plt.xticks([]), plt.yticks([])
    plt.show()
    return labels