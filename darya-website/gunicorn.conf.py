# Gunicorn configuration file optimized for Render free tier
import os

# Server socket
bind = f"0.0.0.0:{os.environ.get('PORT', 8000)}"
backlog = 2048

# Worker processes - REDUCED for free tier memory limits
workers = 1  # Only 1 worker for free tier
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2

# Memory management - CRITICAL for free tier
max_requests = 100  # Restart workers more frequently
max_requests_jitter = 10
preload_app = False  # Don't preload to save memory

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Process naming
proc_name = "darya_website"

# Server mechanics
daemon = False
pidfile = "/tmp/gunicorn.pid"
user = None
group = None
tmp_upload_dir = None

# Memory limits
worker_tmp_dir = "/dev/shm"  # Use shared memory if available
