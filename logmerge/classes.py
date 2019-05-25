import re

class TdarLogProcessor(object):

    __eventPattern = re.compile(r'^(DEBUG|INFO|WARN|ERROR|FATAL)')
    
    def __init__(self, fileh):
        self.fileh = fileh

    def events(self):
        """
        Return a generator that streams log "events". An event is a complete log message, which
        may contain zero or more newlines.  In other words, the boundaries of an event are not
        defined by newlines.S
        """
        buf = ""
        for line in self.fileh.lines():
            buf += line
            yield line
            
    