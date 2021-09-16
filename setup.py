import setuptools
with open("lol", "r") as lo:
    long_description = lo.read()

setuptools.setup(
     name='fbkdc',  
     version='0.0.1',
     author="phillychi3",
     author_email="phillychi3@gmail.com",
     description="discord bot core(python)",
     long_description=long_description,
     url="https://github.com/phillychi3/FBKdc_core",
     py_modules=["discord","discord_bot","bot","discordBOT"],
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: Apache Software License",
         "Operating System :: OS Independent",
     ]
    
 )