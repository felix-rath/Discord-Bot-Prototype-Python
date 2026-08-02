from playwright.async_api import async_playwright


class WebsiteChecker:

    def __init__(self, url, browser_profile):
        self.url = url
        self.browser_profile = browser_profile
        self.playwright = None
        self.context = None
        self.page = None
        self.started = False

    async def start(self):
        self.playwright = await async_playwright().start()

        self.context = await self.playwright.chromium.launch_persistent_context(
            user_data_dir=self.browser_profile,
            headless=False
        )

        self.page = self.context.pages[0]
        self.started = True

    async def check(self):
        await self.page.goto(
            self.url,
            wait_until="domcontentloaded",
            timeout=30000
        )

        await self.page.wait_for_timeout(5000)

        text = await self.page.locator("body").inner_text()

        ##text = await self.page.locator("body").text_content() ## ZEIGT BOT SCHUTZ TEXT
        ##print(repr(text))

        return text

    async def close(self):
        if self.context:
            await self.context.close()

        if self.playwright:
            await self.playwright.stop()

        self.started = False