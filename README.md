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
   # Set environment variable (recommended approach)
   export SERPAPI_KEY=your_api_key_here
   
   # Or copy .env.example to .env and edit it
   cp .env.example .env
   # Edit .env file with your API key
   ```

---

## 📸 Web Dashboard Screenshot

### SerpSearch Dashboard Interface

```
🔍 SerpSearch Dashboard
CLI और Web Dashboard - Developer Tool

┌─────────────────────────────────────────────────┐
│ खोज करें / Search Google...     [ Search ]    │
└─────────────────────────────────────────────────┘

परिणाम / Results (5)

┌─────────────────────────────────────────────────┐
│ 1. Artificial Intelligence - Wikipedia        │
│    https://en.wikipedia.org/wiki/Artificial_...│
│    Artificial intelligence (AI) is intelligence...│
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ 2. What is AI? - Complete Guide                │
│    https://example.com/what-is-ai              │
│    A comprehensive guide to understanding AI...│
└─────────────────────────────────────────────────┘

CLI Usage: python cli/serpsearch.py "your search query"
```

---

## 🎬 Demo GIF

### CLI Tool Demo

```
$ python cli/serpsearch.py "AI startups"
🚀 Starting SerpSearch CLI...
🔍 Searching for: AI startups

🔎 खोज परिणाम:

1. AI startups - Wikipedia
https://en.wikipedia.org/wiki/Artificial_intelligence

2. What is AI startups? - Complete Guide
https://example.com/what-is-ai-startups

3. AI startups Tutorial for Beginners
https://tutorial.example.com/ai-startups-beginners

✅ Found 3 results
```

### Web Dashboard Demo

1. **Start the server**: `cd web && python app.py`
2. **Open browser**: Navigate to `http://127.0.0.1:5000`
3. **Enter search query**: Type "machine learning" and click Search
4. **View results**: See formatted results with titles, links, and snippets

---

## 🌍 हिंदी में उपयोग कैसे करें (Hindi Tutorial)

### CLI टूल चलाने के लिए:

```bash
# हिंदी में खोज करें
python cli/serpsearch.py "कृत्रिम बुद्धिमत्ता"

# आउटपुट:
🔎 खोज परिणाम:

1. कृत्रिम बुद्धिमत्ता - विकिपीडिया
https://hi.wikipedia.org/wiki/कृत्रिम_बुद्धिमत्ता

2. AI क्या है? - पूर्ण गाइड
https://example.com/hi/what-is-ai
```

### वेब डैशबोर्ड हिंदी में:

1. **सर्वर चलाएं**: `cd web && python app.py`
2. **ब्राउज़र खोलें**: `http://127.0.0.1:5000`
3. **हिंदी में खोजें**: "मशीन लर्निंग" टाइप करें
4. **परिणाम देखें**: हिंदी और अंग्रेजी में खोज परिणाम

### हिंदी डेवलपर्स के लिए टिप्स:

- **खोज क्वेरी**: हिंदी में भी टाइप कर सकते हैं
- **भाषा समर्थन**: `hl: "hi"` पैरामीटर का उपयोग
- **आउटपुट**: हिंदी में संदेश और निर्देश

---

## 🚀 Future Features

### Upcoming Improvements

- **📰 Google News Search**: Real-time news search functionality
- **📊 Google Trends Dashboard**: Visual trends analysis
- **🖼️ Image Search Support**: Search and display images
- **📈 API Analytics Dashboard**: Usage statistics and analytics
- **📚 Hindi Developer Documentation**: Comprehensive Hindi tutorials
- **🔍 Advanced Search Filters**: Date, language, and region filters
- **📱 Mobile Responsive Design**: Better mobile experience
- **🔐 User Authentication**: Save search history and preferences
- **🌍 Multi-language Support**: More Indian languages
- **⚡ Search History**: Recent searches and favorites
- **📤 Export Results**: PDF, CSV, and JSON export options
- **🔗 API Rate Limiting**: Professional rate limiting
- **🎨 Dark Mode**: Dark theme support
- **🔍 Search Suggestions**: Auto-complete functionality

### Developer API Features

- **📡 REST API Endpoints**: Full API for developers
- **📖 API Documentation**: Comprehensive API docs
- **🧪 Code Examples**: Multiple language examples
- **🔧 SDK Development**: Python, Node.js, and Java SDKs
- **📊 Usage Analytics**: API usage tracking
- **🔑 API Key Management**: Secure key management

---

## 💭 Developer Advocate Motivation

### Why I Built This

This project was created to demonstrate how **SerpApi can be used to build developer-friendly tools** and **localized experiences for Hindi-speaking developers**.

It includes both a **CLI tool** and a **web dashboard** to show how SerpApi can power different types of developer applications:

- **CLI Tool**: Shows how SerpApi integrates into developer workflows
- **Web Dashboard**: Demonstrates web application integration
- **Hindi Language Support**: Focus on Indian developer community
- **Simple Code**: Easy to understand and modify
- **Best Practices**: Environment variables, error handling, documentation

### Target Audience

- **Hindi-speaking developers** who want localized search tools
- **Python developers** looking for SerpApi integration examples
- **Web developers** building search applications
- **Developer Advocates** creating demo projects
- **API enthusiasts** exploring search APIs

### Impact

This project shows that **developer tools can be accessible** and **localized** for different communities, making technology more inclusive for Indian developers.

---

## 🛠️ Development

### Environment Setup
```bash
# Copy environment template
cp .env.example .env

# Edit .env with your API key
nano .env

# Set environment variable
export SERPAPI_KEY=your_api_key_here
```

### Running the CLI Tool
```bash
# Test CLI tool
python cli/serpsearch.py "test query"

# With Hindi query
python cli/serpsearch.py "भारतीय तकनीक"

# Check environment variable
echo $SERPAPI_KEY
```

### Running the Web App
```bash
# Start Flask development server
cd web
python app.py

# The app will be available at http://127.0.0.1:5000

# Check if API key is set
curl -X POST http://127.0.0.1:5000/ \
  -H "Content-Type: application/json" \
  -d '{"query": "test"}'
```

### Dependencies
```bash
# Install required packages
pip install google-search-results flask

# Or use requirements file
pip install -r requirements.txt

# Check installed packages
pip list | grep -E "(flask|google-search-results)"
```

### Debug Mode
```bash
# Enable debug mode in Flask
export FLASK_DEBUG=1
export FLASK_ENV=development

# Run with debug
python web/app.py
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