from os.path import join
import re
import logmerge


print("hello world")
processor = logmerge.TdarLogProcessor()
print(processor.processor_name)

print(f"processor val: {processor.getval()}")
processor.setval(5)
print(f"processor val: {processor.getval()}")
print(f"TdarLogProcessor.val: {logmerge.TdarLogProcessor.val}")

logmerge.TdarLogProcessor.val = 5
processor2 = logmerge.TdarLogProcessor()
print(f"processor2 val: {processor2.getval()}")
processor2.setval(10)
print(f"processor2 val: {processor2.getval()}")
print(f"TdarLogProcessor.val: {logmerge.TdarLogProcessor.val}")
