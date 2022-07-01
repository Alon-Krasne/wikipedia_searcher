import logging
from argparse import Namespace, ArgumentParser, RawTextHelpFormatter
import uvicorn

from wiki_searcher.utils import configure_logger


def parse_arguments() -> Namespace:
    parser = ArgumentParser(formatter_class=RawTextHelpFormatter)
    parser.add_argument("-p", "--port", dest="port", default=3000, type=int, help="The port to listen on")
    parser.add_argument("-d", "--debug", dest="debug", default=True, type=bool, help="Enable debug mode")

    return parser.parse_args()


def main():
    args = parse_arguments()
    logger = configure_logger('wikiSearcher')
    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger.debug('Debug mode enabled')

    logger.info('Port is %s', args.port)
    uvicorn.run("wiki_searcher.app:app", host='0.0.0.0', port=args.port, reload=True, debug=True, workers=3)


if __name__ == "__main__":
    exit(main())
