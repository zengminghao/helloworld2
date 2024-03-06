# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

import google.generativeai as genai
genai.configure(api_key=st.secrets["gemini_api_key"])

def gen(content):
    # Set up the model
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }
    
    safety_settings = []
    
    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)
    
    prompt_parts = [
        """Generate the outline of an argumentative essay.
        Requirements:
        1. Three arguments/points should be provided.
        2. The analysis should be insightful.
        3. List briefly some examples that can be used to support the argument.

        The prompt is as follows:
        """,
        content
    ]
    
    response = model.generate_content(prompt_parts)

    return response.text



def run():
    st.set_page_config(
        page_title="My Example 0",
        page_icon="👋",
    )

    st.write("# Welcome to GP Essay Helper! 👋")
    st.sidebar.success("Select a demo.")
    st.markdown("""Hello! I help to generate outlines of GP Essays""")
    
    st.text_input(
        "Enter the question",
        "",
        key="placeholder",
    )
    input_text = st.session_state.placeholder
    if input_text.strip() == "":
        resp = "Please enter the question"
    else:
        resp = gen(input_text)

    st.write(str(resp))


if __name__ == "__main__":
    run()
