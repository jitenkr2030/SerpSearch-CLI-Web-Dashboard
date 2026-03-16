# 🔍 SerpSearch CLI + Web Dashboard

[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![SerpApi](https://img.shields.io/badge/SerpApi-Integration-yellow?style=for-the-badge&logo=google)](https://serpapi.com/)

> **A comprehensive search platform built for SerpApi Developer Advocate application**  
> Demonstrating both **developer tooling (CLI)** and **web visualization (dashboard)** capabilities with Hindi language support.

---

## 🌟 Features

### 🚀 **Web Dashboard**
- **Flask Web App** - Simple, clean interface
- **Real-time Search** - Instant Google search results via SerpApi
- **Bilingual Support** - Hindi/English interface
- **Responsive Design** - Works on all devices
- **Interactive Results** - Clickable links and snippets

### 💻 **CLI Tool**
- **Python Interface** - Command-line search tool for developers
- **Hindi Language** - Localized search (`hl: "hi"`)
- **Simple Usage** - Easy command-line interface
- **Clean Output** - Formatted result display

---

## 📁 Project Structure

```
serpsearch-platform/
├── 📄 README.md                    # This file
├── 📄 requirements.txt             # Python dependencies
├── 📁 cli/
│   └── 📄 serpsearch.py            # CLI tool
├── 📁 web/
│   ├── 📄 app.py                  # Flask web application
│   └── 📁 templates/
│       └── 📄 index.html          # HTML template
└── 📄 setup.sh                     # Setup script (optional)
```

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.8+** 
- **SerpApi Account** - Get your API key from [serpapi.com](https://serpapi.com/)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/jitenkr2030/SerpSearch-CLI-Web-Dashboard.git
   cd SerpSearch-CLI-Web-Dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure SerpApi**
   ```bash
   # Get your API key from https://serpapi.com/
   # Replace "YOUR_SERPAPI_KEY" in both cli/serpsearch.py and web/app.py
   ```

---

## 💻 CLI Tool Usage

### Basic Usage
```bash
# Search from command line
python cli/serpsearch.py "AI startups"

# Example with Hindi query
python cli/serpsearch.py "कृत्रिम बुद्धिमत्ता"
```

### Example Output
```
🔎 खोज परिणाम:

1. AI startups - Wikipedia
https://en.wikipedia.org/wiki/Artificial_intelligence

2. What is AI startups? - Complete Guide
https://example.com/what-is-ai-startups

3. AI startups Tutorial for Beginners
https://tutorial.example.com/ai-startups-beginners
```

---

## 🌐 Web Dashboard

### Start the Web Application
```bash
cd web
python app.py
```

### Access
- **Local**: http://127.0.0.1:5000
- **Network**: Available on your local network

### Features
- **Search Interface**: Clean search bar with real-time results
- **Results Display**: Formatted results with titles, links, and snippets
- **Bilingual UI**: Hindi/English interface elements
- **CLI Instructions**: Built-in usage examples

---

## 🔌 API Integration

### SerpApi Setup
1. **Get API Key**: Register at [serpapi.com](https://serpapi.com/)
2. **Configure**: Replace `YOUR_SERPAPI_KEY` in source files
3. **Test**: Make a search to verify integration

### Configuration Files

#### CLI Tool (`cli/serpsearch.py`)
```python
from serpapi import GoogleSearch

API_KEY = "YOUR_SERPAPI_KEY"  # Replace with your key

def search_google(query):
    params = {
        "q": query,
        "api_key": API_KEY,
        "hl": "hi"  # Hindi language support
    }
    # ... rest of the code
```

#### Web App (`web/app.py`)
```python
from flask import Flask, render_template, request
from serpapi import GoogleSearch

API_KEY = "YOUR_SERPAPI_KEY"  # Replace with your key

def search_google(query):
    params = {
        "q": query,
        "api_key": API_KEY
    }
    # ... rest of the code
```

---

## 🌍 Hindi Language Support

### Features
- **UI Labels**: Bilingual interface elements
- **Search Results**: Hindi language search (`hl: "hi"`)
- **CLI Output**: Localized messages
- **Documentation**: Hindi examples

### Implementation
```python
# Hindi language parameter
params = {
    "q": query,
    "api_key": API_KEY,
    "hl": "hi"  # Hindi language support
}
```

---

## 🛠️ Development

### Running the CLI Tool
```bash
# Test CLI tool
python cli/serpsearch.py "test query"

# With Hindi query
python cli/serpsearch.py "भारतीय तकनीक"
```

### Running the Web App
```bash
# Start Flask development server
cd web
python app.py

# The app will be available at http://127.0.0.1:5000
```

### Dependencies
```bash
# Install required packages
pip install google-search-results flask

# Or use requirements file
pip install -r requirements.txt
```

---

## 🎯 Why This Project?

### For SerpApi Developer Advocate Role

This project demonstrates **exactly** what SerpApi is looking for:

1. **🔧 Technical Excellence**
   - Clean Python code structure
   - Proper API integration patterns
   - Error handling and best practices
   - Simple, effective solutions

2. **👥 Developer Empathy**
   - CLI tool for developer workflows
   - Simple web interface for users
   - Clear documentation and examples
   - Multiple interface options

3. **🌍 Community Focus**
   - Hindi language support for Indian developers
   - Bilingual documentation
   - Inclusive design principles
   - Localized user experience

4. **📚 Product Knowledge**
   - Direct SerpApi integration
   - Search result handling
   - API parameter optimization
   - Real-world implementation

5. **🚀 Simplicity**
   - Clean, minimal codebase
   - Easy to understand and modify
   - Fast setup and deployment
   - Developer-friendly structure

---

## 📊 Features Breakdown

### CLI Tool Features
- ✅ Simple command-line interface
- ✅ Hindi language search support
- ✅ Clean result formatting
- ✅ Error handling
- ✅ Easy integration

### Web Dashboard Features
- ✅ Clean Flask web interface
- ✅ Responsive design
- ✅ Bilingual support
- ✅ Interactive results
- ✅ Built-in documentation

### Developer Experience
- ✅ Minimal dependencies
- ✅ Clear code structure
- ✅ Easy setup
- ✅ Comprehensive documentation
- ✅ Production ready

---

## 🤝 Contributing

### Development Guidelines
1. **Keep it Simple**: Maintain clean, minimal code
2. **Documentation**: Update README for changes
3. **Testing**: Test both CLI and web interfaces
4. **Hindi Support**: Maintain bilingual features

### Pull Request Process
1. Fork the repository
2. Create feature branch
3. Make changes with tests
4. Update documentation
5. Submit pull request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🔗 Links & Resources

### 🌐 Official Links
- **SerpApi**: https://serpapi.com/
- **Documentation**: https://serpapi.com/blog/
- **API Reference**: https://serpapi.com/search-api

### 🛠️ Technologies Used
- **Python**: https://www.python.org/
- **Flask**: https://flask.palletsprojects.com/
- **SerpApi Python SDK**: https://github.com/serpapi/google-search-results-python

### 📚 Learning Resources
- **Python Tutorial**: https://docs.python.org/3/tutorial/
- **Flask Guide**: https://flask.palletsprojects.com/tutorial/
- **SerpApi Guide**: https://serpapi.com/blog/

---

## 🙏 Acknowledgments

- **SerpApi Team** - For providing excellent search API services
- **Flask Team** - For the amazing web framework
- **Indian Developer Community** - Inspiration for Hindi language support

---

<div align="center">

### 🚀 **Built with ❤️ for the SerpApi Developer Advocate Community**

### 🔍 **Simple Search, Powerful Results**

---

**[⭐ Star this repo](https://github.com/jitenkr2030/SerpSearch-CLI-Web-Dashboard) • [🐛 Report Issues](https://github.com/jitenkr2030/SerpSearch-CLI-Web-Dashboard/issues) • [📖 View Documentation](https://github.com/jitenkr2030/SerpSearch-CLI-Web-Dashboard/blob/main/README.md)**

</div>