import reflex as rx
from .components.navbar import Navbar
from rxconfig import config
from .pages import(student)

__all__ = ["students"]

class State(rx.State):
    """The app state."""


def info() -> rx.Component:
    return rx.container(
        rx.box(
            "Learn it your Way!",

            text_align = "center",
            text_wrap = "pretty",
            font_size="2em",
            padding="1em",
        ),
        rx.box(
            "Use TeachIt to succeed in class!",

            text_align = "center",
            text_wrap = "pretty",
            font_size="2em",
            padding="1em",
        ),
    )

def options() -> rx.Component:
    return rx.container(
        rx.box(
            rx.hstack(
                rx.text("Are you a...", font_size="2em"),
                
                
                rx.link(
                    rx.button(
                        "Student", 
                        size="lg", 
                        variant="solid", 
                        radius="full", 
                        font_size="1em",
                        padding_x="1.5em",
                        padding_y="0.5em",
                    ), 
                    href="/student"
                ),
                
                
                rx.link(
                    rx.button(
                        "Teacher", 
                        size="lg", 
                        variant="solid", 
                        radius="full", 
                        font_size="1em",
                        padding_x="1.5em",
                        padding_y="0.5em",
                    ), 
                    href="/student"
                ),
                
                spacing="20px",  
                align_items="center",
                justify = "center"
            ),
            text_align="center",  
            font_size="1.5em",
            padding="2em",
            border_radius="10px",
            width="70%",
            margin="auto",
        )
    )




def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        Navbar(),
        info(),
        options(),
    )

#def student() -> rx.Component:
#    return rx.container(
#        Navbar(),
#        rx.text("About Page")
#    )

#def student() -> rx.Component:
#    return rx.container(
#        Navbar(),
#    )
app = rx.App()
app.add_page(index)
