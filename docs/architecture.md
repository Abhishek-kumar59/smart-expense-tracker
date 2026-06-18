# Architecture Overview

## High-Level Flow

Client
↓
API Layer (FastAPI)
↓
Service Layer
↓
Database Layer (SQLAlchemy)
↓
PostgreSQL

---

## Backend Components

### API Layer

Handles:

- Request Validation
- Authentication
- Response Formatting

### Service Layer

Handles:

- Business Logic
- Calculations
- Permissions

### Database Layer

Handles:

- Queries
- Transactions
- Relationships

---

## Future Components

- Redis Cache
- Background Jobs
- OCR Service
- AI Insights Service
- Email Notification Service