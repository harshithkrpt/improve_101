import logging

# logging.basicConfig(level=logging.DEBUG)
# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning")
# logging.error("This is an error")
# logging.critical("This is critical")


# by default only will print from warning , error, critical
# to pring info or debug we have to set explicitly
# logging.basicConfig(level=logging.DEBUG)
# logging.debug("Now this will print")

logging.basicConfig(
    filename="files/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("App started")
logging.warning("Low disk space")
logging.error("An unexpected error occurred")

