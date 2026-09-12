from flask import Flask, request, jsonify, send_from_directory
import re
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "..", "frontend")


def analyze_idea(idea):
    text = idea.lower()

    features = []

    keywords = {
        "Authentication": ["login", "signup", "register", "user", "authentication"],
        "Database": ["database", "data", "records", "storage"],
        "AI": ["ai", "artificial intelligence", "machine learning", "ml"],
        "Notifications": ["notification", "alert", "message", "reminder"],
        "Analytics": ["analytics", "analysis", "report", "dashboard", "statistics"],
        "Payments": ["payment", "payments", "upi", "transaction"],
        "Location": ["location", "gps", "map", "maps", "tracking"],
        "Search": ["search", "filter", "find"],
        "File Upload": ["file", "upload", "document", "image"],
        "API": ["api", "integration", "third party"]
    }

    for feature, words in keywords.items():
        if any(word in text for word in words):
            features.append(feature)

    if not features:
        features = ["User Interface", "Core Application Logic"]

    constraints = []

    if any(word in text for word in ["college", "school", "student"]):
        constraints.append("Simple and affordable deployment")

    if any(word in text for word in ["mobile", "android", "ios", "app"]):
        constraints.append("Mobile-friendly design")

    if any(word in text for word in ["real-time", "live", "instant"]):
        constraints.append("Low-latency or real-time communication")

    if "database" in text or "data" in text:
        constraints.append("Data storage and security")

    if not constraints:
        constraints = [
            "Define project scope",
            "Keep architecture modular",
            "Consider scalability and security"
        ]

    project_type = "Web Application"

    if any(word in text for word in ["android", "ios", "mobile app"]):
        project_type = "Mobile Application"

    if any(word in text for word in ["website", "web", "portal", "platform"]):
        project_type = "Web Application"

    technologies = {
        "Frontend": "HTML, CSS, JavaScript",
        "Backend": "Python + Flask",
        "Database": "SQLite / PostgreSQL"
    }

    if "AI" in features:
        technologies["AI Layer"] = "LLM / Machine Learning API"

    if "Notifications" in features:
        technologies["Notifications"] = "Email / Push Notification Service"

    if "Location" in features:
        technologies["Maps"] = "Maps API"

    architecture = [
        "User Interface",
        "Backend API"
    ]

    if "Database" in features:
        architecture.append("Database")

    if "AI" in features:
        architecture.append("AI Service")

    if "Notifications" in features:
        architecture.append("Notification Service")

    if "Analytics" in features:
        architecture.append("Analytics Module")

    if "Payments" in features:
        architecture.append("Payment Service")

    if "Location" in features:
        architecture.append("Location / Maps Service")

    tasks = [
        "Define project requirements",
        "Design application architecture",
        "Create project repository structure",
        "Build frontend interface",
        "Develop backend API",
        "Implement core features",
        "Add validation and error handling",
        "Test the application",
        "Prepare deployment"
    ]

    if "Authentication" in features:
        tasks.insert(4, "Implement user authentication")

    if "Database" in features:
        tasks.insert(5, "Design database schema")

    if "AI" in features:
        tasks.insert(6, "Integrate AI service")

    return {
        "project_type": project_type,
        "idea": idea,
        "requirements": features,
        "constraints": constraints,
        "technologies": technologies,
        "architecture": architecture,
        "development_tasks": tasks,
        "agent_context": {
            "project_name": "GhostBuild X",
            "goal": "Convert software intent into an executable engineering plan",
            "workflow": "Intent → Requirements → Constraints → Architecture → Tasks → Execution"
        }
    }


@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.get_json(silent=True)

    if not data or not data.get("idea"):
        return jsonify({
            "error": "Please provide a software idea."
        }), 400

    idea = data["idea"].strip()

    if len(idea) < 10:
        return jsonify({
            "error": "Please enter a more detailed software idea."
        }), 400

    result = analyze_idea(idea)

    return jsonify(result)


@app.route("/api/health")
def health():
    return jsonify({
        "status": "online",
        "project": "GhostBuild X"
    })


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))



