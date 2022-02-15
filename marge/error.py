"""Exceptions and error handling.
"""
import signal


def install_signal_handler():
    """Turn SIGTERM into an exception, so it gets logged."""
    signal.signal(signal.SIGTERM, handle)


def handle(sig, _):
    raise SignalError(sig)


class SignalError(Exception):
    """Raised on an signal."""
    def __init__(self, sig):
        Exception.__init__(self)
        self.signal = sig
