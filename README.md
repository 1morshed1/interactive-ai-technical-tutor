# 🎓 Interactive AI Technical Tutor

A powerful command-line tool that provides interactive technical explanations using multiple AI models. Get instant help with Python code, software engineering concepts, data science techniques, and LLM-related questions.

## ✨ Features

- **🤖 Multi-Model Support**: Switch between OpenAI GPT and local Ollama models
- **💬 Interactive Conversations**: Continuous Q&A sessions with conversation history
- **📚 Technical Expertise**: Specialized in Python, software engineering, data science, and LLMs
- **🔄 Real-time Model Switching**: Change AI models on-the-fly during conversations
- **💾 Conversation Management**: Save, view, and clear conversation history
- **🎯 Smart Commands**: Built-in command system for advanced functionality
- **🚀 Easy Setup**: Simple installation and configuration process
- **📱 User-Friendly Interface**: Clean CLI with emoji indicators and clear formatting

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai/) (for local models)
- OpenAI API key (optional, for GPT models)

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/1morshed1/interactive-ai-technical-tutor.git
cd interactive-ai-technical-tutor
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Set up environment variables:**

```bash
# Create .env file
echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
```

4. **Install and setup Ollama (for local models):**

```bash
# Install Ollama (visit https://ollama.ai for platform-specific instructions)
curl -fsSL https://ollama.ai/install.sh | sh

# Pull the Llama model
ollama pull llama3.2
```

### Usage

**Start the interactive tutor:**

```bash
python interactive_ai_tutor.py
```

**Example session:**

```
🎓 Interactive AI Technical Tutor

Welcome! I'm here to help you understand Python code, software engineering, data science, and LLMs.

Available Models:
- gpt: OpenAI GPT-4o Mini ✅
- llama: Llama 3.2 (Local) ✅

Current model: Llama 3.2 (Local)

🤔 Please enter your question: What does yield from do in Python?
🤖 Thinking... (using Llama 3.2)

[Detailed AI explanation appears here]

🤔 Please enter your question: !model gpt
✅ Switched to OpenAI GPT-4o Mini

🤔 Please enter your question: !save
✅ Conversation saved to: tutor_conversation_20240117_143022.md
```

## 📋 Requirements

Create a `requirements.txt` file:

```txt
python-dotenv>=1.0.0
openai>=1.0.0
ollama>=0.1.0
ipython>=8.0.0
```

## 🛠️ Available Commands

| Command            | Description                        |
| ------------------ | ---------------------------------- |
| `!model <name>`    | Switch between models (gpt/llama)  |
| `!history`         | Show conversation history          |
| `!clear`           | Clear conversation history         |
| `!save`            | Save conversation to markdown file |
| `!help`            | Show available commands            |
| `!quit` or `!exit` | Exit the tutor                     |

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# OpenAI API Key (optional - only needed for GPT models)
OPENAI_API_KEY=your_openai_api_key_here

# Optional: Custom model configurations
MODEL_GPT=gpt-4o-mini
MODEL_LLAMA=llama3.2
```

### Model Configuration

You can modify the available models by editing the `AVAILABLE_MODELS` dictionary in `interactive_ai_tutor.py`:

```python
AVAILABLE_MODELS = {
    'gpt': {'name': 'gpt-4o-mini', 'provider': 'openai', 'description': 'OpenAI GPT-4o Mini'},
    'llama': {'name': 'llama3.2', 'provider': 'ollama', 'description': 'Llama 3.2 (Local)'},
    # Add more models here
}
```

## 📚 Topics Covered

The AI tutor specializes in explaining:

- **🐍 Python Programming**: Code analysis, best practices, debugging
- **🏗️ Software Engineering**: Design patterns, architecture, testing
- **📊 Data Science**: Algorithms, libraries (pandas, numpy, scikit-learn)
- **🤖 Machine Learning**: Models, training, evaluation techniques
- **🧠 Large Language Models**: Architecture, training, fine-tuning
- **⚡ Performance Optimization**: Code efficiency, profiling, scaling

## 💡 Example Questions

- "Explain what `yield from` does in Python and why it's useful"
- "What's the difference between `__str__` and `__repr__` methods?"
- "How does gradient descent work in machine learning?"
- "What are the best practices for API design?"
- "Explain the transformer architecture in LLMs"
- "How do I optimize this SQL query?"

## 🎯 Advanced Features

### Conversation History

All your questions and answers are automatically saved during the session:

```bash
🤔 Please enter your question: !history
📜 Conversation History:

1. What does yield from do in Python and why it's useful?
2. Explain the difference between lists and tuples...
3. How do I implement a binary search algorithm?
```

### Save Conversations

Export your learning session to a markdown file:

```bash
🤔 Please enter your question: !save
✅ Conversation saved to: tutor_conversation_20240117_143022.md
```

### Model Switching

Switch between different AI models during your session:

```bash
🤔 Please enter your question: !model gpt
✅ Switched to OpenAI GPT-4o Mini

🤔 Please enter your question: !model llama
✅ Switched to Llama 3.2 (Local)
```

## 🏗️ Architecture

### Core Components

1. **TechnicalTutor Class**: Main application logic and session management
2. **Model Management**: Dynamic model switching and availability testing
3. **Command System**: Built-in commands for advanced functionality
4. **Conversation History**: Persistent session storage and export
5. **Error Handling**: Robust error recovery and user feedback

### Code Structure

```
ai-technical-tutor/
├── interactive_ai_tutor.py # Main application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables
├── .env.example            # Environment template
├── README.md               # This file
└── conversations/          # Saved conversation files
```

## 🔍 Troubleshooting

### Common Issues

**Ollama Connection Failed:**

```bash
# Make sure Ollama is running
ollama serve

# Check if model is available
ollama list

# Pull the model if missing
ollama pull llama3.2
```

**OpenAI API Issues:**

```bash
# Verify your API key
echo $OPENAI_API_KEY

# Test API connectivity
curl -H "Authorization: Bearer YOUR_API_KEY" https://api.openai.com/v1/models
```

**Module Import Errors:**

```bash
# Install missing dependencies
pip install -r requirements.txt

# Check Python version
python --version  # Should be 3.8+
```

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature-name`
3. **Make your changes** and add tests
4. **Commit changes**: `git commit -am 'Add new feature'`
5. **Push to branch**: `git push origin feature-name`
6. **Submit a pull request**

### Development Setup

```bash
# Clone your fork
git clone https://github.com/1morhsed1/interactive-ai-technical-tutor.git

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Run linting
flake8 tutor.py
```

## 📊 Performance

- **Response Time**: 1-5 seconds depending on model and complexity
- **Memory Usage**: ~100MB for base application + model requirements
- **Concurrent Users**: Single-user CLI application
- **Conversation Limit**: No limit (depends on available storage)

## 🔒 Privacy & Security

- **Local Processing**: Ollama models run entirely on your machine
- **API Security**: OpenAI API key stored locally in `.env` file
- **Data Privacy**: Conversations saved locally, not transmitted unless using OpenAI
- **No Telemetry**: No usage data collected or transmitted

## 📈 Roadmap

- [ ] **Web Interface**: Streamlit/Gradio web UI
- [ ] **More Models**: Support for Anthropic Claude, Google Gemini
- [ ] **Plugin System**: Custom model integrations
- [ ] **Code Execution**: Run and test code snippets
- [ ] **Multi-language Support**: Support for other programming languages
- [ ] **Team Features**: Shared conversations and knowledge base
- [ ] **API Mode**: REST API for integration with other tools

## 🙏 Acknowledgments

- **[Ollama](https://ollama.ai/)** for making local LLMs accessible
- **[OpenAI](https://openai.com/)** for powerful language models
- **[IPython](https://ipython.org/)** for excellent display capabilities
- **Python Community** for amazing libraries and tools

## 📞 Support

- 📧 **Email**: morshedfahim87@gmail.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/1morshed1/interactive-ai-technical-tutor/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/1morshed1/interactive-ai-technical-tutor/discussions)
- 📖 **Wiki**: [Project Wiki](https://github.com/1morshd1/interactive-ai-technical-tutor/wiki)

## ⭐ Star History

If you find this project helpful, please consider starring the repository!

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/ai-technical-tutor&type=Date)](https://star-history.com/1morshed1/interactive-ai-technical-tutor&Date)

---

**Made with ❤️ by developers, for developers**
