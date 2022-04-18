import streamlit as st
from tldr_paragraph import summarizer

# favicon and page configs
favicon = './assets/icon.jpeg'
st.set_page_config(page_title='Paragraph Summarizer', page_icon = favicon, initial_sidebar_state = 'expanded')
# favicon being an object of the same kind as the one you should provide st.image() with (ie. a PIL array for example) or a string (url or local file path)
st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 140px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 140px;
        margin-left: -140px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


text = st.text_area("Enter your paragraph here!")



if st.button("Summarize"):
    with st.spinner('Running the {} text summarization model...'.format('Pegasus')):
        output = str(summarizer(text)[0])
    st.success(output)
    st.balloons()
