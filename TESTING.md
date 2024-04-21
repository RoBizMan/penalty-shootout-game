# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| run.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/penalty-shootout-game/main/run.py) | ![screenshot](documentation/pythonvalidation.png) | All clear, no errors found |

## Browser Compatibility

I have tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/chrome.png) | Works as expected |
| Firefox | ![screenshot](documentation/firefox.png) | Works as expected |
| Edge | ![screenshot](documentation/edge.png) | Works as expected |
| Ulaa | ![screenshot](documentation/ulaa.png) | Works as expected |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Main Menu | | | | | |
| | When a player inputs their name using letter and less than 40 characters, it is expected to go to the coin toss and display the welcome message with the name of the player. | Tested the name input by typing Robert. | The feature behaved as expected, and it did went to the coin toss and displayed the player's name beside the welcome message. | Test concluded and passed | ![screenshot](documentation/defensive1a.png) |
| | When the player inputs their name using letter and exceeds 40 characters, it is expected to display the error and tell a player to input their name again but not to exceed 40 characters. | Tested the name input by typing letters randomly that exceeded 40 characters limit. | The feature behaved as expected, and it handled the error well. | Test concluded and passed | ![screenshot](documentation/defensive1b.png) |
| | When the player inputs their name other than alphabetic letters, it is expected to display the error and tell a player to input their name using alphabetic letters. | Tested the name input by randomly typing @, Rob2, 21, Rob!, `space`, `space`Rob and blank (just press `Enter` button). | The feature behaved as expected, and it handled the error well. | Test concluded and passed | ![screenshot](documentation/defensive1ca.png) ![screenshot](documentation/defensive1cb.png) |