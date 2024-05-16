python -m venv regular_env
source regular_env/bin/activate  # On Windows use `regular_env\Scripts\activate`
pip install pandas
python -c "import numpy; print('Regular Install:', numpy.__version__); print('Test Array:', numpy.array([1, 2, 3]))"
deactivate
rm -rf regular_env

python -m venv cutoff_env
source cutoff_env/bin/activate  # On Windows use `cutoff_env\Scripts\activate`
pip install --index-url http://localhost:5000/2020-12-31 pandas
python -c "import numpy; print('Cutoff 2020 Install:', numpy.__version__); print('Test Array:', numpy.array([1, 2, 3]))"
deactivate
rm -rf cutoff_env

# python -m venv default_proxy_env
# source default_proxy_env/bin/activate  # On Windows use `default_proxy_env\Scripts\activate`
# pip install --index-url http://localhost:5000 numpy
# python -c "import numpy; print('Default Proxy Install:', numpy.__version__); print('Test Array:', numpy.array([1, 2, 3]))"
# deactivate
# rm -rf default_proxy_env
