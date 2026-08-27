function setResult(type, message, details = "") {
    const resultBox = document.getElementById("result");

    resultBox.style.display = "block";
    resultBox.className = "result " + type;

    if (details) {
        resultBox.innerHTML = `
            <div class="result-title">${message}</div>
            <div class="result-details">${details}</div>
        `;
    } else {
        resultBox.textContent = message;
    }
}


function getPayload() {
    return {
        Age: Number(document.getElementById("age").value),
        Fare: Number(document.getElementById("fare").value),
        Embarked: document.getElementById("embarked").value,
        Sex: document.getElementById("sex").value,
        Pclass: Number(document.getElementById("pclass").value),
        FamilySize: Number(document.getElementById("familySize").value),
        IsAlone: document.getElementById("isAlone").checked
    };
}


function validatePayload(payload) {
    if (Number.isNaN(payload.Age) || payload.Age < 0) {
        return "Age must be a valid non-negative number.";
    }

    if (Number.isNaN(payload.Fare) || payload.Fare < 0) {
        return "Fare must be a valid non-negative number.";
    }

    if (Number.isNaN(payload.FamilySize) || payload.FamilySize < 0) {
        return "Family Size must be a valid non-negative number.";
    }

    return null;
}


async function predict() {
    const button = document.querySelector("button");
    const payload = getPayload();
    const validationError = validatePayload(payload);

    if (validationError) {
        setResult("error", "Invalid input", validationError);
        return;
    }

    button.disabled = true;
    button.textContent = "Running model...";

    setResult("", "Model is calculating prediction...");

    try {
        const response = await fetch("/predict_model", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (!response.ok) {
            setResult("error", "API request failed", JSON.stringify(data));
            return;
        }

        const prediction = data.Prediction || data.prediction || data.result;
        const requestCount = data.request_count || data.requestCount;

        if (prediction === "Survived") {
            setResult(
                "success",
                "Prediction: Survived",
                requestCount ? `API request count: ${requestCount}` : "The model predicts that this passenger survived."
            );
        } else if (prediction === "Not survived") {
            setResult(
                "danger",
                "Prediction: Not survived",
                requestCount ? `API request count: ${requestCount}` : "The model predicts that this passenger did not survive."
            );
        } else {
            setResult("error", "Unexpected API response", JSON.stringify(data));
        }

    } catch (error) {
        setResult("error", "Request failed", String(error));
    } finally {
        button.disabled = false;
        button.textContent = "Run Prediction";
    }
}