from PIL import Image 

def resize(img,w,h):
    image =  Image.open(img).resize((w,h))
    image.show()

if __name__ == '__main__':
    img = input("enter the image name with extension  : ")
    w = int(input("Enter the width : "))
    h = int(input("Enter the height : " )) 
    resize(img,w,h)

    
