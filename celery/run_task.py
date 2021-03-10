from tasks1 import add

result = add.delay(4, 4)
print('Is task ready: %s' % result.ready())

run_result = result.get(timeout=30)
print('task result: %s' % run_result)
