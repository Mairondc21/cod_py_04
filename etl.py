import pandas as pd
import os 
import glob
from utils_log import log_decorator

@log_decorator
def extrair_dados(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta,'*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)

    return df_total

@log_decorator
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

@log_decorator
def carregar_dados(df:pd.DataFrame, formato_saida: list) -> pd.DataFrame:
    for formato in  formato_saida:
        if formato == 'csv':
            df.to_csv("df_tratado.csv",index=False)
        if formato == 'parquet':
            df.to_parquet("df_tratado.parquet")
            
@log_decorator
def pipeline_leitura_vendas(pasta:str, formato_saida:list ):
    df_extraido = extrair_dados(pasta)
    df_novo = calcular_kpi_de_total_de_vendas(df_extraido)
    carregar_dados(df_novo,formato_saida)

if __name__ == "__main__":
    pasta = 'data'
    formato_saida = ["csv","parquet"]
    pipeline_leitura_vendas(pasta,formato_saida)