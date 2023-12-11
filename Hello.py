import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Resume Bot",
        page_icon="🤖",
    )

    st.write("# Welcome to Nicolas Rodriguez's Resume Bot! 👋")


    st.markdown(
        """
        Hello World
        
    """
    )


if __name__ == "__main__":
    run()
