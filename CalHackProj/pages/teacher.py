import reflex as rx
from components.navbar import Navbar
import os 
from embedchain import App


#class State(rx.State):
#    """The app state."""
#    ai_result: str

#    def get_ai_result(self):
#        return self.ai_result

os.environ["OPENAI_API_KEY"] = ""

class TeacherState(rx.State):
    img: list[str]
    ai_result: str

    def get_ai_result(self):
        return self.ai_result
    
    async def handle_upload(self, files: list[rx.UploadFile]):
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_upload_dir() / file.filename

            # Save the file.
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)

            # Update the img var.
            self.img.append(file.filename)

            app = App()
            app.add(f"../uploaded_files/{file.filename}.pdf")

            result = app.query("Make a quiz based on this")
            print(result)
            self.ai_result = result

            print(self.ai_result)


def learningMaterials() -> rx.Component:
    global ai_output
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

        rx.text(TeacherState.ai_result, size="4"),
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