#!/usr/bin/env bash
# Render Build Script
set -o errexit  # exit on error

echo "🚀 Installing and upgrading pip, setuptools, wheel..."
pip install --upgrade pip setuptools wheel

echo "📦 Installing Pillow explicitly (Render Pillow fix)..."
pip install --no-cache-dir Pillow

echo "📦 Installing all project dependencies..."
pip install -r requirements.txt

echo "🧱 Collecting static files..."
python manage.py collectstatic --noinput

echo "🧩 Applying database migrations..."
python manage.py migrate

echo "✅ Build completed successfully!"
