import ast
from hstest.stage_test import List
from hstest import *

answer_y = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
answer_x = [[330.8, 35, 1.33, 0, 0, 0, 1], [214.0, 45, 1.44, 0, 1, 0, 0],
            [338.4, 30, 1.37, 0, 0, 0, 1], [531.2, 25, 1.18, 0, 0, 0, 1],
            [274.4, 28, 0.86, 0, 0, 0, 1], [194.0, 32, 1.82, 1, 0, 0, 0],
            [110.8, 41, 1.66, 1, 0, 0, 0], [161.2, 29, 1.9, 0, 0, 1, 0],
            [200.0, 55, 1.96, 0, 0, 0, 1], [82.8, 38, 1.78, 0, 0, 1, 0]]

class ModifyTest(StageTest):

    def generate(self) -> List[TestCase]:
        return [TestCase(time_limit=1000000)]

    def check(self, reply: str, attach):

        reply = reply.strip()

        if len(reply) == 0:
            return CheckResult.wrong("No output was printed")

        if reply.count('[') < 2 or reply.count(']') < 2:
            return CheckResult.wrong('Print the answer as two lists')

        if len(reply.split('\n')) != 2:
            return CheckResult.wrong('As a result, you should print two lists, each on a separate line.\n'
                                     'Now the number of lines does not equal 2.')

        reply_y = reply.split('\n')[0]
        reply_x = reply.split('\n')[1]
        index_from_y = reply_y.find('[')
        index_to_y = reply_y.find(']')
        user_answer_y = reply_y[index_from_y: index_to_y + 1]
        index_from_x = reply_x.find('[')
        index_to_x = reply_x.rfind(']')
        user_answer_x = reply_x[index_from_x: index_to_x + 1]
        try:
            user_list_y = ast.literal_eval(user_answer_y)
        except Exception as e:
            return CheckResult.wrong(f"Seems that output is in wrong format.\n"
                                     f"Make sure you use only the following Python structures in the output: string, int, float, list, dictionary")

        if not isinstance(user_list_y, list):
            return CheckResult.wrong(f'Print the first answer as a list')

        if len(user_list_y) != len(answer_y):
            return CheckResult.wrong(
                f'First answer should be a list of {len(answer_y)} values, found {len(user_list_y)} values')

        for i in range(len(answer_y)):
            if user_list_y[i] != answer_y[i]:
                return CheckResult.wrong(f"Seems like the first answer is not correct. Check element {i} of your first list.\n"
                f"Note that numeration starts from 0.")

        try:
            user_list_x = ast.literal_eval(user_answer_x)
        except Exception as e:
            return CheckResult.wrong(f"Seems that output is in wrong format.\n"
                                     f"Make sure you use only the following Python structures in the output: string, int, float, list, dictionary")

        if not isinstance(user_list_x, list):
            return CheckResult.wrong(f'Print the second answer as a list')

        if len(user_list_x) != len(answer_x):
            return CheckResult.wrong(
                f'Second answer should be a nested list of {len(answer_x)} lists, found {len(user_list_x)} lists')

        for i in range(len(user_list_x)):
            if len(user_list_x[i]) != 7:
                return CheckResult.wrong(
                    f'Nested list {i} of your second answer should contain 7 values, found {len(user_list_x[i])}.\n'
                    f'Note that numeration starts from 0.')
            for j in range(len(user_list_x[i])):
                if user_list_x[i][j] != answer_x[i][j]:
                    return CheckResult.wrong(f"Seems like second answer is not correct;\n"
                                             f"Check element {j} of your {i} nested list.\n"
                                             f"Note that numeration starts from 0.")

        return CheckResult.correct()


if __name__ == '__main__':
    ModifyTest().run_tests()