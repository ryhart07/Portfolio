import shutil
from pathlib import Path
from app import app

out = Path("build")
shutil.rmtree(out, ignore_errors=True)
shutil.copytree("static", out / "static")

pages = {"/": "index.html", "/journey": "journey.html", "/contact": "contact.html"}
with app.test_client() as client:
    for route, filename in pages.items():
        (out / filename).write_bytes(client.get(route).data)