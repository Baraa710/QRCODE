import qrcode
from PIL import Image


def make_qr_code(data_to_encode, logo_file_name = None, color = 'black'):
    """takes in the link for the qr code, and optional logo file name and color
    saves a png of the new qr code named qr_code.png"""
    qr_code = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    qr_code.add_data(data_to_encode)
    qr_code.make()

    # qr code image
    qr_code_image = qr_code.make_image(fill_color=(color)).convert('RGB')

    # logo image 
    if logo_file_name:
        logo = Image.open(logo_file_name)
        logo_width, logo_height = logo.size 
        img_width, img_height = qr_code_image.size
        scale_factor = min(img_width // 3, img_height // 3, logo_width, logo_height)
        logo.thumbnail((scale_factor, scale_factor))
        # populate the position of the logo to center of QR code
        logo_x_position = (qr_code_image.size[0] - logo.size[0]) // 2
        logo_y_position = (qr_code_image.size[1] - logo.size[1]) // 2
        logo_position = (logo_x_position, logo_y_position)

        # insert logo image into qr code image
        qr_code_image.paste(logo, logo_position)

    # save QR code image
    qr_code_image.save('qr_code.png')

def main():
    github_icon = './baraa_github_logo.png'
    link = "https://github.com/Baraa710"
    make_qr_code(data_to_encode=link, logo_file_name=github_icon, color=(153,116,225))
    print('QR code with logo successful generated as qr_code.png')

if __name__ == "__main__":
    main()