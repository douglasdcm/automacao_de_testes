import asyncio
from playwright.async_api import async_playwright
from pytest import mark
@mark.asyncio
async def test_full_page_flow():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False)
        page = await browser.new_page()
        # Navigate to the target page
        await page.goto("https://douglasdcm.github.io/aulas/")
        # Basic form elements
        await page.fill("input[name='username']", "testuser")
        await page.fill("input[name='password']", "P@ssw0rd!")
        await page.fill("input[type='email']", "testuser@example.com")
        await page.fill("textarea[name='bio']", "This is a test bio.")
        await page.select_option("select[name='country']", label="United States")
        await page.fill("input[name='age']", "30")
        # birthdate – assuming type date or text
        await page.fill("input[name='birthdate']", "1990-01-01")
        # Submit the form
        await page.click("button[id='submit-btn']")
        page.once("dialog", lambda dialog: dialog.accept())

        # Checkboxes & radio buttons
        await page.check("input[id='simple-dropdown']")
        # await page.check("input[type='checkbox'][value='Sports']")
        # await page.check("input[type='checkbox'][value='Music']")
        # await page.check("input[type='radio'][value='Male']")
        # await page.check("input[type='radio'][value='Female']")
        # await page.check("input[type='radio'][value='Other']")
        # await page.check("input[name='agree']")
        # Buttons
        await page.click("button:has-text('Simple Button')")
        await page.click("button:has-text('Show Alert')")
        # Handle alert
        await page.once("dialog", lambda dialog: dialog.accept())
        await page.click("button:has-text('Show Confirm')")
        await page.once("dialog", lambda dialog: dialog.accept())
        await page.click("button:has-text('Show Prompt')")
        await page.once("dialog", lambda dialog: dialog.accept("some input"))
        await page.click("button:has-text('Open New Tab')")
        # Switch to new tab
        pages = page.context.pages
        if len(pages) > 1:
            new_page = pages[-1]
            await new_page.bring_to_front()
            # maybe close it
            await new_page.close()
        await page.click("button:has-text('Disabled Button')").catch(lambda e: None)
        await page.click("button:has-text('Success')")
        await page.click("button:has-text('Danger')")
        await page.click("button:has-text('Warning')")
        # Dynamic elements
        await page.click("button:has-text('Show Hidden Element')")
        await page.wait_for_selector("div:has-text('This element was hidden and now is visible!')", timeout=5000)
        await page.click("button:has-text('Add New Element')")
        await page.wait_for_selector("div.new-element", timeout=5000)
        await page.click("button:has-text('Change Text')")
        await page.wait_for_selector("div:has-text('Original text content')", timeout=5000)
        await page.click("button:has-text('Toggle Class')")
        # you could verify CSS class changed
        await page.click("button:has-text('Load Content via AJAX')")
        await page.wait_for_selector("div:has-text('Content will appear here after AJAX call') ~ div.ajax-content", timeout=10000)
        # Dropdowns & Multi-Select
        await page.select_option("select[name='simple-dropdown']", label="Option 2")
        await page.select_option("select[name='multi-select']", label=["Red", "Blue"])
        await page.select_option("select[name='disabled-dropdown']", label="Option 1").catch(lambda e: None)
        await page.click("button:has-text('Dynamic Dropdown')")  # assume this adds option
        await page.select_option("select[name='dynamic-dropdown']", label="New Option")
        # HTML Tables
        # Verify existing rows
        rows = await page.query_selector_all("table tbody tr")
        assert len(rows) >= 3
        # Add table row
        await page.click("button:has-text('Add Table Row')")
        new_rows = await page.query_selector_all("table tbody tr")
        assert len(new_rows) == len(rows) + 1
        # Remove last row
        await page.click("button:has-text('Remove Last Row')")
        back_rows = await page.query_selector_all("table tbody tr")
        assert len(back_rows) == len(rows)
        # Tooltips & Popovers
        tooltip_target = await page.query_selector("span:has-text('Hover over me')")
        await tooltip_target.hover()
        await page.wait_for_selector("div.tooltip", timeout=5000)
        await page.click("button:has-text('Show Popover')")
        await page.wait_for_selector("div.popover-content", timeout=5000)
        # File Upload
        # Provide local file path; adapt path as needed
        file_input1 = await page.query_selector("input[type='file']:nth-of-type(1)")
        await file_input1.set_input_files("path/to/single_file.txt")
        file_input2 = await page.query_selector("input[type='file']:nth-of-type(2)")
        await file_input2.set_input_files(["path/to/file1.txt", "path/to/file2.txt"])
        # IFrame
        frame = await page.frame_locator("iframe").frame()
        await frame.wait_for_selector("body", timeout=5000)
        # maybe interact inside iframe
        # Clean up / close
        await browser.close()

# For running
if __name__ == "__main__":
    asyncio.run(test_full_page_flow())
