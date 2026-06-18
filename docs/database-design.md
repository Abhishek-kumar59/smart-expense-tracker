# Database Design

## Users

| Column | Type | Constraints |
|----------|---------|-------------|
| id | Integer | PK |
| name | String | NOT NULL |
| email | String | UNIQUE |
| password_hash | String | NOT NULL |