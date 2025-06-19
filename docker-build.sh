#!/bin/bash
# Build and run script for the FastMCP Docker container

set -e  # Exit on any error

echo "🚀 FastMCP Docker Setup"
echo "======================"

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first:"
    echo "   sudo apt update"
    echo "   sudo apt install docker.io"
    echo "   sudo systemctl start docker"
    echo "   sudo systemctl enable docker"
    echo "   sudo usermod -aG docker $USER"
    echo "   (Then log out and back in)"
    exit 1
fi

# Check if .env file exists
if [ ! -f .env ]; then
    echo "⚠️  .env file not found. Creating from example..."
    if [ -f .env.example ]; then
        cp .env.example .env
        echo "📝 Please edit .env and add your ANTHROPIC_API_KEY"
    else
        echo "❌ No .env.example found. Please create .env with your ANTHROPIC_API_KEY"
    fi
fi

# Build the Docker image
echo "🔨 Building Docker image 'myfastmcp'..."
docker build -t myfastmcp .

if [ $? -eq 0 ]; then
    echo "✅ Docker image built successfully!"
    echo ""
    echo "🎯 Usage options:"
    echo "   1. Run with docker:"
    echo "      docker run -p 8000:8000 --env-file .env myfastmcp"
    echo ""
    echo "   2. Run with docker-compose:"
    echo "      docker-compose up -d"
    echo ""
    echo "   3. Run in background:"
    echo "      docker run -d -p 8000:8000 --env-file .env --name myfastmcp-server myfastmcp"
    echo ""
    echo "📡 Server will be available at: http://localhost:8000/mcp"
    echo "🔍 Check logs with: docker logs myfastmcp-server"
    echo "🛑 Stop with: docker stop myfastmcp-server"
else
    echo "❌ Docker build failed!"
    exit 1
fi