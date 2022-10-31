import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="heatmap",
    version="0.0.1",
    author="Michael C",
    author_email="midwestmichael636@gmail.com",
    description="Data Visualizations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MC-intel/Data-Visualization.git",
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License'
    ],
    packages=['heatmap'],
    python_requires=">=3.6",
    keywords='heatmap'
)
