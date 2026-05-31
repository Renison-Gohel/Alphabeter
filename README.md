# ⚡ ALPHABETER

> **Advanced OSINT Framework for Google Infrastructure Analysis**

Alphabeter is a specialized reconnaissance tool designed for deep analysis of Google accounts, infrastructure, and associated digital footprints. Built for speed, efficiency, and stealth.

---

## 🛠 Features

- **Profile Extraction**: Deep-dive into Gaia IDs and public profile metadata.
- **Service Mapping**: Identify active Google services linked to targets.
- **Geographic Intelligence**: Advanced BSSID geolocation capabilities.
- **Drive & Calendar Forensics**: Analyze public file sharing and calendar visibility.
- **Infrastructure Spidering**: Discover assets via Digital Assets Links.
- **Async Engine**: Fully asynchronous requests for high-performance scanning.

---

## 🚀 Quick Start

### Installation

Ensure you have Python 3.10+ installed.

```bash
git clone https://github.com/Renison-Gohel/Alphabeter.git
cd Alphabeter
pip install .
```

### 🔑 Authentication & Handshake

To interact with restricted Google APIs, Alphabeter requires a valid session handshake. Use the integrated **Alphabeter Companion** extension for seamless synchronization.

1. **Initialize Login**: Run the login command in your terminal:
   ```bash
   alphabeter login
   ```
2. **Select Sync Method**: When prompted, choose **Option [2]** (Handshake Synchronization):
   - Open your browser and ensure you are logged into the target Google account.
   - Click the **Alphabeter Companion** icon in your toolbar.
   - Click the **"Synchronize to Alphabeter"** button.
   - Copy the generated base64 handshake string.
3. **Authorize**: Paste the string back into your terminal to complete the authentication flow.

---

## 📖 Operational Usage

### Target Email Analysis
```bash
alphabeter email target@gmail.com
```

### Gaia ID Lookup
```bash
alphabeter gaia 103739321269930414867
```

### Drive File Inspection
```bash
alphabeter drive <file_id>
```

### Global Data Export
Export any module results to JSON for further analysis:
```bash
alphabeter email target@gmail.com --json results.json
```

---

## 🛡 Disclaimer

**For authorized security testing and educational purposes only.** 
Usage of Alphabeter for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. The developers assume no liability and are not responsible for any misuse or damage caused by this program.

---

## 🔗 Project Info

- **Version**: 2.3.4 (Spider Edition)
- **License**: AGPL-3.0
- **Lead Developer**: RC
- **Core Engine**: Python 3.13 Compatible

---
<p align="center">Built for the shadows. 🌑</p>
