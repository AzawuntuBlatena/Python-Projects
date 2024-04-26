import qrcode

def qrcode_generator(text):
  qr = qrcode.QRCode(
    version =1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size =4,
    border = 10,
  )

  qr.add_data(text)
  qr.make(fit=True)
  img = qr.make_image(fill_color='black', back_color='white')
  img.save('andomqr.png')
qrcode_generator('www.youtube.com')