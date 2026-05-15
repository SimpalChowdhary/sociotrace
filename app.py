from flask import Flask, render_template, request
from main import run_osint_pipeline

app = Flask(__name__)

# ------------------------------
# Home Page
# ------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# ------------------------------
# Run OSINT Analysis
# ------------------------------
@app.route("/analyze", methods=["POST"])
def analyze():

    profile_url = request.form["profile"]
    result = run_osint_pipeline(profile_url)

    # Handle error
    if "error" in result:
        return render_template("results.html", error=result["error"])

    # --------------------------------
    # 🔥 FIX: Normalize platform data
    # --------------------------------
    platform_info = None

    if result.get("platform_data"):

        # LinkedIn → nested inside "data"
        if isinstance(result["platform_data"], dict) and result["platform_data"].get("data"):
            platform_info = result["platform_data"]["data"]

        # GitHub / others → already flat
        else:
            platform_info = result["platform_data"]

    # --------------------------------
    # Image Analysis
    # --------------------------------
    image_analysis = result.get("image_analysis")

    # --------------------------------
    # Graph Visualization
    # --------------------------------
    graph_path = result.get("graph")

    # --------------------------------
    # Render Results Page
    # --------------------------------
    return render_template(
        "results.html",

        username=result.get("username"),
        platform=result.get("platform"),

        # ✅ FIXED
        platform_data=platform_info,

        # Sherlock
        sherlock=result.get("sherlock"),

        # NLP
        nlp=result.get("nlp"),
        interests=result.get("interests"),

        # Risk
        risk=result.get("risk"),

        # ✅ ADDED (your new feature)
        account_type=result.get("account_type"),

        # Image
        image_analysis=image_analysis,

        # Summary
        summary=result.get("summary"),

        # Recommendations
        recommendations=result.get("recommendations", []),

        # Graph
        graph=graph_path,

        # ✅ FIXED (correct key)
        attacker_view=result.get("attacker_view", [])
    )


# ------------------------------
# Run Flask Server
# ------------------------------
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)