# validator.py
import os
import sys

BASE_DIR = "/home/yutw/project/md_templates/results/geotechnical_management"

required_files = [
    "backend/main.py",
    "backend/database/database.py",
    "backend/api/models/geotechnical_data.py",
    "backend/api/schemas/geotechnical_data.py",
    "backend/api/routers/geotechnical_data.py",
    "backend/core/services/geotechnical_data_service.py",
    "frontend/src/components/GeotechnicalData.vue",
    "frontend/src/App.vue",
    "frontend/package.json",
    "frontend/vite.config.js",
]

missing = []
for rel in required_files:
    path = os.path.join(BASE_DIR, rel)
    if not os.path.isfile(path):
        missing.append(rel)

if missing:
    print("Missing files:")
    for f in missing:
        print(" -", f)
    sys.exit(1)
else:
    print("All required files exist.")
