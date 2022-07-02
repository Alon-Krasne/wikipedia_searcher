import logging
from argparse import Namespace, ArgumentParser, RawTextHelpFormatter
import uvicorn

from wiki_searcher.utils import configure_logger


def parse_arguments() -> Namespace:
    parser = ArgumentParser(formatter_class=RawTextHelpFormatter)
    parser.add_argument("-d", "--debug", dest="debug", default=False, type=bool, help="Enable debug mode")

    return parser.parse_args()


def main():
    args = parse_arguments()
    logger = configure_logger(__package__)
    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger.debug('Debug mode enabled')

    uvicorn.run("wiki_searcher.app:app", host='0.0.0.0', port=8000, reload=True, debug=True, workers=3)


if __name__ == "__main__":
    exit(main())
