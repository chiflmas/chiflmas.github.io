import qrcode

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('berdinidss.es')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
type(img)  # qrcode.image.pil.PilImage
img.save("qr_web.png")