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

During the image preprocessing the image passed through different stages.

```python
  def image_preprocessing(self, given_image):
      self.convert_to_gray_scale(given_image)
      self.pure_image = given_image

      _, self.image_threshold_bw = cv2.threshold(self.image_gray_scale, 190, 255, cv2.THRESH_BINARY)
      kernel = np.ones((3, 3), np.uint8)
      self.image_morph = cv2.morphologyEx(self.image_threshold_bw, cv2.MORPH_CLOSE, kernel, iterations=9)
      self.image_mask = 255 - self.image_morph
      self.background = cv2.dilate(self.image_mask, kernel, iterations=5)
      dist_transform = cv2.distanceTransform(self.image_mask, cv2.DIST_L2, 3)
      _, self.foreground = cv2.threshold(dist_transform, 0.237 * dist_transform.max(), 255, 0)
      self.the_unknown_image = self.background - self.foreground
      self.foreground = np.uint8(self.foreground)
```

## Creating new borders  

From the previous chapter the image has a small thing to care of. Some pills are touching the border and as a result the pills are not well separeted and create a solid body with pills and the background. 


```python

```
