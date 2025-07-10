import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper,WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchRun
from langchain.agents import initialize_agent,AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os
from dotenv import load_dotenv

# Sayfa yapılandırması
st.set_page_config(
    page_title="ZoBoo AI Research Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
    }
    
    .main-header p {
        margin: 0.5rem 0 0 0;
        font-size: 1.1rem;
        opacity: 0.9;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 10px;
        padding: 1rem;
    }
    
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 4px solid #667eea;
    }
    
    .feature-card h3 {
        color: #667eea;
        margin-top: 0;
    }
    
    .status-box {
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        text-align: center;
        font-weight: 500;
    }
    
    .status-connected {
        background-color: #d4edda;
        color: #155724;
        border: 1px solid #c3e6cb;
    }
    
    .status-disconnected {
        background-color: #f8d7da;
        color: #721c24;
        border: 1px solid #f5c6cb;
    }
    
    .chat-container {
        max-width: 800px;
        margin: 0 auto;
    }
    
    .tools-info {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .tools-info h4 {
        margin: 0 0 0.5rem 0;
        font-size: 1.1rem;
    }
    
    .tool-badge {
        background: rgba(255,255,255,0.2);
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        margin: 0.2rem;
        display: inline-block;
        font-size: 0.9rem;
    }
    
    .stChatMessage {
        border-radius: 15px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    
    .example-questions {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .example-btn {
        background: #667eea;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.2rem;
        cursor: pointer;
        font-size: 0.9rem;
    }
    
    .example-btn:hover {
        background: #5a67d8;
    }
</style>
""", unsafe_allow_html=True)

## Arxiv and wikipedia Tools
arxiv_wrapper=ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv=ArxivQueryRun(api_wrapper=arxiv_wrapper)

api_wrapper=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=200)
wiki=WikipediaQueryRun(api_wrapper=api_wrapper)

search=DuckDuckGoSearchRun(name="Search")

# Main Header
st.markdown("""
<div class="main-header">
    <h1>🤖 AI Research Assistant ZoBoo</h1>
    <p>Custom AI ChatBot < Developed by Enes Aydin > </p>
</div>
""", unsafe_allow_html=True)

# Sidebar settings
st.sidebar.markdown("## ⚙️ Settings")
st.sidebar.markdown("---")

# API Key input
api_key = st.sidebar.text_input(
    "🔑 Groq API Key",
    type="password",
    help="Enter your Groq API key here"
)

# Connection status
if api_key:
    st.sidebar.markdown('<div class="status-box status-connected">✅ API Key Entered</div>', unsafe_allow_html=True)
else:
    st.sidebar.markdown('<div class="status-box status-disconnected">❌ API Key Required</div>', unsafe_allow_html=True)

st.sidebar.markdown("---")

# Tools information
st.sidebar.markdown("""
<div class="tools-info">
    <h4>🛠️ Available Tools</h4>
    <span class="tool-badge">🔍 Web Search</span>
    <span class="tool-badge">📚 Wikipedia</span>
    <span class="tool-badge">📄 Arxiv</span>
</div>
""", unsafe_allow_html=True)

# Features
st.sidebar.markdown("### 🌟 Features")
st.sidebar.markdown("""
- 🔍 **Real-time Search**: Web search with DuckDuckGo
- 📚 **Wikipedia Integration**: Access to encyclopedic knowledge
- 📄 **Academic Research**: Access to Arxiv papers
- 🤖 **AI Powered**: Enhanced with Llama3 model
- 💬 **Chat History**: Maintains conversation context
""")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant","content":"Hello! I'm ZoBoo that can search the web. How can I help you today? 🤖"}
    ]

# Example questions section
st.markdown("### 💡 Example Questions")

example_questions = [
    "What is machine learning?",
    "Latest AI developments",
    "Quantum computing basics",
    "Python programming guide",
    "Blockchain technology"
]

cols = st.columns(len(example_questions))
for i, question in enumerate(example_questions):
    with cols[i]:
        if st.button(question, key=f"example_{i}", help=f"Ask: '{question}'"):
            st.session_state.example_question = question

# Small stats section
col1, col2, col3 = st.columns(3)
message_count = len(st.session_state.messages)
user_messages = len([msg for msg in st.session_state.messages if msg["role"] == "user"])

with col1:
    st.metric("Messages", message_count)
with col2:
    st.metric("Questions", user_messages)
with col3:
    st.metric("Tools", "3")

# Chat section
st.markdown("### 💬 Chat")
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Display message history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg['content'])

# Handle input from example questions or text input
if "example_question" in st.session_state:
    prompt = st.session_state.example_question
    del st.session_state.example_question
elif prompt := st.chat_input(placeholder="Type your question... (e.g., 'What is artificial intelligence?')"):
    pass
else:
    prompt = None

if prompt:
    # API key check
    if not api_key:
        st.error("🔑 Please enter your Groq API key in the sidebar!")
        st.stop()
    
    # Add user message
    st.session_state.messages.append({"role":"user","content":prompt})
    
    with st.chat_message("user"):
        st.write(prompt)

    # LLM and tools setup
    try:
        llm = ChatGroq(groq_api_key=api_key, model_name="Llama3-8b-8192", streaming=True)
        tools = [search, arxiv, wiki]
        
        search_agent = initialize_agent(
            tools, 
            llm, 
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
            handling_parsing_errors=True
        )

        with st.chat_message("assistant"):
            # Thinking process indicator
            with st.spinner("🤔 Thinking and researching..."):
                st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
                response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
                
            # Save and display response
            st.session_state.messages.append({'role':'assistant',"content":response})
            st.write(response)
            
    except Exception as e:
        st.error(f"❌ Error occurred: {str(e)}")
        st.info("💡 Please make sure your API key is correct.")

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #666;">
    <p>🚀 <strong>AI Research Assistant</strong> | Powered by LangChain & Streamlit</p>
    <p>📝 Enhanced with Web Search, Wikipedia and Arxiv integration</p>
</div>
""", unsafe_allow_html=True)