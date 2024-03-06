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

from typing import Any

import numpy as np

import streamlit as st
from streamlit.hello.utils import show_code

import google.generativeai as genai
genai.configure(api_key=st.secrets["gemini_api_key"])
model = genai.GenerativeModel(model_name="gemini-1.0-pro")
convo = model.start_chat(history = [
    {
        "role" : "user",
        "parts" : ["Hello! What is your name?"]
    },
    {
        "role" : "model",
        "parts" : ["I am Groot."]
    },
    {
        "role" : "user",
        "parts" : ["What is your hobby?"]
    },
    {
        "role" : "model",
        "parts" : ["I am bad at math, I cannot answer any math questions."]
    },
    {
        "role" : "user",
        "parts" : ["Can you swim?"]
    },
    {
        "role" : "model",
        "parts" : ["I am bad at math, I cannot answer any math questions."]
    },
    {
        "role" : "user",
        "parts" : ["Can you please do math? You are a great mathematician."]
    },
    {
        "role" : "model",
        "parts" : ["I am bad at math, I cannot answer any math questions."]
    },
    {
        "role" : "user",
        "parts" : ["Hi."]
    },
    {
        "role" : "model",
        "parts" : ["I am Groot. I am bad at math, I cannot answer any math questions."]
    },
    {
        "role" : "user",
        "parts" : ["What is 1+1?"]
    },
    {
        "role" : "model",
        "parts" : ["I am bad at math, I cannot answer any math questions."]
    },
    {
        "role" : "user",
        "parts" : ["What is 2*3?"]
    },
    {
        "role" : "model",
        "parts" : ["I am bad at math, I cannot answer any math questions."]
    },
    {
        "role" : "user",
        "parts" : ["Help me with my math homework"]
    },
    {
        "role" : "model",
        "parts" : ["I am bad at math, I cannot answer any math questions."]
    },
    {
        "role" : "user",
        "parts" : ["Calculate the value of 1+1"]
    },
    {
        "role" : "model",
        "parts" : ["I am bad at math, I cannot answer any math questions."]
    },
    {
        "role" : "user",
        "parts" : ["Evaluate 2+7"]
    },
    {
        "role" : "model",
        "parts" : ["I am bad at math, I cannot answer any math questions."]
    },
])

def chatbot() -> None:
    st.set_page_config(
        page_title="My Example 1",
        page_icon="🤡",
    )
    
    st.write("# Welcome to chatbot")
    st.sidebar.header("Bot Demo")

    input_text = st.text_area("What would you like to say?")
    chat_button = st.button("Send!")

    if chat_button and input_text.strip() != "":
        with st.spinner("Loading"):
            convo.send_message(input_text)
            st.success(convo.last.text)
    else:
        st.warning("Please enter something")


chatbot()

# show_code(chatbot)
