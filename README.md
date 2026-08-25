# Cloud Billing Assistant - Week 1

## Overview
A Python utility designed to load and parse FOCUS-compliant cloud billing data from CSV format and convert it into structured JSON reports.

## Features
- Dynamic environment variable management via `.env`.
- Full CSV to JSON conversion for raw data distribution.
- Creates a basic data summary report.

## Project Structure
```text
cloud-billing-assistant/
├── data/
│   ├── billing_sample.csv
│   ├── billing_full.json
│   └── billing_summary.json
├── src/
│   └── data_loader.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md