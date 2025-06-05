import fitz  
def extract_pages_render(input_pdf, output_pdf, first_page, last_page):
    doc = fitz.open(input_pdf)
    total_pages = doc.page_count
    print(f"PDF has {total_pages} pages.")

    if first_page < 1 or last_page < first_page or last_page > total_pages:
        raise ValueError(f"Invalid range: {first_page}–{last_page}")

    new_doc = fitz.open()

    for page_num in range(first_page - 1, last_page):  
        print(f"Rendering page {page_num + 1}")
        rect = doc[page_num].rect
        new_page = new_doc.new_page(width=rect.width, height=rect.height)
        new_page.show_pdf_page(rect, doc, page_num)

    new_doc.save(output_pdf)
    new_doc.close()
    doc.close()
    print(f"Saved to {output_pdf}")

extract_pages_render(
    r"The Developing Person Through Childhood and Adolescence.pdf",
    r"Biosocial Development.pdf",
    418,
    464
)
