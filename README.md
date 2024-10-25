# Outlook Account Checker

Este é um programa em Python para verificação automática de contas do Outlook utilizando o Selenium. Ele autentica contas com credenciais fornecidas e realiza uma verificação para confirmar se a conta é válida ou não. 

## Pré-requisitos

- **Python 3.6+**
- **Google Chrome** (ou outro navegador compatível com o Selenium)
- **Chromedriver** (compatível com a versão do navegador)
- **Bibliotecas Python necessárias** (ver seção de instalação)

## Instalação

1. **Clone este repositório:**

   ```bash
   git clone https://github.com/seu_usuario/outlook-account-checker.git
   cd outlook-account-checker
   ```

2. **Instale as dependências do projeto:**

   Certifique-se de ter um ambiente virtual configurado e ative-o. Em seguida, execute:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure o Chromedriver:**

   Baixe o [ChromeDriver](https://sites.google.com/chromium.org/driver/) e certifique-se de colocá-lo no mesmo diretório do script ou no PATH do sistema. O ChromeDriver deve corresponder à versão do Google Chrome instalada.

## Como usar

1. **Preencha as Credenciais**:
   
   Crie um arquivo `contas.txt` no diretório do projeto, onde cada linha deve conter um email e senha separados por ponto e vírgula (`email@dominio.com;senha123`).

2. **Execute o Programa**:
   
   Inicie o script para iniciar a verificação automática das contas.

   ```bash
   python main.py
   ```

   O programa abrirá uma instância do navegador Chrome (ou outro configurado) e tentará fazer login em cada conta do arquivo `contas.txt`. Para cada conta, o programa validará se a senha está correta e registrará o status da verificação.

3. **Resultados**:

   - As contas verificadas com sucesso serão registradas no arquivo `contasuteis.txt`.
   - Contas inválidas ou bloqueadas não serão adicionadas ao arquivo de resultados.

## Funcionalidades

- **Verificação Automática**: O Selenium automatiza o processo de login no Outlook para verificar a validade das contas.
- **Controle de Erros**: O script trata exceções como senhas incorretas, contas bloqueadas e falhas de login.
- **Remoção de Duplicatas**: As contas duplicadas no arquivo de entrada são removidas automaticamente para evitar tentativas de login repetidas.
- **Configuração Flexível**: O tempo de espera e outras configurações podem ser ajustadas diretamente no código para se adequar às necessidades.

## Estrutura do Código

```plaintext
outlook-account-checker/
├── chromedriver.exe         # Driver necessário para automação (versão correspondente ao seu navegador)
├── contas.txt               # Arquivo de entrada com as credenciais (email;senha)
├── contasuteis.txt          # Arquivo de saída com as contas verificadas com sucesso
├── main.py      # Script principal para verificar as contas
└── requirements.txt         # Dependências do projeto
```

## Dependências

O projeto usa as seguintes bibliotecas:

- **Selenium**: Para automação do navegador e login automático.
- **Tempmail-lol**: Para gerar email automaticamente

## Licença

Este projeto está licenciado sob a Licença MIT
