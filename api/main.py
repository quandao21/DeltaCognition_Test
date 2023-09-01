from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
import fitz
import os
import transformers
from transformers import T5ForConditionalGeneration, T5Tokenizer
from sentence_transformers import SentenceTransformer, util

Summaried_model = T5ForConditionalGeneration.from_pretrained('t5-small')
tokenizer = T5Tokenizer.from_pretrained('t5-small')
length = 100

Textual_similarity_model = SentenceTransformer('saved_models\model_ver1')

app = FastAPI()
# Configure CORS
origins = [
    "http://127.0.0.1:5500",  # Allow your web interface's origin
    "http://localhost:5500",  # Additional origin if applicable
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def extract_text_from_pdf(pdf_path):
    text = ""
    pdf_document = fitz.open("pdf", pdf_path)

    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text += page.get_text()

    pdf_document.close()
    words_in_text = text.split()
    return " ".join(words_in_text[:500])

def recommendation(score):
    # Define threshold values for different recommendations
    confident_threshold = 0.8
    moderate_threshold = 0.3
    low_threshold = 0.1

    if score >= confident_threshold:
        return "You should definitely read the article."
    elif score >= moderate_threshold:
        return "You can consider reading the article."
    elif score >= low_threshold:
        return "I think it's not very suitable. You might want to reconsider reading the article."
    else:
        return "You probably should not read the article."



@app.post("/read_PDF")
async def read_PDF(file: UploadFile = File()):
    pdf_file = await file.read()
    extracted_text = extract_text_from_pdf(pdf_file)
    input_ids = tokenizer.encode("summarize: "+ extracted_text, return_tensors='pt')
    summary = Summaried_model.generate(input_ids, max_length=length)
    summary_text = tokenizer.decode(summary[0], skip_special_tokens=True)
    print(summary_text)
    # print(extracted_text)
    return {"summary": summary_text}

@app.post("/read_text")
async def read_text(data: dict):
    user_text = data.get('text', '')

    # Process the user input text
    extracted_text = user_text
    input_ids = tokenizer.encode("summarize: " + extracted_text, return_tensors='pt')
    summary = Summaried_model.generate(input_ids, max_length=length)
    summary_text = tokenizer.decode(summary[0], skip_special_tokens=True)
    print(summary_text)
    return {"summary": summary_text}

@app.post("/evaluate_similarity")
async def evaluate_similarity(data: dict):
    user_content = data.get('content', '')
    summaried_content = data.get('summary', '')
    query_embedding = Textual_similarity_model.encode(user_content)
    passage_embedding = Textual_similarity_model.encode(summaried_content)
    scores = util.cos_sim(query_embedding, passage_embedding)
    # print(user_content)
    # print(summaried_content)
    
    return {"score": scores[0,0].item(), "recommendation": recommendation(scores[0,0].item())}

if __name__ == "__main__":
    uvicorn.run(app,host='localhost',port=8000)