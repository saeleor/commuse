"""Git operations module."""
import subprocess
from typing import Optional

def get_staged_changes() -> Optional[str]:
    """Get the staged changes from git."""
    try:
        result = subprocess.run(
            ['git', 'diff', '--cached'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout if result.stdout.strip() else None
    except subprocess.CalledProcessError:
        return None
