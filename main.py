# import youtube-dl
# https://github.com/ytdl-org/youtube-dl
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Program:
    def __init__(self, url):
        super().__init__()
        self.driver = webdriver.Firefox()
        self.driver.get(url)

        self.text_file = open("Links.txt", "x")
        sleep(2)
        self.scrollToBottom()
        sleep(1)
        self.get_links()
        sleep(1)
        self.text_file.close()

    def get_links(self):
        video_items = self.driver.find_elements_by_xpath(
            '//div[@class = "style-scope ytd-grid-renderer"]/*')
        for item in video_items:
            link = item.find_element_by_tag_name('a').get_attribute('href')
            print(link, file=self.text_file)

    def scrollToBottom(self):
        SCROLL_PAUSE_TIME = 1
        # Get scroll height
        last_height = self.driver.execute_script(
            "return document.getElementById('page-manager').scrollHeight")
        while True:
            # Scroll down to bottom
            self.driver.execute_script(
                'window.scrollTo(0, document.getElementById("page-manager").scrollHeight);'
            )
            # Wait to load page
            sleep(SCROLL_PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script(
                "return document.getElementById('page-manager').scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height


if __name__ == "__main__":
    Program(
        input(
            # https://www.youtube.com/channel/.../videos
            "link of the 'videos' section of the channel: "))