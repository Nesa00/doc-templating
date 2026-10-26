from templating import Generator, load_data, open_in_browser

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

logger = logging.getLogger(__name__)

if __name__ == "__main__":

    CV_paths = r"examples\CV\data\CV_data.json" , r"examples\CV\data\CV_private.json"
    CV_data = load_data(*CV_paths)

    CV = Generator(browser="brave", templates_folder=r"examples\CV\minimalistic\CV", output_html="CV.html", data=CV_data)
    CV.pdf()

    CL_paths = r"examples\CV\data\CL_data.json"
    CL_data = load_data(CL_paths)

    CL = Generator(browser="brave", templates_folder=r"examples\CV\minimalistic\cover-letter", output_html="CL.html", data=CL_data)
    CL.pdf()

