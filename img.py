import cv2

def convert_to_sketch(image_path):
    image = cv2.imread('pikachu.png')
    if image is None:
        print("Error: Could not read image file")
        return
    
    #grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #INVERT GRAYSCALE
    inverted_image = 255 - gray_image
    #BLUR
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21),0)
    #INVERT BLURRED IMG
    inverted_blurred = 255 - blurred_image
    #Create sketch
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

    #show and save sketch
    cv2.imshow('Pencil Sketch', pencil_sketch)
    cv2.imwrite('pencil_sketch.png',pencil_sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#provide path to image
convert_to_sketch('path_to_your_image.jpg')
