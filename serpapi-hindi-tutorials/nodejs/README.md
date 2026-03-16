# 🟢 Node.js से SerpApi का उपयोग कैसे करें

[![Node.js](https://img.shields.io/badge/Node.js-18+-green?style=for-the-badge&logo=node.js)](https://nodejs.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow?style=for-the-badge&logo=javascript)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![SerpApi](https://img.shields.io/badge/SerpApi-Hindi_Tutorial-green?style=for-the-badge&logo=google)](https://serpapi.com/)

> **हिंदी भाषा में SerpApi Node.js ट्यूटोरियल**  
> भारतीय JavaScript डेवलपर्स के लिए complete guide

---

## 📋 विषय सूची

1. [परिचय](#-परिचय)
2. [आवश्यकताएं](#-आवश्यकताएं)
3. [Installation और Setup](#-installation-और-setup)
4. [पहला SerpApi Program](#-पहला-serpapi-program)
5. [Advanced Features](#-advanced-features)
6. [Express.js Integration](#expressjs-integration)
7. [Error Handling](#-error-handling)
8. [Real-World Applications](#-real-world-applications)

---

## 🌟 परिचय

Node.js के साथ SerpApi का उपयोग करके आप powerful server-side applications बना सकते हैं जो Google search results को real-time में process कर सकें। इस ट्यूटोरियल में हम step-by-step सीखेंगे कि कैसे Node.js और JavaScript का उपयोग करके SerpApi को integrate करें।

### 🎯 इस ट्यूटोरियल में क्या सीखेंगे:

- Node.js में SerpApi integration
- RESTful API development
- Hindi language search support
- Async/await patterns
- Express.js web applications
- Professional error handling

---

## 📦 आवश्यकताएं

### Basic Requirements:
- **Node.js 18+** installed
- **npm या yarn** package manager
- **SerpApi Account** (Free available)
- **Basic JavaScript knowledge**
- **VS Code** (recommended)

### Node.js Installation Check:
```bash
# Node.js version check
node --version  # Should be 18.x or higher

# npm version check  
npm --version   # Should be 9.x or higher
```

---

## 🚀 Installation और Setup

### Step 1: Project Initialize करें

```bash
# New project folder बनाएं
mkdir serpapi-nodejs-project
cd serpapi-nodejs-project

# npm project initialize करें
npm init -y

# Basic project structure
mkdir src tests
touch src/index.js src/search.js .env .gitignore
```

### Step 2: Dependencies Install करें

```bash
# Core dependencies
npm install axios dotenv

# Development dependencies
npm install --save-dev nodemon jest

# या yarn का उपयोग करें
yarn add axios dotenv
yarn add --dev nodemon jest
```

### Step 3: Environment Setup

```bash
# .env file बनाएं
echo "SERPAPI_KEY=your_api_key_here" > .env

# .gitignore file
echo "node_modules/
.env
cache/
.DS_Store" > .gitignore
```

### Step 4: package.json Scripts Add करें

```json
{
  "scripts": {
    "start": "node src/index.js",
    "dev": "nodemon src/index.js",
    "test": "jest",
    "search": "node src/search.js"
  }
}
```

---

## 🎯 पहला SerpApi Program

### Basic Search Implementation

```javascript
// src/search.js
require('dotenv').config();
const axios = require('axios');

class SerpApiSearch {
    constructor(apiKey = null) {
        this.apiKey = apiKey || process.env.SERPAPI_KEY;
        this.baseUrl = 'https://serpapi.com/search';
        
        if (!this.apiKey) {
            throw new Error('❌ SERPAPI_KEY environment variable required!');
        }
    }

    async search(query, options = {}) {
        try {
            const params = {
                q: query,
                api_key: this.apiKey,
                hl: 'hi',           // Hindi language
                gl: 'in',           // India location
                ...options
            };

            console.log(`🔍 "${query}" के लिए खोज रहे हैं...`);
            
            const response = await axios.get(this.baseUrl, { params });
            const results = response.data;

            if (results.error) {
                throw new Error(`SerpApi Error: ${results.error}`);
            }

            return this.formatResults(results);
            
        } catch (error) {
            console.error('❌ Search Error:', error.message);
            throw error;
        }
    }

    formatResults(results) {
        const organicResults = results.organic_results || [];
        
        return {
            query: results.search_parameters?.q,
            totalResults: organicResults.length,
            results: organicResults.map((result, index) => ({
                position: index + 1,
                title: result.title,
                link: result.link,
                snippet: result.snippet,
                displayed_link: result.displayed_link
            }))
        };
    }

    async printResults(query, options = {}) {
        try {
            const searchResults = await this.search(query, options);
            
            console.log('\n🎯 खोज परिणाम:');
            console.log('='.repeat(60));
            
            if (searchResults.results.length === 0) {
                console.log('कोई परिणाम नहीं मिला।');
                return;
            }

            searchResults.results.forEach(result => {
                console.log(`\n${result.position}. ${result.title}`);
                console.log(`   🔗 ${result.link}`);
                if (result.snippet) {
                    console.log(`   📝 ${result.snippet.substring(0, 120)}...`);
                }
            });

            console.log(`\n✅ कुल ${searchResults.totalResults} परिणाम मिले।`);
            
        } catch (error) {
            console.error('❌ Results printing failed:', error.message);
        }
    }
}

// Direct usage
if (require.main === module) {
    const searchQuery = process.argv[2] || 'कृत्रिम बुद्धिमत्ता';
    
    const serpApi = new SerpApiSearch();
    serpApi.printResults(searchQuery);
}

module.exports = SerpApiSearch;
```

### Program Run करें:

```bash
# Direct run
node src/search.js "मशीन लर्निंग"

# या npm script के साथ
npm search "पायथन प्रोग्रामिंग"
```

**Expected Output:**
```
🔍 "मशीन लर्निंग" के लिए खोज रहे हैं...

🎯 खोज परिणाम:
============================================================

1. मशीन लर्निंग क्या है? - हिंदी गाइड
   🔗 https://example.com/machine-learning-hindi
   📝 मशीन लर्निंग एक AI का अहम हिस्सा है...

2. Machine Learning Tutorial in Hindi
   🔗 https://youtube.com/watch?v=example
   📝 यह video में machine learning को हिंदी में...

✅ कुल 10 परिणाम मिले।
```

---

## 🔥 Advanced Features

### 1. Advanced Search Class

```javascript
// src/advanced-search.js
const SerpApiSearch = require('./search');

class AdvancedSerpApi extends SerpApiSearch {
    constructor(apiKey) {
        super(apiKey);
        this.cache = new Map();
    }

    async newsSearch(query, options = {}) {
        """News search के लिए"""
        return this.search(query, {
            tbm: 'nws',           // News search
            ...options
        });
    }

    async imageSearch(query, options = {}) {
        """Image search के लिए"""
        return this.search(query, {
            tbm: 'isch',          // Image search
            ...options
        });
    }

    async videoSearch(query, options = {}) {
        """Video search के लिए"""
        return this.search(query, {
            tbm: 'vid',           // Video search
            ...options
        });
    }

    async shoppingSearch(query, options = {}) {
        """Shopping search के लिए"""
        return this.search(query, {
            tbm: 'shop',          // Shopping search
            ...options
        });
    }

    async cachedSearch(query, options = {}) {
        """Cached search implementation"""
        const cacheKey = `${query}_${JSON.stringify(options)}`;
        
        if (this.cache.has(cacheKey)) {
            console.log('📁 Cache hit!');
            return this.cache.get(cacheKey);
        }

        const results = await this.search(query, options);
        this.cache.set(cacheKey, results);
        
        return results;
    }

    async batchSearch(queries, options = {}) {
        """Multiple queries को parallel में search करें"""
        const searchPromises = queries.map(query => 
            this.search(query, options)
        );

        const results = await Promise.allSettled(searchPromises);
        
        return results.map((result, index) => ({
            query: queries[index],
            status: result.status,
            data: result.status === 'fulfilled' ? result.value : null,
            error: result.status === 'rejected' ? result.reason : null
        }));
    }
}

// Usage examples
async function demonstrateAdvancedFeatures() {
    const advanced = new AdvancedSerpApi();
    
    try {
        // News search
        console.log('📰 News Search:');
        const newsResults = await advanced.newsSearch('टेक्नोलॉजी न्यूज़');
        
        // Image search
        console.log('🖼️ Image Search:');
        const imageResults = await advanced.imageSearch('ताजमहल');
        
        // Batch search
        console.log('🔄 Batch Search:');
        const batchResults = await advanced.batchSearch([
            'पायथन',
            'जावा',
            'जावास्क्रिप्ट'
        ]);
        
        batchResults.forEach(result => {
            console.log(`${result.query}: ${result.status}`);
        });
        
    } catch (error) {
        console.error('❌ Advanced search error:', error.message);
    }
}

module.exports = AdvancedSerpApi;
```

### 2. Search Filters और Options

```javascript
// src/search-filters.js
const AdvancedSerpApi = require('./advanced-search');

class SearchFilters extends AdvancedSerpApi {
    
    async searchWithFilters(query, filters = {}) {
        """Advanced filters के साथ search"""
        
        const defaultFilters = {
            hl: 'hi',              // Hindi language
            gl: 'in',              // India location
            num: 10,               // 10 results
            safe: 'active',        // Safe search
            filter: '1'            // Filter similar results
        };

        const searchParams = { ...defaultFilters, ...filters };
        
        return this.search(query, searchParams);
    }

    async locationBasedSearch(query, location = 'in') {
        """Location-based search"""
        return this.searchWithFilters(query, {
            gl: location,
            uule: `+w+CAIQICINVXJpbGF5YW5h`  # Location encoded
        });
    }

    async timeBasedSearch(query, timeRange = 'y') {
        """Time-based search filters
        y = past year
        m = past month  
        w = past week
        d = past day
        """
        return this.searchWithFilters(query, {
            tbs: `qdr:${timeRange}`
        });
    }

    async fileTypeSearch(query, fileType = 'pdf') {
        """Specific file type search"""
        return this.searchWithFilters(`${query} filetype:${fileType}`);
    }

    async siteSpecificSearch(query, site) {
        """Specific website search"""
        return this.searchWithFilters(`${query} site:${site}`);
    }

    async priceRangeSearch(query, minPrice, maxPrice) {
        """Price range search for shopping"""
        return this.searchWithFilters(query, {
            tbs: `p_ord:cr,p_price:${minPrice}-${maxPrice}`,
            tbm: 'shop'
        });
    }
}

// Usage examples
async function filterExamples() {
    const filters = new SearchFilters();
    
    try {
        // Location-based search
        console.log('📍 USA Search:');
        const usResults = await filters.locationBasedSearch('artificial intelligence', 'us');
        
        // Time-based search
        console.log('⏰ Recent News:');
        const recentNews = await filters.timeBasedSearch('blockchain technology', 'w');
        
        // File type search
        console.log('📄 PDF Documents:');
        const pdfDocs = await filters.fileTypeSearch('machine learning research');
        
        // Site-specific search
        console.log('🌐 Government Sites:');
        const govResults = await filters.siteSpecificSearch('digital india', 'gov.in');
        
    } catch (error) {
        console.error('❌ Filter search error:', error.message);
    }
}

module.exports = SearchFilters;
```

---

## 🌐 Express.js Integration

### RESTful API Server

```javascript
// src/api-server.js
require('dotenv').config();
const express = require('express');
const cors = require('cors');
const rateLimit = require('express-rate-limit');
const SearchFilters = require('./search-filters');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());

// Rate limiting
const limiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 100 // limit each IP to 100 requests per windowMs
});
app.use('/api/', limiter);

// Initialize search
const searchEngine = new SearchFilters();

// Routes
app.get('/', (req, res) => {
    res.json({
        message: '🚀 SerpApi Hindi Search Server',
        version: '1.0.0',
        endpoints: {
            search: '/api/search',
            news: '/api/news',
            images: '/api/images',
            filters: '/api/filters'
        }
    });
});

app.post('/api/search', async (req, res) => {
    try {
        const { query, options = {} } = req.body;
        
        if (!query) {
            return res.status(400).json({
                error: '❌ Query parameter required',
                message: 'कृपया खोज query provide करें'
            });
        }

        const results = await searchEngine.searchWithFilters(query, options);
        
        res.json({
            success: true,
            query,
            results: results.results,
            total: results.totalResults,
            timestamp: new Date().toISOString()
        });
        
    } catch (error) {
        res.status(500).json({
            error: 'Search failed',
            message: error.message,
            timestamp: new Date().toISOString()
        });
    }
});

app.post('/api/news', async (req, res) => {
    try {
        const { query } = req.body;
        
        if (!query) {
            return res.status(400).json({
                error: '❌ Query required for news search'
            });
        }

        const results = await searchEngine.newsSearch(query);
        
        res.json({
            success: true,
            type: 'news',
            query,
            results: results.results,
            total: results.totalResults
        });
        
    } catch (error) {
        res.status(500).json({
            error: 'News search failed',
            message: error.message
        });
    }
});

app.post('/api/batch', async (req, res) => {
    try {
        const { queries } = req.body;
        
        if (!Array.isArray(queries) || queries.length === 0) {
            return res.status(400).json({
                error: '❌ Queries array required'
            });
        }

        const results = await searchEngine.batchSearch(queries);
        
        res.json({
            success: true,
            batchSize: queries.length,
            results: results
        });
        
    } catch (error) {
        res.status(500).json({
            error: 'Batch search failed',
            message: error.message
        });
    }
});

// Health check endpoint
app.get('/api/health', (req, res) => {
    res.json({
        status: '✅ Healthy',
        timestamp: new Date().toISOString(),
        uptime: process.uptime()
    });
});

// Error handling middleware
app.use((error, req, res, next) => {
    console.error('❌ Server Error:', error);
    res.status(500).json({
        error: 'Internal server error',
        message: 'कुछ गलत हो गया, कृपया बाद में try करें'
    });
});

// Start server
app.listen(PORT, () => {
    console.log(`🚀 SerpApi Server running on port ${PORT}`);
    console.log(`🌐 http://localhost:${PORT}`);
    console.log(`📊 Health: http://localhost:${PORT}/api/health`);
});

module.exports = app;
```

### API Testing Script

```javascript
// src/test-api.js
const axios = require('axios');

const API_BASE = 'http://localhost:3000/api';

async function testAPI() {
    try {
        console.log('🧪 API Testing Started...\n');

        // Test basic search
        console.log('1️⃣ Testing Basic Search:');
        const searchResponse = await axios.post(`${API_BASE}/search`, {
            query: 'कृत्रिम बुद्धिमत्ता'
        });
        console.log('✅ Search Response:', searchResponse.data.success);

        // Test news search
        console.log('\n2️⃣ Testing News Search:');
        const newsResponse = await axios.post(`${API_BASE}/news`, {
            query: 'टेक्नोलॉजी'
        });
        console.log('✅ News Response:', newsResponse.data.success);

        // Test batch search
        console.log('\n3️⃣ Testing Batch Search:');
        const batchResponse = await axios.post(`${API_BASE}/batch`, {
            queries: ['पायथन', 'जावा', 'node.js']
        });
        console.log('✅ Batch Response:', batchResponse.data.batchSize);

        // Test health check
        console.log('\n4️⃣ Testing Health Check:');
        const healthResponse = await axios.get(`${API_BASE}/health`);
        console.log('✅ Health Status:', healthResponse.data.status);

        console.log('\n🎉 All API tests passed!');

    } catch (error) {
        console.error('❌ API Test Failed:', error.response?.data || error.message);
    }
}

// Run tests
if (require.main === module) {
    testAPI();
}

module.exports = { testAPI };
```

---

## ⚠️ Error Handling

### Professional Error Management

```javascript
// src/error-handler.js
class SerpApiError extends Error {
    constructor(message, code = 'SERPAPI_ERROR', details = null) {
        super(message);
        this.name = 'SerpApiError';
        this.code = code;
        this.details = details;
        this.timestamp = new Date().toISOString();
    }
}

class RateLimitError extends SerpApiError {
    constructor(message, retryAfter = null) {
        super(message, 'RATE_LIMIT_ERROR');
        this.retryAfter = retryAfter;
    }
}

class ErrorHandler {
    static async safeApiCall(apiCall, ...args) {
        try {
            const result = await apiCall(...args);
            return { success: true, data: result };
        } catch (error) {
            return ErrorHandler.handleApiError(error);
        }
    }

    static handleApiError(error) {
        if (error.response) {
            // HTTP error
            const status = error.response.status;
            const message = error.response.data?.message || error.message;
            
            switch (status) {
                case 400:
                    return { 
                        success: false, 
                        error: new SerpApiError('Bad Request', 'BAD_REQUEST', message) 
                    };
                case 401:
                    return { 
                        success: false, 
                        error: new SerpApiError('Invalid API Key', 'INVALID_API_KEY') 
                    };
                case 429:
                    const retryAfter = error.response.headers['retry-after'];
                    return { 
                        success: false, 
                        error: new RateLimitError('Rate limit exceeded', retryAfter) 
                    };
                case 500:
                    return { 
                        success: false, 
                        error: new SerpApiError('Server Error', 'SERVER_ERROR', message) 
                    };
                default:
                    return { 
                        success: false, 
                        error: new SerpApiError(`HTTP ${status}`, 'HTTP_ERROR', message) 
                    };
            }
        } else if (error.code === 'ENOTFOUND') {
            return { 
                success: false, 
                error: new SerpApiError('Network error', 'NETWORK_ERROR') 
            };
        } else {
            return { 
                success: false, 
                error: new SerpApiError(error.message, 'UNKNOWN_ERROR') 
            };
        }
    }

    static async retryWithBackoff(apiCall, maxRetries = 3, ...args) {
        let lastError;
        
        for (let attempt = 1; attempt <= maxRetries; attempt++) {
            const result = await ErrorHandler.safeApiCall(apiCall, ...args);
            
            if (result.success) {
                return result;
            }
            
            lastError = result.error;
            
            // Don't retry on certain errors
            if (lastError.code === 'INVALID_API_KEY') {
                break;
            }
            
            // Exponential backoff
            if (attempt < maxRetries) {
                const delay = Math.pow(2, attempt) * 1000;
                console.log(`⏳ Retry ${attempt}/${maxRetries} in ${delay}ms...`);
                await new Promise(resolve => setTimeout(resolve, delay));
            }
        }
        
        return { success: false, error: lastError };
    }
}

// Usage example
const AdvancedSerpApi = require('./advanced-search');

class RobustSerpApi extends AdvancedSerpApi {
    async safeSearch(query, options = {}) {
        const result = await ErrorHandler.retryWithBackoff(
            super.search.bind(this),
            3,
            query,
            options
        );
        
        if (!result.success) {
            console.error('❌ Search failed after retries:', result.error.message);
            throw result.error;
        }
        
        return result.data;
    }
}

module.exports = {
    SerpApiError,
    RateLimitError,
    ErrorHandler,
    RobustSerpApi
};
```

---

## 🎪 Real-World Applications

### 1. Hindi Content Aggregator

```javascript
// src/content-aggregator.js
const RobustSerpApi = require('./error-handler').RobustSerpApi;

class HindiContentAggregator {
    constructor() {
        this.searchEngine = new RobustSerpApi();
    }

    async getEducationalContent(topic, level = 'beginner') {
        """Educational content collect करें"""
        
        const queries = [
            `${topic} हिंदी ट्यूटोरियल ${level}`,
            `${topic} हिंदी में समझाएं`,
            `${topic} भारतीय students के लिए`,
            `${topic} hindi explanation`
        ];

        const content = {
            tutorials: [],
            videos: [],
            articles: [],
            total: 0
        };

        for (const query of queries) {
            try {
                const results = await this.searchEngine.safeSearch(query);
                
                results.results.forEach(item => {
                    const contentType = this.categorizeContent(item);
                    
                    if (!content[contentType].find(existing => existing.link === item.link)) {
                        content[contentType].push({
                            ...item,
                            query: query,
                            relevance: this.calculateRelevance(item, query)
                        });
                    }
                });
                
            } catch (error) {
                console.warn(`⚠️ Failed to fetch "${query}":`, error.message);
            }
        }

        // Sort by relevance
        Object.keys(content).forEach(key => {
            if (key !== 'total') {
                content[key].sort((a, b) => b.relevance - a.relevance);
            }
        });

        content.total = content.tutorials.length + content.videos.length + content.articles.length;
        return content;
    }

    categorizeContent(item) {
        const title = item.title.toLowerCase();
        const link = item.link.toLowerCase();

        if (link.includes('youtube') || link.includes('video') || title.includes('वीडियो')) {
            return 'videos';
        } else if (title.includes('ट्यूटोरियल') || title.includes('tutorial') || title.includes('guide')) {
            return 'tutorials';
        } else {
            return 'articles';
        }
    }

    calculateRelevance(item, query) {
        let score = 0;
        const title = item.title.toLowerCase();
        const snippet = (item.snippet || '').toLowerCase();
        const queryWords = query.toLowerCase().split(' ');

        // Title matches
        queryWords.forEach(word => {
            if (title.includes(word)) score += 3;
            if (snippet.includes(word)) score += 1;
        });

        // Hindi content bonus
        if (this.containsHindi(title + snippet)) {
            score += 2;
        }

        // Educational keywords bonus
        const eduKeywords = ['ट्यूटोरियल', 'tutorial', 'guide', 'समझाएं', 'explain', 'learn'];
        eduKeywords.forEach(keyword => {
            if (title.includes(keyword)) score += 2;
        });

        return score;
    }

    containsHindi(text) {
        const hindiRegex = /[\u0900-\u097F]/;
        return hindiRegex.test(text);
    }

    async generateStudyPlan(subjects, studentLevel) {
        """Personalized study plan generate करें"""
        
        const studyPlan = {
            studentLevel,
            subjects: {},
            generatedAt: new Date().toISOString(),
            totalResources: 0
        };

        for (const subject of subjects) {
            console.log(`📚 Collecting content for ${subject}...`);
            
            try {
                const content = await this.getEducationalContent(subject, studentLevel);
                
                studyPlan.subjects[subject] = {
                    ...content,
                    recommendations: this.getRecommendations(content)
                };
                
                studyPlan.totalResources += content.total;
                
            } catch (error) {
                console.error(`❌ Failed to generate plan for ${subject}:`, error.message);
                studyPlan.subjects[subject] = {
                    error: error.message,
                    tutorials: [],
                    videos: [],
                    articles: [],
                    total: 0
                };
            }
        }

        return studyPlan;
    }

    getRecommendations(content) {
        const recommendations = [];
        
        if (content.tutorials.length > 0) {
            recommendations.push(`📖 "${content.tutorials[0].title}" से शुरुआत करें`);
        }
        
        if (content.videos.length > 0) {
            recommendations.push(`🎥 "${content.videos[0].title}" video देखें`);
        }
        
        if (content.articles.length > 2) {
            recommendations.push(`📚 ${content.articles.length} articles पढ़ें`);
        }
        
        return recommendations;
    }
}

// Usage example
async function demonstrateAggregator() {
    const aggregator = new HindiContentAggregator();
    
    try {
        // Study plan for multiple subjects
        const subjects = ['पायथन', 'जावा', 'वेब डेवलपमेंट'];
        const studyPlan = await aggregator.generateStudyPlan(subjects, 'beginner');
        
        console.log('🎯 Generated Study Plan:');
        console.log(`Level: ${studyPlan.studentLevel}`);
        console.log(`Total Resources: ${studyPlan.totalResources}`);
        
        Object.entries(studyPlan.subjects).forEach(([subject, data]) => {
            console.log(`\n${subject}:`);
            console.log(`  Tutorials: ${data.tutorials.length}`);
            console.log(`  Videos: ${data.videos.length}`);
            console.log(`  Articles: ${data.articles.length}`);
            
            if (data.recommendations.length > 0) {
                console.log('  Recommendations:');
                data.recommendations.forEach(rec => console.log(`    ${rec}`));
            }
        });
        
    } catch (error) {
        console.error('❌ Aggregator failed:', error.message);
    }
}

module.exports = HindiContentAggregator;
```

---

## 🏆 Best Practices

### 1. Environment Configuration

```javascript
// config/index.js
require('dotenv').config();

const config = {
    serpApi: {
        apiKey: process.env.SERPAPI_KEY,
        baseUrl: 'https://serpapi.com/search',
        timeout: parseInt(process.env.SERPAPI_TIMEOUT) || 10000,
        retries: parseInt(process.env.SERPAPI_RETRIES) || 3
    },
    
    server: {
        port: process.env.PORT || 3000,
        environment: process.env.NODE_ENV || 'development'
    },
    
    cache: {
        enabled: process.env.CACHE_ENABLED !== 'false',
        ttl: parseInt(process.env.CACHE_TTL) || 3600
    }
};

// Validation
if (!config.serpApi.apiKey) {
    throw new Error('❌ SERPAPI_KEY environment variable required!');
}

module.exports = config;
```

### 2. Logging System

```javascript
// utils/logger.js
const winston = require('winston');

const logger = winston.createLogger({
    level: process.env.LOG_LEVEL || 'info',
    format: winston.format.combine(
        winston.format.timestamp(),
        winston.format.errors({ stack: true }),
        winston.format.json()
    ),
    defaultMeta: { service: 'serpapi-hindi' },
    transports: [
        new winston.transports.File({ filename: 'logs/error.log', level: 'error' }),
        new winston.transports.File({ filename: 'logs/combined.log' })
    ]
});

if (process.env.NODE_ENV !== 'production') {
    logger.add(new winston.transports.Console({
        format: winston.format.simple()
    }));
}

module.exports = logger;
```

---

## 📝 Summary

### इस Node.js ट्यूटोरियल में सीखा:

1. ✅ **Basic SerpApi integration**
2. ✅ **Express.js REST API**
3. ✅ **Advanced search features**
4. ✅ **Professional error handling**
5. ✅ **Rate limiting और caching**
6. ✅ **Hindi content aggregation**
7. ✅ **Production-ready patterns**

### Next Steps:
- 📚 [Python Tutorial](../python/README.md)
- 🔧 [CLI Tool Tutorial](../cli-tool/README.md)
- 🌐 [Live Demo](https://your-app.herokuapp.com)

---

## 🤝 Community और Support

### Hindi Node.js Community:
- [Node.js Hindi](https://t.me/nodejshindi)
- [JavaScript India](https://t.me/javascriptindia)
- [Stack Overflow Hindi](https://stackoverflow.co/teams/hindi-devs)

### Help & Resources:
- 📧 Email: nodejs@example.com
- 💬 Discord: [Hindi Node.js](https://discord.gg/hindinode)
- 🐛 Issues: [GitHub Issues](https://github.com/issues/new)

---

<div align="center">

### 🟢 **Node.js से SerpApi Mastery**

### 🇮🇳 **Made with ❤️ for Indian JavaScript Developers**

### 🚀 **Happy Coding!**

</div>