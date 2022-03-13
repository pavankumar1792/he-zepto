from enum import Enum


class BookingStatus(Enum):
    """
    Enum for booking status.
    """
    CONFIRMED = 1
    CANCELLED = 2
    FAILED = 3
    PENDING = 4
    REFUNDED = 5
    

    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)

    @staticmethod
    def from_str(label):
        if label in [1, 'CONFIRMED']:
            return BookingStatus.CONFIRMED
        elif label in [2, 'CANCELLED']:
            return BookingStatus.CANCELLED
        elif label in [3, 'FAILED']:
            return BookingStatus.FAILED
        elif label in [4, 'PENDING']:
            return BookingStatus.PENDING
        elif label in [5, 'REFUNDED']:
            return BookingStatus.REFUNDED
        else:
            raise ValueError('Invalid booking status label: {}'.format(label))