import flet as ft

from shared.profile_parser.vless_parser import parse_vless_url


def main(page: ft.Page):
    page.title = "Octara IOS"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 700
    page.window_height = 700

    status_text = ft.Text("Вставь VLESS-ссылку и нажми импорт", color=ft.Colors.GREY_400)
    result_title = ft.Text("", size=20, weight="bold")
    result_text = ft.Text("", selectable=True)

    link_input = ft.TextField(
        label="VLESS ссылка",
        hint_text="vless://...",
        multiline=True,
        min_lines=4,
        max_lines=8,
        width=600,
    )

    result_card = ft.Container(
        visible=False,
        padding=15,
        width=600,
        border_radius=10,
        bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.BLUE),
        content=ft.Column(
            [
                result_title,
                result_text,
            ],
            tight=True,
            spacing=10,
        ),
    )

    def import_click(e):
        link = link_input.value.strip()

        if not link:
            status_text.value = "Ошибка: ссылка пустая"
            status_text.color = ft.Colors.RED_400
            result_card.visible = False
            page.update()
            return

        try:
            profile = parse_vless_url(link)

            result_title.value = f"Профиль: {profile.remark or 'Без имени'}"
            result_text.value = (
                f"UUID: {profile.uuid}\n"
                f"Адрес: {profile.address}\n"
                f"Порт: {profile.port}\n"
                f"Сеть: {profile.network}\n"
                f"Security: {profile.security}\n"
                f"SNI: {profile.sni}\n"
                f"Host: {profile.host}\n"
                f"Path: {profile.path}\n"
                f"Flow: {profile.flow}\n"
                f"Fingerprint: {profile.fingerprint}\n"
                f"Public key: {profile.public_key}\n"
                f"Short ID: {profile.short_id}"
            )

            status_text.value = "Профиль успешно импортирован"
            status_text.color = ft.Colors.GREEN_400
            result_card.visible = True

        except Exception as ex:
            status_text.value = f"Ошибка импорта: {ex}"
            status_text.color = ft.Colors.RED_400
            result_card.visible = False

        page.update()

    btn_import = ft.ElevatedButton(
        "Импортировать профиль",
        on_click=import_click,
    )

    page.add(
        ft.Text("Octara IOS", size=28, weight="bold"),
        ft.Text("Импорт VLESS профиля", size=18),
        link_input,
        btn_import,
        status_text,
        result_card,
    )


if __name__ == "__main__":
    ft.app(target=main)