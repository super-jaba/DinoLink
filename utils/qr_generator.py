import os
import qrcode


def generate_qr_of(data: str, save_as: str):
    try:
        img = qrcode.make(data)

        # TODO: Add watermark to the image

        filename = f'./client_images/{save_as}.png'
        img.save(filename)
    except Exception as e:
        print(f'Failed to delete file {save_as}: {e}')


def delete_client_image(filename: str):
    try:
        os.remove(f'./client_images/{filename}.png')
    except Exception as e:
        print(f'Failed to delete file {filename}: {e}')
