import logging

from logging import StreamHandler
from logging import Formatter

LOG_FORMAT = "%(asctime)s [%(levelname)s]: %(message)s in %(pathname)s:%(lineno)d"

DEFAULT_HANDLER = StreamHandler()
DEFAULT_HANDLER.setFormatter(Formatter(LOG_FORMAT))

package_logger = logging.getLogger("focus")
package_logger.addHandler(DEFAULT_HANDLER)
package_logger.setLevel(logging.DEBUG)
