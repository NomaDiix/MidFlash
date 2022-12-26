import os
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


PATH_BASE = os.getcwd()
PATH_SOURCE = os.path.join(PATH_BASE, "base_images")
PATH_PROSSED = os.path.join(PATH_BASE, "processed_images")
PATH_PROSSED_RESOLUTION = os.path.join(PATH_BASE, "processed_resolution_images")

WEB = 'https://zyro.com/es/herramientas/upscaler-de-imagenes'
BUTTON_CLOSE = 'button-close.modal__close-button'
BUTTON_COOKIES = 'button.medium-up.button--small.button--small-mobile.button--black'
BUTTON_LOAD = 'button.hero__button.button--small.button--small-mobile.button--white'
BUTTON_DOWNLOAD = 'button.button--medium.button--medium-mobile.button--black'
BUTTON_NEWLOAD = 'button.button--outline.button--medium.button--medium-mobile.button--black'
IMAGE = 'C:\\Users\\fabian\\Desktop\\Imagenes\\Midjourney\\Recortadas\\Elegidas\\1.png'
PATH_DOWNLOAD = "C:\\Users\\fabian\\Downloads"


if not os.path.exists(PATH_PROSSED):
    os.makedirs(PATH_PROSSED, exist_ok=True)
    
if not os.path.exists(PATH_PROSSED_RESOLUTION):
    os.makedirs(PATH_PROSSED_RESOLUTION, exist_ok=True)

def download_wait(path_to_downloads):
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < 20:
        time.sleep(1)
        dl_wait = False
        for fname in os.listdir(path_to_downloads):
            if fname.endswith('.crdownload'):
                dl_wait = True
        seconds += 1
    return seconds

def push_button(button, driver):
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            driver.find_element(By.CLASS_NAME, button)
        )).click()
    
def cutout(image):
    imagen = Image.open(os.path.join(PATH_SOURCE, image))
    ancho, alto = imagen.size
    ancho_cuadrante = ancho // 2
    alto_cuadrante = alto // 2

    # Crea una lista con las coordenadas de cada cuadrante
    cuadrantes = [
        (0, 0, ancho_cuadrante, alto_cuadrante),
        (ancho_cuadrante, 0, ancho, alto_cuadrante),
        (0, alto_cuadrante, ancho_cuadrante, alto),
        (ancho_cuadrante, alto_cuadrante, ancho, alto)
    ]

    for i, cuadrante in enumerate(cuadrantes):
        # Utiliza el método crop() para cortar la imagen en el cuadrante especificado
        imagen_cuadrante = imagen.crop(cuadrante)
        
        imagen_cuadrante.save(
            os.path.join(
                PATH_PROSSED, 
                image.replace('.png', '_{}.jpg'.format(i))
                )
            )

def resolution(image):
    return


# Recorre la lista de cuadrantes y crea una imagen para cada uno
try:
    imagenes = [
        imagen for imagen in os.listdir(PATH_SOURCE) 
        if imagen.endswith(('.jpg', '.png'))
    ]
    for image in imagenes:
        cutout(image)
        
    imagenes_procesadas = [
        imagen for imagen in os.listdir(PATH_PROSSED) 
        if imagen.endswith(('.jpg', '.png'))
    ]
    
    for image in imagenes_procesadas:
        print(os.path.join(PATH_PROSSED, image))
     
except FileNotFoundError:
    print('No existe la ruta', PATH_SOURCE)
except NotADirectoryError:
    print('La ruta no es un directorio ', PATH_SOURCE)