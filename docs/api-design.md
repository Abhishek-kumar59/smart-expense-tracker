# API Design

## Health Check

### GET /

Response

```json
{
  "message": "Smart Expense Tracker API"
}
```

## Database Check

### GET /test-db

Response

```json
{
  "database": "connected",
  "result": 1
}
```