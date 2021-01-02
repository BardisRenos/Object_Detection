# Object_Detection

In this repo will demostrates the ability a machine to detect different objects and in different position. This repo will shows the steps that need to follow in order to achieve that. 


## Reading the image and showing  

As the first step. Read the image using the opencv module.

```python
  def read_image(path):
      return cv2.imread(path)
```

Showing the image that I will use 

```python
  def show_image_with_opencv(image):
      cv2.imshow("Given Image", image)
      cv2.waitKey(0)
      cv2.destroyAllWindows()

```

## Showing the stages of the images



## Creating new borders  
