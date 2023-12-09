# pmGPT

pmGPT is a CLI application that uses GPT-4 to generate a project management plan based on a project description into one or more tasks.

## Installation

### Source

```bash
pip install -r requirements.txt
```

### Docker

```bash
docker build -t pmgpt .
```

### Windows

- Download the latest release from [here]()
- Extract the zip file
- Run `pmgpt.exe`

### Linux/MacOS

- Download the latest release from [here]()
- Extract the tar.gz file
- Run `pmgpt`

> Note: You can also add the executable to your PATH

## Usage

### Python

```bash
python -m cli.main --help
```

### Docker

```bash
docker run -it --rm pmgpt --help
```

### Windows

```bash
pmgpt.exe --help
```

### Linux/MacOS

```bash
pmgpt --help
```

## Examples

> You will need to create a [OpenAI API Key](https://platform.openai.com/api-keys). You will be prompted to enter your API key when you run the application for the first time.

You can create tasks from a project description by running:

```bash
pmgpt task new "Create a CLI application that uses GPT-4 to generate a project management plan based on a project description into one or more tasks."
```
You can see all the tasks by running:

```bash
pmgpt task list
```

You can see the details of a task by running:

```bash
pmgpt task show 1
```
