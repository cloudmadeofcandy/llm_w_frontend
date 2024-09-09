import streamlit as st
import time
import local_llm_interface as lli

st.title('Chat UI')

if 'messages' not in st.session_state:
    st.session_state.messages = [{'role': 'assistant', 'content': 'Hello! How can I help you today?'}]
    
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if prompt := st.chat_input('Insert your questions here?'):
    with st.chat_message('user'):
        st.markdown(prompt)

    st.session_state.messages.append({'role': 'user', 'content': prompt})

with st.chat_message('assistant'):
    llm_instance = lli.local_llm_interface()
    response = st.write_stream(llm_instance.stream_chat(st.session_state.messages))

st.session_state.messages.append({'role': 'assistant', 'content': response})

