# [PENALTY SHOOTOUT GAME](https://penalty-shootout-game-8766b5475b75.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/RoBizMan/penalty-shootout-game)](https://github.com/RoBizMan/penalty-shootout-game/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/RoBizMan/penalty-shootout-game)](https://github.com/RoBizMan/penalty-shootout-game/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/RoBizMan/penalty-shootout-game)](https://github.com/RoBizMan/penalty-shootout-game)

### Introduction

Experience the excitement of a realistic penalty shoot-out game from your terminal with our interactive game. This project aims to design an immersive experience that allows users to engage in a simulated penalty shoot-out, making strategic decisions just like in an actual game. The game was created with Python, highlighting the language’s flexibility and strength. This is part of the third portfolio project of the Code Institute course.

#### Target Audience ⁤

The primary focus of the target audience is football enthusiasts, gamers, and anyone intrigued by interactive command-line games. Whether you are a seasoned football fan wanting to simulate the thrill of a penalty shoot-out, a casual gamer looking for a quick and fun distraction, or a Python learner interested in seeing what the language can do, this game is for you.

#### Value Proposition ⁤

Immerse yourself in penalty shoot-outs from the comfort of your desk. The game goes beyond mere victories or defeats. It is about the path you take and the choices you make. It combines strategy and chance, recreating a real penalty shoot-out's unpredictable nature and high stakes. Each decision you make, whether shooting or guarding the goal, can alter the game. The game is designed to be interactive and enjoyable, regardless of your football knowledge or gaming proficiency.

![screenshot](documentation/amiresponsive.png)

Source: [amiresponsive](https://ui.dev/amiresponsive?url=https://penalty-shootout-game-8766b5475b75.herokuapp.com)

## UX

In this project, I follow the Five Planes of User Experience model invented by Jesse James Garrett.

### Five Planes of User Experience

This model aids in transforming from abstract ideas, such as creating objectives of the project and identifying the user needs, to concrete concepts, such as assembling visual elements together to produce the visual design of the idea to meet the project's objectives and users' needs.

#### The Strategy Plane

This project centred around creating a captivating command-line game that mimics the experience of a football penalty shootout. This game was designed to entertain players, challenge their decision-making abilities, and showcase Python’s development potential.

#### The Scope Plane

The game was designed to incorporate essential elements of a penalty shootout. The included elements are the coin toss for determining who goes first, choosing the target area, deciding which area to defend, and calculating and displaying scores. The game was created to be replayable, offering unique outcomes in every playthrough.

##### Content requirements:
- Clear and concise guidelines for playing, including shooting and defending.
- The latest game status, including the score and whose turn it is.
- Instant feedback on the result of each turn, like whether a shot was successful or saved.

##### Functionality requirements:
- Players can input their decisions in the game, whether it is selecting a target area for a shot or choosing an area to defend.
- The game must correctly execute the penalty shoot-out rules, with the user and computer opponent taking turns.
- The game should have replayability, allowing users to play again without restarting the program.

#### The Structure Plane

Please refer to the [Data Model](#DataModel) section for more detailed data model.

#### The Skeleton Plane

The game’s interface is text-based. Information is presented to the user in a clear and organised manner. The purpose of user input prompts is to be straightforward and clear. The implementation of error handling helps direct the user to valid inputs.

#### The Surface Plane

[Click here to view the live site.](https://penalty-shootout-game-8766b5475b75.herokuapp.com/)

## User Stories

### New Site Users

- As a new site user, I would like to understand how to play the game so I can start playing without confusion.
- As a new site user, I would like to get immediate feedback on my actions to understand the consequences of my decisions in the game.
- As a new site user, I would like to see my current score and progress in the game to keep track of my progress.

### Returning Site Users

- As a returning site user, I would like to be able to start a new game quickly so that I can jump back into the action without unnecessary delays.
- As a returning site user, I would like to replay the game with the same consistent experience so that I can continue to enjoy it.

## Features

### Existing Features

- **Main Menu**

When the file is loaded, this is the first page that features the ASCII image of Penalty Shootout with instructions for the game. Ultimately, the game asks the player to input their name before starting. Also, it displays the error handling message to guide the player in inputting the correct one.

| Start | End |
| - | - |
| ![screenshot](documentation/feature1start.png) | ![screenshot](documentation/feature1end.png) |
| ![screenshot](documentation/feature1error.png) | - |

- **Coin Toss**

The coin toss allows the game to determine who should take the penalty kick first. It contains the coin that gives the player a head or a tail. Once chosen, the game will display the outcome of the coin toss with a green or red background to tell if you have won or lost the coin toss. Also, it displays the error handling message to guide the player in inputting the correct one.

| Start | End |
| - | - |
| ![screenshot](documentation/feature2start.png) | ![screenshot](documentation/feature2enda.png) ![screenshot](documentation/feature2endb.png)|
| ![screenshot](documentation/feature2errora.png) | ![screenshot](documentation/feature2errorb.png) |

- **Penalty Shootout game**

The penalty shootout game starts with either the player or the opponent taking the first penalty kick based on the outcome of the coin toss result. The game displays the ASCII image of the goalpost guiding the player of a target area to save or to score depending on their turn. It will then display whether the player scores as a penalty kicker or save as a goalkeeper. Also, it shows the error handling message to guide the player in inputting the correct one.

| Start | End |
| - | - |
| ![screenshot](documentation/feature3starta.png) | ![screenshot](documentation/feature3enda.png) ![screenshot](documentation/feature3endb.png)|
| ![screenshot](documentation/feature3startb.png) | ![screenshot](documentation/feature3endc.png) ![screenshot](documentation/feature3endd.png) |
| ![screenshot](documentation/feature3errora.png) | ![screenshot](documentation/feature3errorb.png) |

- **Penalty Shootout result**

Whoever scores 5 goals within 10 turns or has a +1 goal advantage with more than 10 turns wins the game. The result will be displayed whether the player wins the game or not. Finally, the player will be asked whether to restart the game or exit the game. Also, it shows the error handling message to guide the player in inputting the correct one.

| Start | End |
| - | - |
| ![screenshot](documentation/feature4starta.png) | ![screenshot](documentation/feature4enda.png) ![screenshot](documentation/feature4endb.png)|
| ![screenshot](documentation/feature4startb.png) | ![screenshot](documentation/feature4endc.png) ![screenshot](documentation/feature4endd.png) |
| ![screenshot](documentation/feature4error.png) | - |

### Future Features

- Realistic team names imported from the real-world football data.
- Offers the player to play the knock-out game where the player wins the penalty shootout and is advanced to the next round from 1/16 to the final.

## Tools & Technologies Used

- [![Markdown Builder](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://tim.2bn.dev/markdown-builder) used to generate README and TESTING templates.
- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [![GitHub](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.
- [![Gitpod](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) used as a cloud-based IDE for development.
- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.
- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for hosting the deployed back-end site.
- [![ChatGPT](https://img.shields.io/badge/ChatGPT-grey?logo=chromatic&logoColor=75A99C)](https://chat.openai.com) used to help debug, troubleshoot, and explain things.
- [MyDraw](https://www.mydraw.com/) used to create a flowchart.
- [CI Python Linter](https://pep8ci.herokuapp.com/#) used to maintain high quality of Python programming.

