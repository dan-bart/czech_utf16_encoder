from setuptools import setup,find_packages


setup(
    name='Czech UTF-16 Hex Encoder',
    version = '1.0',
    author_email = "dan.bartusek@seznam.cz",
    packages=['czech_utf16_encoder'],
    package_dir={'czech_utf16_encoder': 'czech_utf16_encoder'},
    include_package_data=True
)