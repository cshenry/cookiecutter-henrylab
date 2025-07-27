# Multi-stage build for {{cookiecutter.friendly_name}}
FROM python:3.12-slim as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Create and activate virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy dependency files
WORKDIR /app
COPY pyproject.toml ./

# Install dependencies
RUN uv pip install -e .

# Production stage
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV=/opt/venv \
    PATH="/opt/venv/bin:$PATH"

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Create non-root user
RUN groupadd --gid 1001 appuser && \
    useradd --uid 1001 --gid appuser --shell /bin/bash --create-home appuser

# Copy application code
WORKDIR /app
COPY --chown=appuser:appuser . .

# Switch to non-root user
USER appuser

{% if cookiecutter.use_fastapi == 'true' -%}
# Expose port for FastAPI
EXPOSE 8000

# Run FastAPI application
CMD ["uvicorn", "{{cookiecutter.package_name}}.api:app", "--host", "0.0.0.0", "--port", "8000"]
{%- else -%}
# Run CLI application
CMD ["{{cookiecutter.project_name}}"]
{%- endif %}
