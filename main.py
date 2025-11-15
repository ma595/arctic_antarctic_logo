from arctic_antarctic_logo import make_arctic_logo, make_antarctic_logo

make_arctic_logo('output/arctic.png', fill_ocean=False, fill_lakes=False, ocean_colour='white', land_colour='black', border_colour="black", border_width=8,)
make_antarctic_logo('output/antarctic.png', fill_ocean=False, fill_lakes=False, ocean_colour='white', land_colour='black', border_colour="black", border_width=8,)

make_arctic_logo('output/arctic_filled.png', fill_ocean=True, fill_lakes=True, ocean_colour='white', land_colour='black', border_colour="black", border_width=8,)
make_antarctic_logo('output/antarctic_filled.png', fill_ocean=True, fill_lakes=True, ocean_colour='white', land_colour='black', border_colour="black", border_width=8,)