# FreeCodeCamp - How to Create a Horoscope API with Beautiful Soup and Flask

## Set up

### First, create and activate your virtual environment.
```bash
# Linux
python -m venv venv
source venv/bin/active
echo "-Environment created and activated"
```

### Second, install requirements.
```bash
# Linux
pip install --quiet -r requirements.txt
echo "-Requirements intalled" 
```

### Create .env file. Insert a value for SECRET_KEY
```bash
cat << 'EOF' > .env
APP_SETTINGS=config.DevelopmentConfig
SECRET_KEY=your_secret_key_here
EOF
```


### Run API
```bash
python main.py
```