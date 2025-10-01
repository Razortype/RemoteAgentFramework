# React Dashboard Dockerfile
FROM node:20-alpine AS builder

LABEL maintainer="Educational Cybersecurity Team"
LABEL description="Educational cybersecurity simulation - React Dashboard"
LABEL version="1.0.0"

# Set work directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy source code
COPY . .

# Build the application
RUN npm run build

# Production stage
FROM nginx:alpine

# Create non-root user for security
RUN addgroup -g 1001 -S nginxuser && \
    adduser -S nginxuser -u 1001

# Copy built application from builder stage
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy custom nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:3000 || exit 1

# Change ownership to non-root user
RUN chown -R nginxuser:nginxuser /usr/share/nginx/html
USER nginxuser

# Expose port
EXPOSE 3000

# Educational safety: Configure for localhost-only access
ENV NODE_ENV=production
ENV REACT_APP_API_URL=http://localhost:8080

# Start nginx
CMD ["nginx", "-g", "daemon off;"]