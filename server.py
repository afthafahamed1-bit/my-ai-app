from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Allow your app to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # in production, replace * with your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PERPLEXITY_API_KEY = "pplx-ek3J0JsdsmseDh6btBiqNbANUmUArcNHCje9XqRsaqy9wDpnX"

@app.post("/api/perplexity")
async def perplexity_chat(request: Request):
    body = await request.json()
    query = body.get("query")

    try:
        response = requests.post(
            "https://api.perplexity.ai/chat/completions",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {PERPLEXITY_API_KEY}"
            },
            json={
                "model": "llama-3.1-sonar-large-128k-online",
                "messages": [{"role": "user", "content": query}],
                "temperature": 0.2
            }
        )
        return response.json()
    except Exception as e:
        return {"error": str(e)}
