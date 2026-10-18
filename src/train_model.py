# src/train_model.py
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score

def generate_synthetic_biomarker_data(num_samples=1000):
    """
    Generates synthetic biomedical and biomarker data for prototyping
    the AI classification engine before large-scale clinical dataset integration.
    """
    np.random.seed(42)
    
    # Simulating clinical features: [Age, White Blood Cell Count, Inflammatory Marker (CRP), Viral Load Proxy]
    age = np.random.randint(18, 80, size=num_samples)
    wbc_count = np.random.normal(7.0, 2.0, size=num_samples)  # Normal range ~4.5 - 11.0 10^3/uL
    crp_level = np.random.exponential(3.0, size=num_samples)  # C-reactive protein mg/L
    viral_load_proxy = np.random.exponential(1.5, size=num_samples)
    
    # Target label: 1 if anomaly/disease detected, 0 if normal
    # Higher CRP and viral load proxy increase the probability of an abnormal label
    risk_score = (0.02 * (age - 30)) + (0.1 * (wbc_count - 7)) + (0.2 * crp_level) + (0.3 * viral_load_proxy)
    probabilities = 1 / (1 + np.exp(-risk_score)) # Sigmoid function
    target = (probabilities > np.percentile(probabilities, 75)).astype(int) # Top 25% marked as positive findings
    
    df = pd.DataFrame({
        "Age": age,
        "WBC_Count": wbc_count,
        "CRP_Level": crp_level,
        "Viral_Load_Proxy": viral_load_proxy,
        "Anomaly_Label": target
    })
    
    return df

def train_baseline_classifier():
    print("=" * 60)
    print("PROJECT OMNISCAN AI: BASELINE AI/ML CLASSIFICATION ENGINE")
    print("=" * 60)
    
    # 1. Generate dataset
    print("Generating synthetic biomedical training dataset...")
    df = generate_synthetic_biomarker_data(num_samples=1500)
    
    # Split features (X) and target (y)
    X = df[["Age", "WBC_Count", "CRP_Level", "Viral_Load_Proxy"]]
    y = df["Anomaly_Label"]
    
    # 2. Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"Training samples: {len(X_train)} | Testing samples: {len(X_test)}")
    
    # 3. Model Selection & Training (Random Forest Classifier)
    print("Training Random Forest classification model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # 4. Evaluation
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]
    
    acc = accuracy_score(y_test, y_pred)
    try:
        roc_auc = roc_auc_score(y_test, y_prob)
    except Exception:
        roc_auc = 0.5
        
    print("\n--- Model Evaluation Metrics ---")
    print(f"Accuracy : {acc * 100:.2f}%")
    print(f"ROC-AUC  : {roc_auc:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Save model summary
    print("=" * 60)
    print("AI baseline model successfully trained and evaluated.")

if __name__ == "__main__":
    train_baseline_classifier()