from fastapi import FastAPI

app = FastAPI(title="System Maintenance & Optimization — Pro")

@app.get("/healthz")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {
        "tier": "Pro",
        "features": [
            "Predictive patch automation (SmartPatch™)",
            "Backup & disaster recovery (QuickRecover Vault)",
            "Hardware & software lifecycle management",
            "Performance tuning & resource optimization",
        ],
    }
