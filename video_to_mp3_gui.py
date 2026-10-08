
import os
import threading
import queue
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from moviepy import VideoFileClip


class VideoToMP3Converter:
    def __init__(self, root):
        self.root = root
        self.root.title("Video to MP3 Converter")
        self.root.geometry("560x330")
        self.root.resizable(False, False)

        self.video_path = ""
        self.messages = queue.Queue()
        self.is_converting = False

        self.build_gui()
        self.root.after(100, self.check_messages)

    def build_gui(self):
        main = ttk.Frame(self.root, padding=22)
        main.pack(fill="both", expand=True)

        ttk.Label(
            main,
            text="VIDEO TO MP3 CONVERTER",
            font=("Segoe UI", 17, "bold")
        ).pack(pady=(0, 8))

        ttk.Label(
            main,
            text="Extract audio from your video files",
            font=("Segoe UI", 10)
        ).pack(pady=(0, 18))

        self.file_label = ttk.Label(
            main,
            text="No video selected",
            wraplength=480
        )
        self.file_label.pack(pady=5)

        self.select_button = ttk.Button(
            main,
            text="Select Video",
            command=self.select_video
        )
        self.select_button.pack(pady=8)

        self.convert_button = ttk.Button(
            main,
            text="Convert to MP3",
            command=self.convert_video
        )
        self.convert_button.pack(pady=5)

        self.progress = ttk.Progressbar(
            main,
            mode="indeterminate",
            length=400
        )
        self.progress.pack(pady=12)

        self.status_label = ttk.Label(
            main,
            text="Ready",
            wraplength=480
        )
        self.status_label.pack(pady=3)

    def select_video(self):
        path = filedialog.askopenfilename(
            title="Choose a video file",
            filetypes=[
                (
                    "Video files",
                    "*.mp4 *.mkv *.avi *.mov *.webm "
                    "*.flv *.wmv *.m4v *.mpeg *.mpg"
                ),
                ("All files", "*.*")
            ]
        )

        if path:
            self.video_path = path
            self.file_label.config(
                text=f"Selected: {os.path.basename(path)}"
            )
            self.status_label.config(text="Video selected. Ready to convert.")

    def convert_video(self):
        if self.is_converting:
            return

        if not self.video_path:
            messagebox.showwarning(
                "No video selected",
                "Please select a video file first."
            )
            return

        if not os.path.isfile(self.video_path):
            messagebox.showerror(
                "File not found",
                "The selected video file no longer exists."
            )
            return

        output_path = filedialog.asksaveasfilename(
            title="Save MP3 audio",
            defaultextension=".mp3",
            initialfile=os.path.splitext(
                os.path.basename(self.video_path)
            )[0] + ".mp3",
            filetypes=[("MP3 audio", "*.mp3")]
        )

        if not output_path:
            return

        if os.path.abspath(output_path) == os.path.abspath(
            self.video_path
        ):
            messagebox.showerror(
                "Invalid output",
                "The output file cannot be the input video."
            )
            return

        self.is_converting = True
        self.select_button.config(state="disabled")
        self.convert_button.config(state="disabled")
        self.progress.start(10)
        self.status_label.config(text="Converting... Please wait.")

        thread = threading.Thread(
            target=self.worker,
            args=(self.video_path, output_path),
            daemon=True
        )
        thread.start()

    def worker(self, video_path, output_path):
        clip = None

        try:
            clip = VideoFileClip(video_path)

            if clip.audio is None:
                self.messages.put((
                    "no_audio",
                    "This video does not contain an audio track."
                ))
                return

            clip.audio.write_audiofile(
                output_path,
                fps=44100,
                codec="libmp3lame",
                logger=None
            )

            self.messages.put(("success", output_path))

        except Exception as error:
            # Avoid displaying an excessively long error message.
            self.messages.put(("error", str(error)[:1200]))

        finally:
            if clip is not None:
                try:
                    clip.close()
                except Exception:
                    pass

    def check_messages(self):
        try:
            while True:
                kind, detail = self.messages.get_nowait()

                self.progress.stop()
                self.is_converting = False
                self.select_button.config(state="normal")
                self.convert_button.config(state="normal")

                if kind == "success":
                    self.status_label.config(
                        text="Conversion completed successfully!"
                    )
                    messagebox.showinfo(
                        "Success",
                        f"MP3 saved successfully!\n\n{detail}"
                    )

                elif kind == "no_audio":
                    self.status_label.config(
                        text="No audio track found."
                    )
                    messagebox.showwarning(
                        "No Audio",
                        detail
                    )

                elif kind == "error":
                    self.status_label.config(
                        text="Conversion failed."
                    )
                    messagebox.showerror(
                        "Conversion Error",
                        "Unable to convert this video.\n\n"
                        f"Details: {detail}\n\n"
                        "Check that the file is valid, the output "
                        "folder is writable, and FFmpeg is available."
                    )

        except queue.Empty:
            pass

        self.root.after(100, self.check_messages)


if __name__ == "__main__":
    root = tk.Tk()
    app = VideoToMP3Converter(root)
    root.mainloop()
