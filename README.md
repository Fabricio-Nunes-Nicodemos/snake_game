# **Snake Game 🐍 - Python**
Clone do jogo da cobra construído em Python para praticar meus fundamentos 

## **Descrição do Projeto**
Este projeto é um **Jogo da cobra (Snake Game)** desenvolvido em Python, utilizando:
- A biblioteca **Turtle, Screen** para gráficos 2D.
- A biblioteca **Random** para gerar a comida da cobra aleatóriamente na tela.
- O paradigma de **Programação Orientada a Objetos (POO)** para organizar o código em classes.

### **📚 Funcionamento do jogo**
- **Objetivo**: Controle a cobra para comer os alimentos e aumentar sua pontuação.
- **Controles**: Use as setas do teclado (↑, ↓, →, ←) para mover a cobra.
- **Fim de jogo**: O jogo termina se a cobra colidir consigo mesma ou com as bordas da tela.

## **🎮 Demonstração do jogo**
Aqui está uma prévia do jogo em ação:

<div align="center">
  <img src="img/GIF_jogo_da_cobra.gif" alt="Snake Game GIF" width="400">
</div>

---

## **🛠️ Tecnologias Utilizadas**
- **Python 3.12**
- **Turtle**: Renderização gráfica simples.
- **Screen**: Usada para configurar a tela do jogo, incluindo as dimensões, cor de fundo e detecção de eventos como pressionar teclas.
- **Random**: Elementos aleatórios no jogo.
- **Programação Orientada a Objetos (POO)**: Para modularizar o código

---

## **📂 Estrutura do Projeto**

```plaintext
SnakeGame/
│
├── main.py              # Arquivo principal que inicializa o jogo
├── snake.py             # Classe para controlar o comportamento da cobra
├── food.py              # Classe para controlar o comportamento dos alimentos
├── scoreboard.py        # Classe para gerenciar a pontuação
├── requirements.txt     # Dependências do projeto
└── README.md            # Documentação do projeto

---

## **Como Executar o Projeto**
1. Certifique-se de ter o **Python 3.12+** instalado em sua máquina.
2. Clone este repositório:
   ```bash
   git clone https://github.com/Fabricio-Nunes-Nicodemos/snake_game.git
3. Navegue até o diretório do projeto e execute o arquivo principal:
  ```bash
  python main.py
