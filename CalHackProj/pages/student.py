import reflex as rx
from ..components.navbar import Navbar

@rx.page(route="/student")
def student():
    return rx.container(
        Navbar(),
    )