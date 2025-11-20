# 🚗 Road Safety Intervention GPT

An intelligent road safety chatbot that provides professional IRC-compliant recommendations for traffic safety interventions. Built for the National Road Safety Hackathon 2025 at IIT Madras.

## ✨ Features

- 🎯 **Instant Recommendations** - No waiting, no API calls needed
- 📚 **IRC Standards Compliant** - Based on IRC 35, 67, 99, SP 84, SP 87, SP 88
- 💻 **100% Offline** - Works without internet connection
- 🚀 **Zero Setup** - Just open and use
- 🆓 **Completely Free** - No API keys, no subscriptions
- 🌐 **Browser-Based** - Works on any device with a web browser
- 📱 **Responsive Design** - Desktop, tablet, and mobile friendly

## 🎮 Two Usage Options

### Option 1: Standalone HTML (Recommended - No Setup!)

**Perfect for:**
- Quick demos and presentations
- Offline environments
- Users without technical background
- Instant deployment

**How to use:**
1. Download `standalone.html`
2. Double-click to open in any browser
3. Start getting recommendations immediately!

### Option 2: Flask Web Application (Optional)

**For developers who want to:**
- Customize the interface
- Add database integration
- Deploy on a web server
- Extend functionality

**Requires:** Python 3.11+, Flask

---

## 🚀 Quick Start (No Installation!)

### Easiest Method: Standalone HTML

1. **Download the file:**
   - Download `standalone.html` from this repository
   
2. **Open it:**
   - Double-click `standalone.html`
   - It opens in your default browser
   
3. **Start using:**
   - Type your road safety issue
   - Click "Get AI Recommendations"
   - Receive instant IRC-compliant solutions!

✅ **That's it! No installation, no configuration, no API keys!**

---

## 📦 Installation (For Flask Version)

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/vidhyabme3197/road-safety-gpt.git
cd road-safety-gpt
```

### Step 2: Install Dependencies
```bash
pip install flask
```

### Step 3: Run the Application
```bash
python app.py
```

Then open: http://localhost:5000

---

## 🏗️ Project Structure
```
road-safety-gpt/
├── standalone.html        # 🌟 Main standalone version (recommended!)
├── app.py                 # Flask web application
├── chatbot.py             # Command-line interface
├── main.py                # Alternative entry point
├── requirements.txt       # Python dependencies (only Flask)
├── README.md              # This file
├── .gitignore            # Git ignore rules
├── templates/
│   └── index.html        # Flask template
└── data/                 # Optional data files
```

---

## 🎯 Supported Use Cases

### 1. 🛣️ Sharp Curve Safety
**Input:** "Sharp curves causing accidents at night on National Highway"

**Recommendations:**
- Curve warning signs (IRC:67)
- Chevron alignment markers (IRC:35)
- Street lighting improvements (IRC:SP:84)
- Anti-skid surface treatment
- Speed control measures (IRC:99)

### 2. 🏫 School Zone Safety
**Input:** "Pedestrian accidents near school zone in urban area"

**Recommendations:**
- School zone warning signs
- Pedestrian crossings with signals
- Speed humps and traffic calming
- Drop-off zone designation
- Safety barriers and CCTV

### 3. ⚡ Speed Control
**Input:** "Speeding vehicles on residential roads"

**Recommendations:**
- Speed limit signage (IRC:67)
- Speed cameras and enforcement
- Rumble strips (IRC:99)
- Road narrowing techniques
- LED speed displays

### 4. 🚦 Intersection Safety
**Input:** "Poor visibility at intersection during fog"

**Recommendations:**
- Modern traffic signals (IRC:93)
- High-intensity lighting (IRC:SP:84)
- Reflective road markings (IRC:35)
- CCTV surveillance
- Pedestrian safety infrastructure

### 5. 🌙 Night-time Safety
**Input:** "Low visibility causing accidents at night"

**Recommendations:**
- Street lighting installation
- Reflective road markings and cat-eyes
- Delineator posts
- High-reflectivity signs (IRC:67)
- Vegetation clearance

---

## 🔧 How It Works

### Intelligent Pattern Matching System

The application uses keyword-based pattern recognition to identify road safety issues:
```javascript
User Query → Keyword Analysis → Match Safety Category → Return IRC-Compliant Solutions
```

**Categories detected:**
- Curves and bends
- School zones
- Speed control
- Intersections
- Night visibility
- Pedestrian safety
- General road safety

**Each recommendation includes:**
- ✅ Specific intervention steps
- ✅ Relevant IRC standard references
- ✅ Estimated cost ranges
- ✅ Implementation timeline
- ✅ Maintenance considerations

---

## 📊 Technology Stack

- **Frontend:** HTML5, CSS3, JavaScript
- **Backend (Optional):** Python, Flask
- **Standards:** IRC (Indian Road Congress) Guidelines
- **Deployment:** Static HTML (no server required!)

---

## 📚 IRC Standards Referenced

Our recommendations are based on official IRC standards:

| Standard | Title | Application |
|----------|-------|-------------|
| IRC:35 | Road Markings | Lane markings, zebra crossings, reflective materials |
| IRC:67 | Road Signs | Warning signs, regulatory signs, information boards |
| IRC:93 | Traffic Signals | Signal design, timing, placement guidelines |
| IRC:99 | Speed Control | Speed breakers, rumble strips, calming measures |
| IRC:SP:84 | Road Safety Audits | Safety assessment procedures |
| IRC:SP:87 | Manual for Road Safety | Comprehensive safety guidelines |
| IRC:SP:88 | Highway Safety Code | Standards and best practices |
| IRC:103 | Footpaths and Facilities | Pedestrian infrastructure |

---

## 💡 Example Queries

Try these queries to see the system in action:
```
1. "Sharp curves causing accidents at night on National Highway"
2. "Pedestrian accidents near school zone in urban area"
3. "Speeding vehicles on residential roads causing safety concerns"
4. "Poor visibility at intersection during fog"
5. "Frequent accidents on highway during monsoon season"
6. "Uncontrolled intersection with multiple vehicle conflicts"
7. "Two-wheeler accidents at railway crossing"
8. "Blind spot issues at T-junction in residential area"
```

---

## 🎨 Features Highlight

### ✨ User Interface
- Clean, modern design
- Intuitive navigation
- Responsive layout
- Example queries for quick testing
- Instant results display

### 🎯 Recommendations Quality
- IRC standard-compliant
- Cost estimates included
- Implementation timelines
- Practical and actionable
- Context-aware suggestions

### ⚡ Performance
- Instant response time
- No server delays
- Works offline
- No dependencies
- Lightweight (< 20KB)

---

## 🚀 Deployment Options

### 1. Local Use (Double-click)
- Download `standalone.html`
- Open in any browser
- Use immediately

### 2. GitHub Pages (Free Hosting)
- Fork this repository
- Go to Settings → Pages
- Enable GitHub Pages
- Your site will be live at: `https://username.github.io/road-safety-gpt`

### 3. Flask Server (For Development)
```bash
python app.py
```

### 4. Share via USB/Email
- Copy `standalone.html` to USB drive
- Share via email attachment
- Recipients can open and use immediately

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Report Issues:** Found a bug? Open an issue!
2. **Suggest Features:** Have ideas? We'd love to hear them!
3. **Improve Documentation:** Help us make this README better
4. **Add More Scenarios:** Expand the knowledge base
5. **Submit Pull Requests:** Code contributions are appreciated!

---

## 📝 License

This project is open source and available under the MIT License.

---



---

## 🙏 Acknowledgments

- **Indian Road Congress (IRC)** - For comprehensive road safety standards and guidelines
- **Ministry of Road Transport and Highways, India** - For road safety initiatives
- All contributors and testers who helped improve this tool

---



---

## 🎉 Why This Tool?

### The Problem
Road safety engineers need quick, standardized recommendations based on IRC guidelines. Traditional methods require:
- Manual reference of multiple IRC documents
- Time-consuming analysis
- Risk of missing relevant standards
- Inconsistent recommendations

### Our Solution
- ✅ Instant IRC-compliant recommendations
- ✅ Zero learning curve - just type and get results
- ✅ Comprehensive coverage of common scenarios
- ✅ Professional-grade outputs with cost estimates
- ✅ Works anywhere, anytime, even offline

---

## 📈 Future Enhancements

Planned features for future versions:
- [ ] More safety scenarios (railway crossings, flyovers, etc.)
- [ ] Regional language support (Hindi, Tamil, etc.)
- [ ] PDF report generation
- [ ] Image upload for site analysis
- [ ] Cost calculator based on region
- [ ] 3D visualization of interventions
- [ ] Mobile app version

---

