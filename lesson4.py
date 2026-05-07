import flet as ft

def main(page: ft.Page):
    page.title = "My first Flet app"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    greeting_history = []

    greeting_text = ft.Text("History of greetings: \n")

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
            greeting_history.append(name)
            greeting_text.value += f"{greeting_history[-1]}, \n" #or use join 
        page.update() # page.update() is no longer necessary

    text_hello = ft.Text("Hello", color=ft.Colors.RED_900, size = 20)
    text_input = ft.TextField(label="Your name", on_submit=text_name, expand=True)
    button = ft.Button("SEND", on_click=text_name)

    def theme_update(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        page.update()

    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=theme_update)

    def clear_history(e):
        greeting_history.clear()
        greeting_text.value = "History of greetings: \n"
        page.update()

    button_clear = ft.IconButton(icon = ft.Icons.DELETE, on_click=clear_history)

    text = "skibid dop dop. six seven, say my name"

    main_object = ft.Row(
        [
            text_input, button, button_clear
        ]
    
    )

    text_row = ft.Row(
       controls=[text_hello],
       alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(
        text_row,
        main_object,
        theme_button,
        greeting_text,
    )

if __name__ == "__main__":
    ft.run(main, view = ft.AppView.WEB_BROWSER)