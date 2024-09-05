from etl import pipeline_leitura_vendas

pasta = 'data'
formato_saida = ["csv","parquet"]
pipeline_leitura_vendas(pasta,formato_saida)