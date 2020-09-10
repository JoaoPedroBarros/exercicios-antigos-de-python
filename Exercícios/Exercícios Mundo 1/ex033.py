g = float(input('Digite um número:'))
h = float(input('Digite outro número:'))
j = float(input('Digite outro número:'))
if g>h>j:
    print('O maior numero é {} e o menor, {}.'.format(g,j))
if g>j>h:
    print('O maior numero é {} e o menor, {}.'.format(g, h))
if j>g>h:
    print('O maior numero é {} e o menor, {}.'.format(j, h))
if j>h>g:
    print('O maior numero é {} e o menor, {}.'.format(j, g))
if h>g>j:
    print('O maior numero é {} e o menor, {}.'.format(h, j))
if h>j>g:
    print('O maior numero é {} e o menor, {}.'.format(h, g))
