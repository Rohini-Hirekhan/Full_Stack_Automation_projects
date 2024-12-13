import time

import pytest
from Pages_APIScanner.Add_collection.initiate_Scan import InitiateScan
from Pages_APIScanner.Add_collection.sensfrx import Sensfrx
from Pages_APIScanner.Add_collection.swagger import Swagger
from Pages_APIScanner.Add_collection.haircut import Haircut
from Pages_APIScanner.Add_collection.zoho_crm import Zoho_CRM
from Pages_APIScanner.Add_collection.zoho_desk import Zoho_Desk
from Test_APIScanner.test_base import BaseTest
from config.config import TestData


class Test_initateScan(BaseTest):
    @pytest.mark.login
    def test_initiateScanf(self):
        self.scan = InitiateScan(self.driver)
        self.sensfrx = Sensfrx(self.driver)
        self.swagger = Swagger(self.driver)
        self.haircut = Haircut(self.driver)
        self.zohocrm = Zoho_CRM(self.driver)
        self.zdesk = Zoho_Desk(self.driver)
        self.driver.get(TestData.URL)
        self.driver.maximize_window()
        self.scan.initiate_scan()

        self.zohocrm.initiate_scan()
        self.zdesk.initiate_scan()






