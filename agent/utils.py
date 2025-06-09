import pymupdf4llm
from pathlib import Path
from typing import List, Dict, Union
import os

class PDFProcessor:
    def __init__(self, output_dir: str = "processed_docs"):
        """
        Initialize PDF processor with output directory for processed files
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def process_pdf(self, pdf_path: str, write_images: bool = True) -> Dict:
        """
        Process a PDF file and extract its content in LLM-friendly format
        
        Args:
            pdf_path: Path to the PDF file
            write_images: Whether to extract and save images
            
        Returns:
            Dictionary containing:
            - markdown_text: The extracted text in markdown format
            - metadata: Document metadata
            - images: List of extracted images (if any)
        """
        try:
            # Extract markdown text
            md_text = pymupdf4llm.to_markdown(
                pdf_path,
                write_images=write_images,
                image_path=self.output_dir,
                image_format="png",
                dpi=300
            )
            
            # Get document metadata
            doc = pymupdf4llm.open(pdf_path)
            metadata = {
                "title": doc.metadata.get("title", ""),
                "author": doc.metadata.get("author", ""),
                "subject": doc.metadata.get("subject", ""),
                "keywords": doc.metadata.get("keywords", ""),
                "page_count": len(doc),
                "file_size": os.path.getsize(pdf_path)
            }
            
            # Get list of extracted images if any
            images = []
            if write_images:
                image_dir = Path(self.output_dir)
                images = [str(f) for f in image_dir.glob(f"{Path(pdf_path).stem}*.png")]
            
            return {
                "markdown_text": md_text,
                "metadata": metadata,
                "images": images
            }
            
        except Exception as e:
            raise Exception(f"Error processing PDF {pdf_path}: {str(e)}")

    def process_pdf_for_llama_index(self, pdf_path: str) -> List:
        """
        Process a PDF file and convert it to LlamaIndex documents
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            List of LlamaIndex documents
        """
        try:
            llama_reader = pymupdf4llm.LlamaMarkdownReader()
            llama_docs = llama_reader.load_data(pdf_path)
            return llama_docs
        except Exception as e:
            raise Exception(f"Error processing PDF for LlamaIndex {pdf_path}: {str(e)}") 