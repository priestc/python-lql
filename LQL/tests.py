import unittest
from LQL import Query

class LQLParseTest(unittest.TestCase):
    cases = [
        [    
            'including mime.type == "video/*"',
            [['including', [['mime.type', '==', 'video/*']]]]
        ],
        [
            "EXCLUDING mimetype ExAcT 'text/plain', key exact 'string value'",
            [['excluding', [['mimetype', 'exact', 'text/plain'], ['key', 'exact', 'string value']]]]
        ],
        [
            'INCLUDING source exact DVD; EXCLUDING date == 2006',
            [["including", [['source', 'exact', 'DVD']]], ['excluding', [['date', '==', '2006']]]]
        ],
        [
            'including source == DVD, date == 2006; excluding mimetype matches  "text/*"',
            [["including", [['source', '==', 'DVD'], ['date', '==', '2006']]],["excluding", [['mimetype', 'matches', 'text/*']]]]
        ]
    ]

    def test_parsing(self):
        for defined_string_query, defined_ast_query in self.cases:
            #import debug
            # runs _calc_ast
            query = Query(as_string=defined_string_query)
            calculated_ast = query.ast

            # convert that ast back into a string...
            recalculated_string = Query(ast=calculated_ast).as_string
            
            # then back into a ast again.
            recalculated_ast = Query(as_string=recalculated_string).ast
            
            # assert that they are the same.
            self.assertEquals(defined_ast_query, recalculated_ast)

    def test_invalid_init(self):
        self.assertRaises(ValueError, lambda: Query())

if __name__ == '__main__':
    unittest.main()