from setuptools import setup, find_packages

setup(
    name="polymancy",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["numpy", "scipy", "scikit-learn", "pandas"],
    author="Zeyu Yao",
    author_email="zeyu.yao@stonybrook.edu",
    description="Polystyrene Film Thickness and Molecular Weight Predictor for the Garcia Research Program 2024",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cytronicoder/polymancy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
