"""Commit message generation module."""
from dataclasses import dataclass
import os
from openai import OpenAI
from dotenv import load_dotenv
from .prompts import SYSTEM_PROMPT, get_commit_prompt

load_dotenv()

@dataclass
class CommitMessage:
    """Structured commit message."""
    title: str
    description: str

def generate_commit_message(diff: str) -> CommitMessage:
    """Generate a semantic commit message using OpenAI."""
    client = OpenAI()
    
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": get_commit_prompt(diff)},
        ]
    )
    
    response = completion.choices[0].message.content.strip()
    parts = response.split('\n\n', 1)
    
    title = parts[0].strip()
    description = parts[1].strip() if len(parts) > 1 else ""
    
    return CommitMessage(title=title, description=description)
