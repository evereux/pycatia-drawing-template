#! /usr/bin/python3.8

"""
    A script that uses pycatia to generate a drawing format for all sheets
    in the active drawing.
"""

import argparse

from pycatia.drafting_interfaces.drawing_view import DrawingView

from application.caa import caa
from application.caa import get_active_drawing
from application.border import create_border
from application.copyright_box import create_copyright_box
from application.drawing import create_drawing
from application.paper_size import get_sheet_size_info
from application.parameters import create_parameters
from application.purge import purge_background_view
from application.settings import sheet_sizes
from application.template_name import create_template_name
from application.title_block import create_title_block

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='pycatia-drawing-template',
        usage='%(prog)s [options]',
        description='Create drawing border templates using pycatia.'
    )

    # optional argument
    parser.add_argument(
        '-create-new',
        nargs='?',
    )

    parser.add_argument(
        '-draw-existing',
        action='store_true'
    )

    args = parser.parse_args()

    if args.create_new:
        if args.create_new not in sheet_sizes:
            raise ValueError('Please supply a valid sheet size.')
        sheet_size = args.create_new
        print(f'Creating new "{sheet_size}" sheet.')
        create_drawing(sheet_size)

    if args.draw_existing is True:
        drawing = get_active_drawing(caa)
        sheets = drawing.sheets
        parameters = create_parameters(drawing)
        sheet_number = 1
        for sheet in sheets:
            size_info = get_sheet_size_info(sheet)

            # !! delete everything in the background view!!
            purge_background_view(drawing, sheet)

            create_border(sheet, size_info)
            create_copyright_box(sheet, parameters)
            create_title_block(sheet, size_info, parameters, sheet_number)
            create_template_name(sheet, size_info)
            # required as colour changes are not otherwise visible.
            sheet.force_update()
            sheet_number += 1

        # activate the first sheet and main view.
        # on border creation the main view is activated after work in the
        # background view is completed yet it seems to have no effect on sheet 1.
        # I even tried looping through the sheets to activate the main view but
        # then this didn't work for sheet.2.
        for sheet in sheets:
            sheet.activate()
            main_view = DrawingView(sheet.views.get_item_by_name('Main View').com_object)
            main_view.activate()
            viewer = caa.active_window
            # fit all in.
            viewer.active_viewer.reframe()
        sheets[0].activate()

