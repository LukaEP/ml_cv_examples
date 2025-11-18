# Breakout
This projects consists in playing the [Breakout game](https://en.wikipedia.org/wiki/Breakout_(video_game)) using computer vision.

## Explanation
Computer vision techniques will be used to find an orange object in a frame. With its position, it is possible to move the Breakout platform according it.

### Finding the Orange
In order to find the orange object, it is needed to filter the frame with a mask, that contains a range of the desired color (in this case, orange). All the are explained in [find_orange.ipynb](find_orange.ipynb).

### Playing
After finding the orange object, and its position, the frame was divide into three areas. And, depending on which area the object is found, the Breakout platform can move to the left, right or stay still. All steps to play the game are detailed in [breakout.py](breakout.py).

## Result

<video controls width="640" poster="media/orange_me.jpg">
	<source src="media/playing_breakout_with_computer_vision.mp4" type="video/mp4">
	Your browser does not support the video tag. You can download the video here: [playing_breakout_with_computer_vision.mp4](media/playing_breakout_with_computer_vision.mp4)
</video>
