# RobocinSP-2023-Drones-DM
### Robôcin CIN UFPE 2023 Selection Process - Drones - Decision and Movement

This repository is for storage and submission of the drone decision and movement challenge for Robôcin's 2023 selection process. Robôcin is a research group at the Center for Informatics of the Federal University of Pernambuco that utilizes robotics to solve problems. The chosen category for the selection process is Drones, and the subcategory is Decision and Movement.

The objective of the challenge is to create one or more codes that make a drone from a 3D simulation traverse the perimeter of a square that contains 4 colors. After traversing all the colors, the drone should land. The starting point of the drone is the intersection of the green part of the perimeter with the red part of the perimeter.

The project was approved and praised by the Robôcin team, and I moved on to the next phase of the selection process.

## Links:

Selection process announcement: https://robocin.com.br/archives/ps-2023/edital-ps2023-v1.pdf?

Drones challenge PDF: https://robocin.com.br/archives/ps-2023/projeto-ps2023-drones-v1.pdf?

Challenge setup: https://bymateus.notion.site/Software-Setup-b3f9eecaa44946b0a59bfc81c0adb44e

Robôcin website: https://robocin.com.br/

UFPE website: https://www.ufpe.br/

CIN website: https://portal.cin.ufpe.br/

Official Python website: https://www.python.org

## Information about important files:

- The `quadrado_seletiva.world` file is the environment where the drone decision and movement challenge will take place. It should be loaded by the 3D simulator after the challenge setup.
- The `video_completando_o_desafio_DM.mkv` file is a video showing the challenge being completed.

### In the `Arquivos Python` directory:

- The `decolar.py` file makes the drone take off to a height of 0.8.
- The `pousar.py` file makes the drone land on the surface.
- The `movimento1.py` file makes the drone move. If the drone is hovering over the center of the selection square, it will move to the red edge of the square.
- The `movimento2.py` file makes the drone move. If the drone is hovering over the starting point of the challenge, it will move to the center of the square.
- The `movimentocores.py` file makes the drone move based on the colors captured by the camera beneath it. It will always land the drone after seeing a green color following a red color.
- The `movimentocoresreserva.py` file is a version of the `movimentocores.py` file, with the difference that this reserve file does not interact with the color white (this file may be outdated compared to `movimentocores.py`).

### In the `Informações sobre o projeto` directory:

- The `edital-ps2023-v1.pdf` and `projeto-ps2023-drones-v1.pdf` files contain information about the selection process and the challenges.
- The `Software Setup.html` file shows the challenge setup.

## Challenge instructions:

1. Set up the challenge.

2. The 3D environment file for the challenge is `quadrado_seletiva.world`. The file should be loaded in the 3D simulator.

3. Run the `decolar.py` file and wait for the drone to stabilize at a certain height.

4. Run the `movimentocores.py` file and wait for the drone to land at the starting point of the challenge.

### CHALLENGE START:

5. Run the `decolar.py` file and wait for the drone to stabilize at a certain height.

6. Run the `movimentocores.py` file again and wait for the drone to complete the trajectory to finish the challenge. It will automatically land at the end.

