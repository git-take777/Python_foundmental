# dictionary: キーと値の組み合わせを複数保持するデータ型

fruites_colors = {'apple': 'red', "lemon": "yellow", "grapes": 'purple'}

fruites_colors['peach'] = "pink"
print(fruites_colors)
# dict_sample = {'1': 'One', '2': 'two', 'three': [1,2,3], 'four': {'index': 'fourth'}}
# print(dict_sample)

# .keyと.value
for fruit in fruites_colors.key():
  print(fruit)
