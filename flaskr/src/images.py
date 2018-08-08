IMAGES = {
    "croissant": {
        "name": "croissant",
        "image_url": "https://i0.wp.com/basicndelicious.com/wp-content/uploads/2014/03/dulce-de-leche-croissants.jpg"
    },
    "tartine": {
        "name": "tartine",
        "image_url": "https://assets.epicurious.com/photos/54af3160c4a891cc44ccaa66/master/pass/51180220_hummus-curried-cauliflower-tartine_1x1.jpg"
    }
}


def get_all():
    """
    This function responds to a request for /api/images
    with the complete lists of images

    :return:        sorted list of images
    """
    # Create the list of people from our data
    return [IMAGES[key] for key in sorted(IMAGES.keys())]


def get_one(image_name):
    """

    :param image_name:
    :return:
    """
    if image_name in IMAGES:
        return IMAGES.get(image_name)
    else:
        return None


def create(image_name, image_url):
    """

    :param image_name:
    :param image_url:
    :return:
    """
    if image_name not in IMAGES and image_name is not None:
        IMAGES[image_name] = {"name": image_name,
                              "image_url": image_url}
        return "Successful"
    else:
        return None


def update(image_name, up_image_name, image_url):
    if image_name not in IMAGES:
        return None
    else:
        IMAGES[image_name] = {"name": up_image_name,
                              "image_url": image_url}
        return "Successful"


def delete(image_name):
    if image_name not in IMAGES:
        return None
    else:
        del IMAGES[image_name]
        return "deleted"

