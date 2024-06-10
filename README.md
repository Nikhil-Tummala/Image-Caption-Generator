# Image Caption Generator

This project uses a Convolutional Neural Network (VGG16) and a Long Short-Term Memory (LSTM) network to generate captions for images. The generated captions are then converted to audio output using a text-to-speech module.

## Overview

The Image Caption Generator project leverages deep learning techniques to analyze an image and generate a descriptive caption. The model architecture includes:
- **VGG16**: A pre-trained convolutional neural network for image feature extraction.
- **LSTM**: A type of recurrent neural network used for generating sequences, in this case, text captions.
- **Text-to-Speech**: Converts the generated text captions to audio output.

## Features

- Image upload via a web interface.
- Automatic generation of image captions.
- Conversion of text captions to audio.
- User-friendly Streamlit app for easy interaction.

## Usage

1. **Run the Streamlit app:**
   - Open your browser and navigate to the local Streamlit app URL (usually `http://localhost:8501`).
   - Use the file uploader to upload an image for caption generation.
   - After uploading the image, the app will display the generated caption and provide an audio playback option.

## File Descriptions

- `app.py`: Main file to run the Streamlit app.
- `caption_generator.py`: Contains the code for generating captions using VGG16 and LSTM.
- `text_to_speech.py`: Module to convert text to speech.
- `features.pkl`: Serialized features for the model.
- `model1.h5`: Pre-trained model file.
- `token.pkl`: Tokenizer file.

## Dataset
The dataset used for training and evaluation can be found [here](https://www.kaggle.com/datasets/srbhshinde/flickr8k-sau).

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.


## Acknowledgements

- The VGG16 model for image feature extraction.
- The Streamlit team for the amazing web app framework.
- TensorFlow and Keras for providing the deep learning tools.

---

Feel free to explore, use, and contribute to this project. Happy coding!
