# 🐍 Python से SerpApi का उपयोग कैसे करें

[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![SerpApi](https://img.shields.io/badge/SerpApi-Hindi_Tutorial-green?style=for-the-badge&logo=google)](https://serpapi.com/)

> **हिंदी भाषा में SerpApi Python ट्यूटोरियल**  
> भारतीय डेवलपर्स के लिए step-by-step गाइड

---

## 📋 विषय सूची

1. [परिचय](#-परिचय)
2. [आवश्यकताएं](#-आवश्यकताएं)
3. [Installation](#-installation)
4. [पहला SerpApi Program](#-पहला-serpapi-program)
5. [उन्नत Features](#-उन्नत-features)
6. [Error Handling](#-error-handling)
7. [Practical Examples](#-practical-examples)
8. [Best Practices](#-best-practices)

---

## 🌟 परिचय

SerpApi एक powerful API है जो आपको Google search results को programmatically access करने की सुविधा देता है। इस ट्यूटोरियल में हम Python का उपयोग करके SerpApi को कैसे integrate करें, यह step-by-step सीखेंगे।

### 🎯 इस ट्यूटोरियल में क्या सीखेंगे:

- SerpApi Python SDK का उपयोग
- Hindi language search results
- Error handling और best practices
- Real-world applications
- Professional development patterns

---

## 📦 आवश्यकताएं

### Basic Requirements:
- **Python 3.8+** installed
- **SerpApi Account** (Free account available)
- **Basic Python knowledge**
- **Internet connection**

### SerpApi Account बनाएं:
1. [SerpApi.com](https://serpapi.com/) पर जाएं
2. **Free Account** बनाएं
3. **API Key** प्राप्त करें
4. **Email verification** करें

---

## 🚀 Installation

### Step 1: SerpApi SDK Install करें

```bash
# Method 1: Direct pip install
pip install google-search-results

# Method 2: Requirements file के साथ
echo "google-search-results" > requirements.txt
pip install -r requirements.txt

# Method 3: Virtual environment में (Recommended)
python -m venv serpapi_env
source serpapi_env/bin/activate  # Linux/Mac
# या
serpapi_env\Scripts\activate     # Windows
pip install google-search-results
```

### Step 2: Environment Variable Set करें

```bash
# Linux/Mac
export SERPAPI_KEY="your_api_key_here"

# Windows
set SERPAPI_KEY="your_api_key_here"

# .env file के लिए
echo "SERPAPI_KEY=your_api_key_here" > .env
```

---

## 🎯 पहला SerpApi Program

### Basic Search Example

```python
import os
from serpapi import GoogleSearch

def simple_search():
    """Basic Google search using SerpApi"""
    
    # API key
    api_key = os.getenv("SERPAPI_KEY")
    
    if not api_key:
        print("❌ कृपया SERPAPI_KEY environment variable set करें")
        return
    
    # Search parameters
    params = {
        "q": "कृत्रिम बुद्धिमत्ता",  # Hindi search query
        "api_key": api_key,
        "hl": "hi",              # Hindi language
        "gl": "in"               # India location
    }
    
    try:
        # Search perform करें
        search = GoogleSearch(params)
        results = search.get_dict()
        
        # Results display करें
        print("🔍 खोज परिणाम:")
        print("=" * 50)
        
        for i, result in enumerate(results.get("organic_results", []), 1):
            print(f"{i}. {result['title']}")
            print(f"   🔗 {result['link']}")
            if result.get('snippet'):
                print(f"   📝 {result['snippet'][:100]}...")
            print()
            
    except Exception as e:
        print(f"❌ Error: {e}")

# Program run करें
if __name__ == "__main__":
    simple_search()
```

### Program Save करें और run करें:

```bash
# File save करें: basic_search.py
python basic_search.py
```

**Expected Output:**
```
🔍 खोज परिणाम:
==================================================
1. कृत्रिम बुद्धिमत्ता - विकिपीडिया
   🔗 https://hi.wikipedia.org/wiki/कृत्रिम_बुद्धिमत्ता
   📝 कृत्रिम बुद्धिमत्ता (Artificial Intelligence)...

2. AI क्या है? - हिंदी ट्यूटोरियल
   🔗 https://example.com/ai-hindi
   📝 Artificial Intelligence के बारे में...
```

---

## 🔥 उन्नत Features

### 1. Custom Search Parameters

```python
def advanced_search(query, location="in", language="hi"):
    """Advanced search with custom parameters"""
    
    params = {
        "q": query,
        "api_key": os.getenv("SERPAPI_KEY"),
        "hl": language,           # Language code
        "gl": location,           # Country code
        "num": 10,               # Number of results
        "safe": "active",        # Safe search
        "filter": "1",           # Filter results
        "tbm": "news"           # News search (optional)
    }
    
    search = GoogleSearch(params)
    return search.get_dict()

# Usage
results = advanced_search("मशीन लर्निंग", "in", "hi")
```

### 2. Different Search Types

```python
def search_examples():
    """Different types of searches"""
    
    api_key = os.getenv("SERPAPI_KEY")
    
    # Images Search
    image_params = {
        "q": "ताजमहल",
        "api_key": api_key,
        "tbm": "isch",           # Image search
        "hl": "hi"
    }
    
    # News Search
    news_params = {
        "q": "टेक्नोलॉजी न्यूज़",
        "api_key": api_key,
        "tbm": "nws",            # News search
        "hl": "hi"
    }
    
    # Videos Search
    video_params = {
        "q": "पायथन ट्यूटोरियल",
        "api_key": api_key,
        "tbm": "vid",            # Video search
        "hl": "hi"
    }
    
    return {
        "images": GoogleSearch(image_params).get_dict(),
        "news": GoogleSearch(news_params).get_dict(),
        "videos": GoogleSearch(video_params).get_dict()
    }
```

### 3. Pagination Implementation

```python
def paginated_search(query, pages=3):
    """Search with multiple pages"""
    
    api_key = os.getenv("SERPAPI_KEY")
    all_results = []
    
    for page in range(pages):
        params = {
            "q": query,
            "api_key": api_key,
            "hl": "hi",
            "start": page * 10,  # Page offset
            "num": 10
        }
        
        search = GoogleSearch(params)
        results = search.get_dict()
        
        page_results = results.get("organic_results", [])
        all_results.extend(page_results)
        
        print(f"📄 Page {page + 1}: {len(page_results)} results")
    
    return all_results

# Usage
all_results = paginated_search("पायथन प्रोग्रामिंग", 3)
print(f"कुल {len(all_results)} results मिले")
```

---

## ⚠️ Error Handling

### Professional Error Handling

```python
import logging
from typing import List, Dict, Optional

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SerpApiManager:
    """Professional SerpApi management class"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.max_retries = 3
        
    def safe_search(self, query: str, **kwargs) -> Optional[Dict]:
        """Safe search with retry logic"""
        
        for attempt in range(self.max_retries):
            try:
                params = {
                    "q": query,
                    "api_key": self.api_key,
                    "hl": "hi",
                    **kwargs
                }
                
                search = GoogleSearch(params)
                results = search.get_dict()
                
                # Validate results
                if "error" in results:
                    raise Exception(f"SerpApi Error: {results['error']}")
                    
                return results
                
            except Exception as e:
                logger.warning(f"Attempt {attempt + 1} failed: {e}")
                
                if attempt == self.max_retries - 1:
                    logger.error(f"All {self.max_retries} attempts failed")
                    return None
                    
                # Wait before retry
                import time
                time.sleep(2 ** attempt)  # Exponential backoff
    
    def get_organic_results(self, query: str) -> List[Dict]:
        """Get organic results only"""
        
        results = self.safe_search(query)
        
        if not results:
            return []
            
        return results.get("organic_results", [])

# Usage
manager = SerpApiManager(os.getenv("SERPAPI_KEY"))
organic_results = manager.get_organic_results("डेटा साइंस")
```

---

## 🎪 Practical Examples

### Example 1: Hindi Blog Content Finder

```python
def find_hindi_blogs(topic: str, min_results: int = 5):
    """Hindi blogs find करने के लिए"""
    
    manager = SerpApiManager(os.getenv("SERPAPI_KEY"))
    
    # Hindi blog search
    params = {
        "q": f"{topic} हिंदी ब्लॉग",
        "hl": "hi",
        "gl": "in"
    }
    
    results = manager.safe_search(f"{topic} हिंदी ब्लॉग", **params)
    
    if not results:
        return []
    
    organic_results = results.get("organic_results", [])
    
    # Filter Hindi content
    hindi_results = []
    for result in organic_results:
        title = result.get("title", "").lower()
        snippet = result.get("snippet", "").lower()
        
        # Check for Hindi content
        if any(word in title or word in snippet for word in ["हिंदी", "ब्लॉग", "ट्यूटोरियल"]):
            hindi_results.append(result)
    
    return hindi_results[:min_results]

# Usage
hindi_blogs = find_hindi_blogs("पायथन")
for blog in hindi_blogs:
    print(f"📝 {blog['title']}")
    print(f"🔗 {blog['link']}")
```

### Example 2: Educational Content Aggregator

```python
class EducationalContentAggregator:
    """Educational content aggregator for Hindi students"""
    
    def __init__(self):
        self.manager = SerpApiManager(os.getenv("SERPAPI_KEY"))
    
    def get_study_materials(self, subject: str, level: str = "beginner"):
        """Study materials collect करें"""
        
        queries = [
            f"{subject} हिंदी ट्यूटोरियल {level}",
            f"{subject} भारतीय छात्रों के लिए",
            f"{subject} हिंदी में समझाएं"
        ]
        
        all_materials = []
        
        for query in queries:
            results = self.manager.get_organic_results(query)
            all_materials.extend(results)
        
        # Remove duplicates
        unique_materials = []
        seen_links = set()
        
        for material in all_materials:
            link = material.get("link", "")
            if link not in seen_links:
                unique_materials.append(material)
                seen_links.add(link)
        
        return unique_materials
    
    def categorize_content(self, materials: List[Dict]):
        """Content को categories में divide करें"""
        
        categories = {
            "ट्यूटोरियल": [],
            "वीडियो": [],
            "ब्लॉग": [],
            "दस्तावेज़": []
        }
        
        for material in materials:
            title = material.get("title", "").lower()
            link = material.get("link", "").lower()
            
            if "tutorial" in title or "ट्यूटोरियल" in title:
                categories["ट्यूटोरियल"].append(material)
            elif "youtube" in link or "वीडियो" in title:
                categories["वीडियो"].append(material)
            elif "blog" in title or "ब्लॉग" in title:
                categories["ब्लॉग"].append(material)
            else:
                categories["दस्तावेज़"].append(material)
        
        return categories

# Usage
aggregator = EducationalContentAggregator()
materials = aggregator.get_study_materials("पायथन")
categories = aggregator.categorize_content(materials)

for category, items in categories.items():
    print(f"\n📚 {category} ({len(items)} items):")
    for item in items[:3]:  # Show first 3 items
        print(f"  • {item['title']}")
```

---

## 🏆 Best Practices

### 1. API Key Security

```python
# ✅ Good: Environment variable use
api_key = os.getenv("SERPAPI_KEY")

# ❌ Bad: Hardcoded API key
# api_key = "your_actual_api_key_here"

# ✅ Good: Configuration management
class Config:
    SERPAPI_KEY = os.getenv("SERPAPI_KEY")
    DEFAULT_LANGUAGE = "hi"
    DEFAULT_LOCATION = "in"
    MAX_RETRIES = 3
```

### 2. Rate Limiting

```python
import time
from datetime import datetime, timedelta

class RateLimitedSerpApi:
    """Rate limiting के साथ SerpApi"""
    
    def __init__(self, api_key: str, calls_per_minute: int = 60):
        self.api_key = api_key
        self.calls_per_minute = calls_per_minute
        self.call_times = []
    
    def search_with_rate_limit(self, query: str, **kwargs):
        """Rate limit के साथ search"""
        
        # Rate limit check
        now = datetime.now()
        recent_calls = [t for t in self.call_times if now - t < timedelta(minutes=1)]
        
        if len(recent_calls) >= self.calls_per_minute:
            sleep_time = 60 - (now - recent_calls[0]).seconds
            print(f"⏰ Rate limit reached, sleeping {sleep_time} seconds...")
            time.sleep(sleep_time)
        
        # Make API call
        self.call_times.append(now)
        params = {"q": query, "api_key": self.api_key, **kwargs}
        
        search = GoogleSearch(params)
        return search.get_dict()
```

### 3. Caching Implementation

```python
import json
import hashlib
from pathlib import Path

class CachedSerpApi:
    """Caching के साथ SerpApi"""
    
    def __init__(self, api_key: str, cache_dir: str = "cache"):
        self.api_key = api_key
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
    
    def _get_cache_key(self, query: str, **kwargs) -> str:
        """Cache key generate करें"""
        key_data = f"{query}_{sorted(kwargs.items())}"
        return hashlib.md5(key_data.encode()).hexdigest()
    
    def cached_search(self, query: str, use_cache: bool = True, **kwargs):
        """Cached search perform करें"""
        
        cache_key = self._get_cache_key(query, **kwargs)
        cache_file = self.cache_dir / f"{cache_key}.json"
        
        # Check cache
        if use_cache and cache_file.exists():
            with open(cache_file, 'r', encoding='utf-8') as f:
                print(f"📁 Cache hit for: {query}")
                return json.load(f)
        
        # Make API call
        params = {"q": query, "api_key": self.api_key, **kwargs}
        search = GoogleSearch(params)
        results = search.get_dict()
        
        # Save to cache
        with open(cache_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        print(f"🌐 Fresh API call for: {query}")
        return results
```

---

## 🎯 Real-World Project Ideas

### 1. Hindi Educational Platform
```python
# Student के लिए personalized study materials
def generate_study_plan(student_level: str, subjects: List[str]):
    """Personalized study plan generate करें"""
    
    plan = {}
    for subject in subjects:
        materials = find_hindi_blogs(subject)
        plan[subject] = materials[:3]  # Top 3 resources
    
    return plan
```

### 2. Content Research Tool
```python
# Bloggers और content creators के लिए
def content_research_tool(topic: str, target_audience: str):
    """Content research करें"""
    
    queries = [
        f"{topic} {target_audience} के लिए",
        f"{topic} हिंदी में",
        f"{topic} trends 2024"
    ]
    
    research_data = {}
    for query in queries:
        results = manager.get_organic_results(query)
        research_data[query] = results[:5]
    
    return research_data
```

---

## 📝 Summary

### इस ट्यूटोरियल में सीखा:

1. ✅ **Basic SerpApi integration**
2. ✅ **Hindi language search**
3. ✅ **Error handling और retry logic**
4. ✅ **Advanced search parameters**
5. ✅ **Rate limiting और caching**
6. ✅ **Real-world applications**
7. ✅ **Professional development practices**

### Next Steps:
- 📚 [Node.js Tutorial](../nodejs/README.md)
- 🔧 [CLI Tool Tutorial](../cli-tool/README.md)
- 🌐 [Main Project](../../SerpSearch-CLI-Web-Dashboard/)

---

## 🤝 Community

### Hindi Developer Community:
- Join [Hindi Python Community](https://t.me/hindipython)
- Follow [Hindi Tech Bloggers](https://blog.example.com/hindi)
- Contribute to [Hindi Open Source](https://github.com/topics/hindi)

### Help & Support:
- 📧 Email: support@example.com
- 💬 Discord: [Hindi Developers](https://discord.gg/hindi)
- 🐛 Issues: [GitHub Issues](https://github.com/issues/new)

---

<div align="center">

### 🇮🇳 **Made with ❤️ for Indian Developers**

### 🐍 **Python से SerpApi Mastery**

### 🚀 **Happy Coding!**

</div>