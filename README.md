# Chrome Dino Automation
- This project automates the Chrome Dino game.
- It is a basic Robotic Process Automation (RPA) project, which detects change in pixel color in a specific location to make the dinosaur jump or duck accordingly.
- It uses simple image processing to detect cacti and pterodactyls.
- I'm using a program to automate the game so it might violate Google's Terms of Services, I don't have any idea regarding this.
- It even broke my record of 832 by 1044.

## Video
- The following video shows the game play of this program.
- I made this video using my phone as a proof that no one is pressing any key.
- Sorry for the poor video quality.

https://github.com/Harshit1234G/Chrome-Dino-Automation/assets/119939567/a1d1a67a-30b2-4cf3-a014-4bd9af7f3629


## Technologies\Modules used
1. **pyautogui:** For pressing `up` & `down` keys.
2. **PIL:** For taking screenshot and using that data for further image processing.
3. **time:** For a 3 second sleep, so that user get the time to switch the programming window to Chrome Dino tab.

## Working
- Initially, the program is in a sleep of 3 seconds so that user can shift to Chrome Dino tab. After that it'll press the up key to start the game.
- Then it countinously takes screenshots (the screen pixel values in greyscale) in the background and passess that data to `isColliding()` function.
- `isColliding()` funciton checks in those two areas that the pixel value is equal to 172 or not.
- If cactus area has a pixel value of 172 then it returns 1, if bird (pterodectyl) area has a pixel value of 172 then it return 2, else None.
- For `1` it presses `up` key for `2` it holds `down` key for 0.3 seconds.

![This box detects bird](https://github.com/Harshit1234G/Chrome-Dino-Automation/assets/119939567/c0b3ad97-97be-4250-b822-8419ffef70e4)

You can also see these boxes by uncommenting the code in `if __name__ == "__main__"`. I found those boxes values using that code by hit and trial approach, I'm using the values that most suits for me.

## Usage
- Open the Chrome Dino game, there is no need of going offline for this you can also open the game by searching `chrome://dino` in the browser.
- Run the script.
- Switch to the Chrome Dino game tab.
- Enjoy the show!

## Note
- These coordinates or boxes that I used will only work for my laptop, they won't work for any other monitor or screen.
- Use the hit and trial approach and commented code to find the values that most suits you.
