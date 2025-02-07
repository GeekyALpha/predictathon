# predictathon
**README for Predictathon Deepfake Detection**

This document provides an overview of the Deepfake Detection AI model developed for Predictathon 2025. The model is designed to accurately classify real and fake images using CNN-based feature extraction and deep learning models.

---

**Project Overview**

This project aims to build a highly accurate deepfake detection model that generalizes well to unseen images. The model is trained on real and fake images with their corresponding deepfake probability scores, enabling it to distinguish between authentic and manipulated media.

---

**Project Structure**

predictathon/
- train/
  - fake_cifake_images/
  - real_cifake_images/
  - fake_cifake_preds.json
  - real_cifake_preds.json
- test/
  - test_images/
- outputs/
  - cifake_model.pth  # Trained Model
  - teamname_prediction.json  # Final JSON Output
- notebooks/
  - training_notebook.ipynb
  - evaluation_notebook.ipynb
- api/
  - app.py  # Flask API
- streamlit_app/
  - app.py  # Streamlit Frontend
- teamname_presentation.pptx  # Final PPT Submission
- README.md  # This File

---

**Dataset & Preprocessing**

**Dataset Used:**
- CIFake Dataset (Deepfake & Real Images)
- JSON file containing deepfake detection scores  

**Preprocessing Steps:**
- Resized images to 224x224 pixels  
- Normalized using mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]  
- Data Augmentation (Flip, Rotation, Brightness Adjustments)  
- Loaded images using PyTorch’s DataLoader  

---

**Model Architecture**

**Base Model:**  
- ResNet18 (Pretrained on ImageNet)  
- Replaced Fully Connected Layer with a single neuron for binary classification  

**Training Configuration:**  
- Loss Function: Binary Cross-Entropy Loss  
- Optimizer: Adam (Learning Rate: 0.0001)  
- Batch Size: 32  
- Training Epochs: 10  
- Validation Split: 20%  

---

**Model Performance**

| Epoch  | Loss  | Accuracy  |
|--------|-------|----------|
| 1      | 0.3096 | 86.70%  |
| 2      | 0.0896 | 97.00%  |
| 3      | 0.0303 | 99.05%  |
| 4      | 0.0269 | 99.30%  |
| 5      | 0.0251 | 99.25%  |
| 6      | 0.0157 | 99.75%  |
| 7      | 0.0140 | 99.60%  |
| 8      | 0.0221 | 99.35%  |
| 9      | 0.0139 | 99.60%  |
| 10     | 0.0084 | 99.85%  |

**Evaluation Metrics:**  
- Accuracy: 99.80%  
- Precision: 99.80%  
- Recall: 99.80%  
- F1 Score: 99.80%  

---

**Deployment**

**Backend (Flask API)**

We deployed the trained model using Flask API on Google Colab, exposing it through ngrok for external access.

**Run API in Google Colab:**
```
!python api/app.py &
from pyngrok import ngrok
public_url = ngrok.connect(5000)
print("API is running at:", public_url)
```

**Frontend (Streamlit)**

A Streamlit Web App was built for user interaction, allowing image uploads and real-time deepfake detection.

**Run Streamlit App Locally:**
```
streamlit run streamlit_app/app.py
```

---

**API Usage**

**Endpoint:**  
```
POST https://<your-ngrok-url>/predict
```

**Request Format:**
```
{
  "file": "image.jpg"
}
```

**Sample Response:**
```
{
  "label": "FAKE",
  "confidence": 0.95
}
```

---

**Challenges & Solutions**

**Challenges Faced**
- Imbalanced Dataset (More real images than fake)  
- Overfitting on training data  
- Compute constraints in Google Colab  
- Ensuring accurate predictions on unseen images  

**Solutions Implemented**
- Data Augmentation to balance dataset  
- Early Stopping & Dropout Layers to prevent overfitting  
- Fine-tuned Learning Rate Scheduling  
- Implemented Grad-CAM Visualization to interpret model predictions  

---

**Future Improvements**

- Use Vision Transformers (ViTs) for better deepfake detection.  
- Improve real-time processing for faster inference.  
- Implement Self-Supervised Learning (SSL) for feature extraction.  
- Deploy as a scalable cloud-based API for broader adoption.  

---

**Conclusion**

- Successfully developed a 99.85% accurate deepfake detection model.  
- Implemented advanced preprocessing, feature extraction, and model training techniques.  
- Deployed as an API + Web App for real-time deepfake detection.  
- Future work includes faster inference & enhanced model robustness.  

---

**Contributors**

- **Team Name:** sanskarshree1182  
- **Hackathon:** Predictathon 2025  
- **Contact:** sanskarshree11822gmail.com  

