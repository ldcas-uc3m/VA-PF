from torchvision import transforms
from PIL import Image

def data_augmentation_pipeline(img: Image) -> Image:
    trans = transforms.ColorJitter(
        brightness=0.28,
        contrast=0.3,
        saturation=0.3,
        hue=0.06
    )

    return trans(img)



if __name__ == "__main__":
    # grab image and apply pipeline, save it to report img folder
    img = Image.open("myVOC4/test/images/2010_000284.jpg")
    img.save("../report/img/sample_og.jpg")

    for i in range(1, 6):
        data_augmentation_pipeline(img).save(f"../report/img/sample_v{i}.jpg")