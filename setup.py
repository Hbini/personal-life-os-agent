from setuptools import setup, find_packages
setup(name='personal-life-os-agent', version='0.1.0', author='Hernane Bini', description='Personal Life OS Agent', packages=find_packages(), python_requires='>=3.9', install_requires=['openai>=1.3.0', 'langchain>=0.1.0', 'fastapi>=0.104.0', 'pytest>=7.4.0'])
