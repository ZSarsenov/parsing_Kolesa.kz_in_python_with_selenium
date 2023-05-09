from kolesa import take_last_page_paginator, take_all_links, take_all_data_blocks, save_to_CSV

last_page = take_last_page_paginator()

links = take_all_links(last_page)

data = take_all_data_blocks(links)

print(data)
save_to_CSV(data)