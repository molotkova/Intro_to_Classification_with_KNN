import ast
from hstest.stage_test import List
from hstest import *

correct_answer = [0.2812106966355265, 1.4991706027951892, 0.3873684238031154, 0.6039499515901134, 0.7647937207067647,
                  1.579307855293723, 1.5958039687009598, 1.6457031105319977, 0.8894684753340013, 1.6471355362092108]

class DistTest(StageTest):

    def generate(self) -> List[TestCase]:
        return [TestCase(time_limit=1000000)]

    def check(self, reply: str, attach):

        reply = reply.strip()

        if len(reply) == 0:
            return CheckResult.wrong("No output was printed")

        if reply.count('[') != 1 or reply.count(']') != 1:
            return CheckResult.wrong('Print the answer as a list')

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
                f'Output should be a list of {len(correct_answer)} lists, found {len(user_list)} lists')

        for i in range(len(user_list)):
            if user_list[i] < correct_answer[i] - 0.01 * correct_answer[i] or user_list[i] > correct_answer[i] + 0.01 * correct_answer[i]:
                        return CheckResult.wrong(f"Seems like answer is not correct\n"
                                                 f"Check element {i} of your list")
        return CheckResult.correct()


if __name__ == '__main__':
    DistTest().run_tests()