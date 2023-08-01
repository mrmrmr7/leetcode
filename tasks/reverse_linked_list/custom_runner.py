import time
import yaml

from pathlib import Path

import tasks.reverse_linked_list.solution as solution

with open(Path(solution.__file__).parent / 'test.yaml', 'r') as tests:
    cases = yaml.safe_load(tests)
    s = solution.Solution()

    for case in cases:
        answer = case['answer']
        del case['answer']
        start_time = time.time()
        arr = case['head']
        a = solution.ListNode(arr[0])
        t = a
        for i in range(1, len(arr)):
            t.next = solution.ListNode(arr[i])
            t = t.next

        case['head'] = a
        m = [x for x in dir(s.__class__) if not x.startswith("__")][0]
        meth = getattr(s, m)
        res_raw = meth(**case)

        res = [res_raw.val]
        while res_raw.next:
            res_raw = res_raw.next
            res.append(res_raw.val)

        finish_time = time.time()
        ex_time = finish_time - start_time
        print(f"Case: {case}")
        print(f"Passed: {res == answer}")
        print("Ex time: %.3f" % ex_time)
        print(f'Compare: "{res}" == "{answer}"\n')
