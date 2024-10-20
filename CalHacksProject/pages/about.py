import reflex as rx
from components.navbar import Navbar


import reflex as rx
font_style = ("Helvetica", 16, "bold"),

# Create a label with custom font
    
app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap",
    ],
)



def about_page() -> rx.Component:
    return rx.box(rx.vstack(
        rx.center(rx.text("About Us", font_family="IBM Plex Mono", font_size="3em", width="200px")),
        # rx.text("Contact us here!", font_family="IBM Plex Mono", font_size="2em"),
        # You can style the section here if needed
        # style={"background": "#f9fafb", "padding": "6rem 0", "position": "relative"},
        rx.text("Teach It aims to bridge the gap between teachers and students and provide learners with the opportunity to study using methods that work best for them. ", font_family="IBM Plex Mono", font_size="2em", width="800px"),
        rx.text("Ever felt the 'aha!' moment when a concept makes sense when presented in a different way? Teach It is deisgned to help teachers bring those priceless moments to students across the world through our platform.", font_family="IBM Plex Mono", font_size="2em", width="800px"),
        #rx.text("", font_family="IBM Plex Mono", font_size="2em", width="800px")
    ),
    text_align="center"
    )
#rx.flex(
    rx.center(rx.text("Example"), bg="lightblue"),
    rx.spacer(),

@rx.page(route="/contact")
def about_page():
    return rx.container(
        Navbar(),
        about_page()
    )
