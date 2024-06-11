import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from tensorflow.keras.applications.vgg16 import VGG16,preprocess_input
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Model,load_model
from tensorflow.keras.utils import to_categorical,plot_model
from tensorflow.keras.layers import Input,Dense,LSTM,Embedding,Dropout,add
import pickle
import pyttsx3

def generate_audio(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)  

    # Set the voice (optional)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) 
    engine.say(text)
    engine.runAndWait()



def idx_to_word(integer,tokenizer):
    for word,index in tokenizer.word_index.items():
        if index==integer:
            return word
    return None

def prediction(model,image,tokenizer,max_caption_len):
    in_text = 'start'
    for i in range(max_caption_len):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence],max_caption_len)
        yhat = model.predict([image,sequence],verbose=0)
        yhat = np.argmax(yhat)
        word = idx_to_word(yhat,tokenizer)
        if word is None:
            break
        in_text+=' '+ word
        if word=='end':
            break
    return in_text

def externel_caption_generate(image_name):
    img_path = image_name
    
    img = load_img(img_path,target_size=(224,224))
    #img.show()
    img = img_to_array(img)
    img = img.reshape((1,img.shape[0],img.shape[1],img.shape[2]))
    img = preprocess_input(img)
    modelvgg = load_model("model1.h5")
    model=VGG16()
    fe = Model(inputs=model.input, outputs=model.layers[-2].output)
    ext_feature = fe.predict(img, verbose=0)
    tokenizer=pickle.load(open("token.pkl","rb"))
    max_caption_len=34
    y_pred = prediction(modelvgg,ext_feature,tokenizer,max_caption_len)

    return y_pred[6:-4]

def main():
    st.title("Image Caption Generator using Deep Learning")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:

        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

        caption = externel_caption_generate(uploaded_file)
        st.write("Description Of Image:", caption)

        generate_audio(caption)
        
        

if __name__ == "__main__":
    main()



























