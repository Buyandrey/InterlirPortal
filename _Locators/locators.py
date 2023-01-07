"""
.py file with all selectors from Interlir portal, separated by classes(page objects)
"""


class RegistrationPageLocators:
    email_textfield_xpath = "//div/input[@type='email']"
    password_textfield_xpath = "//div/input[@type='password']"
    registerNow_button_xpath = "//div/form/button"
    check_message_xpath = "//div/span[text()[contains(.,'Please, check your mail')]]"
    already_message_xpath = "//div/span[text()[contains(.,'User with given email address already exist')]]"


class LoginPageLocators:
    email_textfield_xpath = "//div/input[@type='email']"
    password_textfield_xpath = "//div/input[@type='password']"
    authorization_button_xpath = "//div/form/button"
    registerHere_button_xpath = "//div[@class='access-page__register-account']/a"


class HomePageLocators:
    avatar_xpath = "//div/div[@class='header__action header__user-avatar']"
    ba_selector_xpath = "//div/div[@class='selector__current-icon']"
    ba_selector_name_xpath = "//div[@class='selector']/div/div/div/div/div/span"


class BusinessAccountPageLocators:
    startRegistrationOrganization = "//div/div/button[@type='button']"
    firstNameField = "(//div/div/input)[2]"
    lastNameField = "(//div/div/input)[3]"""
    emailField = "(//div/div/input)[4]"""
    countrySelector = "(//div/div[@class='select__container input__element'])[1]"
    countryField = "(//div/div[@class='select']/div/input)"
    country = "//div[@class='select__options select__options--active']/div/div[@class='select__item']"
    phoneField = "//div[@type='phone']/div/div/div/div/div/div/input"
    industrySelector = "(//div/div[@class='select__container input__element'])[3]"
    industryField = "(//div/div[@class='select']/div/input)"
    industry = "//div[@class='select__options select__options--active']/div/div[@class='select__item']"
    companyNameField = "(//div/div/input)[6]"
    companyNumberField = "(//div/div/input)[7]"
    vatNumberField = "(//div/div/input)[8]"
    websiteField = "(//div/div/input)[9]"
    addressLineField = "(//div/div/input)[10]"
    zipPostalCodeField = "(//div/div/input)[11]"
    stateField = "(//div/div/input)[12]"
    cityDistrictField = "(//div/div/input)[13]"
    nextStepButton = "//div/button[@type='submit']"
    uploadDocumentsButton = "//div[@class='card__action']/button"
    uploadDocumentFromPath = "//div[@class='file-field']/input"
    nextStepButtonStep3 = "//div/div/button[@type='submit']"
    errorRequiered = "(//*[text()[contains(.,\" This field is required \")]])"
    ok = "(//*[text()[contains(.,\"As soon as we verify your company, you may proceed to work\")]])"
