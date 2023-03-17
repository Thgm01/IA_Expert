import cv2
import random
import numpy as np
	
## Gera cores aleatórias
def random_colors(N, seed, bright=True):
    import colorsys
    # Para poder gerar cores mais distintas visualmente vamos gerar os valores no espaço de cor HSV, depois convertemos para RGB. 
    brightness = 1.0 if bright else 0.7
    hsv = [(i / N, 1, brightness) for i in range(N)]
    colors = list(map(lambda c: colorsys.hsv_to_rgb(*c), hsv))
    random.Random(seed).shuffle(colors)
    return colors

## Aplica mascara na imagem 
def apply_mask(image, mask, color, alpha=0.5):
    for c in range(3):
        image[:, :, c] = np.where(
                mask == 1,
                image[:, :, c] *
                (1 - alpha) + alpha * color[c] * 255,
                image[:, :, c])
    return image

## Exibe as instancias (objetos segmentados)
## Foi necessário modificar essa função para que ela retorne a imagem (para podermos usar em nosso código e salvar os frames do vídeo) 
def display_instances(image, boxes, masks, class_ids, class_names,
                      scores=None, title="", figsize=(16, 16), ax=None,
                      show_mask=True, show_bbox=True, colors=None, captions=None):
    from matplotlib import patches, lines
    from skimage.measure import find_contours
    from matplotlib.patches import Polygon
    
    # Numero de instancias
    N = boxes.shape[0]
    if not N:
        print("\n*** Nenhuma instancia a exibir *** \n")
    else:
        assert boxes.shape[0] == masks.shape[-1] == class_ids.shape[0]

    # Gera cores aleatórias
    colors = colors or random_colors(N)

    height, width = image.shape[:2]

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    masked_image = image.astype(np.uint32).copy()

    for i in range(N):
        color = colors[class_ids[i]]

        # Caixa delimitadora / bounding box
        if not np.any(boxes[i]):
            # Pula essa instancias se não há caixas delimitadoras. Provavelmente foi perdida após crop na imagem 
            continue
        y1, x1, y2, x2 = boxes[i]
        if show_bbox:
            p = patches.Rectangle((x1, y1), x2 - x1, y2 - y1, linewidth=2,
                                alpha=0.7, linestyle="dashed",
                                edgecolor=color, facecolor='none')

        # Rótulo / Label
        if not captions:
            class_id = class_ids[i]
            score = scores[i] if scores is not None else None
            label = class_names[class_id]
            caption = "{} {:.3f}".format(label, score) if score else label
        else:
            caption = captions[i]
        masked_image = cv2.putText(np.float32(masked_image), caption, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255), 1)

        # Mascara
        mask = masks[:, :, i]
        if show_mask:
            masked_image = apply_mask(masked_image, mask, color)

        # Poligono da mascara
        # adiciona um espaçamento Para garantir polígonos adequados para máscaras que tocam as bordas da imagem.
        padded_mask = np.zeros(
            (mask.shape[0] + 2, mask.shape[1] + 2), dtype=np.uint8)
        padded_mask[1:-1, 1:-1] = mask
        contours = find_contours(padded_mask, 0.5)
        for verts in contours:
            # Subtract the padding and flip (y, x) to (x, y)
            verts = np.fliplr(verts) - 1
            p = Polygon(verts, facecolor="none", edgecolor=color)

    return masked_image.astype(np.uint8)

""" 
O código foi criado a partir da modificação das funções do repositório do Mask R-CNN: https://github.com/matterport/Mask_RCNN/blob/master/mrcnn/visualize.py
@ IA Expert Academy   /  @gabevr
""" 