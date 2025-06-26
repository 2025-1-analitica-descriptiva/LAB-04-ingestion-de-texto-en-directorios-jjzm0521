# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    import zipfile
    import os
    import pandas as pd

    zip_file_path = "files/input.zip"
    extracted_dir = "files"
    output_dir = "files/output"

    # 1. Descomprimir el archivo zip
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extracted_dir)

    # Asegurarse de que el directorio de salida exista
    os.makedirs(output_dir, exist_ok=True)

    def process_directory(dataset_type):
        """
        Procesa los archivos de texto en un directorio dado y retorna un DataFrame.
        """
        data = []
        # Define los posibles sentimientos/directorios
        sentiments = ['negative', 'positive', 'neutral']

        for sentiment in sentiments:
            sentiment_path = os.path.join(extracted_dir, 'input', dataset_type, sentiment)
            if os.path.exists(sentiment_path):
                # Recorre todos los archivos .txt en el directorio de sentimiento
                for filename in os.listdir(sentiment_path):
                    if filename.endswith(".txt"):
                        file_path = os.path.join(sentiment_path, filename)
                        try:
                            with open(file_path, 'r', encoding='utf-8') as f:
                                phrase = f.read().strip()  # Lee la frase y elimina espacios en blanco
                            data.append({'phrase': phrase, 'target': sentiment})
                        except Exception as e:
                            print(f"Error reading file {file_path}: {e}")
                            continue
        return pd.DataFrame(data)

    # 2. Procesar el directorio 'train'
    train_df = process_directory('train')
    train_output_path = os.path.join(output_dir, "train_dataset.csv")
    train_df.to_csv(train_output_path, index=False)

    # 3. Procesar el directorio 'test'
    test_df = process_directory('test')
    test_output_path = os.path.join(output_dir, "test_dataset.csv")
    test_df.to_csv(test_output_path, index=False)

    # Debug: Verificar que los DataFrames no estén vacíos
    print(f"Train dataset shape: {train_df.shape}")
    print(f"Test dataset shape: {test_df.shape}")
    
