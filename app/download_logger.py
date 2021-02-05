class DownloadLogger(object):
    def debug(self, msg):
        print('DEBUG: ' + msg)

    def warning(self, msg):
        print('WARNING: ' + msg)

    def error(self, msg):
        print('ERROR: ' + msg)