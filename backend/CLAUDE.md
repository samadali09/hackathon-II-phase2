# Backend Guidelines

## Stack
- Python FastAPI
- SQLModel (ORM)
- Neon Serverless PostgreSQL

## Project Structure
- `main.py` - FastAPI app entry point
- `models.py` - SQLModel database models
- `routes/` - API route handlers
- `db.py` - Database connection
- `auth.py` - JWT Verification middleware

## API Conventions
- All routes under `/api/`
- Return JSON responses
- **Auth:** All endpoints must verify JWT from `Authorization: Bearer <token>`
- Use Pydantic models for request/response

## Database
- Use SQLModel for all database operations
- Connection string from environment variable: DATABASE_URL