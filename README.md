# 🪄 Magic Background Remover

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![PySide6](https://img.shields.io/badge/PySide6-6.5%2B-purple)
![Rembg](https://img.shields.io/badge/Rembg-AI%20Powered-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

An elegant, powerful GUI application to automatically remove backgrounds from images using AI. Transform your photos with just a few clicks!

## ✨ Features

### 🪄 Intelligent Background Removal
- **Advanced AI technology**: Uses U²-Net model for precise detection
- **Detail preservation**: Sharp edges and preserved textures
- **Fast processing**: Generates in seconds
- **High quality**: Resolution maintained, no destructive compression

### 🖼️ Multi-format Support
- **Input formats**: PNG, JPG, JPEG, BMP, TIFF
- **Output format**: PNG with transparency
- **Native resolution**: Original dimensions preserved
- **Colors preserved**: No color alteration

### 🎨 Modern Interface
- **Elegant design**: Dark/light theme options
- **Side-by-side comparison**: Before/After in real-time
- **Visual feedback**: Progress bar and status messages
- **Intuitive UI**: Clear buttons, logical layout

## 🚀 Quick Installation

```bash
# Clone repository
git clone https://github.com/username/magic-background-remover.git
cd magic-background-remover

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate
# Activate (Linux/Mac)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Requirements
```txt
PySide6>=6.5.0
rembg>=2.0.50
pillow>=10.0.0
opencv-python>=4.8.0
numpy>=1.24.0
```

## 🎮 Basic Usage

### 1. **Launch Application**
```bash
python background_remover.py
```

### 2. **Upload an Image**
1. Click **"📷 Upload Image"**
2. Select image from your computer
3. Original image displays on left

### 3. **Remove Background**
1. Click **"✨ Remove Background"**
2. Watch progress bar
3. Processed image appears on right

### 4. **Save Result**
1. Click **"💾 Save Result"**
2. Choose location and filename
3. Image saves as PNG with transparency

## 📦 AI Model Download
On first launch, app automatically downloads the U²-Net model:
- **Size**: ~176MB
- **Type**: Optimized ONNX model
- **Storage**: `~/.u2net/u2net.onnx`
- **One-time**: Initial download only

**Note**: Download may take 1-2 minutes depending on connection.

## 📊 Performance

| Image Type | Processing Time | Memory Usage |
|------------|-----------------|--------------|
| Portrait (1MB) | 2-3 seconds | ~500MB |
| Landscape (3MB) | 4-5 seconds | ~800MB |
| HD (5MB+) | 8-10 seconds | 1-2GB |

**Recommendations**:
- Images < 10MP for optimal processing
- Uniform lighting for best results
- High contrast between subject and background

## 🔧 Troubleshooting

### Common Issues:
- **"No module named 'rembg'"**: Run `pip install rembg pillow`
- **Model not downloading**: Check internet connection
- **Insufficient memory**: Reduce image size
- **Interface frozen**: Wait for processing to complete
- **Poor quality**: Use images with good contrast

## 📁 Project Structure
```
magic-background-remover/
├── background_remover.py  # Main application
├── requirements.txt       # Dependencies
└── README.md             # Documentation
```

## 📄 License
MIT License - see [LICENSE](LICENSE) for details.

## 👤 Author
**omar badrani**  
- GitHub: https://github.com/omarbadrani  
- Email: omarbadrani770@gmail.com

---

⭐ **If you like this project, please star the repository!** ⭐

---

**Version**: 1.0.0  
**Python**: 3.8+  
**OS**: Windows, macOS, Linux

*Magic Background Remover - Bring your images to life with one-click background removal!* 🪄✨
