from workers.simulate_vending_machine import VendingMachineSimulator
import configparser
import logging
import sys

def main():
    logger = logging.getLogger('simple_vending_machine')
    formatter = logging.Formatter('[%(levelname)s] %(message)s')
    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(formatter)
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    config = configparser.RawConfigParser()
    config.read('config.cfg')
    vendingMachine = VendingMachineSimulator(config, logger)
    vendingMachine.simulate_auto()

if __name__ == '__main__':
    main()