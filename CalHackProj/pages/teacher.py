import reflex as rx
from ..components.navbar import Navbar


class TeacherState(rx.State):
    img: list[str]

    async def handle_upload(self, files: list[rx.UploadFile]):
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_upload_dir() / file.filename

            # Save the file.
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)

            # Update the img var.
            self.img.append(file.filename)

def learningMaterials() -> rx.Component:
    return rx.vstack(
        rx.text("Submit teaching material", font_size="2em"),
        rx.upload(
            rx.text("Drag and drop files here or click to select files"),
            id="upload1",
            multiple=True,
            accept={
                "application/pdf": [".pdf"],
                "image/png": [".png"],
                "image/jpeg": [".jpg", ".jpeg"],
                "image/gif": [".gif"],
                "image/webp": [".webp"],
                "text/html": [".html", ".htm"],
            },
            max_files=20,
        ),
        rx.vstack(
            rx.foreach(
                rx.selected_files("upload1"), rx.text
            ),
            justify = "center",
            align = "center"
        ),
        rx.button(
            "Upload",
            on_click=TeacherState.handle_upload(rx.upload_files(upload_id="upload1"),
            ),
            size="4"
        ),
        rx.button(
            "Clear",
            on_click=rx.clear_selected_files("upload1"),
            size="4"
        ),
        align = "center",
        justify = "center",
        padding = "5em"
    )

@rx.page(route="/teacher")
def teacher():
    return rx.container(
        Navbar(),
        rx.center(
            learningMaterials()
        ),
        width="100%",
        height="100vh",
    )