FROM python:3.12

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY config.txt config.txt

# Récupère le modèle configuré dans config.txt
RUN export REF_MODELE=$(grep "^REF_MODELE=" config.txt | cut -d'=' -f2) && \
    cp saved_modes/$REF_MODELE.keras model.keras

# Copie du fichier de configuration .yaml spécifié dans config.txt
RUN export REF_MODELE=$(grep "^REF_MODELE=" config.txt | cut -d'=' -f2) && \
    cp saved_models/$REF_MODELE.yaml model_config.yaml


COPY app_server.py app.py
COPY config config

EXPOSE 5000

CMD ["python", "app.py"]