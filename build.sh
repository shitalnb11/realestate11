#!/usr/bin/env bash
# Render build script

echo "🚀 Installing dependencies..."
pip install --upgrade pip setuptools wheel
pip install --no-cache-dir Pillow
pip install -r requirements.txt

echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

echo "🧩 Applying migrations..."
python manage.py migrate

echo "✅ Build completed successfully!"
