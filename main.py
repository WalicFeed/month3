import flet as ft

def main(page: ft.Page):
    page.title = "Hello, Flet!"
    page.theme_mode = ft.ThemeMode.LIGHT

    hello = ft.Text("Hello, Flet!", size=30, color=ft.Colors.BLUE)

    count = 0
    def button_click(obj):
        nonlocal count
        count += 1
        hello.value = f"Clicked {count} times!"
        page.update()
    button_text = ft.Text("Click me!")
    button = ft.Button("Click me!", icon=ft.Icons.SEND, color=ft.Colors.GREEN, icon_color=ft.Colors.RED, on_click=button_click)
    button_icon = ft.IconButton(ft.Icons.SEND)

    name_input = ft.TextField(label="Your name")
    
    
    page.add(
        hello,
        button_text,
        button,
        button_icon,
        name_input
    )

if __name__ == "__main__":
    #ft.app(target=main)
    ft.run(main, view = ft.AppView.WEB_BROWSER)
