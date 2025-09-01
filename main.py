from PIL import Image, ImageDraw, ImageFont
import cv2
import os

print("Press ENTER to start")
input()

clicked_position = None  

def show_coordinates(event, x, y, flags, param):
    global clicked_position
    if event == cv2.EVENT_RBUTTONDOWN:  # Right click
        clicked_position = (x, y)
        print(f"Right Click at: {clicked_position}")
        cv2.destroyAllWindows()
# Open image with OpenCV
img = cv2.imread("certificate.png")
cv2.imshow("Certificate", img)
cv2.setMouseCallback("Certificate", show_coordinates)

cv2.waitKey(0)
cv2.destroyAllWindows()


# Make sure user clicked somewhere
if clicked_position is None:
    print("No coordinates selected! Run again and right click.")
else:
    input("Press ENTER to generate certificates...")


    # Load names from names.txt
    with open("name.txt", "r") as f:
       name_list = [line.strip() for line in f if line.strip()]

    # Ensure output folder exists
    os.makedirs("output", exist_ok=True)

  
  
    
    
    

    for name in name_list:
        img = Image.open("certificate.png")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 40) 
        draw.text(clicked_position, name, font=font, fill='black')
        img.save(os.path.join("output", f"{name}.png"))
    
        print(f"Saved certificate for {name}")
