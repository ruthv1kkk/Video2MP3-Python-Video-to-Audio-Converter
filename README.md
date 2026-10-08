# 🎵 Video to MP3 Converter | Python GUI

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/GUI-Tkinter-orange" alt="Tkinter">
  <img src="https://img.shields.io/badge/Audio-MP3-red" alt="MP3">
  <img src="https://img.shields.io/badge/Status-Active-success" alt="Project Status">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="MIT License">
</p>

A simple, user-friendly **Video-to-MP3 Converter built with Python** that extracts audio from video files and saves it as an MP3 file. The application features a graphical user interface (GUI), making audio extraction easy without requiring command-line operations from the user.

## 📌 Overview

The Video-to-MP3 Converter is a desktop application designed to extract audio from video files efficiently. Users can select a video, choose the output location, and convert the video into an MP3 audio file through a straightforward graphical interface.

This project demonstrates Python GUI development, multimedia processing, file handling, exception handling, and background threading.

## ✨ Features

* 🎬 **Video Selection:** Browse and select supported video files.
* 🎵 **MP3 Extraction:** Extract audio and save it in MP3 format.
* 📁 **Custom Output Location:** Choose the destination folder and output filename.
* 🖥️ **Graphical User Interface:** Simple desktop interface built using Tkinter.
* ⚡ **Background Processing:** Perform conversion in a separate thread to keep the interface responsive.
* 📊 **Progress Indicator:** Animated progress bar while conversion is running.
* 🛡️ **Error Handling:** Handles missing files, videos without audio, and conversion errors.
* 🔊 **44.1 kHz Audio:** Exports audio at a 44,100 Hz sample rate.
* 🪶 **Lightweight Application:** Uses Python libraries rather than a large GUI framework.

## 🛠️ Technologies Used

| Technology | Purpose                                              |
| ---------- | ---------------------------------------------------- |
| Python     | Core programming language                            |
| Tkinter    | Graphical user interface                             |
| MoviePy    | Video and audio processing                           |
| FFmpeg     | Multimedia encoding and decoding                     |
| Threading  | Background conversion                                |
| Queue      | Safe communication between the worker thread and GUI |

## 📂 Project Structure

```text
video-to-mp3-converter/
│
├── video_to_mp3_gui.py   # Main Python application
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
└── .gitignore            # Git ignore rules
```

## ⚙️ Installation

### 1. Install Python

Download and install Python from:

https://www.python.org/downloads/

During installation on Windows, enable **Add Python to PATH**.

### 2. Clone the repository

Replace `YOUR_USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR_USERNAME/video-to-mp3-converter.git
```

Navigate into the project directory:

```bash
cd video-to-mp3-converter
```

Alternatively, download the repository as a ZIP file and extract it.

### 3. Install dependencies

```bash
python -m pip install moviepy imageio-ffmpeg
```

Tkinter is included with most standard Windows Python installations.

### 4. Run the application

```bash
python video_to_mp3_gui.py
```

The graphical interface will open, allowing you to select a video and convert it to MP3.

## 🚀 How to Use

1. Launch the application.
2. Click **Select Video**.
3. Choose a supported video file from your computer.
4. Click **Convert to MP3**.
5. Select the output location and enter your preferred filename.
6. Wait for the conversion to complete.
7. Find the generated MP3 file at the location you selected.

## 🎞️ Supported Video Formats

The file picker includes these common formats:

* MP4
* MKV
* AVI
* MOV
* WebM
* FLV
* WMV
* M4V
* MPEG / MPG

Actual support depends on the media codecs available to MoviePy and FFmpeg.

## 🎧 Output Details

* **Output format:** MP3
* **Audio sample rate:** 44,100 Hz
* **Output filename:** Chosen by the user; defaults to the video's filename with an `.mp3` extension.
* **Output destination:** User-selected location

The final audio size and quality depend on the source audio and the encoding settings.

## 🛡️ Error Handling

The application includes handling for common problems:

* No video selected.
* Input file missing or unavailable.
* Video has no audio track.
* Invalid output path or unwritable destination.
* Unsupported or corrupted media.
* Multimedia encoding or decoding failures.

If conversion fails, check the error message, verify that the video plays correctly, and ensure the output folder is writable.

## 📦 Requirements File

Create a `requirements.txt` file with:

```text
moviepy
imageio-ffmpeg
```

Install the listed dependencies using:

```bash
python -m pip install -r requirements.txt
```

**Note:** Python's Tkinter module is normally included with Windows Python installations and does not need to be installed using pip.

## 🔮 Future Improvements

Potential features for future versions:

* 🎚️ Adjustable MP3 bitrate and audio quality.
* 📂 Batch conversion of multiple videos.
* 📈 Real conversion percentage and estimated remaining time.
* 🎨 Modern dark-mode interface.
* 🎧 Additional output formats such as WAV and M4A.
* ✂️ Audio extraction from a selected time range.
* 📦 Standalone Windows executable using PyInstaller.
* 📋 Conversion history and recent files.

## 🎯 Learning Outcomes

This project provides practical experience with:

* Python desktop application development.
* GUI design and event-driven programming.
* Video and audio processing.
* File dialogs and filesystem operations.
* Multithreading and queues.
* Exception handling and dependency management.

## 🤝 Contributing

Contributions and suggestions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Test your changes.
5. Submit a pull request.

## 📄 License

This project is intended to be released under the MIT License. Add a `LICENSE` file containing the appropriate MIT License text before publishing it under that license.

## 👨‍💻 Author

**E Ruthvik Chowdary**

Creative Developer | Python | AI/ML | Computer Vision | Interactive Web

GitHub: https://github.com/ruthv1kkk

---

⭐ If you find this project useful, consider giving the repository a star!

**Built with Python, curiosity, and a passion for creating useful tools.**
