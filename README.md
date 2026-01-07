# 🛡️ SentinelGhost: AI-Powered Autonomous Deception Platform

**Problem Statement:** e-Raksha PS1 - Proactive Cyber Threat Detection and Prevention

## 🚀 Overview
SentinelGhost is an advanced network security tool that uses **Deception Technology** to neutralize intruders. Instead of just blocking them, it traps them in a high-fidelity **Honeypot** to capture forensic evidence.

## ✨ Key Features
- **Proactive Scanning:** Real-time network monitoring using Scapy.
- **AI-Driven Risk Scoring:** Uses **Llama-3.2 (Ollama)** to analyze device behavior and assign risk scores.
- **Autonomous Honeypot:** Automatically deploys a fake admin portal for detected intruders.
- **Digital Forensics:** Captures Attacker's IP, Device Model (e.g., Redmi 10S), and OS details.
- **Live Dashboard:** Interactive UI built with Streamlit for real-time monitoring.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **AI Model:** Llama-3.2 via Ollama
- **Frameworks:** Flask (Honeypot), Streamlit (Dashboard)
- **Networking:** Scapy

## 🏃 How to Run
1. Run as Administrator: `python main.py`
2. Start Dashboard: `streamlit run app.py`
