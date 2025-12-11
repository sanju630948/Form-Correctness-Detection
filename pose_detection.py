def detect_pose_and_draw(video_path, save_frames=False):
    cap = cv2.VideoCapture(video_path)
    pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)
    frames=[]
    angles=[]
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image_rgb)

        if results.pose_landmarks:
            lm = results.pose_landmarks.landmark
            left_shoulder = [lm[11].x, lm[11].y]
            left_elbow = [lm[13].x, lm[13].y]
            left_wrist = [lm[15].x, lm[15].y]
            right_shoulder = [lm[12].x, lm[12].y]
            right_elbow = [lm[14].x, lm[14].y]
            right_wrist = [lm[16].x, lm[16].y]

            left_elbow_angle = calculate_angle(left_shoulder, left_elbow, left_wrist)
            right_elbow_angle = calculate_angle(right_shoulder, right_elbow, right_wrist)
            angles.append({'left': left_elbow_angle, 'right': right_elbow_angle})

            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            cv2.putText(frame, f"L_elbow:{int(left_elbow_angle)} R_elbow:{int(right_elbow_angle)}",
                        (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
        else:
            angles.append({'left': None, 'right': None})

        frames.append(frame)

    cap.release()
    return frames, angles
