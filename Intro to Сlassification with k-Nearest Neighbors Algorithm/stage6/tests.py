import ast
from hstest.stage_test import List
from hstest import *

correct_answer = [[1.0, 1.0, 1.0, 1.0], [0.6666666666666666, 1.0, 0.5, 0.6666666666666666]]
metric_list = ['accuracy', 'precision', 'recall', 'F-score']

class MetricTest(StageTest):

    def generate(self) -> List[TestCase]:
        return [TestCase(time_limit=1000000)]

    def check(self, reply: str, attach):

        reply = reply.strip()

        if len(reply) == 0:
            return CheckResult.wrong("No output was printed")

        if len(reply.split('\n')) != 10:
            return CheckResult.wrong('The number of answers supplied does not equal 2 or one answer is partial')

        reply = reply.split('\n')
        reply_modified = '['
        for j in range(len(reply)):
            if j == 0:
                reply_modified += '['
            elif j == 5:
                reply_modified = reply_modified[:len(reply_modified) - 1]
                reply_modified += '],['
            else:
                elem = reply[j].split(' ')[1]
                reply_modified += elem + ','

        reply_modified = reply_modified[:len(reply_modified) - 1]
        reply_modified += ']]'
        print(reply_modified)

        try:
            user_list = ast.literal_eval(reply_modified)


        except Exception as e:
            return CheckResult.wrong(f"Seems that output is in wrong format.\n"
                                     f"Make sure you use only the following Python structures in the output: string, int, float, list, dictionary")

        if not isinstance(user_list, list):
            return CheckResult.wrong(f'Print answer as a list')

        if len(user_list) != len(correct_answer):
            return CheckResult.wrong(
                f'Output should contain {len(correct_answer)} cases, found {len(user_list)}')

        for i in range(len(user_list)):
            if len(user_list[i]) != 4:
                return CheckResult.wrong(
                    f'Case number {i + 1} should have {len(correct_answer[i])} metric values, found {len(user_list[i])}'
                    f'metric values')

            for j in range(len(user_list[i])):
                if user_list[i][j] < correct_answer[i][j] - 0.01 * correct_answer[i][j] or\
                        user_list[i][j] > correct_answer[i][j] + 0.01 * correct_answer[i][j]:
                        return CheckResult.wrong(f"Seems like answer is not correct\n"
                                                 f"Check metric {metric_list[j]} of case {i + 1}")

        return CheckResult.correct()


if __name__ == '__main__':
    MetricTest().run_tests()