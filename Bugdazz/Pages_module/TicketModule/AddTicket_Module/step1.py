from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import Select

linktext_Ticket_Module = ("link_text","#ticketSubmenu")
linktext_addticket_xpath = ("link_text","/tickets/add/step1")
# //*[@id="ID-81b8d50d-0a6e-4b4f-90f6-65bd72f4687b"]
# class="input-search ng-touched remove-rdius ng-invalid is-invalid ng-dirty"
# id = "ID-cf06909a-ca8d-4841-903f-b4c715509b64"
dropdown_selectprogram_id = ("id","ID-5b1659c0-f7ac-46e7-a521-8a00c3f86875")
selectProgram_dropdown_xpath = ("ID-9580d529-ce98-4adc-9971-07817c465b00")

# public static void main() {
#
# 	// Set Driver path
# 	System.setProperty("webdriver.chrome.driver", "C:\\AUTOMATION\\chromedriver.exe");
# 	WebDriver driver=new ChromeDriver();
#
# 	//open google
# 	driver.get("https://www.google.com");
# 	driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
#
# 	//enter techlistic tutorials in search box
# 	driver.findElement(By.name("q")).sendKeys("selenium tutorial techlistic");
#
# 	//wait for suggestions
# 	WebDriverWait wait=new WebDriverWait(driver, 20);
# 	wait.until(ExpectedConditions.presenceOfElementLocated(By.className("sbtc")));
#
# 	WebElement list=driver.findElement(By.className("sbtc"));
# 	List rows=list.findElements(By.tagName("li"));
#
# 	for(WebElement elem:rows) {
# 	System.out.println(elem.getText());
# steps-1)click on "Add ticket module" dropdown
#        2)click on add ticket - link
#        3)1st step - select program - dropdown - select input from list or write
#        4)finding titile - input text -
#        5)vulnerable asset - text + dropdown -
#        6)affect module - text + dropdown -
#        7)next page - button

class Add_Ticket_step1:
    def __init__(self, driver):
        self.driver = driver
    def click_on_ticketModule(self):
        self.driver.findelement("xpath","dropdown_Ticket_xpath")
    def select_program(self):
        select = Select(dropdown_Ticket_xpath)
        select.


