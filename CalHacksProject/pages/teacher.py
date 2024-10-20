import reflex as rx
from ..components.navbar import Navbar
import openai
import pdfplumber
from pathlib import Path
from pydantic import BaseModel
import re
import json
from sqlmodel import select
# Set your OpenAI API key
openai.api_key = ""

class QuizModel(rx.Model, table =  True):
    fileName: str
    questNum: int
    quest: str
    answOne: str
    answTwo: str
    answThree: str
    answFour: str
    ansInd:int
    typeOf: str

class QuizFormat(BaseModel):
    question_num: int
    question:str
    answers: list[str]
    answerIndex: int

class Quiz(BaseModel):
    fullQuiz: list[QuizFormat]


class TeacherState(rx.State):
    img: list[str] = []
    ai_result: list[tuple[int, str, list[str], int]] = []
    resultFinal: str = ""
    file_learning_styles: dict[str, str] = {}
    show_alert: bool = False

    def show_success_alert(self):
        self.show_alert = True

    def hide_success_alert(self):
        self.show_alert = False

    def set_learning_style(self, filename: str, style: str):
        self.file_learning_styles[filename] = style


    def get_ai_result(self):
        return self.ai_result

    async def handle_upload(self, files: list[rx.UploadFile]):
        print("Begin")
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_upload_dir() / file.filename

            # Save the uploaded file.
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)

            # Update the image list (file names).
            self.img.append(file.filename)

            # Extract text from the PDF using pdfplumber
            extracted_text = self.extract_text_from_pdf(outfile)

            # Query OpenAI with the extracted text and specific prompt
            result = await self.query_openai(extracted_text, "Make a 10 question multiple-choice quiz based on the content of the pdf file. Each question should have 4 choices.")
            
            # Parse the result into a structured format
            self.ai_result = result
            
            quiz_data = json.loads(result)
            output_string = ""
            for question in quiz_data['fullQuiz']:
                question_num = question['question_num']
                question_text = question['question']
                answers = question['answers']
                correct_answer = answers[question['answerIndex']]
                with rx.session() as session:
                    db_entry = QuizModel(
                        fileName = file.filename,
                        questNum = question_num,
                        quest = question_text,
                        answOne = answers[0],
                        answTwo = answers[1],
                        answThree = answers[2],
                        answFour = answers[3],
                        ansInd = question['answerIndex'],
                        typeOf = self.file_learning_styles[file.filename]
                    )
                    session.add(db_entry)
                    session.commit()
                    
                    
                # Create a formatted string for each question
                output_string += f"Question {question_num}: {question_text}\n"
                for i, answer in enumerate(answers):
                    # Convert index to corresponding letter (a, b, c, d)
                    letter = chr(97 + i)  # 97 is the ASCII code for 'a'
                    output_string += f"  {letter}. {answer}\n"
                output_string += f"Correct Answer: {correct_answer}\n\n"


            self.resultFinal = output_string
            print("end")
            self.show_success_alert()

    def extract_text_from_pdf(self, pdf_path: Path) -> str:
        """Extracts text from the given PDF file using pdfplumber."""
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ""
            for page in pdf.pages:
                full_text += page.extract_text() or ""
        return full_text

    async def query_openai(self, pdf_text: str, prompt: str) -> str:
        """Sends the PDF text to OpenAI with the specified prompt."""
        response = openai.beta.chat.completions.parse(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an assistant that creates quizzes from documents. It should have 10 questions and be multiple choice."},
                {"role": "user", "content": f"{prompt}\n\nDocument content:\n{pdf_text}"}
            ],
            response_format=Quiz,
        )
        return response.choices[0].message.content
    


# Define the learningMaterials component
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
                rx.selected_files("upload1"),
                lambda file: rx.hstack(
                    rx.text(file),
                    rx.select(
                        ["Visual", "Audio", "Hands On"],
                        placeholder="Select learning style",
                        on_change=lambda value: TeacherState.set_learning_style(file, value),
                    ),
                )
            ),
            justify="center",
            align="center"
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
        rx.text(TeacherState.resultFinal, size="4"),
        rx.alert_dialog.root(
            rx.alert_dialog.content(
                rx.alert_dialog.title("Upload Successful"),
                rx.alert_dialog.description(
                    "Your files have been uploaded successfully.",
                    size="2",
                ),
                rx.flex(
                    rx.alert_dialog.action(
                        rx.button(
              
              "OK",
                            on_click=TeacherState.hide_success_alert,
                        ),
                    ),
                    justify="end",
                ),
            ),
            open=TeacherState.show_alert,
        ),
        align="center",
        justify="center",
        padding="5em"
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
