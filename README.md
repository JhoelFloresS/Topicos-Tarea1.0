# DEVELOPMENT MODE
KEVIN JHOEL FLORES SARMIENTO

1. Create your .venv folder with the next command
```cmd
    py -m venv .venv
```
2. Activate your virtual environment
```bash
    .venv/Scripts/activate
```
3. Install the packages
```bash
    pip install -r requirements.txt
```
4. Create your .env file based on .env.example
5. Write your API_KEY from openai to the .env
6. Start the server with:
```bash
    uvicorn src.app:app --reload
```
by default start at port 8000