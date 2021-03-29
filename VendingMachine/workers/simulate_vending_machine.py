from project.canada_vending_machine import CanadaVendingMachine
import re
import json

class VendingMachineSimulator:
    def __init__(self, config, logger):
        self.logger = logger
        try:
            decimal_to_round=int(config['DEFAULT'].get(
                'APP_NUMBER_OF_DIGITS_TO_ROUND', 2
            ))
            initial_stock = {'CandyBar':[2.00, 12],
                             'Chips':[1.50, 8],
                             'Soda':[1.00,23]}
            self.vending_machine = CanadaVendingMachine(
                    logger=logger, 
                    initial_stock=initial_stock,
                    demonimation_round=decimal_to_round)
        except Exception as e:
            self.logger.error(f'Error = {e}')

    def simulate_auto(self):
        try:
            self.vending_machine.print_stock()
            self.vending_machine.move_stock(2, 16)
            self.vending_machine.print_stock()
            self.vending_machine.add_currency(1.0)
            self.vending_machine.buy_product(16)
            self.vending_machine.add_currency(2.0)
            self.vending_machine.buy_product(18)
            self.vending_machine.add_currency(0.25)
            self.vending_machine.buy_product(1)
            self.vending_machine.add_currency(0.50)
            self.vending_machine.add_currency(0.10)
            self.vending_machine.add_currency(0.05)
            self.vending_machine.buy_product(16)
            self.vending_machine.return_cash()

            self.vending_machine.stock_units({'Doughnuts':[1.75, 24]})
            self.vending_machine.print_stock()
            self.vending_machine.add_currency(1.0)
            self.vending_machine.add_currency(0.25)
            self.vending_machine.add_currency(0.50)
            self.vending_machine.add_currency(0.10)
            self.vending_machine.buy_product(8)
            self.vending_machine.print_stock()
            self.vending_machine.add_currency(2.0)
            self.vending_machine.add_currency(2.0)
            self.vending_machine.add_currency(2.0)
            self.vending_machine.add_currency(2.0)
            self.vending_machine.buy_product(8)
            self.vending_machine.buy_product(8)
            self.vending_machine.buy_product(8)
            self.vending_machine.buy_product(8)
            self.vending_machine.return_cash()
            self.vending_machine.print_stock()
            
        except Exception as e:
            self.logger.error(f'{e}')
        