# Attendance Analyzer

Attendance Analyzer is a Python hobby project aimed at helping KTU (Kerala Technological University) students monitor their attendance and ensure compliance with the required 75% threshold.

## Overview

The project includes several components:

- **`attendance.py`**: This Python script provides functions to calculate attendance percentage and determine the number of classes required for safe attendance.
- **`index.html`**: An HTML file with a form-based interface to calculate attendance percentage and receive safe attendance advice.
- **`script.js`**: JavaScript file handling form submission and displaying the calculated attendance details.
- **`style.css`**: CSS file providing styling for the HTML form and result display.

## Dataset
The project uses data provided by KTU, containing details such as class dates, attendance records, and total classes conducted.


## Features

- Calculate attendance percentage.
- Determine the number of classes required for safe attendance.
- Interactive web-based interface.
- Lightweight and easy-to-use.

## Usage

To utilize the Attendance Analyzer:
1. Run the Python script or open the web interface.
2. Input the total number of classes and the number attended.
3. Receive attendance percentage and safe attendance advice.

## Methodology
- **Data Processing:** The dataset undergoes preprocessing to handle missing values and calculate attendance percentages.
- **Analysis:** Using Python scripts and a web interface, the project calculates attendance percentages and advises on safe attendance thresholds.
- **Interactive Interface:** The web interface allows users to input their attendance data and receive real-time analysis.


### Python Script (`attendance.py`)

You can use the `attendance.py` script to calculate attendance percentage and determine safe attendance thresholds. Run the script and follow the prompts to input the total number of classes and the number of classes attended.

## Web Interface (index.html)

Open index.html in a web browser to access the web-based attendance calculator. Input the total number of classes and the number of classes attended, then click the "Calculate" button to see the attendance details.

## Installation

There's no installation required for this project. Simply download or clone the repository to your local machine and run the Python script or open the HTML file in a web browser.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on GitHub or submit a pull request.

## Acknowledgements

Special thanks to KTU for inspiring this project and providing guidelines on attendance requirements.

## Disclaimer

This project is developed for educational and hobby purposes only. It should not be used for official attendance calculations without proper validation and verification.

## Author
- [Your Name](https://github.com/cmshebeeb)

## Sample Input (Python Script)
- Total number of classes: 20
- Number of classes attended: 14

## Sample Output (Python Script)
- Attendance percentage: 70.0%
- For safe attendance, you need to attend the next 6 days.

## Sample Input (Web Interface)
- Total number of classes: 20
- Number of classes attended: 14

## Sample Output (Web Interface)
- Attendance percentage: 70.0%
- For safe attendance, you need to attend the next 6 days.

```bash
python attendance.py

