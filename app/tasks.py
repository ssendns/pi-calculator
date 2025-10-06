from .celery_worker import celery_app
import decimal
from decimal import Decimal, getcontext

@celery_app.task(bind=True)
def calculate_pi(self, digits: int):
    getcontext().prec = digits + 2 

    C = 426880 * Decimal(10005).sqrt()
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = L

    for i in range(1, digits):
        M = (M * (K ** 3 - 16 * K)) // (i ** 3)
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12
        progress = i / digits
        self.update_state(state="PROGRESS", meta={"progress": progress})

    pi = C / S
    return str(pi)[:digits + 2]