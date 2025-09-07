# src/screens/login_screen.py
import flet as ft

def LoginScreen(page: ft.Page):

    # 1. สร้าง BottomSheet และเก็บไว้ในตัวแปร bs
    bs = ft.BottomSheet(
        ft.Container(
            bgcolor="#F579A4",
            padding=ft.padding.only(top=20, left=20, right=20, bottom=40),
            border_radius=ft.border_radius.only(top_left=20, top_right=20),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                # ทำให้ content ไม่ล้นออกนอก BottomSheet
                tight=True,
                controls=[
                    ft.Container(width=50, height=5, bgcolor="white", border_radius=5),
                    ft.Container(height=10),
                    ft.Image(src="src/assets/logo.png", width=80),
                    ft.Text("KMITL", weight=ft.FontWeight.BOLD, size=20),
                    ft.Container(height=20),
                    ft.Container(
                        bgcolor="#F0F0F0",
                        border_radius=15,
                        padding=20,
                        content=ft.Column(
                            tight=True,
                            controls=[
                                ft.Text("ยืนยันตัวตนด้วยบริการของสถาบันฯ", weight=ft.FontWeight.BOLD, size=16),
                                ft.Text("โดยใช้ E-mail Account ของสถาบันฯ"),
                                ft.Container(height=20),
                                ft.TextField(hint_text="Username", bgcolor="white", border=ft.InputBorder.NONE),
                                ft.TextField(
                                    hint_text="Password", password=True, can_reveal_password=True,
                                    bgcolor="white", border=ft.InputBorder.NONE
                                ),
                                ft.Container(height=20),
                                ft.ElevatedButton(text="Login", width=300, height=50, bgcolor="#D63484", color="white"),
                            ]
                        ),
                    ),
                ]
            )
        )
    )

    # 2. ติดตั้ง BottomSheet เข้าไปในชั้น Overlay ของหน้าจอ (ขั้นตอนที่เคยขาดไป)
    page.overlay.append(bs)

    # 3. สร้างฟังก์ชันสำหรับเปิด BottomSheet โดยใช้คำสั่ง page.open() ที่ถูกต้อง
    def show_login_sheet(e):
        print("Opening BottomSheet...")
        page.open(bs)

    # --- UI ของหน้า Welcome (เหมือนเดิม) ---
    welcome_view = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Container(height=200),
            ft.Image(src="src/assets/logo.png", width=300),
            ft.Container(height=50),
            ft.ElevatedButton(
                text="WELCOME", width=280, height=50,
                bgcolor="#D63484", color="white",
                on_click=show_login_sheet  # <-- เรียกใช้ฟังก์ชันที่ถูกต้อง
            ),
            ft.Container(height=180),
            ft.Text("Graduate Student Tracking System", color=ft.Colors.with_opacity(0.5, "black")),
        ]
    )

    return ft.View(
        route="/login",
        controls=[welcome_view],
        vertical_alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        bgcolor="white"
    )