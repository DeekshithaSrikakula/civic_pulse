# CivicPulse

## Overview

CivicPulse is an AI-powered Telugu Civic Complaint Analyzer that helps authorities process citizen grievances more efficiently. The system accepts complaints in Telugu, identifies the issue category, recommends the responsible department, and generates a structured complaint summary.

## Problem Statement

Civic authorities receive a large number of complaints that require manual categorization and routing, causing delays in grievance resolution.

## Features

* Telugu complaint analysis
* Automatic complaint categorization
* Department recommendation
* Structured complaint summary generation
* Simple user interface

## Tech Stack

* Streamlit
* Python
* SQLite
* Telugu LLM / OpenAI API

## Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Project Structure

civicpulse/
├── app.py
├── requirements.txt
├── data/
├── utils/
├── database/
├── README.md
├── CONTRIBUTING.md
├── USER_MANUAL.md
└── AGENTS.md

## Future Scope

* Voice input
* Multi-language support
* Complaint tracking
* Civic analytics dashboard
