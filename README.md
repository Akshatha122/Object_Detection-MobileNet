# Object-detection

Deployed the MobileNet-SSD v2 algorithm, trained on the COCO dataset, to detect objects in a live video feed.
The general idea of object detection using SSD-MobileNet implemented using OpenCV is to use a pre-trained deep learning model to identify objects in an image, and then draw bounding boxes around those objects to highlight their location.

SSD-MobileNet is a popular deep learning architecture for object detection that uses a combination of convolutional neural networks and single shot detection (SSD) to efficiently detect objects in real time. It is a fast and accurate model that can detect multiple objects of different sizes and shapes in an image.

## Single Shot Detector (SSD)
has two components: a backbone model and SSD head. Backbone model usually is a pretrained image classification network as a feature extractor. This is typically a network like ResNet trained on ImageNet from which the final fully connected classification layer has been removed.
