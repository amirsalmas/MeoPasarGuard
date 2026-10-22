from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import os

app = FastAPI(title="Meo PasarGuard")

# اطلاعات ورود پیش‌فرض
ADMIN_USER = os.getenv("ADMIN_USER", "admin")
ADMIN_PASS = os.getenv("ADMIN_PASS", "meo123456")

@app.get("/api/info")
def get_info():
    return {
        "panel_name": "Meo PasarGuard",
        "version": "1.0.0",
        "theme": "Achaemenid",
        "default_inbounds": ["VLESS-Reality-Meov2ray", "VMess-WS-TLS"]
    }

# اینباند پیش‌فرض (شبیه سازی شده مثل اسپایدر)
@app.get("/api/config")
def get_config():
    return {
        "protocol": "vless",
        "address": "meo.v2ray.com",
        "port": 443,
        "id": "d3b7c9a1-1234-5678-9abc-def012345678",
        "security": "reality",
        "remark": "🇮🇷 Meo PasarGuard - @meov2ray"
    }

# صفحه اصلی (ریدایرکت به داشبورد)
@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
