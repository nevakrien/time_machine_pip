# time_machine_pip
attempting to fix python depency hell by forcing pip into using only package versions from when the project was devloped

# usage

first you need to setup the proxy make a new env for this project

```bash
pip install -r requirments.txt
python proxy.py 
```
u can now use this proxy in any project like so

```bash
pip install --index-url http://localhost:5000/2020-12-31 pandas
```