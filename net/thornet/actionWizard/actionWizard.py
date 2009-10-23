"""
Action wizard
"""

from net.thornet.converter.converter import UnittestConverter
from net.thornet.testsuitecreator.suiteCreator import TestSuiteCreator

class ActionWizard:

    action = None
    validActions = ['convert', 'create']

    def __init__(self, action):
        self.validateAction(action)

    def validateAction(self, action):
        if action in self.validActions:
            self.action = action
            return True
        else:
            raise Usage('Invalid action called')

    def run(self, arguments):

        if self.action == 'convert':

            converter = UnittestConverter(arguments)
            return converter.run()

        if self.action == 'create':
            creator = TestSuiteCreator(arguments)
            return creator.run()
 