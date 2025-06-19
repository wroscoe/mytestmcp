# Docker Deployment Guide

## Building and Running with Docker

### Option 1: Using Docker directly

1. **Build the Docker image:**
   ```bash
   docker build -t myfastmcp .
   ```

2. **Run the container:**
   ```bash
   docker run -p 8000:8000 --env-file .env myfastmcp
   ```

   Or with environment variable directly:
   ```bash
   docker run -p 8000:8000 -e ANTHROPIC_API_KEY=your_api_key_here myfastmcp
   ```

### Option 2: Using Docker Compose (Recommended)

1. **Make sure your `.env` file exists with your ANTHROPIC_API_KEY**

2. **Start the service:**
   ```bash
   docker-compose up -d
   ```

3. **View logs:**
   ```bash
   docker-compose logs -f
   ```

4. **Stop the service:**
   ```bash
   docker-compose down
   ```

## Accessing the Server

Once running, your FastMCP server will be available at:
- **HTTP endpoint:** `http://localhost:8000/mcp`

## Environment Variables

- `ANTHROPIC_API_KEY`: Your Anthropic API key (required)
- `DOCKER_CONTAINER`: Set to 1 when running in Docker (automatically set in Dockerfile)

## Health Check

The container includes a health check that verifies the server is responding on the `/mcp` endpoint every 30 seconds.

## Security Notes

- The container runs as a non-root user for security
- Only port 8000 is exposed
- The `.env` file is excluded from the Docker build context via `.dockerignore`
