# ImageDrawer - Interactive Drawing on Images with OpenCV

This Python script allows you to **interactively draw shapes (rectangle, line, circle) on images** using OpenCV.  
You can also view, reset, and save your edited image through a simple text menu.

## Features

- **Draw Rectangle:** Click and drag to draw a rectangle on the image.
- **Draw Line:** Click two points to draw a line.
- **Draw Circle:** Click for the center, drag to set the radius.
- **Show Image:** Display the current image in a window.
- **Save Image:** Save your edited image to a file.
- **Reset Image:** Restore the image to its original state.
- **Menu System:** Easy-to-use console menu for all actions.

## How to Use

1. **Install dependencies:**  
   Make sure you have [OpenCV](https://pypi.org/project/opencv-python/) and [NumPy](https://pypi.org/project/numpy/) installed:
   ```
   pip install opencv-python numpy
   ```

2. **Run the script:**
   ```
   python draw.py
   ```

3. **Follow the prompts:**
   - Enter the path to your image file.
   - Use the menu to select drawing or image actions.

## Menu Options

1. **Draw Rectangle:**  
   Click and drag on the image window. Press `Enter` to confirm, `ESC` to cancel.

2. **Draw Line:**  
   Click two points on the image. Press `Enter` to confirm, `ESC` to cancel.

3. **Draw Circle:**  
   Click for the center, drag to set the radius. Press `Enter` to confirm, `ESC` to cancel.

4. **Show Image:**  
   Opens the current image in a window.

5. **Save Image:**  
   Enter a filename to save your edited image.

6. **Reset Image:**  
   Restores the image to its original state.

7. **Exit:**  
   Closes the program.

## Code Structure

- **ImageDrawer class:**  
  Handles image loading, drawing, showing, saving, and menu logic.
- **Mouse callbacks:**  
  Used for interactive drawing with OpenCV windows.
- **Main block:**  
  Prompts for image path and starts the menu loop.

## Example

```bash
$ python draw.py
Enter the image path: myphoto.jpg

--- Drawing Menu ---
1. Draw Rectangle
2. Draw Line
3. Draw Circle
4. Show Image
5. Save Image
6. Reset Image
7. Exit
Select an option (1-7):
```

---

**Enjoy editing your images
