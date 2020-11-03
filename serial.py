"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=100):
        self.start = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.start+1}"

    def generate(self):
        """
        Generates new serial number by adding 1 to each new serial number
        """
        self.start += 1
        return self.start

    def reset(self):
        """
        resets serial number to 100
        """
        self.start = 100
