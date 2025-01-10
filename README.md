# Theft Detection using YOLOv11

![Theft Detection](https://img.shields.io/badge/YOLOv11-TheftDetection-brightgreen.svg)

This project uses the YOLOv11 object detection model to identify theft activities, particularly focusing on individuals wearing black masks. The model is trained with a custom dataset and achieves an accuracy of **90%**, making it a reliable solution for real-world theft detection scenarios.

## 🚀 Features
- Detects individuals wearing black masks as a theft indicator.
- Trained using YOLOv11 for state-of-the-art object detection performance.
- Real-time detection capabilities.
- Easily customizable and extendable for additional theft-related scenarios.

---

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/alihassanml/Theft-Detection.git
   cd Theft-Detection
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the pre-trained YOLOv11 weights and place them in the `weights` directory:
   - [YOLOv11 Weights](https://link-to-yolov11-weights)

4. Set up the configuration file:
   - Modify the `config.yaml` file to match your environment and dataset paths.

---

## 🔍 Usage

### 1. Training
To train the model on your dataset:
```bash
python train.py --config config.yaml
```

### 2. Inference
To detect theft in a video or live feed:
```bash
python detect.py --source <video_path_or_camera>
```

Example:
```bash
python detect.py --source data/test_video.mp4
```

### 3. Evaluation
To evaluate the model on the test dataset:
```bash
python evaluate.py --config config.yaml
```

---

## 📂 Project Structure
```
Theft-Detection/
├── data/                  # Dataset files
├── weights/               # Pre-trained YOLOv11 weights
├── models/                # YOLOv11 model architecture
├── utils/                 # Utility scripts
├── train.py               # Training script
├── detect.py              # Inference script
├── evaluate.py            # Evaluation script
├── config.yaml            # Configuration file
└── README.md              # Project documentation
```

---

## 🧠 Model Performance
- **Accuracy:** 90%
- **Precision/Recall:** Available in the `evaluation_results.txt` file.

---

## 💡 Future Improvements
- Support detection for more theft indicators (e.g., specific clothing or suspicious behavior).
- Enhance dataset diversity for better generalization.
- Implement a real-time alert system using IoT devices.

---

## 🤝 Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`feature-xyz`).
3. Commit your changes.
4. Open a Pull Request.

---

## 📜 License
This project is licensed under the [MIT License](LICENSE).

---

## ✉️ Contact
- **Ali Hassan**  
  - GitHub: [alihassanml](https://github.com/alihassanml)  
  - Email: alihassanbscs99@gmail.com 
```
