## Head Worn Display Emulator for Research
This software facilitates the emulation of a head-worn display without the necessity of physical construction. It enables the user to modify various parameters by simply executing a single line of code, as opposed to constructing an actual device, which is particularly advantageous for research projects.

## Usage

To effectively use the software for head-worn display (HWD) emulation, there are a few important steps to follow:

- Ensure that the user's head is facing straight, with 0 degee roll and 0 degree yaw. This can be achieved by attaching a laser to a helmet worn by the user, which points at a photoresistor coded with Arduino. The laser must be in the given range to trigger the photoresistor.
- Perform an initial calibration to ensure that the user's head is at 0 roll and 0 yaw. This can be accomplished using computer vision software or Microsoft Kinect.
- Place the Arduino sensor 1.75 meters away from the user's eye radially, with an error margin of 0.8 degrees.
- Use a television to display the simulated HWD, placing it 2 meters away from the user. The current resolution should be set to that of an iPhone 12, although this may vary depending on the TV used.
By following these steps, researchers can effectively use the software to simulate a HWD without the need for physical construction, allowing for more efficient and flexible testing and development.

## File Stucture
- application.py: This file contains the Python Flask application code used for head-worn display emulation.
- static: This folder contains static files such as CSS and JavaScript used in the Flask application.
- templates: This folder contains the HTML templates used in the Flask application.
- arduino_code: This folder contains the Arduino code used for photoresistor and laser calibration.
- venv: This folder contains the Python virtual environment used for the Flask application.
- kinect_code: This folder contains the Microsoft Kinect code used for initial calibration.
- book.txt: This file contains the text used for the "Left Arrow" control in the software.
- github-images: This folder contains images used in the README.md file.
- README.md: This file provides information about the head-worn display emulator software, including usage instructions, setup instructions, controls, and the file structure of the parent directory.

## Setup
### Microsoft Kinect setup instructions:

- Download the Kinect for Windows SDK from the Microsoft website.
- Install the SDK on your computer.
- Connect the Kinect to your computer via USB.
- Ensure that the Kinect is recognized and working properly by testing it with the sample code provided in the SDK.
### Arduino setup instructions:

- Download the Arduino IDE from the Arduino website.
- Connect the Arduino board to your computer via USB.
- Open the Arduino IDE and select the appropriate board and port.
- Upload the code provided for the photoresistor and laser calibration to the Arduino board.
### Python Flask application setup instructions:

- Install Python on your computer if it is not already installed.
- Install the necessary Python packages by running the following command in the terminal: pip install flask pykinect2.
- Clone or download the code for the Flask application.
- Open the app.py file and modify the HOST_IP variable to match your computer's IP address.
- Run the Flask application by executing the app.py file in the terminal: python app.py.
### To run the code:

Ensure that the Microsoft Kinect and Arduino are properly set up and connected to your computer.
Start the Python Flask application by executing the app.py file in the terminal.
Navigate to http://localhost:5000/ in a web browser to access the Flask application.
Follow the instructions provided in the application to calibrate the laser and photoresistor and begin using the head-worn display emulation software.
By following these instructions, users can set up and run the necessary components to use the software effectively for head-worn display emulation.

## Controls

For the particular project we conducted, we aimed to test the comfort of reading at different angles. To achieve this, the software was designed to automatically hide the display whenever the user moved the laser outside of the sensor's range. We plan to publish our findings soon.

In terms of controls for the software, the following commands can be used:

- Left Arrow: Finds a random sentence (such as nursery rhymes) to display, allowing the user to test the software's functionality.
- D: Retrieves user data and displays it in the console.
- X: Changes to angle mode, allowing the user to place the mouse where they see optical combiners on the glass they are wearing.



Additionally, there are commands for overriding the Arduino:

- Spacebar: Shows the display.
- Spacebar + Enter: Hides the display.

## Conclusion
In conclusion, the Head Worn Display Emulator software provides a convenient solution for researchers who require head-worn display emulation without the need for physical construction. The software allows for the modification of various parameters with just a single line of code, enabling efficient and flexible testing and development. The setup instructions for the Microsoft Kinect, Arduino, and Python Flask application are provided, and the controls for the software are explained. By following the instructions provided, users can effectively set up and use the software for head-worn display emulation, providing a valuable tool for research projects.

<p align="center">
  <img src="/github-images/1.jpeg">
  <br>Complete Setup of Emulator
</p>

