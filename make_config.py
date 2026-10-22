import asyncio
import os
from pasarguard import PasarguardAPI, Tools, UserCreate, UserStatus

async def main():
    # اطلاعات پنل خودت رو اینجا وارد کن
    PANEL_URL = "http://127.0.0.1:8000"  # آدرس پنل PasarGuard
    ADMIN_USER = "admin"                  # یوزرنیم ادمین
    ADMIN_PASS = "your_admin_password"    # پسورد ادمین

    async with PasarguardAPI(base_url=PANEL_URL) as api:
        # ۱. لاگین به پنل و گرفتن توکن
        token = await api.get_token(username=ADMIN_USER, password=ADMIN_PASS)
        
        # ۲. ساخت کاربر جدید با مشخصات دلخواه (۳۰ روزه و ۹۰ گیگ)
        new_user = await api.create_user_in_all_groups(
            UserCreate(
                username=Tools.random_username(prefix="meo"), # یه اسم تصادفی
                data_limit=Tools.gb(90),    # محدودیت حجم: ۹۰ گیگ
                expire=Tools.days(30),      # انقضا: ۳۰ روز
                status=UserStatus.ACTIVE,
                note="Auto-created 30d/90GB"
            ),
            token=token.access_token,
        )
        
        # ۳. چاپ کردن لینک کانفیگ و اطلاعات
        print("✅ کاربر با موفقیت ساخته شد!")
        print(f"👤 نام کاربری: {new_user.username}")
        print(f"🔗 لینک سابسکریپشن: {new_user.subscription_url}")
        print(f"📊 حجم: 90 GB | ⏳ مدت: 30 روز")

if __name__ == "__main__":
    asyncio.run(main())
