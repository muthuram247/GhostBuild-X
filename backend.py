from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# -----------------------------
# Intent Detection
# -----------------------------

def detect_project_type(idea):
    text = idea.lower()

    if any(word in text for word in ["website", "web app", "web application"]):
        return "Web Application"

    if any(word in text for word in ["mobile app", "android app", "ios app"]):
        return "Mobile Application"

    if any(word in text for word in ["api", "backend", "rest api"]):
        return "Backend/API"

    if any(word in text for word in ["desktop app", "desktop application"]):
        return "Desktop Application"

    if any(word in text for word in [
        "ai",
        "artificial intelligence",
        "machine learning"
    ]):
        return "AI Application"

    return "Software Application"


# -----------------------------
# Feature Detection
# -----------------------------

def detect_features(idea):
    text = idea.lower()
    features = []

    feature_keywords = {
        "Authentication": [
            "login",
            "sign in",
            "signup",
            "register",
            "authentication"
        ],
        "Database": [
            "database",
            "store data",
            "save data",
            "records"
        ],
        "AI": [
            "ai",
            "artificial intelligence",
            "machine learning",
            "chatbot"
        ],
        "Payments": [
            "payment",
            "payments",
            "razorpay",
            "stripe"
        ],
        "Notifications": [
            "notification",
            "notifications",
            "alert",
            "alerts"
        ],
        "Analytics": [
            "analytics",
            "dashboard",
            "statistics",
            "reports"
        ],
        "Search": [
            "search",
            "find"
        ],
        "Admin Panel": [
            "admin",
            "administrator"
        ]
    }

    for feature, keywords in feature_keywords.items():
        if any(keyword in text for keyword in keywords):
            features.append(feature)

    return features


# -----------------------------
# Technology Recommendation
# -----------------------------

def recommend_technologies(project_type, features):
    frontend = "HTML, CSS, JavaScript"
    backend = "Python Flask"
    database = "SQLite"

    if project_type == "Mobile Application":
        frontend = "Flutter"

    if "Database" in features:
        database = "PostgreSQL"

    if "AI" in features:
        backend = "Python Flask + AI Service"

    return {
        "frontend": frontend,
        "backend": backend,
        "database": database
    }


# -----------------------------
# Module Generation
# -----------------------------

def create_modules(features):
    modules = [
        "User Interface",
        "Backend API"
    ]

    if "Authentication" in features:
        modules.append("Authentication")

    if "Database" in features:
        modules.append("Database Management")

    if "AI" in features:
        modules.append("AI Processing")

    if "Payments" in features:
        modules.append("Payment Processing")

    if "Notifications" in features:
        modules.append("Notification System")

    if "Analytics" in features:
        modules.append("Analytics and Reporting")

    if "Search" in features:
        modules.append("Search System")

    if "Admin Panel" in features:
        modules.append("Admin Panel")

    return modules


# -----------------------------
# Development Task Generation
# -----------------------------

def create_tasks(modules):
    tasks = [
        "Define project requirements",
        "Design system architecture",
        "Create project structure",
        "Implement frontend",
        "Implement backend API"
    ]

    for module in modules:
        if module not in ["User Interface", "Backend API"]:
            tasks.append(f"Implement {module}")

    tasks.extend([
        "Test the application",
        "Validate generated project",
        "Prepare project documentation"
    ])

    return tasks


# -----------------------------
# GhostBuild-X Analysis Engine
# -----------------------------

def analyze_project(idea):
    project_type = detect_project_type(idea)
    features = detect_features(idea)

    technologies = recommend_technologies(
        project_type,
        features
    )

    modules = create_modules(features)

    tasks = create_tasks(modules)

    return {
        "idea": idea,
        "project_type": project_type,
        "detected_features": features,
        "recommended_technologies": technologies,
        "modules": modules,
        "development_tasks": tasks
    }


# -----------------------------
# API Routes
# -----------------------------

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "name": "GhostBuild-X",
        "status": "running",
        "message": "GhostBuild-X backend is working"
    })


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "project": "GhostBuild-X"
    })


@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "error": "Request body is required"
        }), 400

    idea = data.get("idea", "").strip()

    if not idea:
        return jsonify({
            "success": False,
            "error": "Project idea is required"
        }), 400

    result = analyze_project(idea)

    return jsonify({
        "success": True,
        "project": result
    })


# -----------------------------
# Run Server
# -----------------------------

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
