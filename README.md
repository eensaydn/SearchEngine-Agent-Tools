# 🤖 ZoBoo AI Research Assistant

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.28+-red.svg)
![LangChain](https://img.shields.io/badge/langchain-v0.0.350+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

**ZoBoo** is an intelligent AI research assistant that combines the power of LLaMA3 with real-time web search, Wikipedia, and academic paper access through Arxiv. Built with Streamlit and LangChain, it provides a seamless chat interface for research and information gathering.

## ✨ Features

- 🔍 **Real-time Web Search**: Powered by DuckDuckGo for current information
- 📚 **Wikipedia Integration**: Access to encyclopedic knowledge
- 📄 **Academic Research**: Direct access to Arxiv papers
- 🤖 **AI Powered**: Enhanced with Llama3-8b-8192 model via Groq
- 💬 **Chat Interface**: Intuitive conversational interface
- 🎨 **Modern UI**: Beautiful gradient design with responsive layout
- 📊 **Real-time Stats**: Track messages and interactions
- 💡 **Example Questions**: Quick-start templates for common queries

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Groq API key ([Get it here](https://console.groq.com/))

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/eensaydn/SearchEngine-Agent-Tools.git
cd SearchEngine-Agent-Tools
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables (optional)**
```bash
cp .env.example .env
# Edit .env file and add your GROQ_API_KEY
```

4. **Run the application**
```bash
streamlit run app.py
```

5. **Access the application**
   - Open your browser and go to `http://localhost:8501`
   - Enter your Groq API key in the sidebar
   - Start chatting with ZoBoo!

## 📋 Requirements

```txt
streamlit>=1.28.0
langchain>=0.0.350
langchain-groq>=0.1.0
langchain-community>=0.0.10
python-dotenv>=1.0.0
arxiv>=1.4.0
wikipedia>=1.4.0
duckduckgo-search>=3.9.0
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### Customization Options

- **Model Selection**: Change the model in the `ChatGroq` initialization
- **Search Results**: Modify `top_k_results` and `doc_content_chars_max` for tools
- **UI Theme**: Update the CSS styles in the `st.markdown` sections
- **Tools**: Add or remove tools in the `tools` list

## 🎯 Usage

### Basic Usage

1. **Start a conversation**: Type your question in the chat input
2. **Use example questions**: Click on predefined example buttons
3. **Research topics**: Ask about any topic, and ZoBoo will search multiple sources
4. **Academic research**: Ask about scientific papers or technical topics

### Example Queries

- "What are the latest developments in artificial intelligence?"
- "Explain quantum computing in simple terms"
- "Find recent papers about machine learning"
- "What is the current state of renewable energy?"

### Advanced Features

- **Multi-source research**: ZoBoo automatically determines which tools to use
- **Conversation memory**: Maintains context throughout the chat session
- **Real-time processing**: See the AI's thinking process in real-time
- **Error handling**: Graceful handling of API errors and parsing issues

## 🏗️ Architecture

```
ZoBoo AI Research Assistant
├── Frontend (Streamlit)
│   ├── Chat Interface
│   ├── Sidebar Configuration
│   └── Custom CSS Styling
├── Backend (LangChain)
│   ├── LLM (Groq/LLaMA3)
│   ├── Agent (Zero-shot React)
│   └── Tools Integration
└── Data Sources
    ├── DuckDuckGo Search
    ├── Wikipedia API
    └── Arxiv API
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guidelines
- Add docstrings to functions and classes
- Write tests for new features
- Update documentation as needed

## 🐛 Troubleshooting

### Common Issues

1. **API Key Error**: Make sure your Groq API key is valid and entered correctly
2. **Import Errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`
3. **Port Issues**: If port 8501 is busy, Streamlit will automatically use the next available port

### Getting Help

- Check the [Issues](https://github.com/eensaydn/SearchEngine-Agent-Tools/issues) page
- Create a new issue with detailed information about your problem
- Include error messages and system information

## 📈 Roadmap

- [ ] Add support for more LLM providers
- [ ] Implement document upload and analysis
- [ ] Add multi-language support
- [ ] Create mobile-responsive design improvements
- [ ] Add conversation export functionality
- [ ] Implement user authentication
- [ ] Add more specialized research tools

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **LangChain**: For the amazing framework that makes this possible
- **Streamlit**: For the beautiful and easy-to-use web framework
- **Groq**: For providing fast LLM inference
- **DuckDuckGo**: For privacy-focused search results
- **Wikipedia & Arxiv**: For providing access to knowledge and research

## 📧 Contact

**Enes Aydin** - Developer

- GitHub: [@eensaydn](https://github.com/eensaydn)
- Email: eensaydn@icloud.com
- LinkedIn: [enesaydin00](https://www.linkedin.com/in/enesaydin00/)

## 🐛 Bug Reports & Feature Requests

Found a bug or have a feature request? Please open an issue on [GitHub Issues](https://github.com/eensaydn/SearchEngine-Agent-Tools/issues).

---

<div align="center">
  <p>Made with ❤️ by Enes Aydin</p>
  <p>If you find this project helpful, please give it a ⭐!</p>
</div>
