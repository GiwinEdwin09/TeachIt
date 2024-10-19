import reflex as rx
from ..components.navbar import Navbar
import pdfplumber

class TeacherState(rx.State):
    img: list[str]


    async def handle_upload(self, files: list[rx.UploadFile]):
        if not files:
            return rx.window_alert("No files selected for upload")
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_upload_dir() / file.filename

            # Save the file.
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)

            if file.filename.endswith(".pdf"):
                with pdfplumber.open(outfile) as pdf:
                    extracted_text = ""
                    for page in pdf.pages:
                        extracted_text += page.extract_text()

                print(f"Extracted text from {file.filename}: {extracted_text[:200]}...")
                self.img.append(f"Extracted text from {file.filename}: {extracted_text[:200]}...")
            
            elif file.filename.endswith(".txt"):
                with outfile.open("r", encoding="utf-8") as txt_file:
                    extracted_text = txt_file.read()

                print(f"Extracted text from {file.filename}: {extracted_text[:200]}...")
                self.img.append(f"Extracted text from {file.filename}: {extracted_text[:200]}...")

def learningMaterials() -> rx.Component:
    return rx.vstack(
        rx.text("Submit teaching material", font_size="2em"),
        rx.upload(
            rx.text("Drag and drop files here or click to select files"),
            id="upload1",
            multiple=True,
            accept={
                "application/pdf": [".pdf"],
                "text": [".txt"],
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
        rx.cond(
            rx.selected_files("upload1").length() > 0,
            rx.button(
                "Upload",
                on_click=TeacherState.handle_upload(rx.upload_files(upload_id="upload1")),
                size="4"
            ),
            rx.text("Please select at least one file to upload.", color="white"),
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