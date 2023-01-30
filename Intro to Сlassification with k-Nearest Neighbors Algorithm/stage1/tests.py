import ast
from hstest.stage_test import List
from hstest import *

correct_answer = [['Yes', '330.8', '35', '1.33', 'nothing'], ['Yes', '214', '45', '1.44', 'cycling 4h'],
          ['Yes', '338.4', '30', '1.37', 'nothing'], ['Yes', '531.2', '25', '1.18', 'nothing'],
          ['Yes', '274.4', '28', '0.86', 'nothing'], ['No', '194', '32', '1.82', 'cycling 3h'],
          ['No', '110.8', '41', '1.66', 'cycling 3h'], ['No', '161.2', '29', '1.9', 'cycling 5h'],
          ['No', '200', '55', '1.96', 'nothing'], ['No', '82.8', '38', '1.78', 'cycling 5h']]

class LoadTest(StageTest):

    def generate(self) -> List[TestCase]:
        return [TestCase(time_limit=1000000)]

    def check(self, reply: str, attach):

        reply = reply.strip()

        if len(reply) == 0:
            return CheckResult.wrong("No output was printed")

        if reply.count('[') < 2 or reply.count(']') < 2:
            return CheckResult.wrong('Print the answer as a nested list')

        if len(reply.split('\n')) != 1:
            return CheckResult.wrong('The number of answers supplied does not equal 1')

        index_from = reply.find('[')
        index_to = reply.rfind(']')
        list_str = reply[index_from: index_to + 1]
        try:
            user_list = ast.literal_eval(list_str)
        except Exception as e:
            return CheckResult.wrong(f"Seems that output is in wrong format.\n"
                                     f"Make sure you use only the following Python structures in the output: string, int, float, list, dictionary")

        if not isinstance(user_list, list):
            return CheckResult.wrong(f'Print answer as a list')

        if len(user_list) != len(correct_answer):
            return CheckResult.wrong(
                f'Output should be a nested list of {len(correct_answer)} lists, found {len(user_list)} lists')

        for i in range(len(user_list)):
            if len(user_list[i]) != 5:
                return CheckResult.wrong(
                    f'Nested list {i} should contain 5 values, found {len(user_list[i])}')
            for j in range(len(user_list[i])):
                if user_list[i][j] != correct_answer[i][j]:
                    return CheckResult.wrong(f"Seems like answer is not correct\n"
                                             f"Check element {j} of your {i} list")

        return CheckResult.correct()


if __name__ == '__main__':
    LoadTest().run_tests()