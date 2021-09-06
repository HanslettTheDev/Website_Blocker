import logging
import webview

from contextlib import redirect_stdout
from io import StringIO
from server import server

logger = logging.getLogger(__name__)
print(logger)

if __name__ == '__main__':
    stream = StringIO()
    with redirect_stdout(stream):
        window = webview.create_window('Web Blocker', server)
        webview.start(debug=True)