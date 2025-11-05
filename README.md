# Face Spoofing Detection Challenge

**Zindi + IndabaX Zimbabwe Hackathon: Building Africa's Next Generation of AI Innovators**

## Overview

This is a **Face Spoofing Detection Challenge** for the Zindi + IndabaX Zimbabwe Hackathon. Face spoofing (also known as face anti-spoofing) is a critical security challenge in biometric authentication systems. This project implements a detection system that can distinguish between genuine faces and spoofed faces using both color and depth image information.

The challenge involves building a deep learning model that can accurately classify faces as either **real** or **fake/spoofed** using a combination of RGB color images and depth maps.

## What is Face Spoofing?

**Face spoofing** refers to the act of deceiving facial recognition systems by presenting counterfeit facial data instead of a real person's face. This is a significant security vulnerability in systems that rely on facial biometrics for authentication.

### Common Face Spoofing Attack Types

1. **Printed Photo Attacks**: Using a printed photograph of an authorized individual
   - Static 2D images held up to the camera
   - Most basic form of spoofing attack

2. **Video Replay Attacks**: Displaying a video recording of the authorized person
   - Pre-recorded videos played on screens
   - More sophisticated than static photos

3. **3D Mask Attacks**: Using a three-dimensional mask resembling the authorized individual
   - High-quality 3D printed or silicone masks
   - Most advanced and challenging to detect

4. **Digital Manipulation**: Using deepfakes or digitally altered images
   - AI-generated or manipulated facial images
   - Emerging threat with modern AI capabilities

## Dataset Information

### Dataset Structure

The dataset contains pairs of **color** and **depth** images, which provide complementary information for robust spoofing detection:

```
face_spoofing_data/
├── train_img/
│   └── train_img/
│       ├── color/          # RGB face images (training data)
│       └── depth/          # Depth map images (training data)
├── test_img/
│   └── test_img/
│       ├── color/          # RGB face images (test data)
│       └── depth/          # Depth map images (test data)
└── val_img/
    └── val_img/
        ├── color/          # RGB face images (validation data for ranking)
        └── depth/          # Depth map images (validation data for ranking)
```

### Dataset Statistics

- **Training Set**: Pairs of color/depth images with labels
- **Validation Set**: Pairs of color/depth images (labels NOT provided - used for ranking)
- **Testing Set**: Pairs of color/depth images (labels NOT provided)
- **Image Format**: JPG files
- **Validation Images**: Named sequentially (image_01.jpg, image_02.jpg, ..., image_723.jpg)

### Why Color + Depth?

The combination of color and depth images is particularly effective for face spoofing detection:

- **Color Images**: Capture texture, color, and surface details that can reveal printing artifacts, screen reflections, or mask edges
- **Depth Images**: Provide 3D structure information that helps distinguish between:
  - Real faces (natural 3D curvature)
  - Flat printed photos (no depth variation)
  - Video screens (flat surface with no face depth)
  - 3D masks (artificial depth patterns)

Depth information is crucial because spoofed faces often lack the natural depth profile of real human faces, making depth maps a powerful anti-spoofing feature.

## Project Structure

```
.
├── face_spoofing_data/          # Dataset directory (ignored in git)
│   ├── train_img/              # Training images
│   ├── test_img/               # Test images
│   └── val_img/                # Validation images (for ranking)
├── presentations/               # Presentation materials (ignored in git)
├── Spoofing Detection Starter Notebook.ipynb  # Starter notebook with full pipeline
├── train.csv                   # Training data with labels (image_id, filename, label)
├── validation.csv              # Validation data WITHOUT labels (image_id, filename)
├── test.csv                    # Test data WITHOUT labels (image_id, filename)
├── sample_submission.csv       # Submission template (image_id, real, fake)
├── reference.csv               # Ground truth for validation (organizers only - ignored in git)
├── variables.txt               # Detailed description of all CSV files and variables
├── README.md                   # This file
└── .gitignore                  # Git ignore patterns
```

## CSV Files Description

### 1. `train.csv`
- **Purpose**: Training data with ground truth labels
- **Columns**: `image_id`, `filename`, `label`
- **Labels**: `0` = Real face, `1` = Fake/Spoofed face
- **Usage**: Use this to train your model

### 2. `validation.csv`
- **Purpose**: Validation data for ranking submissions (labels NOT provided)
- **Columns**: `image_id`, `filename`
- **Image IDs**: Sequential format (image_01, image_02, ..., image_723)
- **Usage**: Generate predictions on this set for ranking
- **⚠️ Important**: DO NOT use this for training! This is only for generating predictions.

### 3. `test.csv`
- **Purpose**: Test data for final submission (labels NOT provided)
- **Columns**: `image_id`, `filename`
- **Usage**: Generate predictions on this set for final submission

### 4. `sample_submission.csv`
- **Purpose**: Template for submission format
- **Columns**: `image_id`, `real`, `fake`
- **Format**: Probability scores for each class
  - `real`: Probability of being a real face (0.0 to 1.0)
  - `fake`: Probability of being a fake/spoofed face (0.0 to 1.0)
  - **Note**: `real + fake = 1.0` for each prediction
- **Usage**: Replace probabilities with your model's predictions

### 5. `reference.csv` (Organizers Only)
- **Purpose**: Ground truth labels for validation set
- **Columns**: `image_id`, `label`
- **Labels**: `real` = Real face, `fake` = Fake/Spoofed face
- **⚠️ Important**: This file is ONLY for organizers/evaluators. Participants should NOT use or access this file.

For detailed information about all CSV files, see `variables.txt`.

## Competition Workflow

### Step 1: Training
1. Use `train.csv` to load training images with labels
2. Load corresponding color and depth images from `face_spoofing_data/train_img/train_img/`
3. Train your model using the provided starter notebook or your own implementation

### Step 2: Validation Predictions (For Ranking)
1. Load images from `validation.csv` (no labels provided)
2. Images are located in `face_spoofing_data/val_img/val_img/`
3. Generate probability predictions for each image
4. Create a submission file with format: `image_id`, `real`, `fake`
5. Submit for ranking on the competition platform

### Step 3: Test Predictions (Final Submission)
1. Load images from `test.csv` (no labels provided)
2. Images are located in `face_spoofing_data/test_img/test_img/`
3. Generate probability predictions for each image
4. Create submission file in the same format as `sample_submission.csv`

## Usage

### Prerequisites

```bash
# Required Python packages
tensorflow>=2.0
opencv-python
numpy
pandas
matplotlib
seaborn
scikit-learn
Pillow
```

### Running the Starter Notebook

1. Open `Spoofing Detection Starter Notebook.ipynb` in Jupyter Notebook or JupyterLab
2. Ensure the dataset is properly placed in `face_spoofing_data/` directory
3. Run the cells sequentially to:
   - Load and preprocess the color and depth images
   - Build and train the face spoofing detection model
   - Evaluate the model performance on test data
   - Generate predictions on validation data
   - Create submission file in the correct format

### Key Sections in the Starter Notebook

- **Section 1**: Setup and Imports
- **Section 2**: Dataset Loading and Exploration
- **Section 3**: Data Preprocessing
- **Section 4**: Model Architecture
- **Section 5**: Train-Validation Split
- **Section 6**: Model Training
- **Section 7**: Model Evaluation
  - **Section 7.4**: Validation Set Predictions (for ranking)
- **Section 8**: Save Model and Summary

## Submission Format

Your submission CSV must have the following format:

```csv
image_id,real,fake
image_01,0.85,0.15
image_02,0.23,0.77
image_03,0.91,0.09
...
```

**Requirements:**
- `image_id`: Must match the IDs in `validation.csv` (image_01, image_02, etc.)
- `real`: Probability of being a real face (0.0 to 1.0)
- `fake`: Probability of being a fake/spoofed face (0.0 to 1.0)
- **Important**: `real + fake = 1.0` for each row
- All validation images must be included
- Sorted by `image_id` in ascending order

## Evaluation

- **Ranking**: Based on predictions on the validation set (using `reference.csv` by organizers)
- **Metric**: Likely to be accuracy or F1-score (check competition details)
- **Final Evaluation**: Based on predictions on the test set

## Key Features

- **Multi-modal Input**: Uses both color and depth images for improved detection accuracy
- **Deep Learning Approach**: Implements neural network models for automatic feature extraction
- **Comprehensive Evaluation**: Includes accuracy, confusion matrix, and classification reports
- **Starter Notebook**: Complete pipeline from data loading to submission generation
- **Submission Generation**: Automatic creation of submission file in correct format

## Applications

Face spoofing detection is critical in:

- **Mobile Device Unlocking**: Preventing unauthorized access to smartphones/tablets
- **Banking and Financial Services**: Secure authentication for transactions
- **Access Control Systems**: Building security and entry systems
- **Border Control**: Immigration and passport verification
- **Social Media Platforms**: Preventing fake account creation

## Challenges in Face Spoofing Detection

1. **Variety of Attack Types**: Different spoofing techniques require different detection strategies
2. **Environmental Factors**: Lighting conditions, camera quality, and angles affect detection
3. **Real-time Requirements**: Many applications need fast, real-time detection
4. **Adversarial Attacks**: Sophisticated attackers may try to evade detection
5. **Generalization**: Models must work across different demographics and conditions

## Tips for Success

1. **Use Both Modalities**: Leverage both color and depth information - they provide complementary information
2. **Data Augmentation**: Apply augmentation techniques to improve model generalization
3. **Model Architecture**: Experiment with different architectures (CNNs, ResNet, Vision Transformers)
4. **Ensemble Methods**: Consider combining multiple models for better performance
5. **Validation Strategy**: Use the validation set only for ranking, not for training or hyperparameter tuning
6. **Submission Format**: Double-check that your submission file matches the required format exactly

## Dataset Source

This dataset is based on face anti-spoofing datasets commonly found on **Kaggle** and research platforms. Similar datasets include:

- **CASIA Face Anti-Spoofing Database**: A widely-used research dataset with color and depth information
- **Replay-Attack Dataset**: Contains real and spoofed face videos
- **MSU Mobile Face Spoofing Database**: Includes various spoofing attack types

The dataset structure (color + depth pairs) is characteristic of datasets used for depth-based face anti-spoofing research, which leverages 3D imaging sensors (like RGB-D cameras) to capture both color and depth information simultaneously.

## Important Notes

- **Data Leakage**: DO NOT use `validation.csv` for training your model - it's only for generating predictions for ranking
- **Reference File**: `reference.csv` is for organizers only - participants should not access it
- **Storage**: Ensure you have sufficient storage space for the dataset (~several GB depending on image resolution)
- **GPU Acceleration**: Recommended for training deep learning models
- **Ignored Files**: The following files are excluded from version control:
  - `face_spoofing_data/` directory (large dataset files)
  - `presentations/` directory
  - `reference.csv` (organizers only)
  - Scripts: `create_csv_files.py`, `update_sample_submission.py`, `update_validation_files.py`

## Contact

For any inquiries, questions, or feedback about this challenge:

**Shannon Tafadzwa Sikadi**  
*Zindi Community Ambassador*

📧 shannonsikadi@gmail.com  
🔗 GitHub: https://github.com/ShannonT20

## License

Please refer to the original dataset source for licensing information. This project is for educational and research purposes.

## Acknowledgments

Thank you to all participants in the **Zindi + IndabaX Zimbabwe Hackathon: Building Africa's Next Generation of AI Innovators**! Your dedication and creativity in developing AI solutions make these events truly special. 🙌

Keep innovating and pushing boundaries! 🚀
