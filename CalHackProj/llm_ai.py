import os 
from embedchain import App

from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = App()

app.reset()

app.add("./stp.pdf")

out = app.query("Make a quiz based on this")
 
print(out)

# find index of "Answers", and break the string in 2
