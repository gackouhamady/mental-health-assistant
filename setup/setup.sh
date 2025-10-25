#!/bin/bash

# USAGE EXEMPLE:
# bash setup_project.sh mental_env

ENV_NAME="${1:-mental_env}"
PY_VERSION="python3.11"

# Fonctions messages couleurs
function ok { echo -e "\033[0;32m$1\033[0m"; }
function err { echo -e "\033[0;31m$1\033[0m"; }

# 1) Vérifier Python
if ! command -v $PY_VERSION &>/dev/null; then
    err "Python non trouvé. Installer $PY_VERSION."
    exit 1
fi
ok "Python trouvé: $PY_VERSION"

# 2) Créer l'environnement virtuel
if [ ! -d "$ENV_NAME" ]; then
    $PY_VERSION -m venv "$ENV_NAME"
    if [ $? -ne 0 ]; then err "Echec de création de l'environnement $ENV_NAME"; exit 1; fi
    ok "Environnement virtuel créé: $ENV_NAME"
else
    ok "Environnement déjà présent: $ENV_NAME (utilisé tel quel)"
fi

# 3) Chemin du Python venv
ENV_PY="$ENV_NAME/bin/python"
if [ ! -x "$ENV_PY" ]; then
    err "Le python du venv introuvable: $ENV_PY"
    exit 1
fi

# 4) Installation des dépendances de base pour Jupyter
$ENV_PY -m pip install --upgrade pip ipykernel jupyterlab

# 5) Installer toutes les dépendances du projet (dans le dossier avec requirements.txt)
if [ -f "requirements.txt" ]; then
    $ENV_PY -m pip install -r requirements.txt
else
    err "requirements.txt non trouvé: depéndances non installées"
fi

# 6) Ajout du kernel pour ce venv à Jupyter
KERNEL_NAME="${ENV_NAME}"
DISPLAY_NAME="Python ($ENV_NAME)"
$ENV_PY -m ipykernel install --user --name "$KERNEL_NAME" --display-name "$DISPLAY_NAME"

if [ $? -ne 0 ]; then
    err "Erreur lors de la création du kernel Jupyter"
    exit 1
fi
ok "✅ Jupyter kernel installé: $DISPLAY_NAME (nom interne: $KERNEL_NAME)"

echo -e "\nPour démarrer Jupyter Lab :"
echo "source $ENV_NAME/bin/activate && jupyter lab"
echo "Et sélectionne '$DISPLAY_NAME' dans l'interface Jupyter pour ce venv spécialement configuré."
