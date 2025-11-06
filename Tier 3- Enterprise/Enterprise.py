from fastapi import FastAPI

app = FastAPI(title="Compliance & Risk Management — Enterprise")

@app.get("/healthz")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {
        "tier": "Enterprise",
        "features": [
            "Vulnerability scanning & reporting",
            "Compliance support: HIPAA, PCI-DSS, SOC 2, NIST",
            "Policy creation & risk assessment",
            "Security documentation & audit prep",
        ],
    }
