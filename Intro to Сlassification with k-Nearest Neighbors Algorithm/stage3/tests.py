import ast
from hstest.stage_test import List
from hstest import *

correct_answer = [[0.5530776092774308, 0.3333333333333333, 1.33, 0, 0, 0, 1],
          [0.2925958965209634, 0.6666666666666666, 1.44, 0, 1, 0, 0],
          [0.5700267618198036, 0.16666666666666666, 1.37, 0, 0, 0, 1],
          [1.0, 0.0, 1.18, 0, 0, 0, 1], [0.4272970561998215, 0.1, 0.86, 0, 0, 0, 1],
          [0.247992863514719, 0.23333333333333334, 1.82, 1, 0, 0, 0],
          [0.06244424620874219, 0.5333333333333333, 1.66, 1, 0, 0, 0],
          [0.17484388938447812, 0.13333333333333333, 1.9, 0, 0, 1, 0],
          [0.2613737734165923, 1.0, 1.96, 0, 0, 0, 1],
          [0.0, 0.43333333333333335, 1.78, 0, 0, 1, 0]]

class ScaleTest(StageTest):

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
            if len(user_list[i]) != 7:
                return CheckResult.wrong(
                    f'Nested list {i} should contain 7 values, found {len(user_list[i])}.\n'
                    f'Note that numeration starts from 0.')
            for j in range(len(user_list[i])):
                if j == 0 or j == 1:
                    if user_list[i][j] < correct_answer[i][j] - 0.01 * correct_answer[i][j] or user_list[i][j] > correct_answer[i][j] + 0.01 * correct_answer[i][j]:
                        return CheckResult.wrong(f"Seems like answer is not correct;\n"
                                                 f"Check element {j} of your {i} list.\n"
                                                 f"Note that numeration starts from 0.")
                if j != 0 and j!= 1:
                    if user_list[i][j] != correct_answer[i][j]:
                        return CheckResult.wrong(f"Seems like answer is not correct;\n"
                                                 f"Check element {j} of your {i} list.\n"
                                                 f"Note that numeration starts from 0.")

        return CheckResult.correct()


if __name__ == '__main__':
    ScaleTest().run_tests()