# -*- coding: utf-8 -*-

from copy import deepcopy

class Test(object):
    def __init__(self, results, seats, blocks=None, params=None):
        self.results = results
        self.seats = seats
        self.params = params
        self.blocks = blocks
        self.seat_results = {}
        self.parties = []
        for (ward, votes) in self.results.iteritems():
            for party in votes:
                if party not in self.parties:
                    self.parties.append(party)

    def _key_with_max_val(self, d):
        # a) create a list of the dict's keys and values
        # b) return the key with the max value
        v = list(d.values())
        k = list(d.keys())
        return k[v.index(max(v))]

    def merge_blocks(self, results):
        merged_results = {}
        for (blockname, blockmembers) in self.blocks.iteritems():
            val = 0
            for party in blockmembers:
                val += results[party]
            merged_results[blockname] = val
        return merged_results


    def calculate_seats(self, results):
        """Using the modified Sainte-Laguë method.
        """
        result = {}
        for (ward_name, ward_results) in results.iteritems():

            quotients = {}
            allocated_seats = {}
            mandates_left = self.seats[ward_name]

            for (party, votes) in ward_results.iteritems():
                quotients[party] = votes / 1.4
                allocated_seats[party] = 0
                if party not in result:
                    result[party] = 0

            while mandates_left:
                biggest_party = self._key_with_max_val(quotients)
                mandates_left -= 1
                allocated_seats[biggest_party] += 1
                result[biggest_party] += 1
                divisor = 2 * allocated_seats[biggest_party] + 1
                quotients[biggest_party] = ward_results[biggest_party] / divisor
        if self.blocks is not None:
            result = self.merge_blocks(result)
        return result

    def run(self):
        pass


class MoveVoters(Test):
    """This test will move a number of voters from one ward to another.
       Useful for exploring possible outcomes of altering a border.
    """
    def run(self):
        print "Before moving"
        print self.calculate_seats(self.results)
        print "moving %d people from `%s` to `%s`" % (self.params["numvoters"], self.params["from"], self.params["to"])
        for party in self.parties:
            temp_dic = deepcopy(self.results)
            temp_dic[self.params["from"]][party] -= self.params["numvoters"]
            temp_dic[self.params["to"]][party] += self.params["numvoters"]
            print ("Everyone voted for %s: " % party)
            print self.calculate_seats(temp_dic)

        return

if __name__ == "__main__":
    print "This module should be called from counterfactual_election.py."
    import sys
    sys.exit()
