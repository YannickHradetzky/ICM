from PIL import Image
import os

def create_gif_from_pngs(png_files, output_filename='animation.gif', duration=500):
    """
    Create an animated GIF from a list of PNG files.
    
    Parameters:
    png_files (list): List of PNG filenames
    output_filename (str): Name of the output GIF file
    duration (int): Duration for each frame in milliseconds
    
    Returns:
    bool: True if successful, False otherwise
    """
    try:
        # Validate input files
        images = []
        for png_file in png_files:
            if not os.path.exists(png_file):
                print(f"Error: File {png_file} not found")
                return False
            if not png_file.lower().endswith('.png'):
                print(f"Error: File {png_file} is not a PNG file")
                return False
        
        # Open and collect all PNG images
        for png_file in png_files:
            img = Image.open(png_file)
            images.append(img)
            
        # Save the animated GIF
        if images:
            images[0].save(
                output_filename,
                save_all=True,
                append_images=images[1:],
                duration=duration,
                loop=0
            )
            print(f"Successfully created {output_filename}")
            return True
        else:
            print("Error: No valid images found")
            return False
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False
