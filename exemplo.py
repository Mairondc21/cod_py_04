from loguru import logger

logger.add("meu_log.log", level="CRITICAL")

def soma(x,y):
    try:
        soma = x+y
        logger.info(f"voce digitou valores corretos, parabens {soma}")
        return soma
    except:
        logger.critical("valores errados")


soma(2,5)
soma("dd",5.5)