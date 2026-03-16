# 🔧 CLI Tool Development with SerpApi

[![CLI](https://img.shields.io/badge/CLI-Tools-orange?style=for-the-badge&logo=terminal)](https://en.wikipedia.org/wiki/Command-line_interface)
[![Bash](https://img.shields.io/badge/Bash-Shell-black?style=for-the-badge&logo=gnu-bash)](https://www.gnu.org/software/bash/)
[![SerpApi](https://img.shields.io/badge/SerpApi-Hindi_Tutorial-green?style=for-the-badge&logo=google)](https://serpapi.com/)

> **हिंदी भाषा में CLI Tool Development ट्यूटोरियल**  
> Command-line tools बनाना सीखें SerpApi के साथ

---

## 📋 विषय सूची

1. [परिचय](#-परिचय)
2. [CLI क्या है और क्यों जरूरी?](#-cli-क्या-है-और-क्यों-जरूरी)
3. [Basic CLI Structure](#-basic-cli-structure)
4. [Advanced CLI Features](#-advanced-cli-features)
5. [Multiple Language Support](#-multiple-language-support)
6. [Packaging और Distribution](#-packaging-और-distribution)
7. [Real-World CLI Applications](#-real-world-cli-applications)

---

## 🌟 परिचय

Command-line interface (CLI) tools developers के लिए extremely powerful होते हैं। यह ट्यूटोरियल आपको step-by-step सिखाएगा कि कैसे आप SerpApi का उपयोग करके professional CLI tools बना सकते हैं जो Hindi language को भी support करें।

### 🎯 इस ट्यूटोरियल में क्या सीखेंगे:

- CLI tool fundamentals और architecture
- Command-line arguments parsing
- Interactive CLI features
- Hindi language support in CLI
- Professional CLI development
- Packaging और distribution

---

## 📚 CLI क्या है और क्यों जरूरी?

### CLI क्या है?
CLI (Command-Line Interface) एक text-based interface है जहाँ users commands type करके computer को instructions देते हैं।

### CLI के फायदे:
- ⚡ **Fast**: GUI से तेज़ और efficient
- 🔄 **Automatable**: Scripts में use करना आसान
- 💻 **Resource Efficient**: कम memory और CPU use
- 🌐 **Remote Friendly**: SSH से आसानी से use
- 📝 **Scriptable**: Complex operations automate करें

### Real-world CLI Examples:
```bash
# Git CLI
git commit -m "Update README"

# Docker CLI  
docker run -p 3000:3000 myapp

# npm CLI
npm install serpapi

# हमारा CLI
serpsearch "कृत्रिम बुद्धिमत्ता" --lang=hi --format=json
```

---

## 🏗️ Basic CLI Structure

### 1. Project Setup

```bash
# CLI project बनाएं
mkdir serpapi-cli-tool
cd serpapi-cli-tool

# Python project initialize करें
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Setup files बनाएं
touch setup.py serpsearch.py requirements.txt README.md
mkdir tests
```

### 2. Basic CLI Implementation

```python
#!/usr/bin/env python3
"""
serpsearch.py - Hindi/English Google Search CLI Tool
Author: Your Name
Version: 1.0.0
"""

import sys
import os
import json
import argparse
from typing import List, Dict, Optional
from pathlib import Path
import csv
from datetime import datetime

try:
    from serpapi import GoogleSearch
except ImportError:
    print("❌ Error: serpapi library not installed!")
    print("Install with: pip install google-search-results")
    sys.exit(1)

class SerpSearchCLI:
    """Main CLI class for SerpApi search operations"""
    
    def __init__(self):
        self.api_key = os.getenv("SERPAPI_KEY")
        if not self.api_key:
            self.print_error("SERPAPI_KEY environment variable not set!")
            self.print_info("Set it with: export SERPAPI_KEY=your_key_here")
            sys.exit(1)
    
    def print_error(self, message: str):
        """Print error message in red"""
        print(f"❌ Error: {message}")
    
    def print_success(self, message: str):
        """Print success message in green"""
        print(f"✅ {message}")
    
    def print_info(self, message: str):
        """Print info message in blue"""
        print(f"ℹ️  {message}")
    
    def print_warning(self, message: str):
        """Print warning message in yellow"""
        print(f"⚠️  {message}")

    def search(self, query: str, **kwargs) -> Optional[Dict]:
        """Perform search using SerpApi"""
        try:
            params = {
                "q": query,
                "api_key": self.api_key,
                **kwargs
            }
            
            search = GoogleSearch(params)
            results = search.get_dict()
            
            if "error" in results:
                raise Exception(f"SerpApi Error: {results['error']}")
            
            return results
            
        except Exception as e:
            self.print_error(f"Search failed: {e}")
            return None

    def format_results(self, results: Dict, format_type: str = "simple") -> str:
        """Format search results in different formats"""
        organic_results = results.get("organic_results", [])
        
        if format_type == "json":
            return json.dumps(results, indent=2, ensure_ascii=False)
        
        elif format_type == "csv":
            if not organic_results:
                return "No results found"
            
            # Create CSV data
            csv_data = []
            for i, result in enumerate(organic_results, 1):
                csv_data.append({
                    "Position": i,
                    "Title": result.get("title", ""),
                    "Link": result.get("link", ""),
                    "Snippet": result.get("snippet", "")[:100] + "..." if result.get("snippet") else ""
                })
            
            # Convert to CSV string
            output = []
            if csv_data:
                headers = csv_data[0].keys()
                output.append(",".join(headers))
                for row in csv_data:
                    output.append(",".join([f'"{row[h]}"' for h in headers]))
            
            return "\n".join(output)
        
        else:  # Simple format
            if not organic_results:
                return "🔍 कोई परिणाम नहीं मिला"
            
            output = [f"\n🔍 खोज परिणाम ({len(organic_results)} results):"]
            output.append("=" * 60)
            
            for i, result in enumerate(organic_results, 1):
                title = result.get("title", "No title")
                link = result.get("link", "")
                snippet = result.get("snippet", "")
                
                output.append(f"\n{i}. {title}")
                output.append(f"   🔗 {link}")
                
                if snippet:
                    # Truncate long snippets
                    if len(snippet) > 120:
                        snippet = snippet[:120] + "..."
                    output.append(f"   📝 {snippet}")
            
            return "\n".join(output)

    def save_results(self, results: str, filename: str):
        """Save results to file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(results)
            self.print_success(f"Results saved to {filename}")
        except Exception as e:
            self.print_error(f"Failed to save file: {e}")

def main():
    """Main CLI function"""
    parser = argparse.ArgumentParser(
        description="🔍 SerpSearch - Hindi/English Google Search CLI Tool",
        epilog="Examples:\n  serpsearch.py 'कृत्रिम बुद्धिमत्ता'\n  serpsearch.py 'AI startups' --lang=en --format=json",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Positional arguments
    parser.add_argument(
        "query",
        nargs="*",
        help="Search query (supports Hindi and English)"
    )
    
    # Optional arguments
    parser.add_argument(
        "--lang", "-l",
        default="hi",
        choices=["hi", "en", "bn", "ta", "te", "mr", "gu", "kn", "ml", "pa", "ur"],
        help="Search language (default: hi)"
    )
    
    parser.add_argument(
        "--format", "-f",
        default="simple",
        choices=["simple", "json", "csv"],
        help="Output format (default: simple)"
    )
    
    parser.add_argument(
        "--output", "-o",
        help="Save results to file"
    )
    
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Number of results (default: 10)"
    )
    
    parser.add_argument(
        "--country", "-c",
        default="in",
        help="Country code (default: in)"
    )
    
    parser.add_argument(
        "--safe",
        action="store_true",
        help="Enable safe search"
    )
    
    parser.add_argument(
        "--news",
        action="store_true", 
        help="Search news only"
    )
    
    parser.add_argument(
        "--version", "-v",
        action="version",
        version="SerpSearch CLI 1.0.0"
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # Join query arguments
    query = " ".join(args.query)
    
    if not query:
        parser.print_help()
        print("\n❌ Error: Please provide a search query")
        print("Example: python serpsearch.py 'कृत्रिम बुद्धिमत्ता'")
        sys.exit(1)
    
    # Initialize CLI
    cli = SerpSearchCLI()
    
    # Prepare search parameters
    search_params = {
        "hl": args.lang,
        "gl": args.country,
        "num": args.limit
    }
    
    if args.safe:
        search_params["safe"] = "active"
    
    if args.news:
        search_params["tbm"] = "nws"
    
    # Perform search
    print(f"🔍 '{query}' खोज रहे हैं...")
    
    results = cli.search(query, **search_params)
    
    if not results:
        cli.print_error("No results received")
        sys.exit(1)
    
    # Format and display results
    formatted_results = cli.format_results(results, args.format)
    
    if args.output:
        cli.save_results(formatted_results, args.output)
    else:
        print(formatted_results)

if __name__ == "__main__":
    main()
```

### 3. CLI Tool Testing

```bash
# Basic search
python serpsearch.py "कृत्रिम बुद्धिमत्ता"

# English search
python serpsearch.py "artificial intelligence" --lang=en

# JSON format
python serpsearch.py "machine learning" --format=json

# Save to file
python serpsearch.py "data science" --output=results.txt

# News search
python serpsearch.py "technology news" --news

# Help
python serpsearch.py --help
```

---

## 🔥 Advanced CLI Features

### 1. Interactive CLI Mode

```python
# interactive_mode.py
import sys
from serpsearch import SerpSearchCLI
import readline  # For better input handling

class InteractiveSerpSearch(SerpSearchCLI):
    """Interactive CLI mode with continuous search"""
    
    def __init__(self):
        super().__init__()
        self.history = []
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def welcome_message(self):
        """Display welcome message"""
        print("🚀 Welcome to SerpSearch Interactive Mode!")
        print("Type 'help' for commands or 'exit' to quit")
        print("=" * 50)
    
    def show_help(self):
        """Show help commands"""
        help_text = """
📚 Available Commands:
  search <query>     - Perform search
  lang <code>        - Set language (hi, en, bn, ta, etc.)
  format <type>      - Set output format (simple, json, csv)
  limit <number>     - Set result limit
  history            - Show search history
  clear              - Clear screen
  help               - Show this help
  exit               - Exit interactive mode

💡 Examples:
  search कृत्रिम बुद्धिमत्ता
  lang en
  format json
  limit 5
        """
        print(help_text)
    
    def add_to_history(self, query: str, results_count: int):
        """Add search to history"""
        self.history.append({
            "query": query,
            "results_count": results_count,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        })
        
        # Keep only last 20 searches
        if len(self.history) > 20:
            self.history = self.history[-20:]
    
    def show_history(self):
        """Display search history"""
        if not self.history:
            print("📝 No search history yet")
            return
        
        print("📜 Search History:")
        print("-" * 40)
        for i, item in enumerate(self.history, 1):
            print(f"{i:2d}. {item['timestamp']} - {item['query']} ({item['results_count']} results)")
    
    def interactive_loop(self):
        """Main interactive loop"""
        self.welcome_message()
        
        current_settings = {
            "lang": "hi",
            "format": "simple", 
            "limit": 10,
            "country": "in"
        }
        
        while True:
            try:
                # Get user input
                user_input = input("serpsearch> ").strip()
                
                if not user_input:
                    continue
                
                # Parse command
                parts = user_input.split()
                command = parts[0].lower()
                args = parts[1:] if len(parts) > 1 else []
                
                if command == "exit" or command == "quit":
                    print("👋 Goodbye! Happy searching!")
                    break
                
                elif command == "help":
                    self.show_help()
                
                elif command == "clear":
                    os.system('clear' if os.name == 'posix' else 'cls')
                
                elif command == "history":
                    self.show_history()
                
                elif command == "lang" and args:
                    lang = args[0]
                    if lang in ["hi", "en", "bn", "ta", "te", "mr", "gu", "kn", "ml", "pa", "ur"]:
                        current_settings["lang"] = lang
                        print(f"✅ Language set to: {lang}")
                    else:
                        print("❌ Invalid language code")
                
                elif command == "format" and args:
                    fmt = args[0]
                    if fmt in ["simple", "json", "csv"]:
                        current_settings["format"] = fmt
                        print(f"✅ Format set to: {fmt}")
                    else:
                        print("❌ Invalid format")
                
                elif command == "limit" and args:
                    try:
                        limit = int(args[0])
                        if 1 <= limit <= 100:
                            current_settings["limit"] = limit
                            print(f"✅ Limit set to: {limit}")
                        else:
                            print("❌ Limit must be between 1 and 100")
                    except ValueError:
                        print("❌ Invalid number")
                
                elif command == "search" and args:
                    query = " ".join(args)
                    print(f"🔍 Searching: {query}")
                    
                    results = self.search(query, **current_settings)
                    if results:
                        formatted = self.format_results(results, current_settings["format"])
                        print(formatted)
                        
                        # Add to history
                        results_count = len(results.get("organic_results", []))
                        self.add_to_history(query, results_count)
                
                else:
                    # Treat as direct search
                    if user_input not in ["exit", "quit", "help", "clear", "history", "lang", "format", "limit"]:
                        print(f"🔍 Searching: {user_input}")
                        
                        results = self.search(user_input, **current_settings)
                        if results:
                            formatted = self.format_results(results, current_settings["format"])
                            print(formatted)
                            
                            # Add to history
                            results_count = len(results.get("organic_results", []))
                            self.add_to_history(user_input, results_count)
            
            except KeyboardInterrupt:
                print("\n👋 Use 'exit' to quit")
            except EOFError:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                self.print_error(f"Command error: {e}")

def main_interactive():
    """Run interactive mode"""
    cli = InteractiveSerpSearch()
    cli.interactive_loop()

if __name__ == "__main__":
    main_interactive()
```

### 2. CLI Configuration Management

```python
# config_manager.py
import json
import os
from pathlib import Path
from typing import Dict, Any

class CLIConfig:
    """CLI configuration management"""
    
    def __init__(self, config_file: str = None):
        self.config_file = config_file or Path.home() / ".serpsearch" / "config.json"
        self.config_file.parent.mkdir(parents=True, exist_ok=True)
        self.default_config = self.get_default_config()
        self.config = self.load_config()
    
    def get_default_config(self) -> Dict[str, Any]:
        """Get default configuration"""
        return {
            "api_key": "",
            "default_language": "hi",
            "default_format": "simple",
            "default_limit": 10,
            "default_country": "in",
            "safe_search": False,
            "color_output": True,
            "save_history": True,
            "history_limit": 100,
            "timeout": 30,
            "retry_attempts": 3,
            "cache_enabled": True,
            "cache_ttl": 3600,
            "favorites": []
        }
    
    def load_config(self) -> Dict[str, Any]:
        """Load configuration from file"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    loaded_config = json.load(f)
                # Merge with defaults
                config = self.default_config.copy()
                config.update(loaded_config)
                return config
            else:
                return self.default_config.copy()
        except Exception as e:
            print(f"⚠️  Warning: Could not load config: {e}")
            return self.default_config.copy()
    
    def save_config(self):
        """Save configuration to file"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"❌ Error saving config: {e}")
    
    def get(self, key: str, default=None):
        """Get configuration value"""
        return self.config.get(key, default)
    
    def set(self, key: str, value: Any):
        """Set configuration value"""
        self.config[key] = value
        self.save_config()
    
    def add_favorite(self, query: str, description: str = ""):
        """Add query to favorites"""
        favorite = {
            "query": query,
            "description": description,
            "added_at": datetime.now().isoformat()
        }
        
        # Remove if already exists
        self.config["favorites"] = [f for f in self.config["favorites"] if f["query"] != query]
        self.config["favorites"].append(favorite)
        
        # Keep only last 20 favorites
        if len(self.config["favorites"]) > 20:
            self.config["favorites"] = self.config["favorites"][-20:]
        
        self.save_config()
        print(f"✅ Added to favorites: {query}")
    
    def remove_favorite(self, query: str):
        """Remove query from favorites"""
        original_count = len(self.config["favorites"])
        self.config["favorites"] = [f for f in self.config["favorites"] if f["query"] != query]
        
        if len(self.config["favorites"]) < original_count:
            self.save_config()
            print(f"✅ Removed from favorites: {query}")
        else:
            print(f"❌ Not found in favorites: {query}")
    
    def list_favorites(self):
        """List all favorites"""
        if not self.config["favorites"]:
            print("📝 No favorites saved")
            return
        
        print("⭐ Favorites:")
        print("-" * 40)
        for i, fav in enumerate(self.config["favorites"], 1):
            desc = f" - {fav['description']}" if fav['description'] else ""
            print(f"{i:2d}. {fav['query']}{desc}")

# Usage in CLI
def config_command(args):
    """Handle configuration commands"""
    config = CLIConfig()
    
    if args.action == "show":
        print("⚙️  Current Configuration:")
        for key, value in config.config.items():
            if key == "api_key":
                value = "***" + value[-4:] if value else "Not set"
            print(f"  {key}: {value}")
    
    elif args.action == "set" and args.key and args.value:
        config.set(args.key, args.value)
        print(f"✅ Set {args.key} = {args.value}")
    
    elif args.action == "add-fav" and args.query:
        config.add_favorite(args.query, args.description or "")
    
    elif args.action == "remove-fav" and args.query:
        config.remove_favorite(args.query)
    
    elif args.action == "list-fav":
        config.list_favorites()
    
    else:
        print("❌ Invalid config command")
```

---

## 🌍 Multiple Language Support

### 1. Multi-Language CLI

```python
# multilingual_cli.py
import argparse
from typing import Dict, List

class MultiLanguageCLI:
    """Multi-language support for CLI"""
    
    TRANSLATIONS = {
        "hi": {
            "searching": "खोज रहे हैं",
            "results_found": "परिणाम मिले",
            "no_results": "कोई परिणाम नहीं मिला",
            "error": "त्रुटि",
            "success": "सफलता",
            "saved_to": "सेव किया गया",
            "language": "भाषा",
            "format": "प्रारूप",
            "limit": "सीमा",
            "help": "सहायता"
        },
        "en": {
            "searching": "Searching",
            "results_found": "Results found",
            "no_results": "No results found", 
            "error": "Error",
            "success": "Success",
            "saved_to": "Saved to",
            "language": "Language",
            "format": "Format",
            "limit": "Limit",
            "help": "Help"
        },
        "bn": {  # Bengali
            "searching": "অনুসন্ধান করছি",
            "results_found": "ফলাফল পাওয়া গেছে",
            "no_results": "কোনো ফলাফল পাওয়া যায়নি",
            "error": "ত্রুটি",
            "success": "সফলতা"
        },
        "ta": {  # Tamil
            "searching": "தேடுகிறது",
            "results_found": "முடிவுகள் கிடைத்தன",
            "no_results": "முடிவுகள் இல்லை",
            "error": "பிழை",
            "success": "வெற்றி"
        }
    }
    
    def __init__(self, language: str = "hi"):
        self.language = language
        if language not in self.TRANSLATIONS:
            self.language = "hi"  # Default to Hindi
    
    def t(self, key: str) -> str:
        """Get translated text"""
        return self.TRANSLATIONS.get(self.language, {}).get(key, key)
    
    def format_message(self, template: str, **kwargs) -> str:
        """Format message with translations"""
        try:
            return template.format(**{k: self.t(v) if isinstance(v, str) else v for k, v in kwargs.items()})
        except KeyError:
            return template
    
    def print_localized(self, message_type: str, *args):
        """Print localized message"""
        if message_type == "searching":
            print(f"🔍 {self.t('searching')}: {' '.join(args)}")
        elif message_type == "results":
            print(f"✅ {self.t('results_found')}: {args[0]}")
        elif message_type == "no_results":
            print(f"🔍 {self.t('no_results')}")
        elif message_type == "error":
            print(f"❌ {self.t('error')}: {' '.join(args)}")
        elif message_type == "saved":
            print(f"✅ {self.t('saved_to')}: {args[0]}")

class RegionalSearchCLI(MultiLanguageCLI):
    """Regional language search CLI"""
    
    def __init__(self, language: str = "hi"):
        super().__init__(language)
        self.regional_settings = self.get_regional_settings(language)
    
    def get_regional_settings(self, language: str) -> Dict:
        """Get regional search settings"""
        settings = {
            "hi": {"hl": "hi", "gl": "in"},
            "bn": {"hl": "bn", "gl": "bd"}, 
            "ta": {"hl": "ta", "gl": "in"},
            "te": {"hl": "te", "gl": "in"},
            "mr": {"hl": "mr", "gl": "in"},
            "gu": {"hl": "gu", "gl": "in"},
            "kn": {"hl": "kn", "gl": "in"},
            "ml": {"hl": "ml", "gl": "in"},
            "pa": {"hl": "pa", "gl": "in"},
            "ur": {"hl": "ur", "gl": "pk"}
        }
        return settings.get(language, {"hl": "en", "gl": "us"})
    
    def search_regional(self, query: str) -> Dict:
        """Search with regional settings"""
        from serpsearch import SerpSearchCLI
        
        cli = SerpSearchCLI()
        return cli.search(query, **self.regional_settings)

# Multi-language argument parser
def create_multilingual_parser():
    """Create multi-language argument parser"""
    parser = argparse.ArgumentParser(
        description="🔍 Multi-Language SerpSearch CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Language selection with descriptions
    lang_choices = {
        "hi": "हिंदी (Hindi)",
        "en": "English", 
        "bn": "বাংলা (Bengali)",
        "ta": "தமிழ் (Tamil)",
        "te": "తెలుగు (Telugu)",
        "mr": "मराठी (Marathi)",
        "gu": "ગુજરાતી (Gujarati)",
        "kn": "ಕನ್ನಡ (Kannada)",
        "ml": "മലയാളം (Malayalam)",
        "pa": "ਪੰਜਾਬੀ (Punjabi)",
        "ur": "اردو (Urdu)"
    }
    
    parser.add_argument(
        "--lang", "-l",
        choices=list(lang_choices.keys()),
        default="hi",
        help=f"Search language (default: hi)"
    )
    
    return parser

def main_multilingual():
    """Main multi-language CLI function"""
    parser = create_multilingual_parser()
    args = parser.parse_args()
    
    # Initialize multi-language CLI
    cli = RegionalSearchCLI(args.lang)
    
    # Get query
    query = " ".join(args.query) if hasattr(args, 'query') else input(f"{cli.t('searching')}: ")
    
    if not query:
        cli.print_localized("error", "No query provided")
        return
    
    # Perform search
    cli.print_localized("searching", query)
    results = cli.search_regional(query)
    
    if results and results.get("organic_results"):
        cli.print_localized("results", len(results["organic_results"]))
        
        # Display results in localized format
        for i, result in enumerate(results["organic_results"][:5], 1):
            print(f"{i}. {result['title']}")
            print(f"   {result['link']}")
    else:
        cli.print_localized("no_results")
```

---

## 📦 Packaging और Distribution

### 1. setup.py for Package Distribution

```python
# setup.py
from setuptools import setup, find_packages
import os

# Read README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="serpsearch-cli",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="🔍 Hindi/English Google Search CLI Tool with SerpApi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/serpsearch-cli",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Utilities"
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800"
        ]
    },
    entry_points={
        "console_scripts": [
            "serpsearch=serpsearch.cli:main",
            "serpsearch-interactive=serpsearch.interactive:main"
        ],
    },
    include_package_data=True,
    package_data={
        "serpsearch": ["*.json", "*.txt", "templates/*"]
    },
    keywords="serpapi google search cli hindi english multilingual",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/serpsearch-cli/issues",
        "Source": "https://github.com/yourusername/serpsearch-cli",
        "Documentation": "https://serpsearch-cli.readthedocs.io/",
    }
)
```

### 2. requirements.txt

```txt
google-search-results>=2.4.2
requests>=2.25.1
click>=8.0.0
colorama>=0.4.4
tabulate>=0.8.9
pyyaml>=5.4.0
```

### 3. Makefile for Easy Development

```makefile
# Makefile
.PHONY: install test lint clean build upload

# Install dependencies
install:
	pip install -e .
	pip install -e .[dev]

# Run tests
test:
	python -m pytest tests/ -v

# Lint code
lint:
	flake8 serpsearch/
	black --check serpsearch/
	mypy serpsearch/

# Format code
format:
	black serpsearch/
	isort serpsearch/

# Clean build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

# Build package
build: clean
	python setup.py sdist bdist_wheel

# Upload to PyPI
upload: build
	twine upload dist/*

# Upload to Test PyPI
upload-test: build
	twine upload --repository testpypi dist/

# Development installation
dev-install: install
	pre-commit install

# Run CLI
run:
	python -m serpsearch

# Interactive mode
interactive:
	python -m serpsearch.interactive
```

---

## 🎪 Real-World CLI Applications

### 1. Content Research CLI

```python
# content_research_cli.py
import argparse
import json
from datetime import datetime
from serpsearch import SerpSearchCLI

class ContentResearchCLI:
    """CLI for content research and analysis"""
    
    def __init__(self):
        self.search_cli = SerpSearchCLI()
    
    def research_topic(self, topic: str, depth: int = 3) -> dict:
        """Deep research on a topic"""
        research_data = {
            "topic": topic,
            "timestamp": datetime.now().isoformat(),
            "queries": [],
            "results": {},
            "insights": []
        }
        
        # Generate related queries
        base_queries = [
            topic,
            f"{topic} tutorial",
            f"{topic} examples", 
            f"{topic} best practices",
            f"{topic} vs alternatives",
            f"how to {topic}",
            f"{topic} problems",
            f"{topic} solutions"
        ]
        
        for query in base_queries[:depth]:
            print(f"🔍 Researching: {query}")
            
            results = self.search_cli.search(query, hl="hi", gl="in")
            if results:
                research_data["queries"].append(query)
                research_data["results"][query] = results.get("organic_results", [])
        
        # Generate insights
        research_data["insights"] = self.analyze_results(research_data["results"])
        
        return research_data
    
    def analyze_results(self, results: dict) -> list:
        """Analyze search results and generate insights"""
        insights = []
        all_titles = []
        all_domains = {}
        
        # Collect data
        for query, query_results in results.items():
            for result in query_results:
                title = result.get("title", "").lower()
                domain = result.get("displayed_link", "").split('/')[0]
                
                all_titles.append(title)
                all_domains[domain] = all_domains.get(domain, 0) + 1
        
        # Generate insights
        if all_domains:
            top_domains = sorted(all_domains.items(), key=lambda x: x[1], reverse=True)[:3]
            insights.append(f"Top domains: {', '.join([d[0] for d in top_domains])}")
        
        # Common keywords
        common_words = {}
        for title in all_titles:
            for word in title.split():
                if len(word) > 3:
                    common_words[word] = common_words.get(word, 0) + 1
        
        if common_words:
            top_words = sorted(common_words.items(), key=lambda x: x[1], reverse=True)[:5]
            insights.append(f"Common keywords: {', '.join([w[0] for w in top_words])}")
        
        return insights
    
    def generate_content_outline(self, research_data: dict) -> dict:
        """Generate content outline based on research"""
        outline = {
            "title": research_data["topic"],
            "sections": [],
            "references": []
        }
        
        # Extract sections from results
        for query, results in research_data["results"].items():
            section = {
                "title": query.title(),
                "points": []
            }
            
            for result in results[:3]:  # Top 3 results per query
                point = {
                    "title": result.get("title", ""),
                    "url": result.get("link", ""),
                    "snippet": result.get("snippet", "")[:100] + "..." if result.get("snippet") else ""
                }
                section["points"].append(point)
                outline["references"].append(result.get("link", ""))
            
            outline["sections"].append(section)
        
        return outline

def main_research():
    """Main content research CLI"""
    parser = argparse.ArgumentParser(description="🔍 Content Research CLI")
    parser.add_argument("topic", help="Topic to research")
    parser.add_argument("--depth", type=int, default=3, help="Research depth")
    parser.add_argument("--output", help="Output file (JSON)")
    parser.add_argument("--outline", action="store_true", help="Generate content outline")
    
    args = parser.parse_args()
    
    cli = ContentResearchCLI()
    
    print(f"🔍 Starting research on: {args.topic}")
    research_data = cli.research_topic(args.topic, args.depth)
    
    if args.outline:
        outline = cli.generate_content_outline(research_data)
        research_data["outline"] = outline
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(research_data, f, indent=2, ensure_ascii=False)
        print(f"✅ Research saved to: {args.output}")
    else:
        print("\n📊 Research Results:")
        print(f"Topic: {research_data['topic']}")
        print(f"Queries researched: {len(research_data['queries'])}")
        print(f"Insights: {len(research_data['insights'])}")
        
        for insight in research_data['insights']:
            print(f"💡 {insight}")

if __name__ == "__main__":
    main_research()
```

---

## 📝 Summary

### इस CLI Tool ट्यूटोरियल में सीखा:

1. ✅ **CLI fundamentals और architecture**
2. ✅ **Command-line arguments parsing**
3. ✅ **Interactive CLI features**
4. ✅ **Multi-language support (11 Indian languages)**
5. ✅ **Configuration management**
6. ✅ **Packaging और distribution**
7. ✅ **Real-world applications**

### CLI Commands Learned:
```bash
# Basic usage
serpsearch "कृत्रिम बुद्धिमत्ता"

# Advanced options
serpsearch "AI" --lang=en --format=json --output=results.json

# Interactive mode
serpsearch --interactive

# Content research
serpsearch-research "machine learning" --depth=5 --outline
```

### Next Steps:
- 📚 [Python Tutorial](../python/README.md)
- 🟢 [Node.js Tutorial](../nodejs/README.md)
- 🌐 [Main Project](../../SerpSearch-CLI-Web-Dashboard/)

---

## 🤝 CLI Developer Community

### Hindi CLI Developers:
- [CLI Tools Hindi](https://t.me/cli-hindi)
- [Terminal India](https://t.me/terminalindia)
- [Bash Scripting India](https://t.me/bashindia)

### CLI Resources:
- 📧 Email: cli@example.com
- 💬 Discord: [CLI Developers](https://discord.gg/cli-devs)
- 🐛 Issues: [GitHub Issues](https://github.com/issues/new)

---

<div align="center">

### 🔧 **CLI Tools Development Mastery**

### 🇮🇳 **Made with ❤️ for Indian CLI Developers**

### 🚀 **Happy Commanding!**

</div>