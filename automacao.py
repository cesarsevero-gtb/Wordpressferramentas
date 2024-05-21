import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(by, identifier, timeout=20):
    """Função auxiliar para esperar um elemento estar presente."""
    return WebDriverWait(navegador, timeout).until(
        EC.presence_of_element_located((by, identifier))
    )

try:
    # Número de jogos a buscar
    num_jogos = 3

    # Abrir a página web
    navegador = webdriver.Chrome()

    # Aceitar cookies
    navegador.get("https://gamedistribution.com/games/")
    aceitar_cookies = wait_for_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
    aceitar_cookies.click()

    for i in range(1, num_jogos + 1):
        try:
            # Verificar o tipo da variável navegador
            print(f"Tipo da variável 'navegador': {type(navegador)}")

            # Selecionar o i-ésimo jogo da lista
            jogo_xpath = f'//*[@id="__next"]/div/main/div[2]/div[2]/div[{i}]/a[1]/img'
            jogo = wait_for_element(By.XPATH, jogo_xpath)
            jogo.click()

            # Clicar no botão de download
            baixar = wait_for_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/div[1]/div[2]/div[3]/div[1]/button')
            baixar.click()

            # Extrair informações
            titulo = wait_for_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/span/strong').text
            empresa = wait_for_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/div[1]/div[1]/div[1]/div[2]/div[2]/span[1]/a').text
            btn_iframe = wait_for_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/div[1]/div[1]/div[2]/div[2]/span').get_attribute('outerHTML')
            data_criacao = wait_for_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/div[1]/div[2]/div[2]/ul/li[1]/span').text
            descricao = wait_for_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/div[1]/div[1]/div[1]/article').text

            # Salvar as informações em um arquivo de texto
            with open(f'jogo {titulo}.txt', 'w', encoding='utf-8') as file:
                file.write(f"Título: {titulo}\n")
                file.write(f"Empresa: {empresa}\n")
                file.write(f"Data de Criação: {data_criacao}\n")
                file.write(f"Descrição: {descricao}\n")
                file.write(f"Botão Iframe: {btn_iframe}\n")

            # Voltar para a lista de jogos
            navegador.back()
            time.sleep(2)  # Espera para garantir que a página foi carregada

        except Exception as e:
            print(f"Ocorreu um erro ao processar o jogo {i}: {e}")
            navegador.back()  # Garantir que o navegador volte para a lista de jogos em caso de erro
            time.sleep(2)  # Espera para garantir que a página foi carregada

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    # Esperar um pouco para ver o resultado
    time.sleep(5)
    # Fechar o navegador
    navegador.quit()
