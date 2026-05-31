# 🦖 ALPHABETER COMPANION

> **Stealth Session Synchronization for Google Infrastructure Analysis**

This browser extension is the official companion for the **Alphabeter** framework. It captures and synchronizes high-privilege session cookies to enable deep-dive reconnaissance without manual cookie extraction.

---

## 🛠 Features

- **Automated Sync**: One-click session transfer to the Alphabeter CLI.
- **Customized Auth Flow**: Visual indicator during Google login to confirm injection.
- **Stealth Mode**: Designed to capture cookies needed for GAPI calls.
- **Cross-Browser**: Compatible with all Chromium-based browsers and Firefox.

---

## 🚀 Local Installation (Hacker Style)

Since this is a specialized tool, we do not use public stores. Follow these steps to load the extension manually:

### For Chromium / Chrome / Brave / Edge:
1. Open your browser and navigate to `chrome://extensions/`.
2. Enable **"Developer mode"** in the top right corner.
3. Click **"Load unpacked"**.
4. Select the `Extension/` directory from this repository.

### For Firefox:
1. Navigate to `about:debugging#/runtime/this-firefox`.
2. Click **"Load Temporary Add-on..."`.
3. Select the `manifest.json` file from the `Extension/` directory.

---

## ⚙️ Operational Usage

1. Open a Google login page or any Google service.
2. Click the **Alphabeter Companion** icon in your toolbar.
3. Click the **"Synchronize to Alphabeter"** button.
4. Ensure your Alphabeter API or CLI is in listening mode to receive the handshake.

---

## 🛡 Disclaimer

**For authorized security testing only.** 
This extension captures sensitive session data. Use only on your own accounts or targets where you have explicit authorization. Lead developer: **RC**.

---
<p align="center">Injection successful. ⚡</p>
