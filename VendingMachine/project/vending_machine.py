import logging
import math
#import string

STR_EXCEPTION_OVER_STOCK='Oh oh, it looks like there are too \
    many items that are trying to be added.'
EMPTY_TRAY_TEMPLATE={'product':'', 'count':0, 'price':0.0}

class VendingMachine:
    def __init__(   self,
                    logger,
                    currency_denominations,
                    num_of_trays=25,
                    depth_per_tray=10,
                    initial_stock={},
                    is_alphanumeric_trays=False,
                    demonimation_round=2
                ):
        self.logger = logger
        try:
            self.accepted_currency = list(
                            k for k, v in currency_denominations.items())
            self.change_options = sorted(list(
                            k for k, v in currency_denominations.items() if v[0]))
            self.currency_denominations = currency_denominations
            self.num_of_trays = num_of_trays
            self.depth_per_tray = depth_per_tray
            self.is_alphanumeric_trays = is_alphanumeric_trays
            self.stock = self.create_storage_split()
            self.stock_units(initial_stock)
            self.cash_in_machine = 0.0
            self.demonimation_round = demonimation_round
        except Exception as e:
            self.logger.error(f'Error(VendingMachine) = {e}')

    def create_storage_split(self):
        storage = {}
        if not self.is_alphanumeric_trays:
            for count in range(1, self.num_of_trays + 1):
                storage[count] = EMPTY_TRAY_TEMPLATE
        else:
            # alphabets = string.ascii_uppercase
            # starting_letter = 0
            # previous_tray = ''
            # for count in range(1, self.num_of_trays + 1):
            #     number_of_letters = starting_letter/len(alphabets) + 1
            #     alphanum = alphabets[starting_letter] + str(count)
            #     storage[alphanum] = {'product':'', 'count':0, 'price':0.0}

            #this case would have handled point 1 in 'Things to add'
            pass

        return storage

    def stock_units(self, stock_to_add):
        try:
            if not self.is_alphanumeric_trays:
                tray_count = 1
                for prod in stock_to_add:
                    while stock_to_add[prod][1] > 0:
                        while self.stock[tray_count]['count'] != 0:
                            tray_count += 1
                            if tray_count > self.num_of_trays:
                                raise Exception(STR_EXCEPTION_OVER_STOCK) 
                        count_in_tray = min( stock_to_add[prod][1], 
                                               self.depth_per_tray )
                        self.stock[tray_count] = { 'product':prod,
                                                   'count':count_in_tray,
                                                   'price':stock_to_add[prod][0] }
                        
                        stock_to_add[prod][1] -= count_in_tray
                        tray_count += 1
                        if tray_count > self.num_of_trays:
                            raise Exception(STR_EXCEPTION_OVER_STOCK)
        except Exception as e:
            self.logger.error(f'Error: {e}')
            return False
        
        return True
        
    def move_stock(self, from_tray, to_tray):
        if not self.is_alphanumeric_trays:
            if from_tray > self.num_of_trays or to_tray > self.num_of_trays:
                raise Exception('Please enter valid tray numbers.')

            if self.stock[to_tray]['count'] != 0:
                raise Exception('You are trying to move to a non-empty tray.')
                
            if self.stock[from_tray]['count'] == 0:
                raise Exception('There is nothing at the tray you are moving from.')

            self.stock[to_tray] = self.stock[from_tray]
            self.stock[from_tray] = EMPTY_TRAY_TEMPLATE
            self.logger.info(f'Contents of tray {from_tray} moved to {to_tray}')

    def add_currency(self, currency_added):
        if currency_added not in self.accepted_currency:
            raise Exception('Please enter valid currency.')
            # trigger currency eject
        
        self.cash_in_machine = round(self.cash_in_machine + currency_added,
            self.demonimation_round)
        self.logger.info(f'Cash in machine = {self.cash_in_machine}')

    def buy_product(self, tray_selected):
        try:
            if not self.is_alphanumeric_trays:
                if tray_selected > self.num_of_trays:
                    raise Exception('Please enter a valid product number.')

                if self.stock[tray_selected]['count'] == 0:
                    raise Exception('There is nothing in the tray.')
                
                if self.stock[tray_selected]['price'] > self.cash_in_machine or \
                        self.cash_in_machine < self.get_min_price_of_products():
                    raise Exception('Not enough money, please add more.')

                self.stock[tray_selected]['count'] -= 1
                self.cash_in_machine = round(self.cash_in_machine - 
                    self.stock[tray_selected]['price'], self.demonimation_round)
                self.logger.info(f"Dispensed-{self.stock[tray_selected]['product']}")
                if self.stock[tray_selected]['count'] == 0:
                    self.stock[tray_selected] = EMPTY_TRAY_TEMPLATE
                #trigger product dispense at tray_selected
                self.logger.info(f'Cash in machine = {self.cash_in_machine}')
        except Exception as e:
            self.logger.error(f'{e}')
    
    def return_cash(self):
        for curr in range(len(self.change_options) - 1, -1, -1):
            while self.cash_in_machine >= self.change_options[curr] and \
                    self.currency_denominations[self.change_options[curr]][1] > 0:
                self.logger.info(f'Returned - {self.change_options[curr]}')
                self.currency_denominations[self.change_options[curr]][1] -= 1
                self.cash_in_machine = round(self.cash_in_machine - self.change_options[curr], self.demonimation_round)

        if self.cash_in_machine > 0:
            self.logger.warning(f'Sorry but {self.cash_in_machine} is leftover. You can add more cash and use this to buy a product.')
    
    def get_min_price_of_products(self):
        min_price = math.inf
        for tray in self.stock:
            if self.stock[tray]['count'] > 0:
                min_price = min(min_price, self.stock[tray]['price'])
        
        return min_price

    def print_stock(self, print_empty=False):
        print('***START:Print Stock********************')
        for tray in self.stock:
            if print_empty or (not print_empty and self.stock[tray]['count'] != 0):
                self.logger.info(f"Tray: {tray}, Product: {self.stock[tray]['product']}, Count: {self.stock[tray]['count']}, Price: {self.stock[tray]['price']}")
        print('***END:Print Stock**********************')