# ESRGAN Image Upscaling

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 16.2.16.
With help of https://github.com/tensorflow/docs/blob/master/site/en/hub/tutorials/image_enhancing.ipynb 
https://www.tensorflow.org/hub/tutorials/image_enhancing
For ML Model go to https://www.kaggle.com/models/kaggle/esrgan-tf2/

## Overview

This project allows users to upload an image, which is then processed using the ESRGAN (Enhanced Super-Resolution Generative Adversarial Network) model to upscale the image and enhance its resolution. The application features a cool blueish warm aesthetic with a modern, glassy interface.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.


## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via a platform of your choice. To use this command, you need to first add a package that implements end-to-end testing capabilities.

## Installation

1. **Backend (Flask)**
   - Install the required Python packages:
     ```bash
     pip install flask flask-cors tensorflow pillow
     ```

   - Ensure the ESRGAN model is properly placed:
     ```
     C:\Users\esg\Python\code\
         ├── saved_model.pb
         └── variables\
             ├── variables.data-00000-of-00001
             └── variables.index
     ```

   - Run the Flask server:
     ```bash
     python app.py
     ```

2. **Frontend (Angular)**
   - Navigate to the Angular project directory and install dependencies:
     ```bash
     npm install
     ```

   - Start the Angular development server:
     ```bash
     ng serve
     ```
3. **Backend (Flask)**
      -Navigate to python folder
       ```bash
       python app.py
   
## Usage

1. Open the application in your browser at `http://localhost:4200/`.
2. Upload an image by clicking on the "Choose File" button.
3. Click "Upload" to send the image to the backend for processing.
4. Once processed, a "Download Processed Image" button will appear to download the upscaled image.

## Further help

To get more help on the Angular CLI, use `ng help` or go check out the [Angular CLI Overview and Command Reference](https://angular.io/cli) page.
