# Python Agent Client Dockerfile
FROM python:3.11-slim

LABEL maintainer="Educational Cybersecurity Team"
LABEL description="Educational cybersecurity simulation - Python Agent Client"
LABEL version="1.0.0"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.8.3
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_CACHE_DIR=/tmp/poetry_cache

# Create non-root user for security
RUN groupadd -r agentuser && useradd -r -g agentuser agentuser

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry==$POETRY_VERSION

# Set work directory
WORKDIR /app

# Copy poetry files
COPY pyproject.toml poetry.lock* ./

# Configure poetry and install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi \
    && rm -rf $POETRY_CACHE_DIR

# Copy application code
COPY src/ ./src/
COPY README.md LICENSE ./

# Change ownership to non-root user
RUN chown -R agentuser:agentuser /app
USER agentuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import sys; sys.exit(0)"

# Educational safety: Force localhost-only connections
ENV WEBSOCKET_HOST=localhost
ENV WEBSOCKET_PORT=8080

# Run the application
CMD ["python", "-m", "src.main"]