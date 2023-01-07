class Configurations:


    IMPLICIT_WAIT_TIME          = 10
    EXPLICIT_WAIT_TIME          = 3
    WAIT_TIME                   = 1
    LINUX_CHROMEDRIVER_PATH     = "/home/bans/Projects/Python/InterlirPortal/drivers/chromedriver"
    LINUX_FIREFOX_PATH          = "/home/bans/Projects/Python/InterlirPortal/drivers/"
    """
        Environment for tests
        linux   | firefox
        win     | linux
    """
    PLATFORM_AND_BROWSER        = "linux_chrome"
    """
        Need to clear cookie and storage?
        Yes    | True
        No     | False
    """
    CLEAR_COOKIES_AND_STORAGE   = True
    """
        Is browser window will be shown?
        Yes    | False
        No     | True
    """
    HEADLESS                    = False
    """
        Is browser window will be closed after a test?
        Yes    | True
        No     | False
    """
    HOLD_BROWSER_OPEN           = False

