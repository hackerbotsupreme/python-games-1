# steps 
# install  the libraries needed 
# create a function that collects text and convert it to QR code
# save the QR code as an image 
# run the functon 


# to download packages for windows we will  write  pip 
# we will write-- pip install qrcode  Image --- installing two packages simultaneously 
# in my case look  it is saying ----
#   WARNING: The script sqlformat.exe is installed in 'C:\Users\rekha\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts' which is not on PATH.
#  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
#  WARNING: The script qr.exe is installed in 'C:\Users\rekha\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts' which is not on PATH.
#  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
#  WARNING: The script django-admin.exe is installed in 'C:\Users\rekha\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts' which is not on PATH.
#  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
#  DEPRECATION: Image is being installed using the legacy 'setup.py install' method, because it does not have a 'pyproject.toml' and the 'wheel' package is not installed. pip 23.1 will enforce this behaviour change. A possible replacement is to enable the '--use-pep517' option. Discussion can be found at https://github.com/pypa/pip/issues/8559


import qrcode 
def generate_qrcode(text):
    
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(text)
    qr.make(fit=True)
    img=qr.make_image(fill_colour='black',back_colour='white ')
    img.save=('qrimage1.png')

url=input('enter your url:')
generate_qrcode(url)

# i need to find out where the 'qrimage.png' this file is saving itself  . 


#www.google.com