# src/main.py
import flet as ft
from screens.login_screen import LoginScreen

def main(page: ft.Page):
    page.title = "Graduate Student Tracking System"
    page.window.width = 430
    page.window.height = 932

    # ฟังก์ชันที่จะทำงานทุกครั้งที่ URL ของแอปเปลี่ยน
    def route_change(route):
        page.views.clear() # 1. ล้างหน้าจอเก่าออกทั้งหมด

        # 2. ตรวจสอบ URL แล้วแสดง View (หน้าจอ) ที่ถูกต้อง
        if page.route == "/login":
            page.views.append(LoginScreen(page))
        
        # (ในอนาคตเราจะเพิ่มเงื่อนไขสำหรับ /home และหน้าอื่นๆ ที่นี่)

        page.update() # 3. อัปเดตหน้าจอเพื่อแสดงผล View ใหม่

    # กำหนดให้ Flet เรียกใช้ฟังก์ชัน route_change เมื่อ URL เปลี่ยน
    page.on_route_change = route_change

    # เมื่อเปิดแอปครั้งแรก ให้ไปที่ URL "/login"
    page.go("/login")

# สั่งให้ Flet App เริ่มทำงาน
ft.app(target=main)