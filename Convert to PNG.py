#sadev Hiruditha 

import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image

def convert_images_to_png(input_folder):
    # Create a 'converted_to_png' folder inside the input folder
    output_folder = os.path.join(input_folder, "converted_to_png")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Get all files in the input folder
    files = os.listdir(input_folder)
    
    # Count of successfully converted images
    converted_count = 0
    
    # List of image extensions to check (case insensitive)
    image_extensions = ['.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp']
    
    for filename in files:
        input_path = os.path.join(input_folder, filename)
        
        # Skip if it's a directory or already a PNG file
        if os.path.isdir(input_path) or filename.lower().endswith('.png'):
            continue
        
        # Check if file is likely an image based on extension
        is_image = any(filename.lower().endswith(ext) for ext in image_extensions)
        
        if is_image:
            try:
                # Try to open the file as an image
                img = Image.open(input_path)
                
                # Create output filename (same name but with .png extension)
                output_filename = os.path.splitext(filename)[0] + ".png"
                output_path = os.path.join(output_folder, output_filename)
                
                # Save as PNG without changing quality or size
                img.save(output_path, "PNG")
                converted_count += 1
                print(f"Converted: {filename} -> {output_filename}")
                
            except Exception as e:
                print(f"Failed to convert {filename}: {str(e)}")
    
    print(f"\nConversion complete! {converted_count} images have been converted to PNG.")
    print(f"PNG files saved to: {output_folder}")
    return output_folder

def main():
    # Create a simple tkinter window for folder selection
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    print("Please select a folder containing images to convert...")
    input_folder = filedialog.askdirectory(title="Select Folder with Images")
    
    if input_folder:
        output_folder = convert_images_to_png(input_folder)
        print(f"All PNG images have been saved to {output_folder}")
    else:
        print("No folder selected. Exiting.")

if __name__ == "__main__":
    main()