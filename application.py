from ocr import OCRProcessor
import streamlit as st 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit.components.v1 as components
from PIL import Image
from ctransformers import AutoModelForCausalLM
import re
# from langchain.llms import CTransformers

# # Model initialization
# local_llm = r"D:\\LLM_Models\\codellama-13b-instruct.Q5_K_M.gguf"

# llm = CTransformers(
#     model=local_llm,
#     model_type="llama"
# )

from langchain_community.llms import Ollama
llm = Ollama(base_url = 'http://localhost:11434',model = 'codellama')


# Function to process OCR
def ocr_func(img):
    ocr_processor = OCRProcessor()
    image_path = img
    layout = ocr_processor.extract_layout(image_path)
    return layout

# Custom prompt template for HTML generation
custom_prompt_template = """
        Use the following layout of a website design, including including text and their coordinates of four outer vertices. 
        Make an HTML modern sans-serif website that reflects these elements and decide which 
        CSS can be used to match their relative positions, try to use proper layout tags to match
         their font size and relative placement based on their coordinates. 
         Use <ul> and <li> if the elements look like a menu list. 
         Smartly use function tags like <button> <input> if their names look like that.
         Your design should be prior to the coordinates, 
         then you should also use some imagination for the layout and CSS from common web design principles.
         Remember, don't use absolute coordinates in your HTML source code. 
         Generate only source code file, no description: {layout}.\n
"""

# Function to separate HTML body from additional content (comments, CSS, etc.)
def separate_html_content(html_code):
    body_match = re.search(r"(<body.*?>.*?</body>)", html_code, re.DOTALL)
    
    if body_match:
        body_content = body_match.group(0)  # Extract the body content
        other_content = html_code.replace(body_content, "")  # Remaining content
        return body_content, other_content
    return html_code, ""  # If no separation, treat all as body content

# Function for HTML generation
def html_generation(layout):
    prompt = PromptTemplate(
        template=custom_prompt_template,
        input_variables=["layout"]
    )
    chain = LLMChain(prompt=prompt, llm=llm)
    output = chain.run(layout=layout)
    return output

# Custom prompt template for general code generation
code_prompt_template = """Given an input question, first understand the requirements then generate the appropriate code (Python function, SQL query, etc.):
{use_case_description}\n
"""

# Function for general code generation
def generate_code(use_case_description):
    prompt = PromptTemplate(
        template=code_prompt_template,
        input_variables=["use_case_description"]
    )
    chain = LLMChain(prompt=prompt, llm=llm)
    output = chain.run(use_case_description=use_case_description)
    return output

# Streamlit setup
st.set_page_config(
    page_title="CodeBuddy 🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for dark theme compatibility
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
        html, body, [class*="css"] {
            font-family: 'Roboto', sans-serif;
        }
        h1, h2, h3 {
            color: #f9f9f9;
        }
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)

# Main title and subtitle
st.markdown("<h1 style='text-align: center;'>CodeBuddy 🤖: Your Open Source Assistant </h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #a8a8a8;'>Transform Your Vision into Reality: Generate Customized Code Using Advanced AI Techniques! 💡💻 </h3>", unsafe_allow_html=True)

# Image and HTML layout in columns
col1, col2 = st.columns([0.45, 0.55], gap='medium')

if "html" not in st.session_state:
    st.session_state.html = ""
if "code" not in st.session_state:
    st.session_state.code = ""
if "image" not in st.session_state:
    st.session_state.image = ''

def image_run():
    html_code = ""
    layout = ocr_func(st.session_state.image)
    if layout != []:
        html_code = html_generation(layout)
    st.session_state.html = html_code
    st.session_state.image = st.session_state.image

with col1:
    st.markdown("<h2 style='text-align: center; color: #f0f0f0;'>1. Upload Your Design</h2>", unsafe_allow_html=True)

    # File uploader for images
    uploaded_file = st.file_uploader("Choose an image file (jpg, png, jpeg)", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image_filename = uploaded_file.name
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True, channels="RGB")
        
        # Save the uploaded image
        image = Image.open(uploaded_file)
        image.save(image_filename)
        st.session_state.image = image_filename
        
        # Centering the button
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.button("Generate HTML", on_click=lambda: image_run())
        st.markdown("</div>", unsafe_allow_html=True)

    # New section for user query
    st.markdown("<h2 style='text-align: center; color: #f0f0f0;'>2. Outline Your Use Case or Input </h2>", unsafe_allow_html=True)
    use_case = st.text_area("Describe your use case/query here:")

    if st.button("Generate Code"):
        if use_case:
            st.session_state.code = generate_code(use_case)
        else:
            st.error("Please enter a use case or query.")

with col2:
    st.markdown("<h2 style='text-align: center; color: #f0f0f0;'>Generated Code</h2>", unsafe_allow_html=True)

    if st.session_state.html != '':
        # Separate the body content and additional content
        body_content, other_content = separate_html_content(st.session_state.html)

        # Display the source code
        with st.expander("📄 View Source Code", expanded=True):
            st.code(st.session_state.html, language="html")

        # Render the main HTML UI
        with st.container():
            components.html(body_content, height=600, scrolling=True)

        # Display any additional content (like CSS or comments) in a separate text area
        if other_content.strip():
            st.markdown("<h4 style='color: white;'>Additional Content:</h4>", unsafe_allow_html=True)
            st.text_area("Additional Content", other_content, height=200)

    if st.session_state.code != '':
        with st.expander("📜 Generated Code", expanded=True):
            st.code(st.session_state.code, language="python")  # Change language as needed
        # Optionally, add a download button for generated code
        st.download_button(
            label="Download Generated Code",
            data=st.session_state.code,
            file_name='generated_code.txt',  # Change extension as needed
            mime='text/plain',
            key='download_code'
        )
