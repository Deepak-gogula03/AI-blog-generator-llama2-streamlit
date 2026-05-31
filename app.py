import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import CTransformers

# Function to get response from Llama Model

def get_llama_response(input_text, no_words, blog_style):

    llm = CTransformers(
        model=r"C:\Users\DELL\Desktop\Meta\Llama-2-7B-Chat-q4_1.gguf",
        model_type="llama",
        config={
            "max_new_tokens": int(no_words),
            "temperature": 0.7,
            "context_length": 4096
        }
    )

    template = """
    You are an expert blog writer.

    Write a professional blog for {blog_style} on the topic:
    "{input_text}"

    The blog should be approximately {no_words} words.

    Include:
    - Introduction
    - Main Content
    - Real-world Applications
    - Conclusion

    Blog:
    """

    prompt = PromptTemplate(
        input_variables=["input_text", "blog_style", "no_words"],
        template=template
    )

    final_prompt = prompt.format(
        input_text=input_text,
        blog_style=blog_style,
        no_words=no_words
    )

    response = llm.invoke(final_prompt)

    return response


# Streamlit UI

st.set_page_config(
    page_title="AI Blog Generator",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖AI Blog Generator using Llama 2")

input_text = st.text_input("Enter Blog Topic")

col1, col2 = st.columns(2)

with col1:
    no_words = st.number_input(
        "Number of Words",
        min_value=100,
        max_value=2000,
        value=500
    )

with col2:
    blog_style = st.selectbox(
        "Writing the blog for",
        ("Researchers", "Data Scientists", "Common People")
    )

submit = st.button("Generate Blog")

if submit:

    if input_text == "":
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Generating Blog..."):
            response = get_llama_response(
                input_text,
                no_words,
                blog_style
            )

        st.success("Blog Generated Successfully!")
        st.write(response)
