from templating import Generator, load_data, open_in_browser

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

logger = logging.getLogger(__name__)

data = load_data("examples/.data/data.json", "examples/.data/paths.json")



# gen = Generator(auto_open=True, browser="default", templates_folder=f"{os.getcwd()}\\templates")
# gen = Generator(auto_open=True, browser="default", templates_folder=f"letter")

gen = Generator(browser="brave", templates_folder=r"examples\templates\base-template", data=data)
# gen = Generator(auto_open=True, browser="chrome",templates_folder="cv-template")
# gen = Generator(auto_open=True, browser="chrome",templates_folder="cv-template")

gen.pdf()

