# Commuse

Semantic git commit message scribe that follows the Conventional Commits specification.

## Features

- Generates semantic commit messages from staged changes
- Follows Conventional Commits specification
- Provides both commit title and description
- Modern CLI with rich formatting

## Installation

```bash
pip install commuse
```

## Usage

1. Stage your changes:
   ```bash
   git add .
   ```

2. Generate a commit message:
   ```bash
   commuse generate
   ```

## Configuration

Create a `.env` file in your project root:

```env
OPENAI_API_KEY=your_api_key_here
```

## License

MIT
