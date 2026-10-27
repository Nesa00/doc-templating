from templating import Generator, load_data

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

logger = logging.getLogger(__name__)

if __name__ == "__main__":

    # data_paths = r"examples\CV\data\data.json" , r"examples\CV\data\private.json"
    # # template_path = r"examples\CV\minimalistic"
    # template_path = r"examples\CV\modern"
    # data = load_data(*data_paths)

    # Generator(browser="brave", 
    #           templates_folder=template_path, 
    #           template_file="CV_base.html", 
    #           output_html="CV.html", 
    #           data=data).pdf()
    
    # Generator(browser="brave", 
    #           templates_folder=template_path,
    #           template_file="cover-letter_base.html", 
    #           output_html="CL.html", 
    #           data=data).pdf()


    # data_paths = r"examples\contract\data\rental_data.json", r"examples\contract\data\rental_private_data.json"
    # data = load_data(*data_paths)

    # Generator(browser="brave", 
    #     templates_folder=r"examples\contract\rental",
    #     output_html="contract.html", 
    #     data=data).pdf()


    # data_paths = r"examples\contract\data\classic_data.json", r"examples\contract\data\classic_private_data.json"
    # data = load_data(*data_paths)

    # Generator(browser="brave", 
    #     templates_folder=r"examples\contract\classic",
    #     output_html="contract.html", 
    #     data=data).pdf()

    # data_paths = r"examples\invoice\data\purchase_data.json", r"examples\invoice\data\purchase_private_data.json"
    # data = load_data(*data_paths)

    # Generator(browser="brave", 
    #     templates_folder=r"examples\invoice\purchase",
    #     output_html="invoice.html", 
    #     data=data).pdf()

    data_paths = r"examples\invoice\data\quotation_data.json", r"examples\invoice\data\quotation_private_data.json"
    data = load_data(*data_paths)

    Generator(browser="brave", 
        templates_folder=r"examples\invoice\quotation",
        output_html="invoice.html", 
        data=data).pdf()



