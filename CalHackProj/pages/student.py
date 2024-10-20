import reflex as rx
from components.navbar import Navbar

class StudentState(rx.State):
    option1: str = ""
    option2: str = ""
    option3: str = ""

    def submit(self):
        print("Visual: " + self.option1)
        print("Audio: " + self.option2)
        print("Interactive: " + self.option3)


    def set_option1(self, value: str):
        self.option1 = value

    def set_option2(self, value: str):
        self.option2 = value

    def set_option3(self, value: str):
        self.option3 = value


def learningMethods() -> rx.Component:
    return rx.vstack(
        rx.text("Select Preferred Learning Method", font_size="3em"),
        rx.vstack(
            rx.hstack(
                rx.text("Visual", font_size="2em", width="150px"),
                rx.select.root(
                    rx.select.trigger(placeholder="Choose Yes or No"),
                    rx.select.content(
                        rx.select.item("Yes", value="yes"),
                        rx.select.item("No", value="no"),
                    ),
                    on_change=StudentState.set_option1,
                ),
                align = "center",
                justify = "start",
                spacing = "4"
            ),
            rx.hstack(
                rx.text("Audio", font_size="2em", width="150px"),
                rx.select.root(
                    rx.select.trigger(placeholder="Choose Yes or No"),
                    rx.select.content(
                        rx.select.item("Yes", value="yes"),
                        rx.select.item("No", value="no"),
                    ),
                    on_change=StudentState.set_option2,
                ),
                align = "center",
                justify = "start",
                spacing = "4"
            ),
            rx.hstack(
                rx.text("Interactive", font_size="2em", width="150px"),
                rx.select.root(
                    rx.select.trigger(placeholder="Choose Yes or No"),
                    rx.select.content(
                        rx.select.item("Yes", value="yes"),
                        rx.select.item("No", value="no"),
                    ),
                    on_change=StudentState.set_option3,
                ),
                align = "center",
                justify = "start",
                spacing = "4"
            ),
            spacing = "20px"
        ),
        rx.button("Submit", on_click=StudentState.submit, size="4"),
        spacing = "30px",
        justify = "center",
        align= "center",
        min_height = "80vh",
    )

@rx.page(route="/student")
def student():
    return rx.container(
        Navbar(),
        learningMethods()
    )