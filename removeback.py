import sys
import io
from PIL import Image
from rembg import remove
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel,
                               QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog,
                               QMessageBox, QProgressBar, QFrame, QSizePolicy)
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QPixmap, QImage


class WorkerThread(QThread):
    finished = Signal(object)
    error = Signal(str)

    def __init__(self, image_data):
        super().__init__()
        self.image_data = image_data

    def run(self):
        try:
            # Convertir l'image en bytes
            img_byte_arr = io.BytesIO()
            self.image_data.save(img_byte_arr, format='PNG')
            img_bytes = img_byte_arr.getvalue()

            # Supprimer l'arrière-plan
            output_bytes = remove(img_bytes)

            # Convertir en image PIL
            output_image = Image.open(io.BytesIO(output_bytes))

            self.finished.emit(output_image)
        except Exception as e:
            self.error.emit(str(e))


class BackgroundRemoverApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.input_image = None
        self.output_image = None

    def initUI(self):
        self.setWindowTitle("Magic Background Remover - PySide6")
        self.setGeometry(100, 100, 1200, 800)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f8f9fa;
            }
            QLabel {
                color: #343a40;
            }
            QPushButton {
                background-color: #007bff;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QPushButton:disabled {
                background-color: #6c757d;
            }
            QPushButton#saveButton {
                background-color: #28a745;
            }
            QPushButton#saveButton:hover {
                background-color: #218838;
            }
            QPushButton#processButton {
                background-color: #17a2b8;
            }
            QPushButton#processButton:hover {
                background-color: #138496;
            }
            QFrame {
                background-color: white;
                border-radius: 10px;
                border: 1px solid #dee2e6;
            }
            QProgressBar {
                border: 2px solid #dee2e6;
                border-radius: 5px;
                text-align: center;
                background-color: #e9ecef;
            }
            QProgressBar::chunk {
                background-color: #007bff;
                width: 10px;
            }
        """)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(30, 30, 30, 30)

        # Titre
        title_label = QLabel("Magic Background Remover")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("""
            QLabel {
                font-size: 28px;
                font-weight: bold;
                color: #007bff;
                padding: 15px;
            }
        """)
        main_layout.addWidget(title_label)

        # Boutons d'action
        button_layout = QHBoxLayout()

        self.upload_btn = QPushButton("📷 Upload Image")
        self.upload_btn.clicked.connect(self.upload_image)
        self.upload_btn.setCursor(Qt.PointingHandCursor)

        self.process_btn = QPushButton("✨ Remove Background")
        self.process_btn.clicked.connect(self.process_image)
        self.process_btn.setEnabled(False)
        self.process_btn.setCursor(Qt.PointingHandCursor)
        self.process_btn.setObjectName("processButton")

        self.save_btn = QPushButton("💾 Save Result")
        self.save_btn.clicked.connect(self.save_image)
        self.save_btn.setEnabled(False)
        self.save_btn.setCursor(Qt.PointingHandCursor)
        self.save_btn.setObjectName("saveButton")

        button_layout.addWidget(self.upload_btn)
        button_layout.addWidget(self.process_btn)
        button_layout.addWidget(self.save_btn)

        main_layout.addLayout(button_layout)

        # Zone d'affichage des images
        image_layout = QHBoxLayout()

        # Image d'entrée
        input_frame = QFrame()
        input_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        input_layout = QVBoxLayout(input_frame)

        input_title = QLabel("Original Image")
        input_title.setAlignment(Qt.AlignCenter)
        input_title.setStyleSheet("font-weight: bold; font-size: 16px; padding: 10px;")
        input_layout.addWidget(input_title)

        self.input_label = QLabel("No image uploaded\n\nClick 'Upload Image' to begin")
        self.input_label.setAlignment(Qt.AlignCenter)
        self.input_label.setStyleSheet("""
            QLabel {
                background-color: #e9ecef;
                border: 2px dashed #dee2e6;
                border-radius: 10px;
                padding: 30px;
                color: #6c757d;
            }
        """)
        self.input_label.setMinimumSize(400, 400)
        input_layout.addWidget(self.input_label)

        image_layout.addWidget(input_frame)

        # Image de sortie
        output_frame = QFrame()
        output_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        output_layout = QVBoxLayout(output_frame)

        output_title = QLabel("Processed Image")
        output_title.setAlignment(Qt.AlignCenter)
        output_title.setStyleSheet("font-weight: bold; font-size: 16px; padding: 10px;")
        output_layout.addWidget(output_title)

        self.output_label = QLabel("Processed image will appear here")
        self.output_label.setAlignment(Qt.AlignCenter)
        self.output_label.setStyleSheet("""
            QLabel {
                background-color: #e9ecef;
                border: 2px dashed #dee2e6;
                border-radius: 10px;
                padding: 30px;
                color: #6c757d;
            }
        """)
        self.output_label.setMinimumSize(400, 400)
        output_layout.addWidget(self.output_label)

        image_layout.addWidget(output_frame)

        main_layout.addLayout(image_layout)

        # Barre de progression
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setTextVisible(False)
        main_layout.addWidget(self.progress_bar)

        # Label de statut
        self.status_label = QLabel("Ready to remove backgrounds! 🚀")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("padding: 10px; color: #6c757d;")
        main_layout.addWidget(self.status_label)

        # Footer
        footer_label = QLabel("Powered by AI • Made with Python and PySide6")
        footer_label.setAlignment(Qt.AlignCenter)
        footer_label.setStyleSheet("padding: 10px; color: #6c757d; font-size: 12px;")
        main_layout.addWidget(footer_label)

    def upload_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "",
            "Image Files (*.png *.jpg *.jpeg *.bmp *.tiff)"
        )

        if file_path:
            try:
                self.status_label.setText("Loading image...")
                self.input_image = Image.open(file_path)

                # Afficher l'image
                pixmap = self.pil2pixmap(self.input_image)
                scaled_pixmap = pixmap.scaled(400, 400, Qt.AspectRatioMode.KeepAspectRatio,
                                              Qt.TransformationMode.SmoothTransformation)
                self.input_label.setPixmap(scaled_pixmap)

                # Activer le bouton de traitement
                self.process_btn.setEnabled(True)
                self.status_label.setText("Image loaded. Click 'Remove Background' to process. ✨")

            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load image: {str(e)}")
                self.status_label.setText("Error loading image ❌")

    def process_image(self):
        if self.input_image:
            # Désactiver les boutons pendant le traitement
            self.process_btn.setEnabled(False)
            self.save_btn.setEnabled(False)

            # Afficher la barre de progression
            self.progress_bar.setVisible(True)
            self.progress_bar.setRange(0, 0)  # Mode indéterminé

            self.status_label.setText("Processing image with AI... ⏳")

            # Créer et démarrer le thread de traitement
            self.worker = WorkerThread(self.input_image)
            self.worker.finished.connect(self.on_processing_finished)
            self.worker.error.connect(self.on_processing_error)
            self.worker.start()

    def on_processing_finished(self, output_image):
        self.output_image = output_image

        # Afficher l'image traitée
        pixmap = self.pil2pixmap(self.output_image)
        scaled_pixmap = pixmap.scaled(400, 400, Qt.AspectRatioMode.KeepAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        self.output_label.setPixmap(scaled_pixmap)

        # Cacher la barre de progression
        self.progress_bar.setVisible(False)

        # Activer le bouton de sauvegarde
        self.save_btn.setEnabled(True)
        self.process_btn.setEnabled(True)

        self.status_label.setText("Background removed successfully! ✅")

    def on_processing_error(self, error_msg):
        # Cacher la barre de progression
        self.progress_bar.setVisible(False)

        # Réactiver le bouton de traitement
        self.process_btn.setEnabled(True)

        QMessageBox.critical(self, "Error", f"Failed to remove background: {error_msg}")
        self.status_label.setText("Error processing image ❌")

    def save_image(self):
        if self.output_image:
            file_path, _ = QFileDialog.getSaveFileName(
                self, "Save Image", "",
                "PNG Files (*.png);;All Files (*)"
            )

            if file_path:
                try:
                    self.output_image.save(file_path)
                    QMessageBox.information(self, "Success", "Image saved successfully! 💾")
                    self.status_label.setText(f"Image saved to {file_path} 📁")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Failed to save image: {str(e)}")
                    self.status_label.setText("Error saving image ❌")

    def pil2pixmap(self, image):
        """Convert PIL Image to QPixmap"""
        if image.mode == "RGBA":
            r, g, b, a = image.split()
            image = Image.merge("RGB", (r, g, b))

        data = image.tobytes("raw", "RGB")
        qim = QImage(data, image.size[0], image.size[1], QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qim)
        return pixmap


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BackgroundRemoverApp()
    window.show()
    sys.exit(app.exec())