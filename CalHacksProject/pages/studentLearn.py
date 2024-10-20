import reflex as rx
from ..components.navbar import Navbar


def practiceOrQuiz() -> rx.Component:
    return rx.vstack(
        rx.text("Choose Activity", font_size="3em"),
        rx.hstack(
            rx.button(
                "Learn", 
                size="xl", 
                variant="solid", 
                radius="full", 
                font_size="1.5em",
                padding_x="2em",
                padding_y="1em",
            ),
            rx.link(
            rx.button(
                "Practice", 
                size="xl",
                variant="solid", 
                radius="full", 
                font_size="1.5em",
                padding_x="2em",
                padding_y="1em",
            ),href = "/practice"),
            spacing="20px",  
            align_items="center", 
            justify_content="center",
        ),
        text_align="center",  
        font_size="1.5em",
        padding="6em",
        border_radius="10px",
        width="70%",
        margin="auto",
        justify_content="center",
        align_items="center",
    )



@rx.page(route="/studentLearn")
def studentLearn():
    return rx.container(
        Navbar(),
        practiceOrQuiz(),
    )