from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    page_description = f.read()

with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="nome_do_pacote",
    version="0.0.1",
    author="meu_nome",
    author_email="meu_email",
    description="Minha descrição curta",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="link_do_meu_repositório_no_github",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
)
