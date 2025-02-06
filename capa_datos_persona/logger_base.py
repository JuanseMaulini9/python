import logging

log = logging

log.basicConfig(level=log.DEBUG, 
                format="%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s",
                datefmt="%I:%M:%S %p",
                handlers=[
                  log.FileHandler("capa_datos.log"),
                  log.StreamHandler()
                ]
                )



if __name__ == "__main__":
  log.debug("mensaje a nivel debug")
  log.info("mensaje a nivel de info")
  log.warning("mesanje a nivel de warning")
  log.error("mesanje a nivel de error")
  log.critical("mesanje a nivel de critical")