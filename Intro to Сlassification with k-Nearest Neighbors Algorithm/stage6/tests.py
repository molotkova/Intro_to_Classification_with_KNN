import ast
from hstest.stage_test import List
from hstest import *
import re

correct_answer = [[1.0, 1.0, 1.0, 1.0], [0.6666666666666666, 1.0, 0.5, 0.6666666666666666]]
metric_list = ['accuracy', 'precision', 'recall', 'F-score']
regex4float = "[+-]?([0-9]*[.])?[0-9]+"

class MetricTest(StageTest):

    def generate(self) -> List[TestCase]:
        return [TestCase(time_limit=1000000)]

    def check(self, reply: str, attach):

        reply = reply.strip().replace(" ", "").lower()

        if len(reply) == 0:
            return CheckResult.wrong("No output was printed")

        if len(reply.split('\n')) != 10:
            return CheckResult.wrong('The number of lines is the output does not equal 10.\n'
                                     'Please follow the format specified in the Examples section.')

        answer_k1 = re.search(pattern=f"metricvalueswhenk=1:\naccuracy:{regex4float}\nprecision:{regex4float}\nrecall:{regex4float}\nf-score:{regex4float}", string=reply)

        if answer_k1 is None:
            raise WrongAnswer(
                "Didn't find all or a part of the answer for the k = 1 case.\n"
                "Check whether the format is correct and whether all of the metrics are present")
        list_k1 = answer_k1.group(0)

        user_list_k1 = [float(i.split('\n')[0].lstrip()) for i in list_k1.split(':')[2:]]

        for j in range(len(user_list_k1)):
                if user_list_k1[j] < correct_answer[0][j] - 0.01 * correct_answer[0][j] or\
                        user_list_k1[j] > correct_answer[0][j] + 0.01 * correct_answer[0][j]:
                        return CheckResult.wrong(f"Seems like answer is not correct\n"
                                                 f"Check metric {metric_list[j]} of case k = 1.")

        answer_k3 = re.search(pattern=f"metricvalueswhenk=3:\naccuracy:{regex4float}\nprecision:{regex4float}\nrecall:{regex4float}\nf-score:{regex4float}", string=reply)

        if answer_k3 is None:
            raise WrongAnswer(
                "Didn't find all or a part of the answer for the k = 3 case.\n"
                "Check whether the format is correct and whether all of the metrics are present")

        list_k3 = answer_k3.group(0)
        user_list_k3 = [float(i.split('\n')[0].lstrip()) for i in list_k3.split(':')[2:]]

        for j in range(len(user_list_k3)):
            if user_list_k3[j] < correct_answer[1][j] - 0.01 * correct_answer[1][j] or \
                    user_list_k3[j] > correct_answer[1][j] + 0.01 * correct_answer[1][j]:
                return CheckResult.wrong(f"Seems like answer is not correct\n"
                                         f"Check metric {metric_list[j]} of case k = 3")

        return CheckResult.correct()


if __name__ == '__main__':
    MetricTest().run_tests()