import anthropic
import os
from typing import Optional


from fastmcp import FastMCP


api_key = os.getenv('ANTHROPIC_API_KEY')
if not api_key:
    raise ValueError("ANTHROPIC_API_KEY environment variable not found. Please set it in your .env file.")

mcp = FastMCP("claud_mcp")

@mcp.tool
def extract_pdf_text(pdf_url: str, prompt: str = "Extract all the text content from this PDF document.") -> str:
    """
    Extract text content from a PDF using Claude's document processing capabilities.
    
    Args:
        pdf_url (str): URL to the PDF document
        prompt (str): Custom prompt for text extraction (optional)
    
    Returns:
        str: Extracted text content from the PDF
    
    Raises:
        ValueError: If no API key is found in environment variables
        Exception: If the API request fails
    """
    # Initialize the Anthropic client using environment variable
    
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable not found. Please set it in your .env file.")
    
    client = anthropic.Anthropic(api_key=api_key)
    
    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",  # Using the latest available model
            max_tokens=4096,  # Increased for longer documents
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "document",
                            "source": {
                                "type": "url",
                                "url": pdf_url
                            }
                        },
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ],
        )
        
        # Extract the text content from the response
        if message.content and len(message.content) > 0:
            return message.content[0].text
        else:
            return "No content extracted from the PDF."
            
    except Exception as e:
        raise Exception(f"Failed to extract text from PDF: {str(e)}")
