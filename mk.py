import google.generativeai as genai
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyBAXAbz6I3yhzbWuaWTQyPN9uttEc3HpMU"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

models = genai.list_models()
for model in models:
    print(model.name)

