from torchvision import transforms
from PIL import Image

def data_augmentation_pipeline(img: Image):
    trans = transforms.ColorJitter(
        brightness=0.28,
        contrast=0.3,
        saturation=0.3,
        hue=0.06  
    )

    return trans(img)