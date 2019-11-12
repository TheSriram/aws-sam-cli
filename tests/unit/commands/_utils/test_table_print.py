import io
from contextlib import redirect_stdout
from collections import OrderedDict
from unittest import TestCase

from samcli.commands._utils.table_print import pprint_column_names, pprint_columns

TABLE_FORMAT_STRING = "{Alpha:<{0}} {Beta:<{1}} {Gamma:<{2}}"
TABLE_FORMAT_ARGS = OrderedDict({"Alpha": "Alpha", "Beta": "Beta", "Gamma": "Gamma"})


class TestTablePrint(TestCase):
    def setUp(self):
        self.redirect_out = io.StringIO()

    def test_pprint_column_names(self):
        @pprint_column_names(TABLE_FORMAT_STRING, TABLE_FORMAT_ARGS)
        def to_be_decorated(*args, **kwargs):
            pass

        with redirect_stdout(self.redirect_out):
            to_be_decorated()
        output = (
            "------------------------------------------------------------------------------------------------\n"
            "Alpha                            Beta                             Gamma                          \n"
            "------------------------------------------------------------------------------------------------\n"
            "------------------------------------------------------------------------------------------------\n"
        )

        self.assertEqual(output, self.redirect_out.getvalue())

    def test_pprint_column_names_and_text(self):
        @pprint_column_names(TABLE_FORMAT_STRING, TABLE_FORMAT_ARGS)
        def to_be_decorated(*args, **kwargs):
            pprint_columns(
                columns=["A", "B", "C"],
                width=kwargs["width"],
                margin=kwargs["margin"],
                format_args=kwargs["format_args"],
                format_string=TABLE_FORMAT_STRING,
                columns_dict=TABLE_FORMAT_ARGS.copy(),
            )

        with redirect_stdout(self.redirect_out):
            to_be_decorated()

        output = (
            "------------------------------------------------------------------------------------------------\n"
            "Alpha                            Beta                             Gamma                          \n"
            "------------------------------------------------------------------------------------------------\n"
            "A                                B                                C                              \n"
            "------------------------------------------------------------------------------------------------\n"
        )
        self.assertEqual(output, self.redirect_out.getvalue())
