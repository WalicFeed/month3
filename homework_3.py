import flet as ft

def main(page: ft.Page):
    page.title = 'age restriction'
    page.theme_mode = ft.ThemeMode.LIGHT

    def submit(e):
        age = text_input.value.strip()
        if not age.isdigit():
            text.value = 'Please enter a valid age!'
            text.color = ft.Colors.YELLOW_900
        else:
            age = int(age)
            if age < 18:
                text.value = 'ACCESS DENIED'
                text.color = ft.Colors.RED_900
            else:
                text.value = 'Access granted!'
                text.color = ft.Colors.GREEN_900
        page.update()

    text= ft.Text('Enter your age')
    text_input = ft.TextField(label='Your age')
    button = ft.Button('Submit', on_click=submit)

    page.add(
        text,
        text_input,
        button
    )

if __name__ == "__main__":
    ft.run(main, view = ft.AppView.WEB_BROWSER)