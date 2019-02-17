from setuptools import setup, find_packages
import sys, os

version = '0.1'

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='xiaomi_mqtt',
      version=version,
      description="Xiaomi Mi Home Python MQTT brigde",
      long_description=readme(),
      classifiers=[
          "Development Status :: 4 - Beta",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3",
          "Intended Audience :: Developers",
          "Intended Audience :: System Administrators",
          "Topic :: System :: Hardware"
      ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='xiaomi udp mqtt iot mi home aqara',
      author='Yury Skaletskiy',
      author_email='yury.skaletskiy@gmail.com',
      #url='https://notes.jmsinfor.com/blog/post/admin/Xiaomi-Hub',
      url='https://github.com/yuryskaletskiy/xiaomi_mqtt_python',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          # "future"
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
