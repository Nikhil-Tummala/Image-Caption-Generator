import streamlit as st
from PIL import Image
from caption_generator import externel_caption_generate
from text_to_speech import generate_audio  

def generate_audio_in_memory(caption):
    audio_data = generate_audio(caption)
    st.audio(audio_data, format="audio/wav", start_time=0)

def main():
    st.title("Image Caption Generator using Deep Learning")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:

        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)
        #filename = uploaded_file.name
        #print(type(filename))
        
        caption = externel_caption_generate(uploaded_file)
        st.write("Description Of Image:", caption)

        generate_audio_in_memory(caption)
        if st.button("Play Audio"):
            generate_audio_in_memory(caption)
        

if __name__ == "__main__":
    main()



























