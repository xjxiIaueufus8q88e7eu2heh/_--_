"""Bypass bot-detection to view SocialBlade ranks for YouTube"""
from seleniumbase import SB

with SB(uc=True, test=True, locale_code="en") as sb:
    url = "https://guidedhacking.com/"
    sb.activate_cdp_mode(url)
    sb.sleep(5)
    sb.uc_gui_click_captcha()
#    sb.assert_text("Username", '[for="user_login"]', timeout=3)
 #   sb.assert_element('label[for="user_login"]')
 #   sb.highlight('button:contains("Sign in")')
  #  sb.highlight('h1:contains("GitLab.com")')
    sb.post_message("SeleniumBase wasn't detected", duration=4)
    os.system("ls -tgh; pwd; ls | grep -i *.png")
    sb.save_screenshot("st2k.png")
