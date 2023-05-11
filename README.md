# RobocinPS-2023-Drones-DM
## Robôcin CIN UFPE 2023 Selection Process - Drones - Decision and Movement

This repository is for storage and submission of the drone decision and movement challenge for Robôcin's 2023 selection process. Robôcin is a research group at the Center for Informatics of the Federal University of Pernambuco that utilizes robotics to solve problems. The chosen category for the selection process is Drones, and the subcategory is Decision and Movement.

The objective of the challenge is to create one or more codes that make a drone from a 3D simulation traverse the perimeter of a square that contains 4 colors. After traversing all the colors, the drone should land. The starting point of the drone is the intersection of the green part of the perimeter with the red part of the perimeter.

## Processo Seletivo 2023 do Robôcin do CIN da UFPE - Drones - Decisão e Movimentação

Este repositório é para armazenamento e entrega do desafio de decisão e movimentação de drones do processo seletivo de 2023 do Robôcin. O Robôcin é um grupo de pesquisa do Centro de Informática da Universidade Federal de Pernambuco, que utiliza a robótica para resolver problemas. A categoria escolhida do processo seletivo é Drones, e a subcategoria é Decisão e Movimentação. 

O objetivo do desafio é criar um ou mais códigos que façam um drone de uma simulação 3D percorrer o perímetro de um quadrado que contém 4 cores, após percorrer todas as cores, o drone deve pousar. O ponto de partida do drone é a interseção da parte verde do périmetro com a parte vermelha do perímetro.

## links:

Edital do processo seletivo: https://robocin.com.br/archives/ps-2023/edital-ps2023-v1.pdf?

PDF dos desafios de drones: https://robocin.com.br/archives/ps-2023/projeto-ps2023-drones-v1.pdf?

Setup do desafio: https://bymateus.notion.site/Software-Setup-b3f9eecaa44946b0a59bfc81c0adb44e

Site do Robôcin: https://robocin.com.br/

## Informações sobre os arquivos:

- O arquivo `Software Setup.html` é um arquivo que mostra o setup do desafio.
- O arquivo `video_completando_o_desafio_DM.mkv` é um vídeo mostrando o desafio sendo completado.

### Na pasta `Arquivos Python`:

- O arquivo `decolar.py` faz com que o drone decole a 0.8 de altura.
- O arquivo `pousar.py` faz com que o drone pouse na superfície.
- O arquivo `movimento1.py` faz com que o drone se movimente, se o drone estiver sobrevoando o centro do quadrado da seletiva, ele vai para a borda vermelha do quadrado.
- O arquivo `movimento2.py` faz com que o drone se movimente, se o drone estiver sobrevoando o ponto de partida do desafio, ele vai para o centro do quadrado.
- O arquivo `movimentocores.py` faz com que o drone se movimente baseado nas cores que a câmera abaixo dele está captando, e ele sempre vai pousar o drone depois que ver uma cor verde após ter visto uma cor vermelha.
- O arquivo `movimentocoresreserva.py` é uma versão do arquivo `movimentocores.py`, a diferença é que este arquivo reserva não interage com a cor branca(este arquivo pode estar desatualizado em comparação com o `movimentocores.py`).

### Na pasta `Informações sobre o projeto`:

- Os arquivos `edital-ps2023-v1.pdf` e `projeto-ps2023-drones-v1.pdf` são sobre o processo seletivo e os desafios.
- O arquivo `quadrado_seletiva.world` é o ambiente em que vai acontecer o desafio de decisão e movimentação de drones, ele deve ser carregado pelo simulador 3D após o setup do desafio.

## Instruções para o desafio:

1. Fazer o setup do desafio.

2. O arquivo do ambiente 3D que vai acontecer o desafio é o `quadrado_seletiva.world`. O arquivo deve ser carregado no simulador 3D.

3. Rodar o arquivo `decolar.py` e esperar o drone estabilizar-se em uma altura. 

4. Rodar o arquivo `movimentocores.py` e esperar o drone pousar no ponto de partida do desafio.

### INÍCIO DO DESAFIO:

5. Rodar o arquivo `decolar.py` e esperar o drone estabilizar-se em uma altura.

6. Rodar o arquivo `movimentocores.py` novamente e esperar o drone realizar a trajetória para completar o desafio e então ele pousará no final automaticamente.
