import cv2
import os
import argparse


def video_to_frames(video_path, output_dir, prefix="frame", step=1):
    """
    Extract every `step`-th frame from a video and save them as images.
    """
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Cannot open video: {video_path}")

    frame_idx = 0
    saved_idx = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Save only every `step`-th frame
        if frame_idx % step == 0:
            filename = f"{prefix}_{saved_idx:06d}.png"
            cv2.imwrite(os.path.join(output_dir, filename), frame)
            saved_idx += 1

        frame_idx += 1

    cap.release()
    print(f"Saved {saved_idx} frames to {output_dir}")


def main():
    parser = argparse.ArgumentParser(description="Convert video into frames.")
    parser.add_argument("--video", type=str, required=True, help="Path to input video file.")
    parser.add_argument("--out", type=str, required=True, help="Directory where frames will be saved.")
    parser.add_argument("--prefix", type=str, default="frame", help="Prefix for frame filenames.")
    parser.add_argument("--step", type=int, default=1, help="Save every N-th frame (default 1).")

    args = parser.parse_args()
    video_to_frames(args.video, args.out, args.prefix, args.step)


if __name__ == "__main__":
    main()
