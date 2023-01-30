import ast
from hstest.stage_test import List
from hstest import *

correct_answer = [[1, 0, 0], [1, 0, 1], [1, 0, 1]]

class PredictTest(StageTest):

    def generate(self) -> List[TestCase]:
        return [TestCase(time_limit=1000000)]

    def check(self, reply: str, attach):

        reply = reply.strip()

        if len(reply) == 0:
            return CheckResult.wrong("No output was printed")

        if reply.count('[') < 1 or reply.count(']') < 1:
            return CheckResult.wrong('Print the answers should contain lists')

        if len(reply.split('\n')) != 3:
            return CheckResult.wrong('The number of answers supplied does not equal 3')

        reply= reply.split('\n')
        reply_modified = '['
        for elem in reply:
            index_from = elem.find('[')
            index_to = elem.rfind(']')
            reply_modified += elem[index_from: index_to + 1] + ','
        reply_modified = reply_modified[:len(reply_modified) - 1]
        reply_modified += ']'

        try:
            user_list = ast.literal_eval(reply_modified)


        except Exception as e:
            return CheckResult.wrong(f"Seems that output is in wrong format.\n"
                                     f"Make sure you use only the following Python structures in the output: string, int, float, list, dictionary")

        if not isinstance(user_list, list):
            return CheckResult.wrong(f'Print answer as a list')

        if len(user_list) != len(correct_answer):
            return CheckResult.wrong(
                f'Output should contain {len(correct_answer)} lists, found {len(user_list)}')

        for i in range(len(user_list)):
            if len(user_list[i]) != 3:
                return CheckResult.wrong(
                    f'List {i} has length {len(user_list[i])}, the length of the list should be 3.')
            for j in range(len(user_list[i])):
                if user_list[i][j] != correct_answer[i][j]:
                        return CheckResult.wrong(f"Seems like answer is not correct\n"
                                                 f"Check element {j} of your list {i}")

        return CheckResult.correct()


if __name__ == '__main__':
    PredictTest().run_tests()