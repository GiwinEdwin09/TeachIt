import reflex as rx
from ..components.navbar import Navbar
from .student import StudentState
from sqlmodel import select
from .teacher import QuizModel 

class QuizQuestion(rx.Base):
    fileName: str
    questNum: int
    quest: str
    answOne: str
    answTwo: str
    answThree: str
    answFour: str
    ansInd: int
    typeOf: str

class PracticeState(rx.State):
    questions_data: list[QuizQuestion] = []
    current_question: int = 0
    selected_answer: str | None = None
    score: int = 0

    async def load_questions(self):
        student_state = await self.get_state(StudentState)

        query = select(QuizModel).where(
            (QuizModel.typeOf == 'Visual' if student_state.visTrue else False) |
            (QuizModel.typeOf == 'Audio' if student_state.AudTrue else False) |
            (QuizModel.typeOf == 'Hands On' if student_state.HandTrue else False)
        ).limit(10)

        with rx.session() as session:
            self.questions_data = [QuizQuestion(**q.dict()) for q in session.exec(query)]

    def submit_answer(self, answer):
        if self.current_question < len(self.questions_data):
            if answer == self.questions_data[self.current_question].ansInd:
                self.score += 1
            self.current_question += 1

    async def reset_quiz(self):
        self.current_question = 0
        self.selected_answer = None
        self.score = 0
        await self.load_questions()

    @rx.var
    def quiz_completed(self) -> bool:
        return self.current_question >= len(self.questions_data)


@rx.page(route="/practice", on_load=PracticeState.load_questions)
def practice():
    return rx.container(
        Navbar(),
        rx.vstack(
            rx.cond(
                PracticeState.questions_data.length() > 0,
                rx.cond(
                    PracticeState.quiz_completed,
                    rx.vstack(
                        rx.heading("Quiz Completed"),
                        rx.text(f"Your score: {PracticeState.score} / {PracticeState.questions_data.length()}"),
                    ),
                    rx.vstack(
                        rx.heading(f"Question {PracticeState.current_question + 1}"),
                        rx.text(PracticeState.questions_data[PracticeState.current_question].quest),
                        rx.button(
                            PracticeState.questions_data[PracticeState.current_question].answOne,
                            on_click=PracticeState.submit_answer(1),
                        ),
                        rx.button(
                            PracticeState.questions_data[PracticeState.current_question].answTwo,
                            on_click=PracticeState.submit_answer(2),
                        ),
                        rx.button(
                            PracticeState.questions_data[PracticeState.current_question].answThree,
                            on_click=PracticeState.submit_answer(3),
                        ),
                        rx.button(
                            PracticeState.questions_data[PracticeState.current_question].answFour,
                            on_click=PracticeState.submit_answer(4),
                        ),
                    ),
                ),
            ),
            justify="center",
            align="center",
            height="100vh",
            spacing="2em",
        ),
    )