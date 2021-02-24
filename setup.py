import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jhevrin2-dostuff",
    version="0.0.1",
    author="Jeff Hevrin",
    author_email="jhevrin2@gmail.com",
    description="Test Pip Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jhevrin2/test-package",
    project_urls={
        "Bug Tracker": "https://github.com/jhevrin2/test-package/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
