import time
import yaml

from pathlib import Path

import tasks.minimum_speed_to_arrive_on_time.solution as solution

with open(Path(solution.__file__).parent / 'test.yaml', 'r') as tests:
    cases = yaml.safe_load(tests)
    s = solution.Solution()

    for case in cases:
        answer = case['answer']
        del case['answer']
        start_time = time.time()
        m = [x for x in dir(s.__class__) if not x.startswith("__")][0]
        meth = getattr(s, m)
        res = meth(**case)
        finish_time = time.time()
        ex_time = finish_time - start_time
        print(f"Case: {case}")
        print(f"Passed: {res == answer}")
        print("Ex time: %.3f" % ex_time)
        print(f'Compare: "{res}" == "{answer}"\n')
