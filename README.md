# AI Image Comparator

This repository contains a Python application for comparing images using various AI models with the help of [Gradio](https://www.gradio.app/) for education and research purpose only.

## Table of Contents

- [Description](#description)
- [Usage](#usage)
- [License](#license)
- [Disclaimer](#disclaimer)

## Description

The AI Image Comparator is a Python application that uses several AI models to generate images based on a given prompt. It leverages Hugging Face's inference API for text-to-image generation. Gradio is used to create a user interface that allows users to enter a prompt and visualize the outputs from different AI models side by side.

## Usage

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/manan-garg/AI-image-comparator.git
   cd AI-image-comparator
   ```

2. Requirements:

   To run this application, you need to have the following installed:
   - IPython
   - requests
   - gradio
   
   You can install these dependencies using `pip` with the provided `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```
   The application will launch, and you can interact with it using your web browser. Enter the [Hugging Face API key](https://huggingface.co/docs/api-inference/quicktour#get-your-api-token)  and a prompt and click the "Submit" button to generate images using different AI models. Explore and compare the generated images in the Gradio user interface.

## License
This project is licensed under the MIT License.

## Disclaimer
- The AI Image Comparator tool is a demo project for education and research purpose only.
- Users should not use it for any other purpose.
