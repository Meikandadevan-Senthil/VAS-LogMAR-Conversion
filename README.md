# Visual Acuity Conversion Web Application

## Overview

This Flask web application allows users to upload Excel files containing visual acuity data and convert the data between different formats. The supported conversions are:
- Decimal visual acuity to LogMAR
- LogMAR to Visual Analog Scale (VAS)

## Features

- Upload Excel files (`.xlsx` or `.xls`).
- Choose the input format (Decimal or LogMAR).
- Specify which columns to convert.
- Download the converted file with additional columns for LogMAR and/or VAS.

## Prerequisites

- Python 3.6 or later
- Flask
- Pandas
- Numpy
- Openpyxl (for handling Excel files)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Meikandadevan-Senthil/VAS-LogMAR-Conversion.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd visual-acuity-conversion
   ```

3. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` is not present, you can install the dependencies manually:

   ```bash
   pip install flask pandas numpy openpyxl
   ```

## Usage

1. **Run the Flask application:**

   ```bash
   python convert.py
   ```

2. **Open your web browser and navigate to:**

   ```
   http://127.0.0.1:5000/
   ```

3. **Upload an Excel file:**

   - Select the input format (Decimal or LogMAR).
   - Enter the column names (comma-separated) to convert.
   - Choose the file to upload and click "Convert."

4. **Download the converted file:**

   - The file will be processed and a downloadable link will be provided.
   - The downloaded file will include the original data along with new columns for LogMAR and/or VAS.

## Conversion Functions

- **Decimal to LogMAR**: Converts decimal visual acuity values to LogMAR.
- **LogMAR to VAS**: Converts LogMAR visual acuity values to Visual Analog Scale (VAS).

## Troubleshooting

- **No file part**: Ensure the file is selected before submitting the form.
- **Missing columns in the dataset**: Verify that the column names entered match those in the Excel file.
- **Invalid file type**: Ensure you are uploading an Excel file with an `.xlsx` or `.xls` extension.
