# Модифікувати задачу про подію (e = threading.Event()) таким чином,
# щоб генерація події (e.set()) відбувалась не з основного потоку,
# а з додаткового, третього потоку. Чи буде так працювати ? Документація
import logging
import threading
import time


def wait_for_event(e):
    """Wait for the event to be set before doing anything"""
    logging.debug('wait_for_event starting')
    event_is_set = e.wait()
    logging.debug('event set: %s', event_is_set)


def wait_for_event_timeout(e, t):
    """Wait t seconds and then timeout"""
    while not e.is_set():
        logging.debug('wait_for_event_timeout starting')
        event_is_set = e.wait(t)
        logging.debug('event set: %s', event_is_set)
        if event_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other work')

def for_3_thread(e, t):
    logging.debug('wait_for_event starting')
    event_is_set = e.wait(t)
    e.set()
    logging.debug('Event is set')
    logging.debug('event set: %s', event_is_set)


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

e = threading.Event()
t1 = threading.Thread(
    name='1 thread',
    target=wait_for_event,
    args=(e,),
)
t1.start()

t2 = threading.Thread(
    name='2 thread',
    target=wait_for_event_timeout,
    args=(e, 2),
)
t2.start()

t3 = threading.Thread(
    name='3 thread',
    target=for_3_thread,
    args=(e, 2),
)
t3.start()

logging.debug('Waiting before calling Event.set()')
time.sleep(0.3)
# e.set()
# logging.debug('Event is set')