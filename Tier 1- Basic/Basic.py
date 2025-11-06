from fastapi import FastAPI

app = FastAPI(title="Cybersecurity Protection — Basic")

@app.get("/healthz")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {
        "tier": "Basic",
        "features": [
            "24/7 threat monitoring & incident response",
            "Endpoint detection & response (EDR/XDR)",
            "Firewall & VPN configuration + management",
            "Cloud security posture management (AWS/Azure/GCP)",
            "Security awareness training for employees",
        ],
    }
