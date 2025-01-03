#### Unleash AI Power to Turn Designs and Ideas into Seamless, Ready-to-Use Code—From HTML to Python and Beyond!

# CodeBuddy 🤖: AI-Powered Code & HTML Generator


## Overview

**CodeBuddy** is an open-source AI-powered application designed to convert design layouts into HTML and generate custom code based on user queries. The application uses **OCR** to extract layout details from images and **language models** to generate code, whether it's HTML, Python, SQL, or any other programming language based on the use case provided by the user. 

The project is fully open-source and leverages **Langchain**, **EasyOCR**, **CodeLlama**, and **Streamlit** to offer an accessible and powerful tool for developers looking to automate their design-to-code or custom code generation workflows.


## Tech Stack Used
- **[Python](https://www.python.org/)** - Python forms the backbone of CodeBuddy, providing robust support for integration with various libraries and frameworks.
- **[EasyOCR](https://github.com/JaidedAI/EasyOCR)** - EasyOCR is used for optical character recognition (OCR). This library enables the extraction of textual content and layout from uploaded design images, converting visual information into structured data that can be processed further.
- **[Langchain](https://github.com/hwchase17/langchain)** - LangChain is a framework designed to simplify the creation of applications using large language models.
- **[Ollama](https://ollama.com/)** - It provides a simple API for creating, running, and managing models, as well as a library of pre-built models that can be easily used in a variety of applications.
- **[CodeLlama](https://ai.meta.com/blog/code-llama-large-language-model-coding/)** - Code Llama is a model for generating and discussing code, built on top of Llama 2. It’s designed to make workflows faster and efficient for developers and make it easier for people to learn how to code. It can generate both code and natural language about code. 
- **[Streamlit](https://streamlit.io/)** -Streamlit is the web framework used for building and hosting the user interface. It provides an interactive, easy-to-use platform where users can upload designs, enter queries, and download generated code. The entire UI is hosted on Streamlit, making it accessible and efficient for users.


## Getting Started

### Prerequisites
Before you begin, ensure you have the following installed:
- **Python 3.9+**
- **PIP** (Python package manager)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Ginga1402/Code_Design_with_GenAI
   
   ```

2. **Install the required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Local Model from Ollama**

   Download the CodeLlama model files and configure them according to the instructions.
   ```bash
   ollama pull codellama
   ```
    

5. **Run the Streamlit Application**
   ```bash
   streamlit run app.py
   ```

This will launch the application in your browser at `http://localhost:8501`.


## Usage

### 1. Upload Design to Generate HTML
- Upload an image containing a design layout (e.g., a screenshot or design mockup).
- The application will extract layout data using **EasyOCR** and generate a responsive HTML/CSS file based on the design elements.

### 2. Enter Use Case to Generate Code
- In the "Use Case" section, enter a description of the code you need (e.g., "Write a Python function to calculate the factorial of a number").
- The application will generate the corresponding code using **CodeLlama**.

### 3. Download Generated Code
- You can view the generated code (HTML, Python, SQL, etc.) and download it directly from the interface.

### 4. View Rendered HTML
- After uploading a design and generating HTML, the interface displays both the generated HTML code and the corresponding UI rendered in the browser.


## CodeBuddy User Interface Demo
A glimpse into CodeBuddy’s intuitive interface, showcasing the seamless conversion of designs into functional code.

#### 1. Home Screen 
![codebuddy3](https://github.com/user-attachments/assets/c93e70a0-a917-4cd2-a138-e43c1931af83)
#### 2. Code Generation
##### 1.Python 
![codebuddy4](https://github.com/user-attachments/assets/77a76df7-73d2-4f37-9309-62a775eae4e3)
##### 2. SQL
![383856939-aa03e8af-fec7-4bf7-8456-976ae905a967](https://github.com/user-attachments/assets/aa024867-fb52-44ff-8cfe-e9fa418c0597)
#### 3. UI Design[HTML]
![codebuddy2](https://github.com/user-attachments/assets/0a928171-716a-44e9-9277-d3007fd74026)


### 

## Contributing
Contributions are welcome! If you have suggestions or would like to enhance this project, please fork the repository and submit a pull request.



## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.


