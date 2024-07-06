FROM python:3.12

WORKDIR /app

COPY requirements_server.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY config.txt config.txt

COPY saved_models/ /tmp/saved_models/

# Récupère le modèle configuré dans config.txt
RUN export REF_MODELE=$(grep "^REF_MODELE=" config.txt | cut -d'=' -f2) && \
    echo "REF_MODELE=$REF_MODELE" && \
    cp /tmp/saved_models/$REF_MODELE.keras model.keras

# Copie du fichier de configuration .yaml spécifié dans config.txt
RUN export REF_MODELE=$(grep "^REF_MODELE=" config.txt | cut -d'=' -f2) && \
    cp /tmp/saved_models/$REF_MODELE.yaml model.yaml && \
    rm -rf /tmp/saved_models


COPY app_server.py app.py
COPY config config

EXPOSE 5000

CMD ["python", "app.py"]