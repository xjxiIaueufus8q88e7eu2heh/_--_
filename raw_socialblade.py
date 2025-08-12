"""Bypass bot-detection to view SocialBlade ranks for YouTube"""
from seleniumbase import SB
import time
import os
# Create unique filename based on current timestamp
timestamp = int(time.time())
screenshot_name = f"socialblade_{timestamp}.png"

with SB(uc=True, test=True, ad_block=True, pls="none") as sb:
    url = "https://socialblade.com/"
    sb.activate_cdp_mode(url)
    sb.sleep(1.5)
    if not sb.is_element_visible('input[placeholder*="Search"]'):
        sb.uc_gui_click_captcha()
        sb.sleep(0.5)
    channel_name = "michaelmintz"
    channel_title = "Michael Mintz"
    sb.cdp.press_keys('input[placeholder*="Search"]', channel_name)
    sb.sleep(2)
    sb.cdp.click('a:contains("%s")' % channel_title)
    sb.sleep(2)
    sb.cdp.remove_elements("#lngtd-top-sticky")
    sb.sleep(1.5)
    name = sb.cdp.get_text("h3")
    ch_name = name.split(" ")[-1]
    name = name.split(" @")[0]
    link = "https://www.youtube.com/%s" % ch_name
    print("********** SocialBlade Stats for %s: **********" % name)
    print(">>> (Link: %s) <<<" % link)
    print(sb.get_text('[class*="grid lg:hidden"]'))
    print("********** SocialBlade Ranks: **********")
    print(sb.get_text('[class*="gap-3 flex-1"]'))
    for i in range(17):
        sb.cdp.scroll_down(6)
        sb.sleep(0.1)
    sb.sleep(2)
    os.system("ls -tgh; pwd; ls | grep -i *.png")
    sb.save_screenshot(os.path.join("screenshots", screenshot_name))
