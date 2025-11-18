# Breakout
This projects consists in playing the [Breakout game](https://en.wikipedia.org/wiki/Breakout_(video_game)) using computer vision.

## Explanation
Computer vision techniques will be used to find an orange object in a frame. With its position, it is possible to move the Breakout platform according it.

### Finding the Orange
In order to find the orange object, it is needed to filter the frame with a mask, that contains a range of the desired color (in this case, orange). All the are explained in [find_orange.ipynb](find_orange.ipynb).

### Playing
After finding the orange object, and its position, the frame was divide into three areas. And, depending on which area the object is found, the Breakout platform can move to the left, right or stay still. All steps to play the game are detailed in [breakout.py](breakout.py).

## Results
https://github.com/user-attachments/assets/5c81be27-590f-4815-bdd6-a5aa9248dbb2

