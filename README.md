# Riyadh Barbershop Scraper 🧔✂️🇸🇦

A Python-based web scraper that collects barbershop names, addresses, and contact numbers across various districts in **Riyadh**, Saudi Arabia, using **Selenium** and Arabic Google Maps search queries.

> 🔍 This project demonstrates automation for location-based business listings — useful for market analysis, directory building, or local insights.

---

## 📌 Features

- Searches Google Maps in Arabic for each district (e.g., `صالون حلاقة رجال الصحافة الرياض`)
- Extracts:
  - Name of barbershop
  - District (حي)
  - Address (if available)
  - Phone number (if available)
  - Placeholder for Instagram & WhatsApp links
- Saves data to a clean CSV file
- Can be adapted for other cities like Dammam, Jeddah, etc.

---

## ⚙️ Requirements

Install Python packages:

```bash
pip install -r requirements.txt
