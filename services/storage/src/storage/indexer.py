import os

from bs4 import BeautifulSoup, Comment
import pdfplumber
import faiss
import numpy as np
import docx2txt
from transformers import pipeline
from sentence_transformers import SentenceTransformer
from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer

cwd = os.getcwd()
model_name = "google/flan-t5-small"
model_dir = os.path.join(cwd,"data/models/flan-t5-small")

# Create the directory if it doesn't exist
os.makedirs(model_dir, exist_ok=True)

# Load and save the model and tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Save the model and tokenizer locally
#model.save_pretrained(model_dir)
#tokenizer.save_pretrained(model_dir)

print(f"Model saved to: {model_dir}")

# Load LLM and embedding models
embedding_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
#llm = pipeline("text-generation", model="EleutherAI/gpt-j-6B", device=0)
# Load the model and tokenizer from the saved directory
model = AutoModelForSeq2SeqLM.from_pretrained(model_dir)
tokenizer = AutoTokenizer.from_pretrained(model_dir)
index_path = os.path.join(os.getcwd(),'data/document_index.faiss')
# Initialize the pipeline with the local model
llm = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

'''
def text_from_docx(filename:str)-> str:
    try:
        text = docx2txt.process(filename)
        return text
    except Exception as e:
        print(str(e))
        return ''


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_pdf(filename):
    #with pdfplumber.open(filename) as pdf:
    #å    return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    
    try:
        with pdfplumber.open(filename) as pdf:
            text = ""
            for page in pdf.pages:
                try:
                    text += page.extract_text() + "\n"
                except Exception as e:
                    print(f"Error extracting page: {e}")
            return text
    except Exception as e:
        print(f"Failed to open PDF: {e}")
        return ""
    
def text_from_html(filename):
    text = ''
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    soup = BeautifulSoup(text, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

def text_from_txt(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()
    
def extract_text(file_path):
    print('Analysing file: {0}'.format(file_path))
    if file_path.endswith(".pdf"):
        return text_from_pdf(file_path)   
    elif file_path.endswith(".docx"):
        return text_from_docx(file_path)
    elif file_path.endswith(".html"):
        return text_from_html(file_path)
    elif file_path.endswith(".txt"):
       return text_from_txt
    return ""


def create_index(texts):
    embeddings = embedding_model.encode(texts, convert_to_tensor=True).cpu().numpy()
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

# Gather text data
docs_path = "/Users/test/Downloads"  # Directory containing files
files_metadata = [{"file_name": f, "text": extract_text(os.path.join(docs_path, f))}
                  for f in os.listdir(docs_path) if f.endswith((".pdf", ".txt",'.docx','.html'))]
texts = [meta["text"] for meta in files_metadata]

# Create and save the index
index = create_index(texts)
faiss.write_index(index,index_path)


def search(query, k=3):
    query_embedding = embedding_model.encode([query], convert_to_tensor=True).cpu().numpy()
    index = faiss.read_index("document_index.faiss")
    distances, indices = index.search(query_embedding, k)
    return [files_metadata[i]["file_name"] for i in indices[0]]

# Example search
print("Top results:", search("renewable energy sources"))
'''

def query_llm(files):
    combined_text = "\n".join([files_metadata[i]["text"] for i in files])
    prompt = f"Summarize the following text: {combined_text}"
    response = llm(prompt, max_length=200, num_return_sequences=1)
    return response[0]['generated_text']

# Display the response
result_files = search("renewable energy sources")
print("Generated Summary:", query_llm(result_files))