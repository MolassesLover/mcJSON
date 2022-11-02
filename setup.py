from setuptools import setup, find_packages

with open("README.md", encoding="UTF-8") as readme:
    long_desc = readme.read()

setup(
    name="mcJSON",
    description="A JSON file generated for Minecraft",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    version="0.0.1",
    url="https://github.com/MolassesLover/mcJSON",
    author="Maeve Garside",
    author_email="60114762+MolassesLover@users.noreply.github.com",
    license="Apache v2.0 or MIT",
    keywords="minecraft json",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["colorama"],
    python_requires=">=3.0",
)
