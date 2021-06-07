import key_generator.key_generator as key
import threading

Sk = key.generate(num_of_atom=9,seed=1)
print(Sk.get_key())

