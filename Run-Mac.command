#!/bin/bash
# Double-click di Finder untuk menjalankan GED-SAT LMS di Mac.
# Pertama kali: buka Terminal di folder ini, jalankan:  chmod +x Run-Mac.command

# Pindah ke folder tempat script ini berada
cd "$(cd "$(dirname "$0")" && pwd)" || exit 1

echo "=== GED-SAT LMS ==="
echo "Folder: $(pwd)"

# Cari Python 3 (utamakan 3.11)
PY=""
for c in python3.11 python3 python; do
  if command -v "$c" >/dev/null 2>&1; then PY="$c"; break; fi
done
if [ -z "$PY" ]; then
  echo "ERROR: Python tidak ditemukan. Install Python 3.11 dari https://python.org"
  read -n 1 -s -r -p "Tekan tombol apa saja untuk keluar..."
  exit 1
fi

# Buat venv kalau belum ada / belum valid (mis. dibawa dari Windows)
if [ ! -x "./venv/bin/python" ]; then
  echo "venv belum ada/valid. Membuat venv baru dengan $PY ..."
  rm -rf venv
  "$PY" -m venv venv || { echo "Gagal membuat venv"; read -n 1 -s -r; exit 1; }
  echo "Menginstall paket dari requirements.txt ..."
  ./venv/bin/python -m pip install --upgrade pip
  ./venv/bin/python -m pip install -r requirements.txt || { echo "Gagal install paket"; read -n 1 -s -r; exit 1; }
fi

echo "Menjalankan server... buka http://127.0.0.1:8000"
echo "Tekan CTRL+C untuk berhenti."

# Buka browser setelah 2 detik (server butuh waktu start)
( sleep 2; open http://127.0.0.1:8000 ) &

./venv/bin/python manage.py runserver

echo
read -n 1 -s -r -p "Server berhenti. Tekan tombol apa saja untuk menutup..."
