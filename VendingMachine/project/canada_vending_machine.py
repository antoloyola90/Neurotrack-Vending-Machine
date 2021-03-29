import logging
from project.vending_machine import VendingMachine

CURRENCY_DENOMINATIONS = {
                            0.01:[False],
                            0.05:[True, 100],
                            0.1:[True, 100],
                            0.25:[True, 100],
                            0.50:[False],
                            1.0:[True, 100],
                            2.0:[True, 100],
                            5.0:[False],
                            10.0:[False],
                            20.0:[False],
                            50.0:[False],
                            100.0:[False]
                         }

class CanadaVendingMachine(VendingMachine):
    def __init__(   self,
                    logger,
                    currency_denominations={},
                    num_of_trays=25,
                    depth_per_tray=10,
                    initial_stock={},
                    is_alphanumeric_trays=False,
                    demonimation_round=2
                ):
        self.logger = logger
        try:
            super().__init__(   logger=self.logger,
                                currency_denominations=CURRENCY_DENOMINATIONS,
                                num_of_trays=num_of_trays,
                                depth_per_tray=depth_per_tray,
                                initial_stock=initial_stock,
                                is_alphanumeric_trays=is_alphanumeric_trays,
                                demonimation_round=demonimation_round
                            )
        except Exception as e:
            self.logger.error(f'Error(CanadaVendingMachine) = {e}')