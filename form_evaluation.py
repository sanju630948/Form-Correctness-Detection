def evaluate_elbow(angle):
    if angle is None:
        return "No detection"
    if angle < 45:
        return "Too Low - incomplete"
    elif 45 <= angle <= 160:
        return "Good Rep"
    else:
        return "Too Extended"

def overlay_and_save(frames, angles, out_path="/content/output_video.mp4", fps=25):
    h, w = frames[0].shape[:2]
    writer = cv2.VideoWriter(out_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w,h))
    for frame, a in zip(frames, angles):
        angle = a.get('left') if (a.get('left') not in (None, 0.0)) else a.get('right')
        feedback = evaluate_elbow(angle)
        cv2.putText(frame, feedback, (10, h-30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        writer.write(frame)
    writer.release()
    print("Saved:", out_path)
    return out_path
