## Inspiration
We took inspiration from the Theremin and wanted to recreate the instrument using motion detection and action detection in Python. We wanted to incorporate different loops and beats that could be played with hand actions to create an almost Garageband-esque experience allowing the user to become a DJ with nothing but their hands. We also wanted to add some funny memes to liven up people's moods.

## What it does
### Theremin
The app recreates the Theremin, by taking the relative x and y positions of the user's hand, and creates a chord based on the x position, and adjusts the volume based on the y position. This allows the user to change the pitch by moving their hand left and right, and adjust the volume by moving their hand up and down. The function creates a chord by combining 3 sine waves of different frequencies (The code for this can be found: [link](https://github.com/alex-silcock/bathhack23/blob/main/freq.py) ). 

### Playing sound through action detection
We also incorporated action detection to allow us to add extra sounds and notes when a specific action occurs, e.g. making a fist. This is done by using an LSTM (Long Short Term Memory) which takes in a series of 5 frames of which the action is performed. The LSTM then learns the action and in the live feed it can predict the user's action. When each action is detected a different sound is played. The code for training the model is in this .ipynb file: [link](https://github.com/alex-silcock/bathhack23/blob/main/hand_tracking.ipynb) 

## How we built it
We used OpenCV for web cam stream and then used the mediapipe holistic to allow for hand / posture tracking, which identified the locations of each ligament.
We then created a class to generate chords made out of sine waves (using pysinewave), which would take in a parameter of the x position of the hand. When the x position changes, the new chord is looked up for that x position and the sound smoothly transitions to the updated pitch / frequency.

For action detection we used pygame to output sounds on different channels

We also trained our own datasets for the action detection, by feeding the model videos of us doing each action from which it learnt and was able to predict what action it was in the live feed.

## Challenges we ran into
Some of the challenges we faced were:
1. Issues of having a video feed and music running at the same time - sequential processing of opening and running a .wav file and having a webcam stream lead to errors in the video feed and playing the sounds, so we used threads to solve this by creating and running a new thread when we wanted to play a sound after an action.

2. Creating nice sounding chords for the Theremin part. We struggled to find good chords until we discovered music theory and built chords based off that

## Accomplishments that we're proud of
1. Action detection performing with ~95% accuracy
2. Use of an LSTM
3. Solved lots of our problems efficiently and managed to have a working product
4. Having multiple components, sounds, running over each other using threads
5. Having the application run smoothly
6. Working with sine waves
7. Learnt music theory about creating chords, reading through how to create proper chords, converting frequencies to pitches and creating a continuous sine wave that smoothly transitions when the pitch is changed

## What we learned
1. A lot about action detection, LSTMs and creating our own datasets
2. How to run multiple components at the same time
3. The importance of efficient and fast coding
4. Pair programming is very useful

## What's next for Music fingers
- Potentially using a CNN for better action detection
- Using more training data to make the actions even more accurate
- Threading displaying the camera feed and process each frame to make the application smoother
