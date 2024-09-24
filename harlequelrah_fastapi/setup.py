from setuptools import setup, find_packages

setup(
    name="harlequelrah_fastapi",
    version="0.1",
    packages=find_packages(),
    description="Package personnalisé pour faciliter  le développement avec python avec fastapi",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Harlequelrah",
    author_email="maximeatsoudegbovi@example.com",
    url="https://github.com/Harlequelrah/My_Python_Library",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
        "fastapi[standard]>=0.112.0",
    ],
)
