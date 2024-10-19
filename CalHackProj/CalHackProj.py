import reflex as rx

from rxconfig import config
def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )


def navbar_buttons() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "TeachIt", size="7", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/"),
                    navbar_link("About", "/#"),
                    navbar_link("Contact", "/#"),
                    spacing="5",
                ),
                rx.hstack(
                    rx.button(
                        "Sign Up",
                        size="3",
                        variant="outline",
                    ),
                    rx.button("Log In", size="3"),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "Reflex", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("About"),
                        rx.menu.item("Pricing"),
                        rx.menu.item("Contact"),
                        rx.menu.separator(),
                        rx.menu.item("Log in"),
                        rx.menu.item("Sign up"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
        border_radius="20px",
    )


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
        navbar_buttons(),
        info(),
        options(),
    )

def student() -> rx.Component:
    return rx.container(
        navbar_buttons(),
        rx.text("About Page")
    )

def student() -> rx.Component:
    return rx.container(
        navbar_buttons
    )
app = rx.App()
app.add_page(student)
app.add_page(index)
