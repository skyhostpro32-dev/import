import streamlit as st
from PIL import Image
from rembg import remove

st.title("🧍 Person Remover App")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    input_image = Image.open(uploaded_file)

    st.image(input_image, caption="Original Image", use_column_width=True)

    if st.button("Remove Person"):
        with st.spinner("Processing..."):
            output_image = remove(input_image)

        st.image(output_image, caption="Person Removed", use_column_width=True)

        # Download button
        st.download_button(
            label="Download Result",
            data=output_image.tobytes(),
            file_name="output.png",
            mime="image/png"
        )