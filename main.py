from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import logging
import threading
import re
from selenium.webdriver.common.keys import Keys
import os
from TempMail import TempMail

from selenium import webdriver

logging.basicConfig(level=logging.ERROR)


def remover_linhas_duplicadas(input_file):
    linhas_unicas = set()
    contador_duplicatas = 0

    with open(input_file, 'r') as arquivo:
        linhas = arquivo.readlines()

    with open(input_file, 'w') as arquivo_saida:
        for linha in linhas:
            linha_strip = linha.strip()
            if linha_strip not in linhas_unicas:
                linhas_unicas.add(linha_strip)
                arquivo_saida.write(linha)
            else:
                contador_duplicatas += 1

        print(f"\nTotal de contas duplicadas: {contador_duplicatas}\n")

def remover_linha(arquivo, linha_para_remover):
    with open(arquivo, 'r') as file:
        linhas = file.readlines()

    with open(arquivo, 'w') as file:
        for linha in linhas:
            if linha.strip("\n") != linha_para_remover:
                file.write(linha)


class login:
    def __init__(self):

        self.delay = 14
        self.contasvalidas = []

    def bingantibug(self,
                    xpath, driverz, delay=14):
        try:
            WebDriverWait(driverz, delay).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        except TimeoutException:
            raise Exception('A Pagina nao carregou a tempo')

    def logar(self, email, senha, modo):
        while True:
            try:

                chrome_options = ChromeOptions()
                chrome_options.add_argument('--log-level=3')
                chrome_options.add_argument("--disable-search-engine-choice-screen")
                chrome_options.add_argument("--search-engine-choice-country")
                chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

                try:
                    driver = webdriver.Chrome(service=ChromeService(executable_path='./chromedriver.exe'),
                                              options=chrome_options)
                except Exception as error:
                    print("Incapaz de abrir o navegador", error)
                    exit()

                driver.get(
                    'https://login.microsoftonline.com/common/oauth2/v2.0/authorize?scope=service%3A%3Aaccount.microsoft.com%3A%3AMBI_SSL%20openid%20profile%20offline_access&response_type=code&client_id=81feaced-5ddd-41e7-8bef-3e20a2689bb7&redirect_uri=https%3A%2F%2Faccount.microsoft.com%2Fauth%2Fcomplete-signin-oauth&client-request-id=34301fcd-b6f1-42f7-ad50-0b722e89170b&x-client-SKU=MSAL.Desktop&x-client-Ver=4.45.0.0&x-client-CPU=x64&x-client-OS=Windows%20Server%202019%20Datacenter&prompt=login&client_info=1&state=H4sIAAAAAAAEAAXBt4KCMAAA0H-5lQEQKRkcKKJEigQkhI16oUXUA4Svv_d-LKZEFEuUHGK_lIcduD3BZPNqoFJZuH3-Im1OJjmdMn5ZYcF_8ZXcreP62xc-cda113adtfrcmUEHOH7EmRCyd2QkedzIyjUKSsXwxkfwGjCOvvY0HQRxYVKid8ja_aoeB4VDvi5Q-9b09RuP8Xmv1ZfnNEaFuGc0R0gu3ymCx1ufC0W9vB5uUjkDgx5VxEXq4cZCxS6HtljbDbYpACRkeMnsVJ-uLMCXl8DdIWjAZ2NP5EKUmrauwdkHumhJ3UeifO0kMwzFTjbjYTaH7LsnBo94lvVz35bIJFZO7IiGLs22exLk--AljnRsMNCsJ6xVq3LVizRq5_1sTw-xLNbT6ecfwNfrVloBAAA&msaoauth2=true&lc=1046&ru=https%3A%2F%2Faccount.microsoft.com%2Faccount%2FAccount%3Fru%3Dhttps%253A%252F%252Faccount.microsoft.com%252F%26destrt%3Dhome.landing')
                driver.maximize_window()


                self.bingantibug('//*[@id="i0116"]', driver)
                driver.find_element('xpath', '//*[@id="i0116"]').send_keys(email)

                self.bingantibug('//*[@id="idSIButton9"]', driver)
                driver.find_element('xpath', '//*[@id="idSIButton9"]').click()

                try:
                    self.bingantibug('//*[@id="idA_PWD_SwitchToPassword"]', driver, delay=3)
                    driver.find_element('xpath', '//*[@id="idA_PWD_SwitchToPassword"]').click()
                except:
                    if driver.find_elements('xpath', '//*[@id="usernameError"]'):
                        remover_linha("contas.txt", email + modo + senha.strip())
                        print("Nome invalido")
                        return
                    pass

                self.bingantibug('//*[@id="i0118"]', driver)
                driver.find_element('xpath', '//*[@id="i0118"]').send_keys(senha.strip())

                self.bingantibug('//*[@id="idSIButton9"]', driver)
                driver.find_element('xpath', '//*[@id="idSIButton9"]').click()
                titulo = driver.title
                while titulo.__contains__("Conta da"):
                    if driver.find_elements('xpath', '//*[@id="i0118Error"]'):
                        remover_linha("contas.txt", email + modo + senha.strip())
                        print("Senha invalida")
                        return
                    titulo = driver.title

                if not titulo.__contains__("?"):

                    if titulo.__contains__("Ajude"):
                        remover_linha("contas.txt", email + modo + senha.strip())
                        print("Conta ja usada")
                        while True:
                            continue
                        return

                    while not titulo.__contains__("Vamos"):
                        if titulo.__contains__("account.live"):
                            driver.refresh()


                        if titulo.__contains__("atualizando"):
                            driver.find_element('xpath', '//*[@id="iNext"]').click()

                        if driver.find_elements('xpath', '//*[@id="i0118Error"]'):
                            remover_linha("contas.txt", email + modo + senha.strip())
                            print("Senha invalida")
                            return
                        link = driver.current_url
                        if link.__contains__("Abuse"):
                            bloqueada = False
                            try:
                                texto = driver.find_element('xpath', '//*[@id="serviceAbuseLandingTitle"]').text
                                if texto.__contains__("bloqueada"):
                                    bloqueada = True
                            except:
                                pass
                            if bloqueada:
                                print("Conta bloqueada")
                                remover_linha("contas.txt", email + modo + senha.strip())
                                return
                        titulo = driver.title

                    self.bingantibug('//*[@id="frmAddProof"]', driver)
                    texto = driver.find_element('xpath', '//*[@id="iShowSkip"]').text
                    dias = re.findall(r'\d+', texto)
                    if True:
                        driver.find_element('xpath', '//*[@id="EmailAddress"]').send_keys(inb.address)
                        driver.find_element('xpath', '//*[@id="iNext"]').click()
                        self.bingantibug('//*[@id="iOttText"]', driver)

                        while True:
                            emails = TempMail.getEmails(tmp, inbox=inb)
                            if not len(emails):
                                continue
                            mensagem = emails[0].body
                            break

                        linhas = str(mensagem).splitlines()
                        otp = [i for i in linhas if i.__contains__('Código de segurança:')]

                        ott = otp[0][21:]
                        driver.find_element('xpath', '//*[@id="iOttText"]').send_keys(ott)
                        driver.find_element('xpath', '//*[@id="iNext"]').click()

                        wait = WebDriverWait(driver, 5)

                        bug = False

                        try:
                            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="iProof0"]')))
                            bug = True
                        except:
                            pass

                        if bug:
                            driver.find_element('xpath', '//*[@id="iProofLbl0"]').click()
                            driver.find_element('xpath', '//*[@id="iProofEmail"]').send_keys(inb.address.split("@")[0])
                            html = driver.find_element(By.TAG_NAME, 'html')
                            html.send_keys(Keys.END)
                            driver.find_element('xpath', '//*[@id="iSelectProofAction"]').click()
                            self.bingantibug('//*[@id="iOttText"]', driver)
                            tries = 0
                            while True:
                                emails = TempMail.getEmails(tmp, inbox=inb)
                                if not len(emails):
                                    continue
                                mensagem = emails[0].body
                                tries += 1
                                if tries > 1:
                                    break
                            linhas = str(mensagem).splitlines()
                            otp = [i for i in linhas if i.__contains__('Código de segurança:')]
                            print(linhas)

                            ott = otp[0][21:]
                            driver.find_element('xpath', '//*[@id="iOttText"]').send_keys(ott)
                            driver.find_element('xpath', '//*[@id="iVerifyCodeAction"]').click()

                            if not driver.title.lower().__contains__("gerir"):
                                self.bingantibug('//*[@id="idSIButton9"]', driver)
                                driver.find_element('xpath', '//*[@id="idSIButton9"]').click()

                        self.contasvalidas.append(email + modo + senha)
                        return
                self.contasvalidas.append(email + modo + senha)
                return

            except Exception as e:
                try:
                    threading.Thread(target=driver.quit, args=()).start()
                except:
                    pass


if __name__ == "__main__":
    quantidade = 5
    modo = ":"

    tmp = TempMail()
    inb = TempMail.generateInbox(tmp)
    while not inb.address:
        tmp = TempMail()
        inb = TempMail.generateInbox(tmp)

    remover_linhas_duplicadas("contas.txt")

    Login = login()

    with open('contas.txt', "r") as file:
        contas = file.readlines()

    while len(contas):
        threads = []
        contasremover = []
        for _, conta in enumerate(contas[0:int(quantidade)], start=1):
            if not len(conta):
                continue

            if ";" in conta:
                email, senha = conta.split(";")
            else:
                email, senha = conta.split(":")

            t = threading.Thread(target=Login.logar, args=(email, senha, modo))
            threads.append(t)
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        if not os.path.isfile("contasuteis.txt"):
            with open("contasuteis.txt", 'w+'):
                pass
        with open("contasuteis.txt", 'r') as file:
            linhas_existentes = file.readlines()

        for conta in Login.contasvalidas:
            email, senha = conta.split(modo)
            if email + ";" + senha not in linhas_existentes:
                # Se não existir, adicionar a nova linha ao final do arquivo
                with open("contasuteis.txt", 'a') as arquivo_saida:
                    arquivo_saida.write(email + modo + senha)
            else:
                print("Linha já existe no arquivo. Não foi adicionada.")
            remover_linha("contas.txt", email + modo + senha.strip())
        print(f'{len(Login.contasvalidas)}/{quantidade} Certas!\n\n')
        Login.contasvalidas.clear()

        with open('contas.txt', "r") as file:
            contas = file.readlines()
