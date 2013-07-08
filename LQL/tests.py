import unittest
from . import Parse

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
        for defined_string_query, defined_list_query in self.cases:
            # runs _calc_list
            query = Parse(as_string=defined_string_query)
            calculated_list = query.as_list

            # convert that list back into a string...
            recalculated_string = Parse(as_list=calculated_list).as_string
            
            # then back into a list again.
            recalculated_list = Parse(as_string=recalculated_string).as_list
            
            self.assertEquals(defined_list_query, recalculated_list)

if __name__ == '__main__':
    #unittest.main()
    t=LQL.ParseTest()
    t.test_parsing()