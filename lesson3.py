import flet as ft

def main(page: ft.Page):
    page.title = "My first Flet app"
    page.theme_mode = ft.ThemeMode.DARK

    def text_name(e):
        name = text_input.value.strip()
        if not name:
            text_hello.value = "Please enter your name!"
            text_hello.color = ft.Colors.RED_900
        else:
            print(f"Hello, {name}!")
            text_hello.value = f"Hello, {name}!"
            text_hello.color = ft.Colors.GREEN_900
            text_input.value = ""
        page.update() # page.update() is no longer necessary

    text_hello = ft.Text("Hello", color=ft.Colors.RED_900)
    text_input = ft.TextField(label="Your name")
    button = ft.Button("SEND", on_click=text_name)

    def theme_update(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        page.update()

    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=theme_update)

    page.add(
        text_hello,
        text_input,
        button,
        theme_button
    )

if __name__ == "__main__":
    ft.run(main, view = ft.AppView.WEB_BROWSER)