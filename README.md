# Python Flask REST API

A production-ready Flask REST API with automated deployment pipelines, containerization, and professional development workflows.

## Features

- RESTful API endpoints for item management
- Docker containerization
- Automated testing with pytest
- Code quality checks with pre-commit hooks
- CI/CD pipeline with GitHub Actions
- API documentation
- CORS support

## Prerequisites

- Python 3.8+
- Docker Desktop
- Git
- GitHub account

## Project Structure

```
my-flask-api/
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── app/
│   ├── __init__.py
│   └── routes.py
├── tests/
│   ├── __init__.py
│   └── test_routes.py
├── .pre-commit-config.yaml
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── setup.py
└── README.md
```

## Getting Started

1. Clone the repository:
```bash
git clone <repository-url>
cd my-flask-api
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .[dev]
```

4. Set up pre-commit hooks:
```bash
pre-commit install
```

## Running the Application

### Local Development
```bash
flask run
```

The API will be available at http://localhost:5000

### Using Docker
```bash
docker-compose up --build
```

The API will be available at http://localhost:5000

## API Endpoints

- `GET /api/health` - Health check endpoint
- `GET /api/items` - List all items
- `POST /api/items` - Create a new item
- `GET /api/items/<id>` - Get a specific item
- `PUT /api/items/<id>` - Update a specific item
- `DELETE /api/items/<id>` - Delete a specific item

### Example Requests

Create an item:
```bash
curl -X POST http://localhost:5000/api/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Item"}'
```

Get all items:
```bash
curl http://localhost:5000/api/items
```

## Testing

Run the test suite:
```bash
pytest
```

Run with coverage:
```bash
pytest --cov=app tests/
```

## Development Workflow

1. Create a new branch for your feature/fix
2. Make your changes
3. Ensure tests pass and pre-commit hooks run successfully
4. Submit a pull request

## CI/CD Pipeline

The GitHub Actions workflow will:
1. Run all tests
2. Check code quality
3. Build Docker image
4. Deploy (if configured)

## Security Considerations

- Keep dependencies updated
- Use environment variables for sensitive data
- Enable CORS appropriately
- Regular security audits

## License

This project is licensed under the MIT License - see the LICENSE file for details.
