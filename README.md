# Form Correctness Detection

This project uses **MediaPipe Pose** to detect human body keypoints from a short exercise video and checks whether the movement is performed correctly based on simple rules.

---

## How It Works
1. Upload a 3–5 second exercise video (bicep curl recommended).
2. The notebook extracts pose keypoints for each frame.
3. It calculates the elbow angle.
4. Based on the angle, the system shows feedback like:
   - Good Rep
   - Too Low
   - Too Extended
5. It creates an output video with this feedback written on each frame.

---

## Files in This Repository
- **Form_correctness_detection.ipynb** – Google Colab notebook with the full code.
- **output_video.mp4** – The processed video with feedback.
- **sample_video.mp4** – Input video.
- **Report.pdf** – Description of rules, logic, and challenges.
- **README.md** – Project instructions.

---

## How to Run in Google Colab
1. Open **Form_correctness_detection.ipynb** in Google Colab.
2. Run the first cell to install required libraries.
3. Run the next cells in order (top to bottom).
4. When asked, upload your sample video.
5. After processing, download the output_video.mp4..

---

## Requirements
- Python (handled by Colab)
- MediaPipe
- OpenCV
- NumPy

(All dependencies are installed automatically in the notebook.)

---

## Exercise Video Requirements
- 3–5 seconds long  
- Only 1 person  
- Exercise: Bicep curl or any arm movement  
- Good lighting  
- Camera stable  


## Author
Submitted by **D Sanjay kumar** for Smartan.AI Internship.
