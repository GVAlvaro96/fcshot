from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
import time
import logging


class Bot:
    # Configurar la biblioteca logging para guardar mensajes en un archivo
    logging.basicConfig(filename='archivo_de_log.log', level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def snipefc(self,player_name, buy, max_buy,intervals):

        logging.info('Iniciamos el programa')
        logging.info('Esperamos a que introduzcas las credenciales')

        texto_nombre_jugador = player_name
        importe_puja = 150
        compra = buy
        compra_max = max_buy
        infinito = False
        selector_css = 'div.tile.ut-tile-view--with-gfx.col-2-3-md.col-1-1.ut-tile-transfer-market'

        # Ruta al controlador de Chrome. Reemplaza con la ubicación de tu propio controlador.
        chrome_driver_path = 'D:\Descargas\chromedriver.exe'

        # Crea una instancia de Chrome WebDriver
        driver = webdriver.Chrome()

        # Abre la página web donde deseas introducir el usuario y la contraseña
        driver.get(
            'https://signin.ea.com/p/juno/login?execution=e1938948123s1&initref=https%3A%2F%2Faccounts.ea.com%3A443%2Fconnect%2Fauth%3Fhide_create%3Dtrue%26display%3Dweb2%252Flogin%26scope%3Dbasic.identity%2Boffline%2Bsignin%2Bbasic.entitlement%2Bbasic.persona%26release_type%3Dprod%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.ea.com%252Fea-sports-fc%252Fultimate-team%252Fweb-app%252Fauth.html%26accessToken%3D%26locale%3Den_US%26prompt%3Dlogin%26client_id%3DFC24_JS_WEB_APP')  # Reemplaza con la URL de tu sitio web


        codigo = False
        logging.info('Aun no se ha enviado el codigo...')
        while not codigo:
            try:
                enviar_codigo = driver.find_element(By.ID,'btnSendCode')
                enviar_codigo.click()
                codigo = True
            except (NoSuchElementException, StaleElementReferenceException, TimeoutException):

                pass
        logging.info('Codigo enviado...')

        logging.info('No se ha dado a login')
        login = False
        while not login:
            try:
                boton_login = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/main/div/div/div/button[1]')))
                boton_login.click()
                login = True
            except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
                pass
        logging.info('Se ha dado a login...')

        logging.info('Aun no estamos en transferibles')
        transferibles = False
        while not transferibles:
            try:
                # Ir a "Transferibles"
                boton_transfers = driver.find_element(By.XPATH, '/html/body/main/section/nav/button[3]')
                boton_transfers.click()
                # Abrir "Transferibles"
                elemento = driver.find_element(By.CSS_SELECTOR, selector_css)
                elemento.click()
                transferibles = True
            except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
                pass
        logging.info('Estamos en transferibles')
        if texto_nombre_jugador:
            nombre_jugador = WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/input')))
            nombre_jugador.clear()
            nombre_jugador.send_keys(texto_nombre_jugador)
            pulsar_nombre = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,
                                                                                       '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[2]/ul/button')))
            pulsar_nombre.click()

        campo_entrada = WebDriverWait(driver, 1).until(EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/input')))
        campo_entrada.clear()
        texto_a_escribir = importe_puja
        campo_entrada.send_keys(texto_a_escribir)
        campo_entrada_max = driver.find_element(By.XPATH,
                                                '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input')
        texto_a_escribir_max = str(compra)  # Convierte el resultado a cadena antes de asignarlo
        campo_entrada_max.clear()
        campo_entrada_max.send_keys(texto_a_escribir_max)
        logging.info('Introducimos los filtros')
        logging.info('Tienes 30 segundos para introducir los filtros que quieras')
        # Duración total del contador en segundos
        duracion_total = 30

        # Duración en segundos entre cada mensaje
        intervalo = 5

        tiempo_inicial = time.time()  # Tiempo actual

        while (time.time() - tiempo_inicial) < duracion_total:
            # Mensaje que deseas imprimir
            resultado = str(time.time() - tiempo_inicial)
            tiempo =  resultado.split('.')
            mensaje=f"Han pasado {tiempo[0]} segundos para introducir  los filtros que quieras"
            logging.info(mensaje)

            # Pausa de 5 segundos antes de imprimir el próximo mensaje
            time.sleep(intervalo)

       

        # Bucle principal


        while not infinito:
            try:
                compra = int(compra) + int(intervals)
                if compra >= int(compra_max):
                    compra = buy
                buscar = driver.find_element(By.XPATH,
                                             '/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]')
                buscar.click()
                boton_atras = driver.find_element(By.XPATH, '/html/body/main/section/section/div[1]/button[1]')

                try:
                    lista_jugadores = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located(
                        (By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li')))
                    if len(lista_jugadores) == 1:
                        jugador = lista_jugadores[0]
                        jugador.click()
                        comprar_jugador = driver.find_element(By.XPATH,
                                                              '/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]')
                        comprar_jugador.click()
                        aceptar_compra = driver.find_element(By.XPATH, '/html/body/div[4]/section/div/div/button[1]')
                        aceptar_compra.click()
                        logging.info('El jugador que ha salido es:', jugador.text)
                    else:
                        for jugador in reversed(lista_jugadores):
                            jugador.click()
                            comprar_jugador = driver.find_element(By.XPATH,
                                                                  '/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]')
                            comprar_jugador.click()
                            aceptar_compra = driver.find_element(By.XPATH,
                                                                 '/html/body/div[4]/section/div/div/button[1]')
                            aceptar_compra.click()
                            logging.info('El jugador que ha salido es:', jugador.text)

                    boton_atras.click()
                    campo_entrada_max = driver.find_element(By.XPATH,
                                                            '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input')
                    texto_a_escribir_max = str(int(compra) + int(intervals))  # Convierte el resultado a cadena antes de asignarlo
                    campo_entrada_max.clear()
                    campo_entrada_max.send_keys(texto_a_escribir_max)

                except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
                    pass
                    logging.info('No se ha encontrado ningún jugador')
                    boton_atras = driver.find_element(By.XPATH, '/html/body/main/section/section/div[1]/button[1]')
                    boton_atras.click()
                    logging.info('Volviendo a buscar')
                    if importe_puja == 150:
                        campo_entrada = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,
                                                                                                       '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/input')))
                        campo_entrada.clear()
                        texto_a_escribir = "200"
                        campo_entrada.send_keys(texto_a_escribir)
                        importe_puja = 200
                    else:
                        campo_entrada = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,
                                                                                                       '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/input')))
                        campo_entrada.clear()
                        texto_a_escribir = importe_puja
                        campo_entrada.send_keys(texto_a_escribir)
                        importe_puja = 150

                    campo_entrada_max = driver.find_element(By.XPATH,
                                                            '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input')
                    texto_a_escribir_max = str(int(compra) + int(intervals))  # Convierte el resultado a cadena antes de asignarlo
                    campo_entrada_max.clear()
                    campo_entrada_max.send_keys(texto_a_escribir_max)
            except TimeoutException:
                elemento = driver.find_element(By.CSS_SELECTOR, selector_css)
                elemento.click()
                if texto_nombre_jugador:
                    nombre_jugador = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,                                                                        '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/input')))
                    nombre_jugador.clear()
                    nombre_jugador.send_keys(texto_nombre_jugador)
                    pulsar_nombre = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,
                                                                                                   '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[2]/ul/button')))
                    pulsar_nombre.click()
                campo_entrada = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,
                                                                                               '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/input')))
                campo_entrada.clear()
                texto_a_escribir = importe_puja
                campo_entrada.send_keys(texto_a_escribir)
                campo_entrada = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,
                                                                                               '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/input')))
                campo_entrada.clear()
                texto_a_escribir = importe_puja
                campo_entrada.send_keys(texto_a_escribir)
                campo_entrada_max = driver.find_element(By.XPATH,
                                                        '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input')
                texto_a_escribir_max = str(compra)  # Convierte el resultado a cadena antes de asignarlo
                campo_entrada_max.clear()
                campo_entrada_max.send_keys(texto_a_escribir_max)

                time.sleep(1)
                pass

        time.sleep(5)

        # Cierra el navegador
        driver.quit()


