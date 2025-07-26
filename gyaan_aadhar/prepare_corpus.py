from google.auth import default
import vertexai
from vertexai.preview import rag
import os
from dotenv import load_dotenv, set_key
import requests
import tempfile

load_dotenv()

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
if not PROJECT_ID:
    raise ValueError(
        "GOOGLE_CLOUD_PROJECT environment variable not set. Please set it in your .env file."
    )
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION")
if not LOCATION:
    raise ValueError(
        "GOOGLE_CLOUD_LOCATION environment variable not set. Please set it in your .env file."
    )

CORPUS_DISPLAY_NAME = "NCERT_textbooks_corpus_first_standard"
CORPUS_DESCRIPTION = "Corpus containing NCERT Textbooks for First Standard"

# FILES_FOLDER = os.path.abspath(os.path.join(os.path.dirname(
#     __file__), "..", "..", "pdfs"))  # Change this path as needed
FILES_FOLDER="/home/user/agentone/gyaan_aadhar/data/1_mathematics"

ENV_FILE_PATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", ".env"))


def initialize_vertex_ai():
    credentials, _ = default()
    vertexai.init(
        project=PROJECT_ID, location=LOCATION, credentials=credentials
    )


def create_or_get_corpus():
    """Creates a new corpus or retrieves an existing one."""
    embedding_model_config = rag.EmbeddingModelConfig(
        publisher_model="publishers/google/models/text-embedding-004"
    )
    existing_corpora = rag.list_corpora()
    corpus = None

    for existing_corpus in existing_corpora:
        if existing_corpus.display_name == CORPUS_DISPLAY_NAME:
            corpus = existing_corpus
            print(
                f"Found existing corpus with display name '{CORPUS_DISPLAY_NAME}'")
            break
    if corpus is None:
        corpus = rag.create_corpus(
            display_name=CORPUS_DISPLAY_NAME,
            description=CORPUS_DESCRIPTION,
            embedding_model_config=embedding_model_config,
        )
        print(f"Created new corpus with display name '{CORPUS_DISPLAY_NAME}'")
    return corpus


def update_env_file(corpus_name, env_file_path):
    """Updates the .env file with the corpus name."""
    try:
        set_key(env_file_path, "RAG_CORPUS", corpus_name)
        print(f"Updated RAG_CORPUS in {env_file_path} to {corpus_name}")
    except Exception as e:
        print(f"Error updating .env file: {e}")


def upload_pdf_to_corpus(corpus_name, pdf_path, display_name, description):
    """Uploads a PDF file to the specified corpus."""
    print(f"Uploading {display_name} to corpus...")
    try:
        rag_file = rag.upload_file(
            corpus_name=corpus_name,
            path=pdf_path,
            display_name=display_name,
            description=description,
        )
        print(f"Successfully uploaded {display_name} to corpus")
        return rag_file
    except Exception as e:
        print(f"Error uploading file {display_name}: {e}")
        return None


def list_corpus_files(corpus_name):
    """Lists files in the specified corpus."""
    files = list(rag.list_files(corpus_name=corpus_name))
    print(f"Total files in corpus: {len(files)}")
    for file in files:
        print(f"File: {file.display_name} - {file.name}")


def main():

    initialize_vertex_ai()
    corpus = create_or_get_corpus()
    
    # Update the .env file with the corpus name
    update_env_file(corpus.name, ENV_FILE_PATH)

    # Loop through all files in the specified folder
    if not os.path.isdir(FILES_FOLDER):
        print(
            f"The folder {FILES_FOLDER} does not exist. Please update FILES_FOLDER.")
        return

    files_uploaded = 0
    for filename in os.listdir(FILES_FOLDER):
        file_path = os.path.join(FILES_FOLDER, filename)
        if os.path.isfile(file_path):
            upload_pdf_to_corpus(
                corpus_name=corpus.name,
                pdf_path=file_path,
                display_name=filename,
                description=f"Uploaded file: {filename}"
            )
            files_uploaded += 1
    print(f"Total files uploaded: {files_uploaded}")

    # List all files in the corpus
    list_corpus_files(corpus_name=corpus.name)


if __name__ == "__main__":
    main()
