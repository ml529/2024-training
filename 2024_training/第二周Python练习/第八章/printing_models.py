# -*- coding: utf-8 -*-

# printing_models.py

import printing_function

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 调用print_models函数
printing_function.print_models(unprinted_designs, completed_models)

# 调用show_completed_models函数
printing_function.show_completed_models(completed_models)
