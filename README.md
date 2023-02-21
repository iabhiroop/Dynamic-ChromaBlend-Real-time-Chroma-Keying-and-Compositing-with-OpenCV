# Chroma-keying-live-video-OpenCV

Chroma keying on live video capture using OpenCV's Color Detection and Segmentation methods. Chroma key compositing, or chroma keying, is a visual-effects and post-production technique for compositing (layering) two images or video streams together based on colour hues (chroma range). 

This repository allows you to replace parts of the live video with a previously taken image when a certain range of pixel values are detected. Also known as "green screen" technology, chroma keying allows users to replace the background of a video with a different image or video, making it possible to create visually stunning content that looks like it was filmed on location.

### Requirements
  - Python 3.x   

### Libraries:
  - opencv2
  - numpy
  
### Features
  - Use a coloured material to block parts of the video with the another one.
  - Can hide or reveal objects by using the material of specified colour range.
  - Applicable to specified pixel values and can be adjusted.

### Installation
Install the Chroma keying repository by following the instructions in the repository.

Install the required Python libraries using the following command:
```pip install opencv numpy```

### Usage
Clone the repository to your local machine:  
```git clone https://github.com/iabhiroop/chroma-keying-live-video-OpenCV.git```

Navigate to the project directory:  
```cd chroma-keying-live-video-OpenCV```
    
Run the main script:  
```python opencv_chroma_keying.py```
    


### Contributing
Contributions are welcome! If you would like to contribute to this repository, please create a fork and submit a pull request with your changes.
