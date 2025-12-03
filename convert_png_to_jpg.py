#!/usr/bin/env python3
"""
Simple PNG to JPG converter.

Usage:
    python convert_images.py images/
    python convert_images.py images/ --output jpg_images/
"""

import argparse
from pathlib import Path
from PIL import Image


def convert_png_to_jpg(input_dir, output_dir=None):
    """Convert all PNG files in a directory to JPG."""
    input_path = Path(input_dir)
    output_path = Path(output_dir) if output_dir else input_path
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Find all PNG files
    png_files = sorted(input_path.glob("*.png"))
    
    if not png_files:
        print(f"No PNG files found in {input_path}")
        return
    
    print(f"Converting {len(png_files)} files...")
    
    # Convert each file
    for png_file in png_files:
        img = Image.open(png_file).convert('RGB')
        
        # Extract number from filename like "image_001.png" -> "001.jpg"
        stem = png_file.stem  # e.g., "image_001"
        if "image_" in stem:
            number = stem.split("image_")[-1]  # Get "001"
            jpg_filename = f"{number}.jpg"
        else:
            jpg_filename = f"{stem}.jpg"
        
        jpg_path = output_path / jpg_filename
        img.save(jpg_path, 'JPEG', quality=95)
        print(f"  ✓ {png_file.name} -> {jpg_filename}")
    
    print(f"\nDone! Saved to: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PNG to JPG")
    parser.add_argument('input', help='Input directory with PNG files')
    parser.add_argument('-o', '--output', help='Output directory (default: same as input)')
    
    args = parser.parse_args()
    convert_png_to_jpg(args.input, args.output)