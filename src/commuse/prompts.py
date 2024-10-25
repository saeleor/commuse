"""Prompt templates for the AI model."""

SYSTEM_PROMPT = """You are a commit message generation assistant.
Your task is to analyze git diffs and generate semantic commit messages that
follow the Conventional Commits specification.

Guidelines:
- Type must be one of: feat, fix, docs, style, refactor, perf, test, chore
- Messages should be concise and clear
- Scope is optional
- Break down complex changes into a short title and detailed description
- Focus on the "what" and "why", not the "how"
"""

def get_commit_prompt(diff: str) -> str:
    """Generate the prompt for commit message generation."""
    
    return f"""Given the following git diff, generate a semantic commit message
with title and description. The message should follow the conventional commits
specification.

# Rules:
1. Title format: type(scope): description
2. Title should be under 70 characters
3. Add a blank line after title
4. Description should explain the motivation and impact
5. Wrap description at 72 characters

# Git diff:
{diff}

# Generate both title and description, separated by a blank line.
"""
